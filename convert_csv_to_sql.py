import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = 'companies.csv'  # Your CSV file path
table_name = 'companiesnames'  # Your target table name

df = pd.read_csv(csv_file_path)

# Strip any leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Ensure the column exists
if 'companynames' in df.columns:
    # Start the SQL file content
    sql_content = f"CREATE TABLE {table_name} (\n"
    sql_content += "  companynames TEXT\n"
    sql_content += ");\n\n"

    # Add insert statements
    for index, row in df.iterrows():
        company_name = str(row['companynames']).replace('"', '""')
        sql_content += f'INSERT INTO {table_name} (companynames) VALUES ("{company_name}");\n'

    # Save the SQL content to a file
    sql_file_path = 'output.sql'  # Your desired SQL file path
    with open(sql_file_path, 'w') as file:
        file.write(sql_content)

    print(f"SQL file has been created at: {sql_file_path}")
else:
    print("Error: 'companynames' column not found in the CSV file.")
