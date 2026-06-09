from google_play_scraper import reviews_all, Sort
import pandas as pd

# Awash Bank Mobile Banking App ID
app_id = "pegasus.project.awash.mobile.android.bundle.mobilebank"

# 🔥 Get ALL reviews (no 200 limit)
result = reviews_all(
    app_id,
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total reviews fetched:", len(result))

# Safety check
if len(result) == 0:
    print("❌ No reviews found (try removing country='et')")
else:
    df = pd.DataFrame(result)

    # Keep only needed columns safely
    cols = ["userName", "reviewId", "content", "score", "at"]
    df = df[[c for c in cols if c in df.columns]]

    # Rename columns
    df.columns = ["name", "review_id", "review", "rating", "date"]

    # Preview
    print(df.head())

    # Save file
    df.to_csv(
        "awash_bank_reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Saved successfully!")