import re 
import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    valid_label = re.compile(r'^[a-zA-Z_]+$')

    if not valid_label.match(new_column):
        return pd.DataFrame([])
                            
                            
    
    if not all(valid_label.match(col) for col in df.columns):
        return pd.DataFrame([])
    
    match = re.match(r'^\s*([a-zA-Z_]+)\s*([+\-*])\s*([a-zA-Z_]+)\s*$', role)
    if not match:
        return pd.DataFrame([])
    
    col1, operator, col2 = match.groups()

    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])
    
    result = df.copy()
    if operator == '+':
        result[new_column] = df[col1] + df[col2]
    elif operator == '-':
        result[new_column] = df[col1] - df[col2]
    elif operator == '*':
        result[new_column] = df[col1] * df[col2]

    return result