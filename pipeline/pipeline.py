import sys
print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

import pandas as pd

df = pd.DataFrame({"Car": [1, 2, 3, 4], "Passengers": [3, 4, 5, 6]})
df = pd.DataFrame({"Car": [1, 2, 3, 4], "Passengers": [3, 4, 5, 6]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")
