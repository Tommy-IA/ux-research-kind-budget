# Kind Budget — UX Research Data Cleaning

Multilingual (ENG, ITA, ESP) survey data cleaning and analysis project.
Raw survey responses collected across 3 languages, cleaned and unified into a single dataset.

## Project Overview

Kind Budget is a UX research project focused on personal budgeting habits and financial emotions.
Surveys were distributed in English, Italian, and Spanish to capture diverse user perspectives.

- **Total respondents:** 39
- **Languages:** English (11) · Italian (22) · Spanish (6)
- **Collection date:** April 2025

## Research Goals

- Understand how people manage their personal finances
- Identify emotional triggers related to financial stress
- Explore budgeting app usage and motivations
- Inform the design of Kind Budget — a budgeting app for real people

## Files

| File               |                 Description 
| `Cleaned_dfENG.py` | Data cleaning script — English survey |
| `Cleaned_dfIT.py` | Data cleaning script — Italian survey |
| `Cleaned_dfESP.py` | Data cleaning script — Spanish survey |
| `Cleaned_dfCONCAT.py` | Merges all 3 datasets into one unified CSV |
| `utils.py` | Shared utility functions (missing report, plots) |
| `kindbudget_ENG_clean.csv` | Cleaned English dataset |
| `kindbudget_ITA_clean.csv` | Cleaned Italian dataset |
| `kindbudget_ESP_clean.csv` | Cleaned Spanish dataset |
| `kindbudget_ALL_clean.csv` | Final unified dataset (all 3 languages) |

## Requirements

Python 3.12+
```bash
pip install pandas matplotlib
All cleaning scripts import from `utils.py` — place it in the same directory before running.
```

## Key Cleaning Steps

- Renamed columns from native language questions to standardised English keys
- Created anonymous user index (`user_0`, `user_1`...)
- Extracted and converted timestamps to datetime format
- Corrected inconsistent location values
- Translated ambiguous or non-English responses
- Obscured personal emails for privacy
- Converted categorical columns to `category` dtype
- Merged 3 datasets with `pd.concat()` and normalised values across languages
- Built reusable utility functions in `utils.py` for missing data reporting and visualisation

## Utility Functions (`utils.py`)

| Function               |                           Description |
| `missing_report(df)` | Returns a DataFrame with NaN count and percentage per column |
| `plot(col)` | Interactive bar chart for a single categorical column |
| `plot_menu(df, cat_col)` | Menu to select and visualise any categorical column |
| `plot_compare(df, group_col, target_col)` | Grouped bar chart comparing a variable across surveys |
| `plot_compare_pct(df, group_col, target_col)` | Same as above but with percentage values |
| `plot_main_menu(df, cat_cols, compare_cols)` | Main interactive menu — simple plots or cross-survey comparisons |

> **Note:** `utils.py` is required to run all cleaning scripts. Make sure it is in the same folder.


## Author
**Tommaso Marras**  
[LinkedIn](https://www.linkedin.com/in/tommaso-marras-a681252ba) · [GitHub](https://github.com/Tommy-IA)
