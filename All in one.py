from google_play_scraper import reviews_all, Sort
import pandas as pd
import os

# Create output folder
os.makedirs("reviews", exist_ok=True)

# Ethiopian Digital Finance Apps
apps = {
    "Telebirr": "cn.tydic.ethiopay",
    "CBE Mobile Banking": "com.combanketh.mobilebanking",
    "eBirr": "com.safarifone.ebirr",
    "BoA Mobile Banking": "com.boa.boaMobileBanking",
    "Apollo": "com.boa.apollo",
    "Awash Bank Mobile Banking": "pegasus.project.awash.mobile.android.bundle.mobilebank",
    "Nib Bank Mobile Banking": "com.nib.NibMobileBanking",
    "Dashen Super App": "com.dashen.dashensuperapp",
    "Oromia Bank Mobile Banking": "com.oromiabank.mobilebanking",
    "Coop Mobile Banking": "com.coopbankoromiasc.OLB",
    "Awash Birr Pro": "com.sc.awashpay"
}

all_reviews = []

for app_name, app_id in apps.items():

    print(f"\nScraping {app_name}...")
    
    try:
        result = reviews_all(
            app_id,
            lang="en",
            country="et",
            sort=Sort.NEWEST
        )

        print(f"Total reviews fetched: {len(result)}")

        if len(result) == 0:
            print(f"No reviews found for {app_name}")
            continue

        df = pd.DataFrame(result)

        required_cols = [
            "userName",
            "reviewId",
            "content",
            "score",
            "at"
        ]

        df = df[required_cols]

        df.columns = [
            "name",
            "review_id",
            "review",
            "rating",
            "date"
        ]

        # Add app name
        df["app_name"] = app_name

        # Save individual file
        filename = app_name.lower().replace(" ", "_").replace("+", "plus")
        df.to_csv(
            f"reviews/{filename}.csv",
            index=False,
            encoding="utf-8-sig"
        )

        # Add to master dataset
        all_reviews.append(df)

        print(f"Saved: {filename}.csv")

    except Exception as e:
        print(f"Error scraping {app_name}: {e}")

# Combine all apps
if len(all_reviews) > 0:

    master_df = pd.concat(all_reviews, ignore_index=True)

    master_df.to_csv(
        "reviews/all_ethiopian_finance_apps_reviews.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("\n===================================")
    print("MASTER DATASET CREATED")
    print("===================================")
    print("Total Reviews:", len(master_df))
    print("Total Apps:", master_df["app_name"].nunique())

    print("\nReviews per App:")
    print(master_df["app_name"].value_counts())

else:
    print("No reviews were collected.")