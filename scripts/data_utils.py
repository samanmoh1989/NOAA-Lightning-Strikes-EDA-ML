import pandas as pd

def load_and_clean_data(path):
    """Load CSV, extract latitude and longitude from POINT geometry."""
    df = pd.read_csv(path)
    
    # Extract numeric values from 'POINT(lon lat)'
    df[['longitude', 'latitude']] = (
        df['center_point_geom']
        .str.extract(r'POINT\(([-\d.]+)\s+([-\d.]+)\)')
        .astype(float)
    )
    
    # Drop rows with missing coords
    df = df.dropna(subset=['latitude', 'longitude'])
    
    # Convert date
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    return df
