import pandas as pd
import os
import PyPDF2

folder = r"c:\Users\sunni\OneDrive\Desktop\Data Science\Advance Excel\Projetcs\Coffee-Shop-sales-main\Coffee-Shop-sales-main"
excel_path = os.path.join(folder, "coffee shop sales.xlsx")
pdf_path = os.path.join(folder, "Coffee Shop Sales Analysis.pdf")

with open(os.path.join(folder, "output.txt"), "w", encoding="utf-8") as f:
    f.write("EXCEL INFO:\n")
    try:
        xl = pd.ExcelFile(excel_path)
        for sheet in xl.sheet_names:
            f.write(f"Sheet: {sheet}\n")
            try:
                df = xl.parse(sheet, nrows=5)
                f.write(f"Columns: {df.columns.tolist()}\n")
            except Exception as e:
                pass
    except Exception as e:
        f.write(f"Excel Error: {e}\n")
        
    f.write("\nPDF INFO:\n")
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for i in range(min(2, len(reader.pages))):
                f.write(f"Page {i}:\n")
                f.write(reader.pages[i].extract_text()[:1000] + "\n")
    except Exception as e:
        f.write(f"PDF Error: {e}\n")
