"""
Netflix Data Export Script
Processes netflix_titles.csv and exports JSON data files for the website dashboard.
"""
import pandas as pd
import json
import os


def export_data():
    """Process the Netflix dataset and export JSON files for the web dashboard."""
    os.makedirs('website/data', exist_ok=True)
    
    # Load dataset
    df = pd.read_csv('netflix_titles.csv')
    print(f"Loaded {len(df):,} records")
    
    # Parse dates
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y', errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    
    # Clean country
    df['primary_country'] = df['country'].apply(
        lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Unknown'
    )
    
    # Split genres
    df['genres'] = df['listed_in'].apply(lambda x: [g.strip() for g in str(x).split(',')])
    
    # ─── Export 1: Content by Year (Q1) ───
    yearly = df[(df['year_added'] >= 2011) & (df['year_added'] <= 2021)]
    yearly_type = pd.crosstab(yearly['year_added'], yearly['type'])
    content_by_year = {
        'years': [int(y) for y in yearly_type.index],
        'movies': [int(v) for v in yearly_type.get('Movie', [])],
        'tv_shows': [int(v) for v in yearly_type.get('TV Show', [])]
    }
    with open('website/data/content_by_year.json', 'w') as f:
        json.dump(content_by_year, f, indent=2)
    print("  Exported content_by_year.json")
    
    # ─── Export 2: Countries (Q2) ───
    country_counts = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts()
    countries_data = [{'Country': c, 'Count': int(v)} for c, v in country_counts.head(15).items()]
    with open('website/data/countries.json', 'w') as f:
        json.dump(countries_data, f, indent=2)
    print("  Exported countries.json")
    
    # ─── Export 3: Genres (Q3) ───
    genre_combos = df['listed_in'].value_counts()
    all_genres = [g for sublist in df['genres'] for g in sublist]
    genre_freq = pd.Series(all_genres).value_counts()
    
    genres_data = {
        'combinations': {k: int(v) for k, v in genre_combos.head(20).items()},
        'individual': {k: int(v) for k, v in genre_freq.head(20).items()}
    }
    with open('website/data/genres.json', 'w') as f:
        json.dump(genres_data, f, indent=2)
    print("  Exported genres.json")
    
    # ─── Export 4: Overview Stats ───
    overview = {
        'total_titles': int(df.shape[0]),
        'total_movies': int(df[df['type'] == 'Movie'].shape[0]),
        'total_tv_shows': int(df[df['type'] == 'TV Show'].shape[0]),
        'total_countries': int(country_counts.shape[0]),
        'total_genre_combos': int(genre_combos.shape[0]),
        'total_individual_genres': int(genre_freq.shape[0]),
        'year_min': int(df['release_year'].min()),
        'year_max': int(df['release_year'].max()),
    }
    with open('website/data/overview_stats.json', 'w') as f:
        json.dump(overview, f, indent=2)
    print("  Exported overview_stats.json")
    
    print(f"\nAll data exported to website/data/")


if __name__ == '__main__':
    export_data()
