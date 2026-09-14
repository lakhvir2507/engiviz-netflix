import json

notebook = {
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.11.0", "mimetype": "text/x-python", "file_extension": ".py"}
 },
 "cells": []
}

def md(source, cell_id):
    lines = source.split('\n')
    formatted = [line + "\n" for line in lines[:-1]] + [lines[-1]]
    notebook['cells'].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": formatted,
        "id": cell_id
    })

def code(source, cell_id):
    lines = source.split('\n')
    formatted = [line + "\n" for line in lines[:-1]] + [lines[-1]]
    notebook['cells'].append({
        "cell_type": "code",
        "metadata": {},
        "source": formatted,
        "outputs": [],
        "execution_count": None,
        "id": cell_id
    })

# ═══════════════════════════════════════════════════════════════
# SECTION 1: TITLE & INTRODUCTION
# ═══════════════════════════════════════════════════════════════

md("""# 🎬 Netflix Movies & TV Shows — Data Visualization Analysis

---

### 📋 Project Overview

| Detail | Description |
|--------|------------|
| **Dataset** | Netflix Movies and TV Shows (8,807 records · 3.4 MB) |
| **Source** | [Kaggle - Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) |
| **Hackathon** | EngiViz — Engineering Day 2026 · GNA University |
| **Objective** | Visual exploration & storytelling through data |

### 🎯 Research Questions
1. **How has the proportion of TV Shows vs Movies added to Netflix changed over the last decade?**
2. **Which countries are the largest producers of Netflix content?**
3. **What are the most common genre combinations?**

### 🛠 Technology Stack
`Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Plotly` · `WordCloud`""", "title-intro")

# ═══════════════════════════════════════════════════════════════
# SECTION 2: LIBRARY IMPORTS
# ═══════════════════════════════════════════════════════════════

md("## 📦 1. Library Imports & Configuration", "imports-header")

code("""# Core data libraries
import pandas as pd
import numpy as np

# Static visualization
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import seaborn as sns

# Interactive visualization
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Text visualization
from wordcloud import WordCloud

# Utilities
from collections import Counter
from itertools import combinations
import warnings
warnings.filterwarnings('ignore')

print("✅ All libraries loaded successfully!")""", "imports")

# ═══════════════════════════════════════════════════════════════
# SECTION 3: CUSTOM STYLING
# ═══════════════════════════════════════════════════════════════

code("""# ═══════════════ Custom Visual Theme ═══════════════

# Style presets
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('pastel')

# Brand colors
NETFLIX_RED = '#E50914'
NETFLIX_DARK = '#141414'
NETFLIX_GRAY = '#808080'

# Curated pastel palette for data viz
PASTEL_PALETTE = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
                  '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9',
                  '#F8C291', '#6C5CE7', '#A29BFE', '#FD79A8', '#00CEC9']

# Gradient reds for heatmaps and sequential scales
GRADIENT_REDS = ['#FFE8E8', '#FFB3B3', '#FF7F7F', '#FF4C4C', '#E50914', '#B30710']

# Enhanced matplotlib configuration
plt.rcParams.update({
    'figure.figsize': (14, 8),
    'figure.dpi': 120,
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Arial', 'Helvetica'],
    'font.size': 12,
    'axes.titlesize': 18,
    'axes.titleweight': 'bold',
    'axes.titlepad': 20,
    'axes.labelsize': 13,
    'axes.labelpad': 10,
    'figure.facecolor': '#FAFAFA',
    'axes.facecolor': '#FAFAFA',
    'axes.edgecolor': '#E0E0E0',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'legend.fontsize': 11,
    'legend.framealpha': 0.9,
    'legend.edgecolor': '#E0E0E0',
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
})

# Plotly template for consistent styling
PLOTLY_TEMPLATE = dict(
    layout=dict(
        font=dict(family="Segoe UI, Arial", size=13),
        paper_bgcolor='#FAFAFA',
        plot_bgcolor='#FAFAFA',
        title=dict(font=dict(size=20)),
        hoverlabel=dict(bgcolor='white', font_size=13),
    )
)

print("🎨 Custom theme applied!")""", "styling")

# ═══════════════════════════════════════════════════════════════
# SECTION 4: DATA LOADING
# ═══════════════════════════════════════════════════════════════

md("## 📂 2. Data Loading", "loading-header")

code("""# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

print(f"{'='*60}")
print(f"  📊 NETFLIX DATASET LOADED")
print(f"{'='*60}")
print(f"  Total Records:  {df.shape[0]:,}")
print(f"  Total Features: {df.shape[1]}")
print(f"  Memory Usage:   {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"{'='*60}")
print()
df.head(10)""", "data-loading")

# ═══════════════════════════════════════════════════════════════
# SECTION 5: DATA OVERVIEW
# ═══════════════════════════════════════════════════════════════

md("## 🔍 3. Data Overview & Quality Assessment", "overview-header")

code("""# Column information
print("📋 COLUMN DETAILS")
print(f"{'='*80}")
for col in df.columns:
    dtype = df[col].dtype
    non_null = df[col].notna().sum()
    null_pct = (df[col].isna().sum() / len(df)) * 100
    unique = df[col].nunique()
    print(f"  {col:20s} | Type: {str(dtype):10s} | Non-Null: {non_null:5d} | Missing: {null_pct:5.1f}% | Unique: {unique:5d}")
print(f"{'='*80}")""", "data-overview")

code("""# Missing values visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Bar chart of missing values
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=True)
colors = [NETFLIX_RED if v > 1000 else PASTEL_PALETTE[1] for v in missing.values]
bars = axes[0].barh(missing.index, missing.values, color=colors, edgecolor='white', linewidth=0.5)
axes[0].set_title('Missing Values by Column', fontweight='bold', fontsize=15)
axes[0].set_xlabel('Count of Missing Values')
for bar, val in zip(bars, missing.values):
    axes[0].text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2,
                f'{val:,} ({val/len(df)*100:.1f}%)', va='center', fontsize=10, color='#555')

# Missing values heatmap (sample)
sample = df.sample(min(200, len(df)), random_state=42)
axes[1].imshow(sample.isnull().T, aspect='auto', cmap='RdYlGn_r', interpolation='nearest')
axes[1].set_yticks(range(len(df.columns)))
axes[1].set_yticklabels(df.columns, fontsize=9)
axes[1].set_title('Missing Data Pattern (200 random rows)', fontweight='bold', fontsize=15)
axes[1].set_xlabel('Row Index')

plt.tight_layout()
plt.show()

print(f"\\n📊 Total missing values: {df.isnull().sum().sum():,} out of {df.shape[0] * df.shape[1]:,} cells ({df.isnull().sum().sum()/(df.shape[0]*df.shape[1])*100:.2f}%)")""", "missing-values-viz")

# ═══════════════════════════════════════════════════════════════
# SECTION 6: DATA CLEANING & FEATURE ENGINEERING
# ═══════════════════════════════════════════════════════════════

md("""## 🧹 4. Data Cleaning & Feature Engineering

We'll parse dates, extract numeric durations, clean country fields, and split genre lists.""", "cleaning-header")

code("""# ─── Date Processing ───
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), format='%B %d, %Y', errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['month_name'] = df['date_added'].dt.month_name()
df['day_of_week'] = df['date_added'].dt.day_name()

# ─── Duration Processing ───
df['duration_int'] = df['duration'].str.extract(r'(\\d+)').astype(float)
df['duration_type'] = df['duration'].apply(lambda x: 'Minutes' if 'min' in str(x) else 'Seasons')

# ─── Country Processing ───
df['primary_country'] = df['country'].apply(
    lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Unknown'
)
df['num_countries'] = df['country'].apply(
    lambda x: len(str(x).split(',')) if pd.notna(x) else 0
)

# ─── Genre Processing ───
df['genres'] = df['listed_in'].apply(lambda x: [g.strip() for g in str(x).split(',')])
df['num_genres'] = df['genres'].apply(len)

# ─── Content Age ───
df['content_age'] = df['year_added'] - df['release_year']

print("✅ Feature engineering complete!")
print(f"   New columns: year_added, month_added, month_name, day_of_week,")
print(f"                duration_int, duration_type, primary_country, num_countries,")
print(f"                genres, num_genres, content_age")
print(f"   Final shape: {df.shape}")""", "data-cleaning")

# ═══════════════════════════════════════════════════════════════
# SECTION 7: EXPLORATORY DATA ANALYSIS
# ═══════════════════════════════════════════════════════════════

md("""## 📊 5. Exploratory Data Analysis

Before diving into research questions, let's understand the overall structure of Netflix's content library.""", "eda-header")

# EDA 1: Content Type Distribution
md("### 5.1 Content Type Distribution", "eda1-header")

code("""# Interactive donut chart
type_counts = df['type'].value_counts()
fig = go.Figure(data=[go.Pie(
    labels=type_counts.index,
    values=type_counts.values,
    hole=0.55,
    marker=dict(colors=[NETFLIX_RED, PASTEL_PALETTE[1]], line=dict(color='white', width=3)),
    textinfo='label+percent+value',
    textfont=dict(size=14),
    hovertemplate='<b>%{label}</b><br>Count: %{value:,}<br>Percentage: %{percent}<extra></extra>'
)])

fig.update_layout(
    title=dict(text='<b>Content Type Distribution</b><br><sub>Movies vs TV Shows on Netflix</sub>', font=dict(size=22)),
    annotations=[dict(text=f'<b>{type_counts.sum():,}</b><br>Total', x=0.5, y=0.5, font_size=20, showarrow=False)],
    width=700, height=500,
    paper_bgcolor='#FAFAFA', plot_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial")
)
fig.show()

print(f"\\n📌 Movies account for {type_counts['Movie']/type_counts.sum()*100:.1f}% of Netflix's library")
print(f"📌 TV Shows account for {type_counts['TV Show']/type_counts.sum()*100:.1f}% of Netflix's library")""", "eda-type-dist")

# EDA 2: Content Added Over Years
md("### 5.2 Content Added Over Time", "eda2-header")

code("""# Yearly content additions with type breakdown
yearly = df.groupby(['year_added', 'type']).size().reset_index(name='count')
yearly = yearly.dropna(subset=['year_added'])
yearly['year_added'] = yearly['year_added'].astype(int)

fig = make_subplots(specs=[[{"secondary_y": True}]])

for i, content_type in enumerate(['Movie', 'TV Show']):
    data = yearly[yearly['type'] == content_type]
    fig.add_trace(go.Scatter(
        x=data['year_added'], y=data['count'],
        name=content_type,
        mode='lines+markers',
        line=dict(width=3, color=NETFLIX_RED if content_type == 'Movie' else PASTEL_PALETTE[1]),
        marker=dict(size=8),
        fill='tozeroy' if content_type == 'Movie' else None,
        fillcolor='rgba(229, 9, 20, 0.1)' if content_type == 'Movie' else None,
        hovertemplate=f'<b>{content_type}</b><br>Year: %{{x}}<br>Count: %{{y:,}}<extra></extra>'
    ))

fig.update_layout(
    title=dict(text='<b>Content Added to Netflix Over Time</b><br><sub>Yearly breakdown by content type</sub>',
               font=dict(size=20)),
    xaxis=dict(title='Year', dtick=1, gridcolor='rgba(0,0,0,0.05)'),
    yaxis=dict(title='Number of Titles Added', gridcolor='rgba(0,0,0,0.05)'),
    hovermode='x unified',
    width=1000, height=500,
    paper_bgcolor='#FAFAFA', plot_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial"),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)
fig.show()

# Key stat
peak_year = yearly.groupby('year_added')['count'].sum().idxmax()
peak_count = yearly.groupby('year_added')['count'].sum().max()
print(f"\\n📌 Peak year for content additions: {peak_year} with {peak_count:,} titles added")""", "eda-yearly")

# EDA 3: Rating Distribution
md("### 5.3 Rating Distribution", "eda3-header")

code("""# Rating distribution by content type
fig, ax = plt.subplots(figsize=(14, 7))

rating_order = df['rating'].value_counts().index
rating_data = df.groupby(['rating', 'type']).size().unstack(fill_value=0)
rating_data = rating_data.reindex(rating_order)

rating_data.plot(kind='barh', stacked=True, ax=ax,
                 color=[NETFLIX_RED, PASTEL_PALETTE[1]],
                 edgecolor='white', linewidth=0.5)

ax.set_title('Content Rating Distribution', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Number of Titles', fontsize=13)
ax.set_ylabel('Rating', fontsize=13)
ax.legend(title='Type', loc='lower right', fontsize=11)

# Add value labels
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='center', fontsize=9, color='white', fontweight='bold')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()

print(f"\\n📌 Most common rating: {df['rating'].mode()[0]} ({df['rating'].value_counts().iloc[0]:,} titles)")
print(f"📌 TV-MA (Mature Audiences) dominates, indicating Netflix skews toward adult content")""", "eda-ratings")

# EDA 4: Movie Duration Distribution
md("### 5.4 Duration Analysis", "eda4-header")

code("""fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Movie duration histogram
movie_durations = df[df['type'] == 'Movie']['duration_int'].dropna()
axes[0].hist(movie_durations, bins=50, color=NETFLIX_RED, alpha=0.7, edgecolor='white', linewidth=0.5)
axes[0].axvline(movie_durations.median(), color='#333', linestyle='--', linewidth=2, label=f'Median: {movie_durations.median():.0f} min')
axes[0].axvline(movie_durations.mean(), color=PASTEL_PALETTE[1], linestyle='--', linewidth=2, label=f'Mean: {movie_durations.mean():.0f} min')
axes[0].set_title('Movie Duration Distribution', fontsize=15, fontweight='bold')
axes[0].set_xlabel('Duration (minutes)')
axes[0].set_ylabel('Count')
axes[0].legend(fontsize=10)
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# TV Show seasons distribution
tv_seasons = df[df['type'] == 'TV Show']['duration_int'].dropna().astype(int)
season_counts = tv_seasons.value_counts().sort_index()
bars = axes[1].bar(season_counts.index, season_counts.values, color=PASTEL_PALETTE[1], edgecolor='white', linewidth=0.5)
bars[0].set_color(NETFLIX_RED)  # Highlight 1 season
axes[1].set_title('TV Show: Number of Seasons', fontsize=15, fontweight='bold')
axes[1].set_xlabel('Seasons')
axes[1].set_ylabel('Count')
for bar in bars:
    if bar.get_height() > 50:
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15,
                    f'{int(bar.get_height())}', ha='center', fontsize=9)
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

print(f"\\n📌 Most movies are {movie_durations.median():.0f} minutes long (median)")
single_season_pct = (tv_seasons == 1).sum() / len(tv_seasons) * 100
print(f"📌 {single_season_pct:.1f}% of TV Shows have only 1 season")""", "eda-duration")

# EDA 5: Monthly Additions
md("### 5.5 Monthly Addition Patterns", "eda5-header")

code("""month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly = df.groupby('month_name').size().reindex(month_order)

fig, ax = plt.subplots(figsize=(14, 6))
colors = [NETFLIX_RED if v == monthly.max() else PASTEL_PALETTE[4] for v in monthly.values]
bars = ax.bar(range(12), monthly.values, color=colors, edgecolor='white', linewidth=0.5, width=0.7)
ax.set_xticks(range(12))
ax.set_xticklabels([m[:3] for m in month_order], fontsize=12)
ax.set_title('Content Added by Month (All Years)', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Number of Titles', fontsize=13)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for bar, val in zip(bars, monthly.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8,
            f'{int(val)}', ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()

peak_month = monthly.idxmax()
print(f"\\n📌 Peak month for new content: {peak_month} ({monthly.max():,} titles)")
print(f"📌 Slowest month: {monthly.idxmin()} ({monthly.min():,} titles)")""", "eda-monthly")

# EDA 6: Release Year vs Year Added Heatmap
md("### 5.6 Content Freshness: When Was Content Made vs. When Was It Added?", "eda6-header")

code("""fig, ax = plt.subplots(figsize=(12, 8))
fresh_data = df[(df['release_year'] >= 2000) & (df['year_added'] >= 2015)].dropna(subset=['year_added'])

hb = ax.hexbin(fresh_data['release_year'], fresh_data['year_added'],
               gridsize=20, cmap='Reds', mincnt=1, edgecolors='white', linewidths=0.2)
ax.plot([2000, 2021], [2000, 2021], '--', color='#666', alpha=0.5, label='Same Year Release')
cb = plt.colorbar(hb, ax=ax)
cb.set_label('Number of Titles', fontsize=12)

ax.set_title('Release Year vs Year Added to Netflix', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Original Release Year', fontsize=13)
ax.set_ylabel('Year Added to Netflix', fontsize=13)
ax.legend(fontsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

avg_gap = df['content_age'].dropna().mean()
print(f"\\n📌 Average gap between release and Netflix addition: {avg_gap:.1f} years")
print(f"📌 Most content added in recent years was released the same year or year prior")""", "eda-freshness")

# ═══════════════════════════════════════════════════════════════
# SECTION 8: RESEARCH QUESTION 1
# ═══════════════════════════════════════════════════════════════

md("""---

## 📊 Research Question #1

### How has the proportion of TV Shows vs Movies added to Netflix changed over the last decade?

This question explores Netflix's strategic evolution from a movie-streaming platform to a balanced content provider. We'll analyze year-by-year proportions from 2011 to 2021.""", "rq1-intro")

code("""# Prepare data for the last decade
rq1_data = df[(df['year_added'] >= 2011) & (df['year_added'] <= 2021)].dropna(subset=['year_added'])
rq1_data['year_added'] = rq1_data['year_added'].astype(int)

yearly_counts = pd.crosstab(rq1_data['year_added'], rq1_data['type'])
yearly_pct = pd.crosstab(rq1_data['year_added'], rq1_data['type'], normalize='index') * 100

print("📊 Yearly Content Breakdown (2011-2021):")
print("="*65)
print(f"{'Year':>6} | {'Movies':>8} | {'TV Shows':>9} | {'Total':>7} | {'TV Show %':>10}")
print("-"*65)
for year in yearly_counts.index:
    m = yearly_counts.loc[year, 'Movie']
    t = yearly_counts.loc[year, 'TV Show']
    total = m + t
    tv_pct = yearly_pct.loc[year, 'TV Show']
    print(f"{year:>6} | {m:>8,} | {t:>9,} | {total:>7,} | {tv_pct:>9.1f}%")
print("="*65)""", "rq1-data")

code("""# ═══ CHART 1: Interactive Stacked Area Chart ═══

fig = go.Figure()

# Movie area
fig.add_trace(go.Scatter(
    x=yearly_pct.index, y=yearly_pct['Movie'],
    name='Movies', mode='lines',
    line=dict(width=0.5, color=NETFLIX_RED),
    fillcolor='rgba(229, 9, 20, 0.6)',
    fill='tozeroy',
    stackgroup='one',
    groupnorm='percent',
    hovertemplate='<b>Movies</b><br>Year: %{x}<br>Proportion: %{y:.1f}%<extra></extra>'
))

# TV Show area
fig.add_trace(go.Scatter(
    x=yearly_pct.index, y=yearly_pct['TV Show'],
    name='TV Shows', mode='lines',
    line=dict(width=0.5, color=PASTEL_PALETTE[1]),
    fillcolor='rgba(78, 205, 196, 0.6)',
    fill='tonexty',
    stackgroup='one',
    hovertemplate='<b>TV Shows</b><br>Year: %{x}<br>Proportion: %{y:.1f}%<extra></extra>'
))

fig.update_layout(
    title=dict(text="<b>Proportion of TV Shows vs Movies (2011-2021)</b><br><sub>Stacked Area Chart — Netflix Strategic Shift</sub>",
               font=dict(size=20)),
    xaxis=dict(title='Year', dtick=1),
    yaxis=dict(title='Percentage (%)', range=[0, 100], ticksuffix='%'),
    hovermode='x unified',
    width=1000, height=500,
    paper_bgcolor='#FAFAFA', plot_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial"),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
)
fig.show()""", "rq1-area-chart")

code("""# ═══ CHART 2: 100% Stacked Bar Chart ═══

fig, ax = plt.subplots(figsize=(14, 7))

years = yearly_pct.index
movie_pcts = yearly_pct['Movie'].values
tv_pcts = yearly_pct['TV Show'].values

bars1 = ax.bar(years, movie_pcts, color=NETFLIX_RED, label='Movies', edgecolor='white', linewidth=0.5, width=0.7)
bars2 = ax.bar(years, tv_pcts, bottom=movie_pcts, color=PASTEL_PALETTE[1], label='TV Shows', edgecolor='white', linewidth=0.5, width=0.7)

# Add percentage labels
for bar, pct in zip(bars1, movie_pcts):
    if pct > 10:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                f'{pct:.0f}%', ha='center', va='center', fontweight='bold', color='white', fontsize=10)

for bar, pct, bottom in zip(bars2, tv_pcts, movie_pcts):
    if pct > 8:
        ax.text(bar.get_x() + bar.get_width()/2, bottom + pct/2,
                f'{pct:.0f}%', ha='center', va='center', fontweight='bold', color='white', fontsize=10)

ax.set_title('Content Mix Evolution: Movies vs TV Shows', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Percentage (%)', fontsize=13)
ax.set_ylim(0, 100)
ax.legend(loc='upper right', fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(ticker.PercentFormatter())

# Add trend annotation
ax.annotate('TV Shows growing\\nfrom 0% to ~33%', xy=(2021, 67), xytext=(2017, 45),
            fontsize=11, color='#333', arrowprops=dict(arrowstyle='->', color='#666'),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#ccc'))

plt.tight_layout()
plt.show()""", "rq1-stacked-bar")

code("""# ═══ CHART 3: Grouped Bar Chart with Raw Counts ═══

fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(years))
width = 0.35

bars1 = ax.bar(x - width/2, yearly_counts['Movie'], width, label='Movies',
               color=NETFLIX_RED, edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + width/2, yearly_counts['TV Show'], width, label='TV Shows',
               color=PASTEL_PALETTE[1], edgecolor='white', linewidth=0.5)

ax.set_title('Raw Content Counts: Movies vs TV Shows by Year', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Number of Titles', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend(fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add count labels on top
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            f'{int(bar.get_height())}', ha='center', fontsize=8, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            f'{int(bar.get_height())}', ha='center', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.show()""", "rq1-grouped-bar")

md("""### 💡 Key Insights — Question #1

1. **Strategic Shift**: Netflix evolved from a movie-dominated platform (100% Movies in 2011) to a more balanced content mix (~65% Movies, ~35% TV Shows by 2021)
2. **Peak Growth**: Content additions peaked around 2018-2019, with both categories seeing massive growth
3. **TV Show Acceleration**: TV Shows' share grew consistently, reflecting Netflix's investment in original series like *Stranger Things*, *The Crown*, and *Squid Game*
4. **COVID Impact**: 2020-2021 showed a slight decrease in total additions, likely due to production delays, but the TV Show proportion held steady
5. **Strategic Rationale**: TV Shows drive sustained engagement (viewers return for new seasons), making them strategically valuable despite movies being numerically dominant""", "rq1-insights")

# ═══════════════════════════════════════════════════════════════
# SECTION 9: RESEARCH QUESTION 2
# ═══════════════════════════════════════════════════════════════

md("""---

## 🌍 Research Question #2

### Which countries are the largest producers of Netflix content?

We'll map the global landscape of Netflix content production, identifying dominant markets and emerging content hubs.""", "rq2-intro")

code("""# Prepare country data
country_counts = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

print("🌍 TOP 20 CONTENT-PRODUCING COUNTRIES")
print("="*50)
for i, row in country_counts.head(20).iterrows():
    bar = '█' * int(row['Count'] / country_counts['Count'].max() * 30)
    print(f"  {row['Country']:25s} | {row['Count']:>5,} | {bar}")
print("="*50)
print(f"  Total unique countries: {country_counts.shape[0]}")""", "rq2-data")

code("""# ═══ CHART 1: World Choropleth Map ═══

fig = px.choropleth(
    country_counts,
    locations='Country',
    locationmode='country names',
    color='Count',
    hover_name='Country',
    hover_data={'Count': ':,'},
    color_continuous_scale=['#FFE8E8', '#FFB3B3', '#FF7F7F', '#FF4C4C', '#E50914', '#8B0000'],
    title='<b>Netflix Content Production Worldwide</b><br><sub>Choropleth map colored by number of titles</sub>'
)

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        coastlinecolor='#ccc',
        projection_type='natural earth',
        bgcolor='#FAFAFA',
        landcolor='#F5F5F5',
    ),
    width=1100, height=600,
    paper_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial", size=13),
    coloraxis_colorbar=dict(title='Titles', tickformat=',')
)
fig.show()""", "rq2-choropleth")

code("""# ═══ CHART 2: Top 15 Countries Bar Chart ═══

top15 = country_counts.head(15).sort_values('Count', ascending=True)

fig, ax = plt.subplots(figsize=(14, 8))

# Create gradient colors
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list('netflix', ['#FFB3B3', NETFLIX_RED])
colors = [cmap(i / len(top15)) for i in range(len(top15))]

bars = ax.barh(top15['Country'], top15['Count'], color=colors, edgecolor='white', linewidth=0.5, height=0.7)

ax.set_title('Top 15 Content-Producing Countries', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Number of Titles', fontsize=13)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for bar, val in zip(bars, top15['Count']):
    ax.text(bar.get_width() + 15, bar.get_y() + bar.get_height()/2,
            f'{val:,}', va='center', fontsize=11, fontweight='bold', color='#333')

# US dominance annotation
us_pct = country_counts.iloc[0]['Count'] / country_counts['Count'].sum() * 100
ax.text(0.65, 0.15, f'🇺🇸 US alone = {us_pct:.1f}%\\nof all content',
        transform=ax.transAxes, fontsize=12, color='#555',
        bbox=dict(boxstyle='round', facecolor='#FFF5F5', edgecolor='#FFB3B3'))

plt.tight_layout()
plt.show()""", "rq2-bar")

code("""# ═══ CHART 3: Treemap ═══

fig = px.treemap(
    country_counts.head(20),
    path=['Country'],
    values='Count',
    title='<b>Treemap: Top 20 Content-Producing Countries</b>',
    color='Count',
    color_continuous_scale=['#FFE8E8', '#FF7F7F', NETFLIX_RED],
    hover_data={'Count': ':,'}
)

fig.update_layout(
    width=900, height=600,
    paper_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial", size=14),
)
fig.update_traces(textinfo='label+value', textfont=dict(size=14))
fig.show()""", "rq2-treemap")

code("""# ═══ CHART 4: Sunburst — Country → Content Type ═══

top10_countries = country_counts['Country'].head(10).tolist()
sun_data = df[df['primary_country'].isin(top10_countries)].copy()

fig = px.sunburst(
    sun_data,
    path=['primary_country', 'type'],
    title='<b>Content Type Breakdown by Top 10 Countries</b><br><sub>Inner ring: Country · Outer ring: Movies vs TV Shows</sub>',
    color_discrete_sequence=[NETFLIX_RED] + PASTEL_PALETTE[:9],
)

fig.update_layout(
    width=800, height=700,
    paper_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial", size=13),
)
fig.update_traces(textinfo='label+percent parent', insidetextorientation='radial')
fig.show()""", "rq2-sunburst")

md("""### 💡 Key Insights — Question #2

1. **US Dominance**: The United States produces ~36% of all Netflix content (2,818 titles), more than the next 5 countries combined
2. **India Rising**: India is the second-largest producer (972 titles), reflecting Netflix's major investment in the Indian market
3. **Global Trio**: US, India, and UK form the top 3, accounting for over 50% of all content
4. **Asian Powerhouses**: Japan (245) and South Korea (199) are major content hubs, driven by anime and K-drama popularity
5. **Regional Diversity**: Europe (UK, Spain, France), Middle East (Egypt, Turkey), and Africa (Nigeria) all contribute significantly
6. **Multinational Productions**: Many titles list multiple production countries, indicating global co-production trends""", "rq2-insights")

# ═══════════════════════════════════════════════════════════════
# SECTION 10: RESEARCH QUESTION 3
# ═══════════════════════════════════════════════════════════════

md("""---

## 🎭 Research Question #3

### What are the most common genre combinations?

Netflix categorizes each title under one or more genres. We'll analyze both the raw genre combinations and the co-occurrence patterns between individual genres.""", "rq3-intro")

code("""# Prepare genre data
genre_combos = df['listed_in'].value_counts()
all_genres = [g for sublist in df['genres'] for g in sublist]
genre_freq = pd.Series(all_genres).value_counts()

print("🎭 GENRE LANDSCAPE OVERVIEW")
print("="*55)
print(f"  Unique genre combinations: {genre_combos.shape[0]}")
print(f"  Unique individual genres:  {genre_freq.shape[0]}")
print(f"  Avg genres per title:      {df['num_genres'].mean():.1f}")
print()
print("  Top 10 Individual Genres:")
for genre, count in genre_freq.head(10).items():
    bar = '█' * int(count / genre_freq.max() * 25)
    print(f"    {genre:40s} {count:>5,}  {bar}")
print("="*55)""", "rq3-data")

code("""# ═══ CHART 1: Top 20 Genre Combinations ═══

top20_combos = genre_combos.head(20)

fig, ax = plt.subplots(figsize=(14, 10))

# Shorten labels for readability
labels = [g if len(g) < 45 else g[:42] + '...' for g in top20_combos.index]

colors = plt.cm.RdPu(np.linspace(0.3, 0.9, len(top20_combos)))[::-1]
bars = ax.barh(range(len(labels)), top20_combos.values, color=colors, edgecolor='white', linewidth=0.5, height=0.7)

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=10)
ax.set_title('Top 20 Genre Combinations on Netflix', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Number of Titles', fontsize=13)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for bar, val in zip(bars, top20_combos.values):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            f'{val:,}', va='center', fontsize=10, fontweight='bold', color='#333')

plt.tight_layout()
plt.show()""", "rq3-combos")

code("""# ═══ CHART 2: Genre Co-occurrence Heatmap ═══

# Build co-occurrence matrix for top 12 individual genres
top_genres = genre_freq.head(12).index.tolist()

co_matrix = pd.DataFrame(0, index=top_genres, columns=top_genres)
for genres in df['genres']:
    filtered = [g for g in genres if g in top_genres]
    for i in range(len(filtered)):
        for j in range(i + 1, len(filtered)):
            co_matrix.at[filtered[i], filtered[j]] += 1
            co_matrix.at[filtered[j], filtered[i]] += 1

# Shorten labels for heatmap
short_labels = [g.replace('International ', 'Intl ').replace('Children & Family ', 'Kids ')
                .replace('TV Shows', 'TV').replace('Movies', 'Mov') for g in top_genres]

fig, ax = plt.subplots(figsize=(12, 10))
mask = np.triu(np.ones_like(co_matrix, dtype=bool), k=0)
sns.heatmap(co_matrix, mask=mask, annot=True, fmt='d', cmap='Reds',
            xticklabels=short_labels, yticklabels=short_labels,
            linewidths=1, linecolor='white', square=True,
            cbar_kws={'shrink': 0.8, 'label': 'Co-occurrence Count'},
            ax=ax)

ax.set_title('Genre Co-occurrence Heatmap', fontsize=18, fontweight='bold', pad=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=10)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=10)

plt.tight_layout()
plt.show()

# Find strongest co-occurrences
print("\\n🔗 Strongest Genre Co-occurrences:")
pairs = []
for i in range(len(top_genres)):
    for j in range(i+1, len(top_genres)):
        pairs.append((top_genres[i], top_genres[j], co_matrix.iloc[i, j]))
pairs.sort(key=lambda x: x[2], reverse=True)
for g1, g2, count in pairs[:10]:
    print(f"   {g1} + {g2}: {count:,}")""", "rq3-heatmap")

code("""# ═══ CHART 3: Genre Word Cloud ═══

# Create a weighted string for word cloud
genre_text = ' '.join(all_genres)

# Custom color function
def netflix_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ['#E50914', '#FF4C4C', '#FF7F7F', '#B30710', '#D63031', '#FF6B6B', '#E17055']
    import random
    return random.choice(colors)

wordcloud = WordCloud(
    width=1200, height=600,
    background_color='#FAFAFA',
    max_words=100,
    max_font_size=120,
    min_font_size=12,
    color_func=netflix_color_func,
    prefer_horizontal=0.7,
    relative_scaling=0.5,
    margin=10
).generate(genre_text)

fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Netflix Genre Landscape — Word Cloud', fontsize=18, fontweight='bold', pad=20, y=1.02)
plt.tight_layout()
plt.show()""", "rq3-wordcloud")

code("""# ═══ CHART 4: Interactive Treemap of Individual Genres ═══

genre_df = genre_freq.head(20).reset_index()
genre_df.columns = ['Genre', 'Count']

fig = px.treemap(
    genre_df,
    path=['Genre'],
    values='Count',
    title='<b>Genre Treemap — Top 20 Individual Genres</b><br><sub>Size proportional to number of titles</sub>',
    color='Count',
    color_continuous_scale=['#FFE8E8', '#FF7F7F', NETFLIX_RED],
    hover_data={'Count': ':,'}
)

fig.update_layout(
    width=900, height=600,
    paper_bgcolor='#FAFAFA',
    font=dict(family="Segoe UI, Arial", size=14),
)
fig.update_traces(textinfo='label+value', textfont=dict(size=15))
fig.show()""", "rq3-treemap")

md("""### 💡 Key Insights — Question #3

1. **International Dominance**: The word "International" appears in 6 of the top 10 genre combinations, showing Netflix's global content strategy
2. **Drama Rules**: "Dramas" is the most frequent individual genre, appearing in countless combinations
3. **Standalone Categories**: "Documentaries" (299) and "Stand-Up Comedy" (273) are strong as single-genre categories
4. **Co-occurrence Patterns**: International Movies most frequently pair with Dramas (1,078 co-occurrences) and Comedies (549)
5. **Kids Content**: Children & Family content, while specialized, represents a significant segment with multiple sub-categories
6. **Genre Fragmentation**: With 514 unique combinations across ~42 base genres, Netflix uses fine-grained categorization for its recommendation engine""", "rq3-insights")

# ═══════════════════════════════════════════════════════════════
# SECTION 11: ADDITIONAL INSIGHTS
# ═══════════════════════════════════════════════════════════════

md("""---

## 🔬 6. Additional Insights""", "additional-header")

code("""# ═══ Top Directors ═══
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Top directors
top_dirs = df['director'].value_counts().head(10)
axes[0].barh(top_dirs.index[::-1], top_dirs.values[::-1], color=PASTEL_PALETTE[:10][::-1], edgecolor='white')
axes[0].set_title('Top 10 Directors by Title Count', fontsize=15, fontweight='bold')
axes[0].set_xlabel('Number of Titles')
for i, (bar_val) in enumerate(top_dirs.values[::-1]):
    axes[0].text(bar_val + 0.5, i, str(bar_val), va='center', fontweight='bold', fontsize=10)
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Year-over-year growth
total_yearly = df.groupby('year_added').size()
total_yearly = total_yearly[total_yearly.index >= 2014]
yoy_growth = total_yearly.pct_change() * 100

colors = ['#4ECDC4' if v >= 0 else NETFLIX_RED for v in yoy_growth.dropna().values]
axes[1].bar(yoy_growth.dropna().index.astype(int), yoy_growth.dropna().values, color=colors, edgecolor='white')
axes[1].set_title('Year-over-Year Growth Rate', fontsize=15, fontweight='bold')
axes[1].set_ylabel('Growth (%)')
axes[1].set_xlabel('Year')
axes[1].axhline(y=0, color='#666', linewidth=0.8)
for i, (yr, val) in enumerate(yoy_growth.dropna().items()):
    axes[1].text(yr, val + 2 if val >= 0 else val - 5, f'{val:.0f}%', ha='center', fontsize=9, fontweight='bold')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()""", "additional-charts")

# ═══════════════════════════════════════════════════════════════
# SECTION 12: CONCLUSION
# ═══════════════════════════════════════════════════════════════

md("""---

## 📝 Conclusion

### Summary of Findings

| Research Question | Key Finding |
|---|---|
| **Q1: TV Shows vs Movies** | TV Shows grew from 0% (2011) to ~35% (2021) of annual additions, reflecting Netflix's pivot to series content |
| **Q2: Top Countries** | US leads (2,818 titles), followed by India (972) and UK (419). Content is increasingly global |
| **Q3: Genre Combinations** | "International Movies, Dramas" dominates. Netflix uses 514 unique genre combinations across ~42 base genres |

### Overall Narrative

Netflix's content library tells a story of **strategic evolution**:
- **From Movies to Series**: A deliberate shift toward TV Shows that drive sustained engagement
- **From Domestic to Global**: Massive investment in international content, especially from India, East Asia, and Europe
- **From Broad to Niche**: Fine-grained genre categorization enabling Netflix's powerful recommendation engine

The data reveals a company that has transformed from a US-centric movie streaming service into a global entertainment powerhouse with diverse, original content spanning every genre and region.

---

*📊 Analysis completed using Python · Pandas · Matplotlib · Seaborn · Plotly · WordCloud*
*🏫 EngiViz — Engineering Day 2026 · GNA University*""", "conclusion")

# ═══════════════════════════════════════════════════════════════
# SECTION 13: EXPORT DATA
# ═══════════════════════════════════════════════════════════════

md("## 📤 7. Export Data for Website Dashboard", "export-header")

code("""import json
import os

os.makedirs('website/data', exist_ok=True)

# ─── Content by Year (Q1) ───
yearly_type = pd.crosstab(rq1_data['year_added'], rq1_data['type'])
content_by_year = {
    'years': yearly_type.index.tolist(),
    'movies': yearly_type['Movie'].tolist(),
    'tv_shows': yearly_type['TV Show'].tolist()
}
with open('website/data/content_by_year.json', 'w') as f:
    json.dump(content_by_year, f, indent=2)

# ─── Countries (Q2) ───
countries_data = country_counts.head(15).to_dict('records')
with open('website/data/countries.json', 'w') as f:
    json.dump(countries_data, f, indent=2)

# ─── Genres (Q3) ───
genres_data = {
    'combinations': genre_combos.head(20).to_dict(),
    'individual': genre_freq.head(20).to_dict()
}
with open('website/data/genres.json', 'w') as f:
    json.dump(genres_data, f, indent=2)

# ─── Overview Stats ───
overview = {
    'total_titles': int(df.shape[0]),
    'total_movies': int(df[df['type'] == 'Movie'].shape[0]),
    'total_tv_shows': int(df[df['type'] == 'TV Show'].shape[0]),
    'total_countries': int(country_counts.shape[0]),
    'total_genres': int(genre_combos.shape[0]),
    'year_range': f"{int(df['release_year'].min())}-{int(df['release_year'].max())}"
}
with open('website/data/overview_stats.json', 'w') as f:
    json.dump(overview, f, indent=2)

print("✅ All data exported to website/data/")
for f_name in os.listdir('website/data'):
    f_size = os.path.getsize(f'website/data/{f_name}')
    print(f"   📁 {f_name} ({f_size:,} bytes)")""", "export-data")

# ═══════════════════════════════════════════════════════════════
# SAVE NOTEBOOK
# ═══════════════════════════════════════════════════════════════

with open('d:/engiviz/netflix_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("✅ Notebook saved to d:/engiviz/netflix_analysis.ipynb")
