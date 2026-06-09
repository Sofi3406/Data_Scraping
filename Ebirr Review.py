from google_play_scraper import reviews_all, Sort
import pandas as pd

# Correct app ID
app_id = "com.safarifone.ebirr"

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
    print("❌ No reviews found")
else:
    df = pd.DataFrame(result)

    # Keep only required columns (safe version)
    available_cols = [
        "userName",
        "reviewId",
        "content",
        "score",
        "at"
    ]

    df = df[[col for col in available_cols if col in df.columns]]

    # Rename columns
    df.columns = ["name", "review_id", "review", "rating", "date"]

    # Preview
    print(df.head())

    # Save
    df.to_csv(
        "ebirr_reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Saved successfully!")