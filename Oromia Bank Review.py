from google_play_scraper import reviews_all, Sort
import pandas as pd

# Oromia Bank Mobile Banking App ID
app_id = "com.oromiabank.mobilebanking"

# Get ALL reviews
result = reviews_all(
    app_id,
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total reviews fetched:", len(result))

if len(result) == 0:
    print("❌ No reviews found")
else:
    df = pd.DataFrame(result)

    # Keep required columns
    df = df[[
        "userName",
        "reviewId",
        "content",
        "score",
        "at"
    ]]

    # Rename columns
    df.columns = [
        "name",
        "review_id",
        "review",
        "rating",
        "date"
    ]

    # Preview
    print("\nFirst 5 Reviews:")
    print(df.head())

    # Save CSV
    df.to_csv(
        "oromia_bank_reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\nSaved successfully!")