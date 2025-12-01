---
title: "Global Leadership Project (v1)"
sdk: "datasets"
taskCategories:
  - "research"
tags:
  - "descriptive representation"
  - "political leadership"
  - "political science"
  - "social science"
  - "demographics"
license: "mit"
datasets:
  - "GlobalLeadershipProject_v1.csv"
---
**A distilled dataset of more than 50,000 political elites coded on gender, ethnicity, language, religion, office type, and more.**  
The release accompanies the open‑access paper:

> John Gerring, Connor T. Jerzak & Erzen Öncel (2024).  
> “The Composition of Descriptive Representation.” *American Political Science Review* 118(2): 784‑801.  
> https://doi.org/10.1017/S0003055423000680

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


## Files included
| File | Description |
|------|-------------|
| `GlobalLeadershipProject_v1.csv` | Tabular data (leaders × variables) |
| `LICENSE` | MIT |

## Reference

John Gerring, Connor T. Jerzak, Erzen Öncel. The Composition of Descriptive Representation. _American Political Science Review_, 118(2): 784-801, 2024.

```
@article{gerring2024composition,
  title={The Composition of Descriptive Representation},
  author={Gerring, John and Connor T. Jerzak and Erzen \"{O}ncel},
  journal={American Political Science Review},
  year={2024},
  volume={118},
  number={2},
  pages={784-801}
}
```

## Covariates covered 

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