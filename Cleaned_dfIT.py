from pathlib import Path
import pandas as pd
from utils import plot_choice

# Kind Budget — UX Research Data Cleaning - Italian Survey
# Survey responses collected in 3 languages (ENG, ITA, ESP)
# 22 Italian respondents — April 2025

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
BASE_DIR = Path(r"C:\Users\Tommy\Desktop\AI\progetti\UX Kind by TM")
dfIT = pd.read_csv(BASE_DIR/ 'Risposte ITA Kind by TM – Ricerca UX (Italiano) (Risposte) - Risposte del modulo 1.csv', 
                   na_values= ['?','','null','N/A','NA','None'])

dfIT = dfIT.apply(lambda col: col.str.strip().str.lower() if col.dtype == 'object' else col)

dfIT.rename(columns={
    'Informazioni cronologiche': 'timestamp', 
    "Qual è la tua fascia d'età?": 'age_group',
    'In quale città e paese vivi attualmente?' : 'location',
    'Qual è il tuo stato attuale?' : 'status',
    'Riesci a risparmiare soldi a fine mese?' : 'endMonth_saves_money',
    'In cosa spendi la maggior parte del tuo denaro?' : 'money_goes_to',
    "Utilizzi attualmente un'app per il budgeting?" : 'uses_budgeting_app',
    'Che emozioni provi quando pensi alle tue finanze?' : 'financial_emotions',
    'Quando ti senti più fuori controllo rispetto alle tue finanze?' : 'out_of_control_when',
    "Hai mai usato un'app per il budgeting? Cosa ti è piaciuto o no?" : 'budgeting_app_experience',
    "Cosa ti motiverebbe a usare regolarmente un'app per il budgeting?" : 'motivation_use_budgeting_app',
    'Se potessi cambiare una cosa della tua situazione finanziaria, quale sarebbe?' : 'change_one_thing',
    'Saresti disponibile per una breve intervista di follow-up (15 minuti)?':'open_to_interview',
    'Se sì, lascia la tua email (facoltativo):':'email'
    }, inplace= True)

dfIT.insert(0, 'Survey', 'Italian Survey')

dfIT['user'] = [f"user_{i}" for i in range(0,22)]

dfIT['timestamp'] = dfIT['timestamp'].str[0:10]
dfIT['timestamp'] = pd.to_datetime(dfIT['timestamp'], dayfirst=True)

dfIT.set_index('user', inplace=True)

dfIT.loc['user_2','location'] = 'Iglesias, Sardegna'
dfIT.loc['user_5','location'] = 'Cagliari, Sardegna'
dfIT.loc['user_8','location'] = 'Iglesias, Sardegna'
dfIT.loc['user_9','location'] = 'Cagliari, Sardegna'
dfIT.loc['user_11','location'] = 'Cagliari, Sardegna'
dfIT.loc['user_12','location'] = 'Carloforte, Sardegna'
dfIT.loc['user_15','location'] = 'Cagliari, Sardegna'
dfIT.loc['user_16','location'] = 'Reggio Calabria, Calabria'
dfIT.loc['user_17','location'] = 'Cagliari, Sardegna'
dfIT.loc['user_18','location'] = 'Uta, Sardegna'
dfIT.loc['user_19','location'] = 'Roma, Lazio'
dfIT.loc['user_20','location'] = 'Napoli, Campania'
dfIT.loc['user_21','location'] = 'Cagliari, Sardegna'

dfIT.loc["user_0", "out_of_control_when"] = "Quando arrivo a fine mese con i soldi contati"
dfIT.loc["user_1", "out_of_control_when"] = "All'inizio del mese, quando devo pagare debiti e spese fisse"
dfIT.loc["user_3", "out_of_control_when"] = "Abbastanza spesso"
dfIT.loc["user_4", "out_of_control_when"] = "Quando ci sono spese impreviste"
dfIT.loc["user_5", "out_of_control_when"] = "Non saprei"
dfIT.loc["user_7", "out_of_control_when"] = "In caso di spese impreviste"
dfIT.loc["user_8", "out_of_control_when"] = "Quando arrivano spese impreviste"
dfIT.loc["user_10", "out_of_control_when"] = "Mai"
dfIT.loc["user_11", "out_of_control_when"] = "Mai"
dfIT.loc["user_12", "out_of_control_when"] = "Durante spese importanti come la ristrutturazione della casa"
dfIT.loc["user_13", "out_of_control_when"] = "Quando ci sono spese impreviste"
dfIT.loc["user_14", "out_of_control_when"] = "A fine mese"
dfIT.loc["user_15", "out_of_control_when"] = "Quando ci sono spese impreviste"
dfIT.loc["user_16", "out_of_control_when"] = "Quando ci sono spese impreviste"
dfIT.loc["user_17", "out_of_control_when"] = "Mai"
dfIT.loc["user_19", "out_of_control_when"] = "Quando penso a progetti che vorrei realizzare"
dfIT.loc["user_20", "out_of_control_when"] = "Raramente"
dfIT.loc["user_21", "out_of_control_when"] = "Mi sento disorientata"

dfIT.loc["user_0", "budgeting_app_experience"] = "Sì, ho usato un'app di budgeting, ma era troppo complicata e l'ho disinstallata."
dfIT.loc["user_1", "budgeting_app_experience"] = "Sì, ma non mi aiuta a gestire le spese."
dfIT.loc["user_2", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_3", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_4", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_5", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_7", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_8", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_10", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_11", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_12", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_13", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_14", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_15", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_16", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_17", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_18", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_19", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_20", "budgeting_app_experience"] = "No, non l'ho mai usata"
dfIT.loc["user_21", "budgeting_app_experience"] = "No, non l'ho mai usata"

dfIT.loc["user_0", "change_one_thing"] = "Riuscire a risparmiare ogni mese per non arrivare con i soldi contati a fine mese"
dfIT.loc["user_1", "change_one_thing"] = "Non avere debiti"
dfIT.loc["user_4", "change_one_thing"] = "Aumentare il risparmio"
dfIT.loc["user_5", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_7", "change_one_thing"] = "Estinguere il mutuo"
dfIT.loc["user_8", "change_one_thing"] = "Avere più soldi"
dfIT.loc["user_10", "change_one_thing"] = "Nulla"
dfIT.loc["user_11", "change_one_thing"] = "Nulla"
dfIT.loc["user_12", "change_one_thing"] = "Ridurre le bollette energetiche"
dfIT.loc["user_13", "change_one_thing"] = "Aumento del salario"
dfIT.loc["user_14", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_15", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_16", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_17", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_18", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_19", "change_one_thing"] = "Avere un lavoro migliore"
dfIT.loc["user_20", "change_one_thing"] = "Avere uno stipendio più alto"
dfIT.loc["user_21", "change_one_thing"] = "Gestire meglio il denaro"

dfIT['email'] = dfIT['email'].apply(lambda x: x[0:2] + '****@' + x.split('@')[1] if pd.notna(x) and '@' in x else x)

cat_cols = ['age_group', 'status', 'endMonth_saves_money', 'uses_budgeting_app', 'open_to_interview']

for col in cat_cols:
    dfIT[col] = dfIT[col].astype('category')

cat_col = dfIT.select_dtypes(include='category').columns.tolist()


dfIT.to_csv(BASE_DIR / "kindbudget_ITA_clean.csv", index=True)

plot_choice(dfIT, cat_col)





