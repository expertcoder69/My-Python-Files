import pandas as pd

def json_to_excel(json_file, excel_file):
  """
  Converts a JSON file to an Excel spreadsheet.

  Args:
    json_file: The path to the JSON file.
    excel_file: The path to the output Excel file.
  """

  # Read the JSON file into a pandas DataFrame
  df = pd.read_json(json_file)

  # Write the DataFrame to an Excel file
  df.to_excel(excel_file, index=False)

if _name_ == "_main_":
  json_file = "your_json_file.json"  # Replace with your JSON file path
  excel_file = "output.xlsx"  # Replace with your desired Excel file name

  json_to_excel(json_file, excel_file)
  print("JSON file converted to Excel successfully!")