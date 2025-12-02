## LLM Leaders Ideology Evaluation

This repository provides a workflow to evaluate the political ideology of heads of government using Large Language Models (LLMs). The script processes leadership data from the **“Identifying Ideologues”** dataset, queries a model for ideological classification, and stores the evaluation results for analysis.

---

### 1. Project Overview

Political ideology plays a central role in shaping government behavior and policy outcomes, yet systematic and cross-national ideology evaluation remains challenging. By leveraging LLMs, this project attempts to:

1. Identify heads of government and the year they served.
2. Provide short contextual prompts for each leader.
3. Use a Large Language Model to infer their political ideology.
4. Compare model-generated ideology to the original expert-coded data labels.

This project contributes to the growing set of studies validating whether LLMs can meaningfully classify political ideology in real-world geopolitical contexts.

---

### 2. Data Source

This project uses the publicly available dataset:

**Identifying Ideologues: A Global Dataset of Heads of Government and Their Political Ideology**
Harvard Dataverse
Persistent ID: doi:10.7910/DVN/RTLDXF

Variables used in this project:

| Variable       | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| `country_name` | Country of the leader                                |
| `year`         | Year of leadership                                   |
| `hog`          | Name of head of government                           |
| `hog_ideology` | Expert-coded ideology label (Left/Right/Center etc.) |

Only the `identifying_ideologues.tab` subset is required for this pipeline.

Please cite the dataset if used in academic work (see citation section below).

---

### 3. Pipeline Summary

The main process is implemented in **`leaders_evaluation.py`**:

1. Load leadership dataset (`.tab` or `.csv`)
2. Clean and filter rows with available ideology and leader name
3. Generate prompts based on:

   * leader name
   * country
   * year
4. Query LLM:

   * classifies ideology along Left / Center-Left / Center / Center-Right / Right
   * returns short justification
5. Store results into an Excel spreadsheet (`.xlsx`)
6. Provide comparison vs original expert labels

---

### 4. Output Example

An example output spreadsheet is included:

```
LLM_Leader_Evaluation_20251018_204819.xlsx
```

This shortened version contains preliminary evaluation results for demonstration.
Full evaluation may produce a more complete file with misalignment/error logs, richer justification text, and prompt metadata.

---

### 5. Requirements

Minimal recommended environment:

```bash
Python 3.9+
requests>=2.25.0
pandas>=1.3.0
numpy>=1.21.0
openpyxl>=3.0.0 
urllib3>=1.26.0
```

Install dependencies:

```bash
pip install -r requirements.txt
```
---

### 6. How to Run

```bash
python leaders_evaluation.py 
```
with file `identifying_ideologues.tab` in the same folder.

Optional arguments: You can choose preferred models available on Aihubmix official website by adding or deleting models within the python file.

---

### 7. File Structure

```
├── leaders_evaluation.py         # Main evaluation script
├── leaders_result_short.xlsx     # Example results
├── README.md                     # Documentation
└── (dataset not included, download separately)
```

Dataset should be downloaded manually due to licensing terms.

---

### 8. Citation

Dataset reference:

R. B. Gerring, M. Hoffman, D. Zegers, “Identifying Ideologues: A Global Dataset of Heads of Government and Their Political Ideology.” Harvard Dataverse, 2023. doi:10.7910/DVN/RTLDXF

If using this workflow in academic writing, please cite:

* the Dataverse dataset (required), and
* this repository (software citation recommended).

---

### 9. Rough Conclusion (Interim)

This early-stage experiment shows that:

* LLMs can infer ideology signals from minimal prompts (name + country + year).
* Performance varies across regions and historical periods.
* Misalignment occurs more often for ideologically ambiguous or short-term leaders.
* This approach may support further research on political history and machine learning political science applications.

A more detailed analysis will be provided as complete results become available.

---

## Dataset quick facts
| | |
|---|---|
| **Rows** | >50 000 leaders  |
| **Countries** | 156 |
| **Waves** | 2 (2010‑13, 2017‑19) |
| **Political bodies** | 1 552 (executive, cabinet, parliamentary party group, upper/lower chambers, supreme court) |
| **Identities coded** | Gender · Ethnicity · Language · Religion |
| **File size** | ~92.8 MB CSV |

## Appendix
### Covariates covered 

|   #|Column Name                    |
|---:|:------------------------------|
|   1|glp_country                    |
|   2|glp_country_nid                |
|   3|glp_person                     |
|   4|glp_person_nid                 |
|   5|person_ethnic                  |
|   6|person_ethnic_nid              |
|   7|office1                        |
|   8|office2                        |
|   9|office3                        |
|  10|person_firstname               |
|  11|person_lastname                |
|  12|round1                         |
|  13|round2                         |
|  14|person_round                   |
|  15|country                        |
|  16|country_id                     |
|  17|lexical_index                  |
|  18|pop_wdi_actual                 |
|  19|V_Dem_Country                  |
|  20|country_text_id                |
|  21|person_party_aff_power         |
|  22|pol_party_nid                  |
|  23|pol_party                      |
|  24|person_combethnicity           |
|  25|person_combethnicity_no        |
|  26|person_ethnocultural_title     |
|  27|person_ethnocultural_nid       |
|  28|person_ethnic1_title           |
|  29|person_ethnic1_nid             |
|  30|person_combethnic_title        |
|  31|person_house                   |
|  32|person_bday                    |
|  33|person_gender                  |
|  34|person_gender_no               |
|  35|person_born_abroad             |
|  36|person_birthplace              |
|  37|person_birthcountry            |
|  38|person_marital_stat            |
|  39|person_numchild                |
|  40|person_occupation_all          |
|  41|person_occupation_1            |
|  42|person_occupation_2            |
|  43|person_occupation_3            |
|  44|person_family_clan_name        |
|  45|person_family_clan_nam_rel     |
|  46|person_ethnocultural_crite     |
|  47|person_ethnocultural_crite_all |
|  48|person_ethnocultural_crite_1   |
|  49|person_ethnocultural_crite_2   |
|  50|person_ethnocultural_crite_3   |
|  51|person_ethnocultural_signf_nid |
|  52|prsn_ethncltral_signf_title    |
|  53|person_ethnocultural_rel       |
|  54|person_ethnocultural_rel_no    |
|  55|prsn_ethncltralgp_living_style |
|  56|person_ethnocultural_source    |
|  57|person_ethnocultural_all       |
|  58|person_ethnocultural_all_nid   |
|  59|person_ethnocultural_1_nid     |
|  60|person_ethnocultural_1_title   |
|  61|person_ethnocultural_2_nid     |
|  62|person_ethnocultural_2_title   |
|  63|person_ethnocultural_3_nid     |
|  64|person_ethnocultural_3_title   |
|  65|person_ethnic_criteria         |
|  66|person_ethnic_criteria_all     |
|  67|person_ethnic_criteria_1       |
|  68|person_ethnic_criteria_2       |
|  69|person_ethnic_criteria_3       |
|  70|person_ethnic_signf_nid        |
|  71|person_ethnic_signf_title      |
|  72|person_ethnic_rel              |
|  73|person_ethnic_rel_no           |
|  74|person_ethnicgrp_ecorank       |
|  75|person_ethnicgrp_size          |
|  76|person_ethnicgp_living_style   |
|  77|person_ethnicgrp_source        |
|  78|person_ethnicgrp_population    |
|  79|person_ethnicgrp_defcriteria   |
|  80|person_ethnic_all              |
|  81|person_ethnic_all_nid          |
|  82|person_ethnic_1_nid            |
|  83|person_ethnic_1_title          |
|  84|person_ethnic_2_nid            |
|  85|person_ethnic_2_title          |
|  86|person_ethnic_3_nid            |
|  87|person_ethnic_3_title          |
|  88|person_rel_family_nid          |
|  89|person_rel_family_title        |
|  90|person_rel_family_rel          |
|  91|person_rel_family_rel_no       |
|  92|person_rel_current_nid         |
|  93|person_rel_current_title       |
|  94|person_rel_current_rel         |
|  95|person_rel_current_rel_no      |
|  96|person_lang_native_nid         |
|  97|person_lang_native_title       |
|  98|person_lang_native_rel         |
|  99|person_lang_native_rel_no      |
| 100|person_lang_native_other       |
| 101|person_lang_spoken_nid         |
| 102|person_lang_spoken_title       |
| 103|person_lang_spoken_other       |
| 104|person_lang_english            |
| 105|person_lang_french             |
| 106|person_lang_arabic             |
| 107|person_lang_spanish            |
| 108|person_lang_chinese            |
| 109|person_lang_german             |
| 110|person_lang_russian            |
| 111|person_lang_portuguese         |
| 112|person_lang_other              |
| 113|person_lang_all                |
| 114|person_lang_all_count          |
| 115|person_unv_name_all            |
| 116|person_unv_name_1              |
| 117|person_unv_name_2              |
| 118|person_unv_name_3              |
| 119|person_ug_major                |
| 120|person_ug_major_all            |
| 121|person_ug_major_1              |
| 122|person_ug_major_1_no           |
| 123|person_ug_major_2              |
| 124|person_ug_major_2_no           |
| 125|person_ug_major_3              |
| 126|person_ug_major_3_no           |
| 127|person_education               |
| 128|person_education_no            |
| 129|person_college_country         |
| 130|person_abroad                  |
| 131|person_eduwest                 |
| 132|person_course_of_study         |
| 133|person_combethnic_nid          |
| 134|person_combethnic_all          |
| 135|person_combethnic_all_nid      |
| 136|person_combethnic_1_nid        |
| 137|person_combethnic_1_title      |
| 138|person_combethnic_2_nid        |
| 139|person_combethnic_2_title      |
| 140|person_combethnic_3_nid        |
| 141|person_combethnic_3_title      |
| 142|person_combethnicgrp_size      |
| 143|person_combethnicgrp_ecorank   |
| 144|prsn_cmbthncgrp_livingstyle    |
| 145|person_combethnicgrp_source    |
| 146|prsn_cmbthncgrp_population     |
| 147|prsn_cmbthncgrp_defcriteria    |
| 148|person_party_aff_nonpartisan   |
| 149|person_party_aff_position      |
| 150|prsn_prty_aff_position_local   |
| 151|person_party_aff_coalition     |
| 152|prsn_prty_aff_coalition_differ |
| 153|person_party_aff_longterm_aff  |
| 154|person_party_aff_pol_exp       |
| 155|person_office_position_1       |
| 156|person_office_minposarea_1     |
| 157|person_office_minposarea_lo_1  |
| 158|person_office_service_began_1  |
| 159|prsn_office_srvc_bgn_cabi_1    |
| 160|person_office_terms_1          |
| 161|person_office_pm_participate_1 |
| 162|person_office_howmanydays_1    |
| 163|prsn_office_hwmnydys_miss_1    |
| 164|prsn_office_cnsttncy_nid_1     |
| 165|prsn_office_cnsttncy_title_1   |
| 166|person_office_position_2       |
| 167|person_office_minposarea_2     |
| 168|person_office_service_began_2  |
| 169|prsn_office_srvc_bgn_cabi_2    |
| 170|person_office_terms_2          |
| 171|person_office_pm_participate_2 |
| 172|person_office_howmanydays_2    |
| 173|prsn_office_hwmnydys_miss_2    |
| 174|prsn_office_cnsttncy_nid__2    |
| 175|prsn_office_cnsttncy_title_2   |
| 176|person_office_position_3       |
| 177|person_office_minposarea_3     |
| 178|person_office_service_began_3  |
| 179|prsn_office_srvc_bgn_cabi_3    |
| 180|person_office_terms_3          |
| 181|person_office_pm_participate_3 |
| 182|person_office_howmanydays_3    |
| 183|prsn_office_hwmnydys_miss_3    |
| 184|prsn_office_cnsttncy_nid_3     |
| 185|prsn_office_cnsttncy_title_3   |
| 186|person_office_minposarea_4     |
| 187|person_office_minposarea_5     |
| 188|office_type_1                  |
| 189|office_type_2                  |
| 190|office_type_3                  |
