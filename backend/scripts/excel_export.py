import pandas as pd

def export_to_excel(data, output_path):
    df = pd.DataFrame(data, columns=['X', 'Y'])
    df.to_excel(output_path, index=False)

# Example usage
# data = [(x1, y1), (x2, y2)]
# output_file = 'output.xlsx'
# export_to_excel(data, output_file)
