/* ═══════════════════════════════════════════════════════════════
   CODESTORM — NETFLIX CONTENT ANALYTICS
   Interactive Dashboard Script · Netflix Red & White Visualizations
   ═══════════════════════════════════════════════════════════════ */

// ─── Floating Glowing Bubbles Background ───
function createParticles() {
    const container = document.getElementById('particles');
    if (!container) return;
    container.innerHTML = '';
    const bubbleColors = [
        'rgba(229, 9, 20, 0.65)',
        'rgba(255, 77, 77, 0.55)',
        'rgba(255, 255, 255, 0.45)',
        'rgba(229, 9, 20, 0.35)',
        'rgba(255, 120, 120, 0.5)',
        'rgba(180, 10, 20, 0.55)'
    ];
    for (let i = 0; i < 75; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        const size = Math.random() * 22 + 6;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.background = bubbleColors[Math.floor(Math.random() * bubbleColors.length)];
        const duration = Math.random() * 16 + 10;
        particle.style.animationDuration = duration + 's';
        particle.style.animationDelay = (-Math.random() * duration) + 's';
        container.appendChild(particle);
    }
}
createParticles();

// ─── Scroll Animations (Intersection Observer) ───
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            if (entry.target.closest('.metrics-section')) {
                animateCounters();
            }
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));

window.addEventListener('load', () => {
    document.querySelectorAll('.hero .fade-in-up').forEach(el => {
        el.classList.add('visible');
    });
});

// ─── Counter Animation ───
let countersAnimated = false;
function animateCounters() {
    if (countersAnimated) return;
    countersAnimated = true;

    document.querySelectorAll('.counter').forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const startTime = performance.now();

        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(eased * target);
            counter.textContent = current.toLocaleString();
            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                counter.textContent = target.toLocaleString();
            }
        }
        requestAnimationFrame(update);
    });
}

// ─── Smooth scroll for nav links ───
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
});

// ═══════════════════════════════════════════════════════════════
// EMBEDDED DATASET SUMMARY
// ═══════════════════════════════════════════════════════════════

const DATA = {
    q1: {
        years: [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
        movies: [13, 23, 36, 71, 154, 449, 767, 1123, 1325, 1024, 1070],
        tvShows: [0, 2, 9, 26, 65, 158, 339, 484, 677, 580, 525]
    },
    q2: {
        countries: ['United States', 'India', 'United Kingdom', 'Japan', 'South Korea',
                    'Canada', 'Spain', 'France', 'Mexico', 'Egypt',
                    'Turkey', 'Nigeria', 'Australia', 'Taiwan', 'Indonesia'],
        counts: [2818, 972, 419, 245, 199, 181, 145, 124, 110, 106, 105, 102, 81, 77, 74]
    },
    q3: {
        genres: [
            'International Movies, Dramas', 'Documentaries', 'Dramas, International Movies',
            'Stand-Up Comedy', 'Dramas, Independent Movies, Intl Movies',
            'Comedies, Dramas, Intl Movies', "Kids' TV",
            'Intl TV Shows, TV Dramas, TV Mysteries', 'Crime TV, Intl TV, TV Dramas',
            'Children & Family Movies', 'Docuseries',
            'Children & Family Movies, Comedies', 'Action, Dramas, Intl Movies',
            'Comedies, Intl Movies', 'Intl TV, Romantic TV, TV Comedies'
        ],
        counts: [362, 299, 274, 273, 252, 227, 220, 171, 161, 157, 148, 134, 128, 127, 120],
        coMatrix: {
            labels: ['Intl Movies', 'Dramas', 'Comedies', 'Intl TV Shows', 'TV Dramas',
                     'Action & Adv', 'Documentaries', 'Independent', 'Children & Fam', 'Thrillers'],
            values: [
                [0, 1078, 549, 0, 0, 398, 187, 472, 0, 210],
                [1078, 0, 227, 0, 0, 128, 0, 546, 0, 185],
                [549, 227, 0, 315, 0, 0, 0, 0, 234, 0],
                [0, 0, 315, 0, 676, 243, 0, 0, 0, 180],
                [0, 0, 0, 676, 0, 0, 0, 0, 0, 108],
                [398, 128, 0, 243, 0, 0, 0, 0, 0, 95],
                [187, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [472, 546, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 234, 0, 0, 0, 0, 0, 0, 0],
                [210, 185, 0, 180, 108, 95, 0, 0, 0, 0]
            ]
        }
    },
    additional: {
        ratings: ['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13', 'TV-Y7', 'TV-Y', 'PG', 'TV-G', 'NR'],
        ratingCounts: [3207, 2160, 863, 799, 490, 334, 307, 287, 220, 80],
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        monthCounts: [537, 601, 605, 551, 488, 549, 723, 543, 685, 641, 631, 637]
    }
};

// ═══════════════════════════════════════════════════════════════
// NETFLIX RED & WHITE THEMING & HELPERS
// ═══════════════════════════════════════════════════════════════

function getTheme() {
    return {
        bg: 'rgba(0,0,0,0)',
        text: '#ffffff',
        textMuted: '#b3b3b3',
        grid: 'rgba(255,255,255,0.08)',
        accent: '#e50914',
        accentSoft: '#ff4d4d',
        accentSecondary: '#ffffff',
        colors: ['#e50914', '#ffffff', '#ff4d4d', '#e5e5e5', '#b3b3b3', '#ff8080', '#cccccc', '#999999', '#ff3333', '#666666']
    };
}

function baseLayout() {
    const t = getTheme();
    return {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        font: { color: t.text, family: 'Inter, sans-serif', size: 12 },
        margin: { t: 25, r: 35, l: 45, b: 45 },
        xaxis: { gridcolor: t.grid, zerolinecolor: t.grid, tickfont: { size: 11, color: t.textMuted } },
        yaxis: { gridcolor: t.grid, zerolinecolor: t.grid, tickfont: { size: 11, color: t.textMuted } },
        hoverlabel: { 
            bgcolor: '#1f1f1f', 
            bordercolor: '#e50914',
            font: { family: 'Inter', size: 13, color: '#ffffff' } 
        },
        showlegend: true,
        legend: { font: { size: 12, color: t.text }, orientation: 'h', yanchor: 'bottom', y: 1.02, xanchor: 'center', x: 0.5 }
    };
}

const plotConfig = { responsive: true, displayModeBar: false };

// ═══════════════════════════════════════════════════════════════
// CHART RENDERERS
// ═══════════════════════════════════════════════════════════════

function renderQ1() {
    const d = DATA.q1;

    // Stacked Area
    Plotly.newPlot('q1-area-chart', [
        {
            x: d.years, y: d.movies, name: 'Movies',
            type: 'scatter', mode: 'lines',
            fill: 'tozeroy', fillcolor: 'rgba(229, 9, 20, 0.35)',
            line: { color: '#e50914', width: 3, shape: 'spline' },
            hovertemplate: '<b>Movies</b><br>Year: %{x}<br>Count: %{y:,}<extra></extra>'
        },
        {
            x: d.years, y: d.tvShows, name: 'TV Shows',
            type: 'scatter', mode: 'lines',
            fill: 'tozeroy', fillcolor: 'rgba(255, 255, 255, 0.2)',
            line: { color: '#ffffff', width: 3, shape: 'spline' },
            hovertemplate: '<b>TV Shows</b><br>Year: %{x}<br>Count: %{y:,}<extra></extra>'
        }
    ], {
        ...baseLayout(),
        xaxis: { ...baseLayout().xaxis, dtick: 1, title: 'Year' },
        yaxis: { ...baseLayout().yaxis, title: 'Number of Titles' },
        hovermode: 'x unified'
    }, plotConfig);

    // 100% Stacked Bar
    const total = d.movies.map((m, i) => m + d.tvShows[i]);
    const mPct = d.movies.map((m, i) => (m / total[i] * 100));
    const tPct = d.tvShows.map((tv, i) => (tv / total[i] * 100));

    Plotly.newPlot('q1-bar-chart', [
        {
            x: d.years, y: mPct, name: 'Movies %',
            type: 'bar', marker: { color: '#e50914', line: { color: '#1f1f1f', width: 1 } },
            text: mPct.map(v => v.toFixed(0) + '%'), textposition: 'inside', textfont: { color: 'white', size: 10, weight: 'bold' },
            hovertemplate: '<b>Movies</b><br>%{y:.1f}%<extra></extra>'
        },
        {
            x: d.years, y: tPct, name: 'TV Shows %',
            type: 'bar', marker: { color: '#ffffff', line: { color: '#1f1f1f', width: 1 } },
            text: tPct.map(v => v > 5 ? v.toFixed(0) + '%' : ''), textposition: 'inside', textfont: { color: '#141414', size: 10, weight: 'bold' },
            hovertemplate: '<b>TV Shows</b><br>%{y:.1f}%<extra></extra>'
        }
    ], {
        ...baseLayout(),
        barmode: 'stack',
        xaxis: { ...baseLayout().xaxis, dtick: 1, title: 'Year' },
        yaxis: { ...baseLayout().yaxis, title: 'Percentage (%)', ticksuffix: '%', range: [0, 100] }
    }, plotConfig);
}

function renderQ2() {
    const t = getTheme();
    const d = DATA.q2;
    const reversed = { countries: [...d.countries].reverse(), counts: [...d.counts].reverse() };

    // Netflix Red to White Gradient for Bar Chart
    const gradientColors = reversed.counts.map((_, i) => {
        const ratio = i / (reversed.counts.length - 1);
        const r = Math.round(229 + (255 - 229) * ratio);
        const g = Math.round(9 + (180 - 9) * ratio);
        const b = Math.round(20 + (180 - 20) * ratio);
        return `rgb(${r},${g},${b})`;
    }).reverse();

    Plotly.newPlot('q2-bar-chart', [{
        y: reversed.countries, x: reversed.counts,
        type: 'bar', orientation: 'h',
        marker: { color: gradientColors, line: { color: '#1f1f1f', width: 1 } },
        text: reversed.counts.map(v => v.toLocaleString()),
        textposition: 'outside', textfont: { size: 11, color: t.text },
        hovertemplate: '<b>%{y}</b><br>Titles: %{x:,}<extra></extra>'
    }], {
        ...baseLayout(),
        margin: { t: 20, r: 60, l: 125, b: 40 },
        xaxis: { ...baseLayout().xaxis, title: 'Number of Titles' },
        yaxis: { ...baseLayout().yaxis, automargin: true },
        showlegend: false
    }, plotConfig);

    // World Choropleth Map with Netflix Red Colorscale
    Plotly.newPlot('q2-map-chart', [{
        type: 'choropleth',
        locationmode: 'country names',
        locations: d.countries,
        z: d.counts,
        text: d.countries.map((c, i) => `${c}: ${d.counts[i].toLocaleString()} titles`),
        colorscale: [
            [0, '#1f1f1f'], 
            [0.2, '#500b0e'], 
            [0.5, '#a80910'], 
            [0.8, '#e50914'], 
            [1, '#ff4d4d']
        ],
        showscale: true,
        colorbar: { title: 'Titles', thickness: 14, len: 0.75, tickfont: { size: 10, color: t.text } },
        hovertemplate: '%{text}<extra></extra>'
    }], {
        ...baseLayout(),
        geo: {
            showframe: false, showcoastlines: true,
            coastlinecolor: '#444444',
            landcolor: '#1f1f1f',
            bgcolor: 'rgba(0,0,0,0)',
            projection: { type: 'natural earth' }
        },
        margin: { t: 20, r: 10, l: 10, b: 10 }
    }, plotConfig);
}

function renderQ3() {
    const t = getTheme();
    const d = DATA.q3;

    // Genre bar chart
    const revGenres = [...d.genres].reverse();
    const revCounts = [...d.counts].reverse();
    const barColors = revCounts.map((_, i) => {
        const ratio = i / (revCounts.length - 1);
        return `rgba(229, 9, 20, ${0.4 + ratio * 0.6})`;
    });

    Plotly.newPlot('q3-bar-chart', [{
        y: revGenres, x: revCounts,
        type: 'bar', orientation: 'h',
        marker: { color: barColors, line: { color: '#1f1f1f', width: 1 } },
        text: revCounts.map(v => v.toLocaleString()),
        textposition: 'outside', textfont: { size: 10, color: t.text },
        hovertemplate: '<b>%{y}</b><br>Count: %{x:,}<extra></extra>'
    }], {
        ...baseLayout(),
        margin: { t: 20, r: 60, l: 250, b: 40 },
        xaxis: { ...baseLayout().xaxis, title: 'Number of Titles' },
        yaxis: { ...baseLayout().yaxis, automargin: true, tickfont: { size: 10 } },
        showlegend: false
    }, plotConfig);

    // Co-occurrence Heatmap (Netflix Red Intensity)
    const cm = d.coMatrix;
    const heatmapColorscale = [
        [0, '#1f1f1f'],
        [0.3, '#4a0d0d'],
        [0.65, '#a80910'],
        [1, '#e50914']
    ];

    Plotly.newPlot('q3-heatmap', [{
        z: cm.values,
        x: cm.labels, y: cm.labels,
        type: 'heatmap',
        colorscale: heatmapColorscale,
        hoverongaps: false,
        showscale: true,
        colorbar: { title: 'Count', thickness: 14, len: 0.75, tickfont: { size: 10, color: t.text } },
        text: cm.values.map(row => row.map(v => v > 0 ? v.toString() : '')),
        texttemplate: '%{text}',
        textfont: { size: 9, color: t.text },
        hovertemplate: '<b>%{x}</b> + <b>%{y}</b><br>Co-occurrences: %{z:,}<extra></extra>'
    }], {
        ...baseLayout(),
        margin: { t: 20, r: 20, l: 110, b: 110 },
        xaxis: { ...baseLayout().xaxis, tickangle: -45, tickfont: { size: 9 } },
        yaxis: { ...baseLayout().yaxis, tickfont: { size: 9 }, autorange: 'reversed' },
        showlegend: false
    }, plotConfig);
}

function renderAdditional() {
    const t = getTheme();
    const d = DATA.additional;

    // Ratings
    const ratingColors = d.ratingCounts.map((_, i) => {
        const ratio = 1 - (i / d.ratingCounts.length);
        return `rgba(229, 9, 20, ${0.35 + ratio * 0.65})`;
    });

    Plotly.newPlot('add-ratings-chart', [{
        x: d.ratings, y: d.ratingCounts,
        type: 'bar',
        marker: { color: ratingColors, line: { color: '#1f1f1f', width: 1 } },
        text: d.ratingCounts.map(v => v.toLocaleString()),
        textposition: 'outside', textfont: { size: 10, color: t.text },
        hovertemplate: '<b>%{x}</b><br>Count: %{y:,}<extra></extra>'
    }], {
        ...baseLayout(),
        xaxis: { ...baseLayout().xaxis, title: 'Rating' },
        yaxis: { ...baseLayout().yaxis, title: 'Count' },
        showlegend: false
    }, plotConfig);

    // Monthly
    Plotly.newPlot('add-monthly-chart', [{
        x: d.months, y: d.monthCounts,
        type: 'scatter', mode: 'lines+markers',
        line: { color: '#e50914', width: 3, shape: 'spline' },
        marker: { size: 9, color: '#ffffff', line: { color: '#e50914', width: 2 } },
        fill: 'tozeroy', fillcolor: 'rgba(229, 9, 20, 0.18)',
        hovertemplate: '<b>%{x}</b><br>Titles Added: %{y:,}<extra></extra>'
    }], {
        ...baseLayout(),
        xaxis: { ...baseLayout().xaxis, title: 'Month' },
        yaxis: { ...baseLayout().yaxis, title: 'Number of Titles' },
        showlegend: false
    }, plotConfig);
}

// ─── Render All ───
function renderAllCharts() {
    renderQ1();
    renderQ2();
    renderQ3();
    renderAdditional();
}

// Initial render
window.addEventListener('load', () => {
    setTimeout(renderAllCharts, 150);
});

// Responsive resize
let resizeTimeout;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
        const chartIds = ['q1-area-chart', 'q1-bar-chart', 'q2-bar-chart', 'q2-map-chart',
                          'q3-bar-chart', 'q3-heatmap', 'add-ratings-chart', 'add-monthly-chart'];
        chartIds.forEach(id => {
            try { Plotly.Plots.resize(id); } catch(e) {}
        });
    }, 200);
});
