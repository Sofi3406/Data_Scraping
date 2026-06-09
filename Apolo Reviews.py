from google_play_scraper import reviews_all, Sort
import pandas as pd

app_id = "com.boa.apollo"

result = reviews_all(
    app_id,
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total reviews fetched:", len(result))

df = pd.DataFrame(result)

df = df[[
    "userName",
    "reviewId",
    "content",
    "score",
    "at"
]]

df.columns = [
    "name",
    "review_id",
    "review",
    "rating",
    "date"
]

print(df.head())

df.to_csv(
    "apollo_reviews_all.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Saved successfully!")