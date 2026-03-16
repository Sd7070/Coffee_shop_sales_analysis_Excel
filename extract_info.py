import os
import sys

def main():
    folder = r"c:\Users\sunni\OneDrive\Desktop\Data Science\Advance Excel\Projetcs\Coffee-Shop-sales-main\Coffee-Shop-sales-main"
    excel_path = os.path.join(folder, "coffee shop sales.xlsx")
    
    try:
        import pandas as pd
        print("Pandas loaded.")
        xl = pd.ExcelFile(excel_path)
        for sheet in xl.sheet_names:
            print(f"--- Sheet: {sheet}")
            try:
                df = xl.parse(sheet, nrows=5)
                print("Columns:", df.columns.tolist())
            except Exception as e:
                print(f"Error parsing sheet {sheet}: {e}")
    except ImportError:
        print("Pandas not installed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
