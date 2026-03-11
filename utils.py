import pandas as pd
import matplotlib.pylab as plt

def missing_report(df):
    miss = df.isna().sum().sort_values(ascending= False)
    pct = (miss/len(df)*100).round(2)
    rep = pd.DataFrame({'NaN': miss, '%': pct})
    return rep

def plot_compare_pct(df, group_col, target_col):
    cross_tab = pd.crosstab(df[group_col], df[target_col], normalize="index") * 100
    cross_tab.plot(kind="bar")
    plt.title(f"{target_col} by {group_col} (%)")
    plt.xlabel(group_col)
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.show()

def plot_compare(df, group_col, target_col):
    cross_tab = pd.crosstab(df[group_col], df[target_col])
    ax = cross_tab.plot(kind="bar")
    plt.title(f"{target_col} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot(col):
     import matplotlib.pyplot as plt
     if col.dtype == 'category':
        title = input(f"Insert title for plot {col.name}: ")
        x_label = input(f"Insert x label for {title}: ")
        y_label = input(f"Insert y label for {title}: ")
        plt.figure()
        col.value_counts().plot(kind = "bar")
        ax = plt.gca()
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f"{int(height)}",(p.get_x() + p.get_width() / 2, height),ha="center", va="bottom")
        plt.locator_params(axis='y', integer=True)
        plt.title(f"{title}")
        plt.xlabel(f"{x_label}")
        plt.ylabel(f"{y_label}")
        plt.xticks(rotation=0)          
        plt.tight_layout()
        plt.savefig(f'{col.name}_distribution.png')
        plt.show()


def plot_menu (df, cat_col):
    while True:
          print("\nAvaiable categorical plots:")
          for i, col in enumerate(cat_col):
               print(f"{i} - {col}")
          try:
              plt_chooseINT = int(input("Insert the number for the plot: "))
              if 0 <= plt_chooseINT < len(cat_col):
                 plot(df[cat_col[plt_chooseINT]])
                 again = input("Do you want to see another plot? (Y/N): ").strip().lower()
                 if again == "n":
                     return
                 elif again == "y":
                     continue
                 else:
                    print("\033[91mPlease type Y or N\033[0m")
              else:
                  print("\033[91mInsert a corresponding number from the list\033[0m")
          except ValueError:
              print("\033[91mInvalid input - pleae enter a number\033[0m")

def plot_main_menu(df, cat_cols, compare_cols):
    while True:
        print("\nPlot Menu")
        print("1 - Simple categorical plot")
        print("2 - Comparison plot")
        print("Q - Quit")
        choice = input("Choose an option: ").strip().lower()
        if choice == "1":
            plot_menu(df, cat_cols)
        elif choice == "2":
            print("\nAvailable comparison plots:")
            for i, col in enumerate(compare_cols):
                print(f"{i} - {col}")
            try:
                target_idx = int(input("Select the variable to compare: "))
                if 0 <= target_idx < len(compare_cols):
                    target_col = compare_cols[target_idx]
                    pct = input("Do you want percentages instead of counts? (Y/N): ").strip().lower()
                    if pct == "y":
                        plot_compare_pct(df, "Survey", target_col)
                    else:
                        plot_compare(df, "Survey", target_col)
                else:
                    print("Insert a corresponding number from the list")
            except ValueError:
                print("\033[91mInvalid input - pleae enter a number\033[0m")
        elif choice == "q":
            break
        else:
            print("Please choose 1, 2 or Q")            
          
          
def plot_choice(df, cat_col):
    while True:
      choice = input('Do you want to see the plot? (Y/N): ').strip().lower()
      if choice == 'y':
        plot_menu(df, cat_col)
        break
      elif choice == 'n':
          break
      else:
          print("\033[91mPlease type Y or N\033[0m")