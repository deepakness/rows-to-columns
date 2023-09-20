import pandas as pd

def rearrange_data(input_file, column):
    # Load data from csv
    df = pd.read_csv(input_file)

    # Sorting the data based on the specified column
    df.sort_values(column, inplace=True)

    # Creating an empty DataFrame to store results
    max_items = df[column].value_counts().max()
    columns = [column]
    for i in range(max_items):
        for col in df.columns[df.columns != column]:
            columns.append(f'{col}_{i+1}')
    new_df = pd.DataFrame(columns=columns)

    # For each unique value in specified column, 
    # squeezing values into a series and append to a list
    data = []
    for value in df[column].unique():
        item_df = df[df[column]==value].drop(columns=column).reset_index(drop=True)
        item_data = pd.Series(dtype='object')
        item_data[column] = value
        for i, (_, row) in enumerate(item_df.iterrows()):
            for j, col in enumerate(item_df.columns):
                item_data[f'{col}_{i+1}'] = row[j]
        data.append(item_data)

    # Merge data into the DataFrame
    new_df = pd.DataFrame(data)

    # Saving the new DataFrame to a new CSV file whose name is based on the input file
    output_file = 'rearranged_' + input_file
    new_df.to_csv(output_file, index=False)
    
# Usage
rearrange_data('sample.csv', 'City')
