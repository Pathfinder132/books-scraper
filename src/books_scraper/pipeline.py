import pandas as pd

def save_data(df, csv_path, excel_path):
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    df.to_excel(excel_path, index=False)

def process_books(all_books):
    df = pd.DataFrame(all_books)
    df["price"] = pd.to_numeric(df["price"].str.replace("£",""), errors="coerce")
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    df = df.sort_values("price")
    df["rating"] = pd.to_numeric(df["rating"].map(rating_map),errors="coerce")


    assert len(df) == 1000 # assertions at end always
    assert df["title"].notna().all()
    assert df["rating"].between(1,5).all()
    assert df["price"].notna().all()

    
    return df