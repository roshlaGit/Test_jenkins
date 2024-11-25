import pandas as pd
from fpdf import FPDF
import sys
import os

def csv_to_pdf(input_csv, output_pdf):
    # Check if the input file exists
    if not os.path.exists(input_csv):
        print(f"Input file does not exist: {input_csv}")
        return

    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Create a PDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt="CSV to PDF Conversion", ln=True, align='C')

    # Add content from the CSV
    pdf.set_font("Arial", size=12)
    for row in df.itertuples(index=False):
        pdf.cell(200, 10, txt=", ".join(map(str, row)), ln=True)

    # Save the PDF to the specified output
    pdf.output(output_pdf)
    print(f"PDF created successfully: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_csv_to_pdf.py <input_csv> <output_pdf>")
        sys.exit(1)

    input_csv_path = sys.argv[1]
    output_pdf_path = sys.argv[2]

    csv_to_pdf(input_csv_path, output_pdf_path)
