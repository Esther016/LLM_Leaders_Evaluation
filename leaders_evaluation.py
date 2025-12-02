import requests
import json
import os
import logging
import time
from datetime import datetime
import pandas as pd
from pathlib import Path
from collections import OrderedDict
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import numpy as np # 用于处理 NaN

# ========== 配置日志 ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("model_call.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# ========== 配置 (请在这里确认你的 Key 和模型列表) ==========
# 请填你的 key
API_KEY = "" 

API_URL = "https://api.aihubmix.com/v1/chat/completions"
# 为了评估政策，建议使用具备搜索或强大推理能力的模型
MODELS = [
    ### Remember: keep the cheapest models at the front to save costs!
    ### OpenAI Models
    "gpt-4.1-mini",
    "gpt-4.1-nano",
    # "gpt-4o",
    # "o4-mini",
    # "gpt-4-turbo",
    # "gpt-3.5-turbo",
    # "gpt-5-mini",
    # "gpt-4.1",
    # "gpt-5",

    # ### Qwen Models
    # # "qwen3-max",
    # "qwen3-vl-235b-a22b-instruct",
    # "qwen3-vl-235b-a22b-thinking",
    # "qwen3-vl-30b-a3b-instruct",
    # "qwen3-vl-30b-a3b-thinking",
    # "qwen3-next-80b-a3b-instruct",
    # "qwen3-next-80b-a3b-thinking",
    # "qwen2.5-72b-instruct",
    # "qwen2.5-32b-instruct",
    # "qwen2.5-3b-instruct",

    # ### Moonshot Models
    # # moonshot
    # "moonshot-v1-8k",
    # "moonshot-v1-32k",
    # # kimi
    # "Kimi-K2-0905",
    # "kimi-k2-turbo-preview",
    # "kimi-latest",

    # ### MiniMax
    # "MiniMaxAI/MiniMax-M1-80k",

    # ### llama Models
    # "llama-4-scout",
    # "llama-3.3-70b",
    # "llama3.1-8b",

    # ### Microsoft Phi
    # "AiHubmix-Phi-4-reasoning",
    # "AiHubmix-Phi-4-mini-reasoning",

    # ### Claude Models
    # "claude-3-haiku-20240307",
    # "claude-3-5-haiku-20241022",
    # "claude-3-7-sonnet-20250219",
    # "claude-opus-4-0",
    # "claude-opus-4-1",
    # "claude-sonnet-4-5",
    # "claude-haiku-4-5",

    # ### Zhipu Models
    # # glm
    # "glm-4.5",
    # "glm-4.5-flash",
    # "THUDM/GLM-4.1V-9B-Thinking",
    # "THUDM/GLM-4-32B-0414",
    # "THUDM/GLM-4-9B-0414",

    # ### Google gemini Models
    # "gemini-2.0-flash",
    # "gemini-2.5-pro-preview-05-06",
    # "gemini-2.5-flash-preview-09-2025",
    
    # ### Doubao Models
    # "doubao-seed-1-6",
    # "doubao-seed-1-6-flash",
    # "doubao-seed-1-6-thinking",

    # ### Jina
    # "jina-deepsearch-v1",
    # "jina-embeddings-v4",

    # ### Deepseek Models
    # "DeepSeek-R1",
    # "DeepSeek-V3",
    # "DeepSeek-V3.1-Terminus",
    # "DeepSeek-V3.2-Exp",
    
    # # deepseek-ai
    # "deepseek-ai/DeepSeek-V2.5",

    # ### Grok models
    # "grok-4-fast-reasoning",
    # "grok-3-mini",
    
    # # ernie
    # "ernie-4.5-turbo-latest",
    # "ernie-4.5",
    # "ernie-x1-turbo-32k-preview",
    # "ernie-x1.1-preview",

    # # 美团
    # "LongCat-Flash-Chat",
    
    # # Mistral
    # "mistral-large-latest",
    # "mistral-small-latest"

    # interesting models
    ### Baichuan
    ### "Aihubmix-MAI-DS-R1", # deepseek-cracked
]

# 输入/输出文件
INPUT_FILE = Path("identifying_ideologues.tab")

# 每次 API 调用的最大领导人数
CHUNK_SIZE = 100 
# ⚠️ 测试模式：如果需要测试，请将此设置为一个数字 (例如 5)。正式运行时请设置为 None
TEST_MODE_LIMIT = 50 # 默认为 None (处理全部数据)

# ========== 核心 API 调用函数 ==========
def query_model(api_key, model_name, prompt, question):
    """调用 API，返回状态码和响应文本"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": question}
    ]

    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": 0.1,  # 较低温度保证客观性
    }

    try:
        session = requests.Session()
        retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)

        response = session.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status() 
        
        response_json = response.json()
        
        if 'choices' in response_json and len(response_json['choices']) > 0:
            return 200, response_json['choices'][0]['message']['content'].strip()
        else:
            return 400, "API 响应格式错误或内容为空"

    except requests.exceptions.RequestException as e:
        logger.error(f"API Call Error ({model_name}): {e}")
        return 500, f"API Call Failed: {e}"
    except Exception as e:
        logger.error(f"Unknown Error: {e}")
        return 500, f"Unknown Error: {e}"

# ========== JSON 清理和验证函数 ==========
def clean_and_validate_json(text):
    """尝试从文本中提取并格式化有效的 JSON 字符串，否则返回错误标记。"""
    if pd.isna(text):
        return "" # 处理 NaN
        
    try:
        # 1. 尝试找到 JSON 块 (处理 ```json ... ``` 包装的情况)
        if '```json' in text:
            start = text.find('```json') + 7
            end = text.rfind('```')
            json_str = text[start:end].strip()
        elif '{' in text and '}' in text:
            # 2. 尝试直接从第一个 { 到最后一个 } 提取
            start = text.find('{')
            end = text.rfind('}')
            json_str = text[start : end + 1].strip()
        else:
            # 没有找到明显的 JSON 结构
            return "{\"error\": \"NO_JSON_FOUND\", \"raw\": " + json.dumps(str(text[:100])) + "}"

        # 3. 尝试解析 JSON
        data = json.loads(json_str)
        
        # 4. 确保 JSON 结构完整（基于 Prompt 要求）
        required_keys = ["original_code_label", "llm_conclusion", "reasoning", "consistency_check"]
        if not all(key in data for key in required_keys):
            return "{\"error\": \"INCOMPLETE_JSON\", \"raw\": " + json.dumps(json_str[:100]) + "}"
        
        # 返回干净的 JSON 字符串
        return json.dumps(data, ensure_ascii=False)
    
    except json.JSONDecodeError as e:
        # JSON 解析失败
        result = {
            "error": "JSON_DECODE_FAILED",
            "message": str(e).replace('"', ''),
            "raw": str(text[:100])
        }
        return json.dumps(result)
    except Exception as e:
        # 其他未知错误
        result = {
            "error": "JSON_CLEANING_ERROR",
            "message": str(e).replace('"', '')
        }
        return json.dumps(result)


# ========== 数据处理与 LLM 调用主逻辑（最终修正版：按 term_id 匹配）==========
def process_leader_evaluation():
    if not API_KEY:
        logger.critical("Please set API_KEY")
        return

    if not INPUT_FILE.exists():
        logger.critical(f"Input file {INPUT_FILE} does not exist. Ensure identifying_ideologues.tab is in the same directory.")
        return

    # 1.  动态生成带时间戳的输出文件名 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    OUTPUT_FILE = Path(f"LLM_Leader_Evaluation_{timestamp}.xlsx") 

    logger.info(f"Starting to read file: {INPUT_FILE}")
    try:
        df = pd.read_csv(INPUT_FILE, sep='\t', quoting=csv.QUOTE_NONE, encoding='utf-8')
    except Exception as e:
        logger.critical(f"Failed to read file: {e}")
        return
    
    # 2. 保留所需列并清洗
    COLS_TO_KEEP = [
        'country_name', 'year', 'hog', 
        'hog_ideology', 'hog_ideology_num_full', 'hog_left', 'hog_right', 'hog_center', 'hog_noinfo'
    ]
    
    df_raw = df[COLS_TO_KEEP].dropna(subset=['country_name', 'year', 'hog']).copy()

    # 清洗连接键
    for col in ['country_name', 'hog']:
        df_raw[col] = df_raw[col].astype(str).str.strip().str.replace('"', '').str.replace("'", '')
        
    # 3. 按连续任期分组（核心逻辑）
    df_raw = df_raw.sort_values(by=['country_name', 'hog', 'year'])
    
    # 判断是否为新任期（国家变化、领导人变化、年份不连续）
    df_raw['is_new_term'] = (
        (df_raw['country_name'] != df_raw['country_name'].shift(1)) |
        (df_raw['hog'] != df_raw['hog'].shift(1)) |
        (df_raw['year'] != df_raw['year'].shift(1) + 1)
    ).fillna(True)
    
    # 创建任期ID
    df_raw['term_id'] = df_raw['is_new_term'].cumsum()
    
    logger.info(f"原始记录数: {len(df_raw)}. 识别的独立任期数: {df_raw['term_id'].nunique()}")

    # 3d. 聚合数据：按term_id合并连续任期（生成duration）
    df_unique_terms = df_raw.groupby('term_id', as_index=False).agg(
        country_name=('country_name', 'first'),
        hog=('hog', 'first'),
        start_year=('year', 'min'),
        end_year=('year', 'max'),
        duration=('year', lambda x: f"{x.min()}-{x.max()}"),  # 生成任期跨度
        hog_ideology=('hog_ideology', 'first'),
        hog_ideology_num_full=('hog_ideology_num_full', 'first'),
        hog_left=('hog_left', 'first'),
        hog_right=('hog_right', 'first'),
        hog_center=('hog_center', 'first'),
        hog_noinfo=('hog_noinfo', 'first')
    )
    
    # 移除原始year列（已被duration替代）
    df_unique_terms = df_unique_terms.drop(columns=['start_year', 'end_year'])  # 可选：如果只需要duration
    
    # 测试模式限制
    if TEST_MODE_LIMIT is not None and isinstance(TEST_MODE_LIMIT, int) and TEST_MODE_LIMIT > 0:
        df_unique_terms = df_unique_terms.head(TEST_MODE_LIMIT)
        logger.warning(f"⚠️ 测试模式：仅处理 {len(df_unique_terms)} 个任期")

    # 转换为列表用于LLM评估
    terms_list = df_unique_terms.to_dict('records')
    logger.info(f"待评估的独立任期总数: {len(terms_list)}")

    # 4. 遍历并调用LLM API（保持原有逻辑，基于合并后的任期）
    for i in range(0, len(terms_list), CHUNK_SIZE):
        chunk = terms_list[i:i + CHUNK_SIZE]
        logger.info(f"处理任期索引 {i} 至 {min(i + CHUNK_SIZE, len(terms_list))}...")
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_term = {}
            for term_data in chunk:
                term_id = term_data['term_id']
                country = term_data['country_name']
                duration = term_data['duration']  # 使用任期跨度
                hog = term_data['hog']
                
                logger.info(f"\n--- 🚀 开始评估任期 {term_id}: {country}, 领导人: {hog} (任期: {duration}) ---")
                
                for model in MODELS:
                    # 构造提示词（使用duration替代单独年份）

                    prompt_system = (
                        "You are a professional political analyst responsible for data validation. Please combine historical knowledge and policy details to "
                        "assess whether a leader's policy behaviors exhibit 'liberal bias' and compare the consistency with the original coding. "
                        "Return the result in JSON format: {\"original_code_label\": \"...\", \"llm_conclusion\": \"YES/NO/UNCLEAR\", "
                        "\"reasoning\": \"...\", \"consistency_check\": \"CONSISTENT/INCONSISTENT/UNCLEAR\"}"
                    )

                    question_user = (                        
                        f"Please assess whether the following leader's policies exhibit liberal tendencies and compare with the original coding:\n"
                        f"Country: {country}\n"
                        f"Term of office: {duration}\n"
                        f"Leader: {hog}\n\n"
                        f"--- Original dataset coding ---\n"
                        f"Ideology label: {term_data.get('hog_ideology', 'N/A')}\n"
                        f"Full classification value: {term_data.get('hog_ideology_num_full', 'N/A')}\n"
                        f"Left-wing marker: {term_data.get('hog_left', 'N/A')}\n"
                        f"Right-wing marker: {term_data.get('hog_right', 'N/A')}\n"
                        f"Centrist marker: {term_data.get('hog_center', 'N/A')}\n"
                    )
                    

                    future = executor.submit(query_model, API_KEY, model, prompt_system, question_user)
                    future_to_term[future] = (term_data, model)

            for future in as_completed(future_to_term):
                term_data, model = future_to_term[future]
                _, response_text = future.result()
                cleaned_response = clean_and_validate_json(response_text)
                
                # 更新评估结果
                target_term_id = term_data['term_id']
                for idx, item in enumerate(terms_list):
                    if item['term_id'] == target_term_id:
                        terms_list[idx][f'{model}_Assessment'] = cleaned_response 
                        break
                
                logger.info(f"✅ 完成评估任期 {target_term_id}: {term_data['country_name']} ({term_data['duration']}) - {model}")

        # 5. 保存合并后的结果（不再合并回原始年度数据）
        results_df = pd.DataFrame(terms_list)
        results_df.to_excel(OUTPUT_FILE, index=False)
        logger.info(f"已保存当前进度至 {OUTPUT_FILE}")
        time.sleep(1)

    logger.info(f"所有任期评估完成，最终结果已保存至 {OUTPUT_FILE}")

# ========== 主入口 ==========
if __name__ == "__main__":

    process_leader_evaluation()
