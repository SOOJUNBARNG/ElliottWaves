# データ操作
import pandas as pd

# 時間周りライブラリ
from datetime import datetime

# 本番ライブラリ
from elliottwaves import ElliottWaveFindPattern

# 時間データ
today = pd.to_datetime(datetime.today()).strftime('%Y-%m-%d')

# Load your data into a pandas DataFrame
df = pd.read_csv('./input_data/4188_mitsubishi.csv')

# Call the function
ElliottWaveFindPattern(df, 'close', 'D', '2020-01-01', today)
print(ElliottWaveFindPattern)