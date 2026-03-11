from pathlib import Path
import pandas as pd
from utils import plot_main_menu

# Kind Budget — UX Research Consolidated Dataset
# Multilingual survey data merged for unified analysis
# Languages: ENG | ITA | ESP
# Total respondents: 57
# Purpose: User research insights for budgeting app design
# Collection date: April 2025

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

BASE_DIR = Path(r"C:\Users\Tommy\Desktop\AI\progetti\UX Kind by TM")
dfENG = pd.read_csv(BASE_DIR/'kindbudget_ENG_clean.csv',na_values= ['?','','null','N/A','NA','None'] )
dfESP = pd.read_csv(BASE_DIR/'kindbudget_ESP_clean.csv',na_values= ['?','','null','N/A','NA','None'] )
dfIT = pd.read_csv(BASE_DIR/'kindbudget_ITA_clean.csv',na_values= ['?','','null','N/A','NA','None'] )

dfALL = pd.concat([dfENG,dfESP,dfIT], ignore_index= True)


dfALL.set_index('user', inplace= True)

dfALL['uses_budgeting_app'] = dfALL['uses_budgeting_app'].replace({
    "sì": "yes",
    "si": "yes",
    "sí": "yes",
    "no": "no",
    "non ne ho mai usata una e non mi interessa": "Never think about it"
})

dfALL['status'] = dfALL['status'].replace({
    "lavoratore a tempo pieno" : "full-time worker",
    "trabajador a tiempo completo":"full-time worker",
    "otro" : "other",
    "altro" : "other",
    "pensionato" : "retired",
    "disoccupato" : "unemployed",
    "desempleado" : "unemployed",
    "lavoratore part-time" : "part-time worker"
})

dfALL['endMonth_saves_money'] = dfALL['endMonth_saves_money'].replace({
    "yes": "yes",
    "sì": "yes",
    "si": "yes",
    "sí": "yes",
    "regolarmente": "yes",
    "sometimes": "sometimes",
    "a volte": "sometimes",
    "a veces": "sometimes",
    "raramente": "sometimes",
    "rarely": "sometimes",
    "rara vez": "sometimes",
    "no": "no",
    "mai": "no",
    "never": "no",
    "nunca": "no"
})

dfALL['open_to_interview'] = dfALL["open_to_interview"].replace({
    "yes": "yes",
    "sì": "yes",
    "si": "yes",
    "sí": "yes",
})
cat_cols = ['age_group', 'status', 'endMonth_saves_money', 'uses_budgeting_app', 'open_to_interview']

for col in cat_cols:
    dfALL[col] = dfALL[col].astype('category')

cat_col = dfALL.select_dtypes(include='category').columns.tolist()

compare_cols = [
    "uses_budgeting_app",
    "endMonth_saves_money",
    "open_to_interview"
]

dfALL.to_csv(BASE_DIR / "kindbudget_ALL_clean.csv", index= True)


plot_main_menu(dfALL, cat_col, compare_cols)
