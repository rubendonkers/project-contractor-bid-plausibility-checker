import pandas as pd
import os

input_path = 'materials.csv'
output_dir = '../clean'
output_path = os.path.join(output_dir, 'clean_materials_final.csv')

df = pd.read_csv(input_path, sep=';')

# Make colums simpler (without space)
df = df.rename(columns={
    'Material': 'Material_ID',
    'Material short text': 'Item_Name',
    'Final net price': 'Price',
    'Price quantity unit net price': 'Unit',
    'Consumptions': 'Consumption'
})

# Cleaning up prices: replace commas with full stops and convert to numbers (floats)
df['Price'] = df['Price'].astype(str).str.replace(',', '.').astype(float)

# Fill in empty cells (prevent from crashing)
df['Consumption'] = df['Consumption'].fillna('Geen data')

# Save to clean directory
df.to_csv(output_path, index=False)

print(f"Ready! The file is saved in: {output_path}")