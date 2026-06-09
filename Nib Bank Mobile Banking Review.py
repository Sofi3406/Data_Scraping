from google_play_scraper import reviews_all, Sort
import pandas as pd

app_id = "com.nib.NibMobileBanking"

result = reviews_all(
    app_id,
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total reviews:", len(result))

df = pd.DataFrame(result)

df = df[["userName", "reviewId", "content", "score", "at"]]
df.columns = ["name", "review_id", "review", "rating", "date"]

df.to_csv("nib_bank_reviews.csv", index=False, encoding="utf-8-sig")
print(df.head())