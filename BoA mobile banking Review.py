from google_play_scraper import reviews_all, Sort
import pandas as pd

# BoA Mobile Banking App ID
app_id = "com.boa.boaMobileBanking"

# 🔥 Get ALL reviews (not limited to 200)
result = reviews_all(
    app_id,
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total reviews fetched:", len(result))

# Safety check
if len(result) == 0:
    print("❌ No reviews found (try removing country='et' or check app ID)")
else:
    df = pd.DataFrame(result)

    # Keep only required fields safely
    cols = ["userName", "reviewId", "content", "score", "at"]
    df = df[[c for c in cols if c in df.columns]]

    # Rename columns
    df.columns = ["name", "review_id", "review", "rating", "date"]

    # Preview
    print(df.head())

    # Save file
    df.to_csv(
        "boa_mobile_reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Saved successfully!")