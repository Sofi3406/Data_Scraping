from google_play_scraper import reviews_all, Sort
import pandas as pd

result = reviews_all(
    "cn.tydic.ethiopay",
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Available fields:")
print(result[0].keys())

df = pd.DataFrame(result)

print("\nTotal Reviews:", len(df))

print("\nFirst 5 Reviews:")
print(df.head())

df.to_csv(
    "telebirr_reviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nSaved successfully!")