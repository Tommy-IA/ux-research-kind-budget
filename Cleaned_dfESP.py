import pandas as pd
from pathlib import Path
from utils import plot_choice

# Kind Budget — UX Research Data Cleaning - English Survey
# Survey responses collected in 3 languages (ENG, ITA, ESP)
# 11 English respondents — April 2025

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
BASE_DIR = Path(r"C:\Users\Tommy\Desktop\AI\progetti\UX Kind by TM")
dfESP = pd.read_csv(BASE_DIR/'Risposte ESP Kind by TM – Investigación UX (Español) (Risposte) - Risposte del modulo 1.csv',
                    na_values= ['?','','null','N/A','NA','None'])

dfESP = dfESP.apply(lambda col: col.str.strip().str.lower() if col.dtype == 'object' else col)

print(dfESP.columns)

dfESP.rename(columns={
    'Informazioni cronologiche':'timestamp', 
    '¿Cuál es tu grupo de edad?':'age_group',
    '¿En qué ciudad y país vives actualmente?':'location',
    '¿Cuál es tu situación actual?':'status',
    '¿Puedes ahorrar dinero al final del mes?':'endMonth_saves_money',
    '¿En qué se va la mayor parte de tu dinero?':'money_goes_to',
    '¿Utilizas actualmente alguna app de presupuesto?':'uses_budgeting_app',
    '¿Qué emociones sientes al pensar en tus finanzas?':'financial_emotions',
    '¿Cuándo sientes que pierdes más el control de tus finanzas?':'out_of_control_when',
    '¿Has usado alguna app de presupuesto? ¿Qué te gustó o no te gustó?':'budgeting_app_experience',
    '¿Qué te motivaría a usar una app de presupuesto con regularidad?':'motivation_use_budgeting_app',
    'Si pudieras cambiar una cosa sobre tu situación financiera, ¿cuál sería?':'change_one_thing',
    '¿Estarías dispuesto a una breve entrevista de seguimiento (15 minutos)?':'open_to_interview',
    'Si respondiste que sí, deja tu email (opcional):':'email'
    }, inplace= True)

dfESP.insert(0, 'Survey', 'Spanish Survey')

dfESP['user'] = [f"user_{i}" for i in range(0,6)]

dfESP['timestamp'] = dfESP['timestamp'].str[0:10]
dfESP['timestamp'] = pd.to_datetime(dfESP['timestamp'], dayfirst= True)

dfESP.set_index('user', inplace= True)

dfESP.loc['user_1','location'] = 'London'
dfESP.loc['user_3', 'location'] = 'Madrid, Spain'

dfESP.loc["user_0", "out_of_control_when"] = "Cuando salgo"
dfESP.loc["user_1", "out_of_control_when"] = "Cuando estoy estresada"
dfESP.loc["user_2", "out_of_control_when"] = "Cuando siento ansiedad"
dfESP.loc["user_4", "out_of_control_when"] = "Cuando hay gastos imprevistos"
dfESP.loc["user_5", "out_of_control_when"] = "Siempre"

dfESP.loc["user_0", "change_one_thing"] = "Tener un trabajo"
dfESP.loc["user_1", "change_one_thing"] = "Ganar más dinero"
dfESP.loc["user_2", "change_one_thing"] = "Gastar menos y ahorrar más"
dfESP.loc["user_4", "change_one_thing"] = "Reducir gastos"
dfESP.loc["user_5", "change_one_thing"] = "Separar ingresos para gastos personales, ahorros e inversiones"

dfESP['email'] = dfESP['email'].apply(lambda x: x[2] + '****@' + x.split('@')[1] if pd.notna(x) and '@' in x else x)

cat_cols = ['age_group', 'status', 'endMonth_saves_money', 'uses_budgeting_app', 'open_to_interview']

for col in cat_cols:
    dfESP[col] = dfESP[col].astype('category')

cat_col = dfESP.select_dtypes(include='category').columns.tolist()

print(cat_col)

dfESP.to_csv(BASE_DIR / "kindbudget_ESP_clean.csv", index=True)

plot_choice(dfESP, cat_col)