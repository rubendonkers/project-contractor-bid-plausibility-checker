import pandas as pd
import os

input_path = 'tariflöhne.csv'
output_dir = '../clean'
output_path = os.path.join(output_dir, 'clean_tariflöhne.csv')

df = pd.read_csv(input_path)

# cleaning part
cols_to_fix = ["TL in €", "BZ in €", "GTL in €"]
for col in cols_to_fix:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# saving
clean_df = df[['Lohngruppe', 'GTL in €']].rename(columns={'GTL in €': 'GTL_Price'})
clean_df.to_csv(output_path, index=False)

print(f"Ready! Saved in {output_path}")