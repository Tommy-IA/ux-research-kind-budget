from pathlib import Path
import pandas as pd
from utils import plot_choice

# Kind Budget — UX Research Data Cleaning - English Survey
# Survey responses collected in 3 languages (ENG, ITA, ESP)
# 11 English respondents — April 2025

pd.set_option('display.max_columns',None)

BASE_DIR = Path(r"C:\Users\Tommy\Desktop\AI\progetti\UX Kind by TM")
dfENG = pd.read_csv(BASE_DIR/'Risposte ENG Kind by TM – UX Research (Risposte) - Risposte del modulo 1.csv', 
                    na_values=['?','','null','N/A','NA','None'])

dfENG = dfENG.apply(lambda col: col.str.strip().str.lower() if col.dtype == 'object' else col)

dfENG.rename(columns={'Informazioni cronologiche':'timestamp',
             'What is your age group?': 'age_group',
             'What country and city do you currently live in?':'location',
             'What is your current status?':'status',
             'Are you able to save money at the end of the month?':'endMonth_saves_money',
             'Where does most of your money go?':'money_goes_to',
             'Do you currently use any budgeting app?':'uses_budgeting_app',
             'What emotions do you feel when thinking about your finances?':'financial_emotions',
             'When do you feel most out of control with your finances?':'out_of_control_when',
             'Have you ever used a budgeting app? What did you like or dislike about it?':'budgeting_app_experience',
             'What would motivate you to use a budgeting app regularly?':'motivation_use_budgeting_app',
             'If you could change one thing about your financial life, what would it be?':'change_one_thing',
             'Would you be open to a short follow-up interview (15 minutes)?':'open_to_interview',
             'If yes, please leave your email (optional):':'email'}, inplace= True)

dfENG.insert(0, 'Survey', 'English Survey')

dfENG['user'] = [f'user_{i}' for i in range (0,11)]

dfENG["timestamp"] = dfENG["timestamp"].str[0:10]
dfENG['timestamp'] = pd.to_datetime(dfENG['timestamp'], dayfirst = True)

dfENG.set_index('user', inplace=True)

dfENG.loc['user_7', 'location'] = 'Albania'
dfENG.loc['user_2','location'] = "London"
dfENG.loc['user_5', 'location']= 'London'

dfENG.loc['user_0','out_of_control_when'] = 'every month'
dfENG.loc['user_3','out_of_control_when'] = 'When I feel overwhelmed by my expenses'

dfENG.loc['user_0','budgeting_app_experience'] = "I've used ChatGPT for budgeting help"
dfENG.loc['user_1','budgeting_app_experience'] = "I've never used one"
dfENG.loc['user_3','budgeting_app_experience'] = "I haven't used one yet. I'll consider it once I have a stable income that I can save and manage"
dfENG.loc['user_6','budgeting_app_experience'] = 'I prefer desktop software that works fully offline and do not require a phone or internet connection'


dfENG.loc['user_0','change_one_thing'] = "Be less inclined to spend money on gifts"
dfENG.loc['user_1','change_one_thing'] = "Improve my overall financial situation"
dfENG.loc['user_2','change_one_thing'] = "Be able to save more money"
dfENG.loc['user_3','change_one_thing'] = "Avoid overspending on social outings"
dfENG.loc['user_4','change_one_thing'] = "Have a more positive and stress-free financial life."
dfENG.loc['user_5','change_one_thing'] = "Be able to save money consistently each month"
dfENG.loc['user_6','change_one_thing'] = "Reduce unnecessary and wasteful spending"
dfENG.loc['user_7','change_one_thing'] = "Save more money and have better awareness of how I spend it"

dfENG["email"] = dfENG["email"].apply(lambda x: x[0:2] + '****@' + x.split("@")[1] if pd.notna(x) and "@" in x else x)


cat_cols =["age_group", "status", "endMonth_saves_money", "uses_budgeting_app", "open_to_interview"]
for col in cat_cols:
    dfENG[col] = dfENG[col].astype('category')

cat_col = dfENG.select_dtypes(include = "category").columns.tolist()


dfENG.to_csv(BASE_DIR / "kindbudget_ENG_clean.csv", index=True)

plot_choice(dfENG, cat_col)
          

    

