# 🎬 Netflix Movies & TV Shows — Data Visualization

> **EngiViz** — Engineering Day 2026 · Annual Inter-Department Data Visualization Championship  
> Dataset: Netflix Movies and TV Shows (8,807 records · 3.4 MB)

---

## 📖 Project Description

This project explores the **Netflix Movies and TV Shows** dataset — a rich collection of 8,807 titles featuring structured attributes (release year, country, rating, duration) alongside text data (descriptions and genres). The dataset spans content from 1925 to 2021, covering productions from over 100 countries across hundreds of genre combinations.

Through advanced data visualization techniques, we uncover key insights about Netflix's content strategy evolution, global content distribution, and genre landscape. Our analysis answers three critical research questions: how the proportion of TV Shows vs Movies has shifted over the past decade, which countries dominate Netflix's content library, and what genre combinations are most prevalent. The visualizations reveal Netflix's strategic pivot toward TV series content, the dominance of US and Indian productions, and the heavily international nature of Netflix's genre categorization.

The project is built with a dual-delivery approach: a comprehensive **Jupyter Notebook** for in-depth data analysis using Python's visualization ecosystem (Matplotlib, Seaborn, Plotly), and an interactive **web dashboard** featuring a Pastel Neumorphic UI design with Plotly.js and D3.js for data storytelling. The technology stack combines Python for data processing with modern web technologies for presentation, creating a complete data-to-insights pipeline.

---

## 🛠 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Data Processing** | Python 3.x, Pandas, NumPy | Data cleaning, wrangling, feature engineering |
| **Static Visualization** | Matplotlib, Seaborn | Publication-quality charts, heatmaps, distributions |
| **Interactive Visualization** | Plotly (Python + JS) | Choropleth maps, interactive charts, hover tooltips |
| **Text Visualization** | WordCloud | Genre frequency visualization |
| **Web Frontend** | HTML5, CSS3, JavaScript (ES6+) | Dashboard portal structure and logic |
| **Web Charting** | Plotly.js, D3.js (CDN) | Interactive browser-based visualizations |
| **Design System** | Vanilla CSS (Neumorphic) | Pastel Neumorphic Dashboard theme |
| **Typography** | Google Fonts (Inter, Outfit) | Modern, clean typography |
| **Notebook** | Jupyter Notebook | Interactive analysis environment |

---

## 📁 Project Structure

```
engiviz/
├── netflix_titles.csv              # Dataset (8,807 records)
├── netflix_analysis.ipynb          # Jupyter Notebook — full analysis
├── export_data.py                  # Script to export JSON data for website
├── requirements.txt                # Python dependencies
├── setup_env.bat                   # One-click environment setup (Windows)
├── README.md                       # This file
├── venv/                           # Python virtual environment
└── website/
    ├── index.html                  # Dashboard portal
    ├── style.css                   # Pastel Neumorphic styles
    ├── script.js                   # Chart rendering & interactivity
    └── data/                       # Pre-processed JSON data
        ├── content_by_year.json
        ├── countries.json
        ├── genres.json
        └── overview_stats.json
```

---

## 🚀 Setup Instructions

### Prerequisites
- **Python 3.8+** installed and available in PATH
- **Git** (optional, for cloning)
- A modern web browser (Chrome, Firefox, Edge)

### Option 1: Automated Setup (Windows)

```bash
# Double-click or run from terminal:
setup_env.bat
```

This will automatically create the virtual environment and install all dependencies.

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the Notebook

```bash
# Activate virtual environment (if not already active)
venv\Scripts\activate

# Launch Jupyter Notebook
jupyter notebook netflix_analysis.ipynb
```

### Running the Website

Simply open `website/index.html` in any modern web browser. No server required!

```bash
# Or use Python's built-in server for a better experience:
cd website
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

### Exporting Data for Website

```bash
# Activate virtual environment
venv\Scripts\activate

# Run the export script
python export_data.py
```

---

## 📊 Key Research Questions

### Q1: How has the proportion of TV Shows vs Movies added to Netflix changed over the last decade?
Netflix has undergone a dramatic content strategy shift. In 2011, virtually all additions were Movies. By 2021, TV Shows grew to represent ~35% of new content, reflecting Netflix's strategic investment in original series.

### Q2: Which countries are the largest producers of Netflix content?
The United States leads with 2,818 titles, followed by India (972) and the United Kingdom (419). Netflix has significantly invested in international content, particularly from South Asia and East Asia.

### Q3: What are the most common genre combinations?
"International Movies, Dramas" is the most frequent combination (362 titles). The prevalence of "International" in genre tags highlights Netflix's global content strategy, while standalone categories like Documentaries and Stand-Up Comedy maintain strong presence.

---

## 🎨 Design Approach

The website uses a **Pastel Neumorphic Dashboard** theme:
- Soft, elevated card components with dual-shadow neumorphic effects
- Curated pastel color palette (lavender, mint, peach, sky blue)
- Micro-animations and scroll-triggered reveals
- Interactive Plotly.js charts with hover tooltips
- Animated number counters for key statistics
- Responsive design for all screen sizes
- Dark/light mode toggle

---

## 📋 Judging Criteria Alignment

| Criteria | Weight | Implementation |
|----------|--------|---------------|
| **Visual Appeal & UI/UX** | 25% | Neumorphic design, micro-animations, interactive charts, responsive layout |
| **Data Insight & Storytelling** | 25% | Narrative-driven sections, annotated charts, contextual insights |
| **Technical Complexity** | 25% | Multiple viz libraries, choropleth maps, co-occurrence matrices, custom CSS |
| **Innovation & Creativity** | 25% | Interactive dashboard, animated transitions, genre network analysis |

---

## 📜 License

This project was created for the **EngiViz — Engineering Day 2026** Data Visualization Hackathon at GNA University.

Dataset Source: [Netflix Movies and TV Shows on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
