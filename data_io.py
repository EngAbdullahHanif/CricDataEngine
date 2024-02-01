import pandas as pd

def save_to_csv(data, filename):
    """
    Save data to a CSV file using pandas.

    Parameters:
    - data: List of dictionaries representing the data.
    - filename: Name of the CSV file to be created or overwritten.

    Returns:
    - None
    """
    if not data:
        print("No data to save.")
        return

    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')

        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")
