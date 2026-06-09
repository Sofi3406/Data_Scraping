from google_play_scraper import reviews_all, Sort
import pandas as pd

# Step 1: Scrape reviews
result = reviews_all(
    "com.combanketh.mobilebanking",
    lang="en",
    country="et",
    sort=Sort.NEWEST
)

print("Total Reviews:", len(result))

# Step 2: Convert to DataFrame
df = pd.DataFrame(result)

# Step 3: Check available columns
print("\nAvailable columns:")
print(df.columns)

# Step 4: Keep only required fields safely
df_clean = df[[
    "userName",
    "reviewId",
    "content",
    "score",
    "at"
]].copy()

# Step 5: Rename columns
df_clean.columns = [
    "name",
    "review_id",
    "review",
    "rating",
    "date"
]

# Step 6: Preview data
print("\nFirst 5 reviews:")
print(df_clean.head())

# Step 7: Save file
df_clean.to_csv(
    "cbe_mobile_reviews.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nSaved successfully!")
print("Final dataset size:", len(df_clean))