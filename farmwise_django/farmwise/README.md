# FarmWise — Django Agriculture App
## Andhra Pradesh Farmer Intelligence Platform

---

## 📁 Project Structure

```
farmwise/
├── manage.py
├── requirements.txt
├── README.md
├── farmwise/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── core/
    ├── __init__.py
    ├── models.py       ← All DB models
    ├── views.py        ← 9 screen views + API endpoints
    ├── urls.py         ← URL routing
    ├── data.py         ← All AP district data, crops, reviews, pests
    └── templates/
        └── core/
            ├── base.html           ← Sidebar layout, nav, alert strip
            ├── dashboard.html      ← Screen 1: Stats, top crops, reviews
            ├── reviews.html        ← Screen 2: Filterable crop reviews
            ├── regions.html        ← Screen 3: AP 26-district map
            ├── water_climate.html  ← Screen 4: Water & climate cards
            ├── pest_tracker.html   ← Screen 5: Pest outbreak tracker
            ├── yield_profit.html   ← Screen 6: Yield & profit charts
            ├── forum.html          ← Screen 7: Farmer Q&A forum
            ├── upload.html         ← Screen 8: Camera upload + AI analysis
            └── alerts.html         ← Screen 9: Push notifications
```

---

## 🚀 Setup Instructions

### 1. Prerequisites
- Python 3.10+
- pip

### 2. Install & Run

```bash
# Navigate to project folder
cd farmwise

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install Django
pip install -r requirements.txt

# Run migrations (creates SQLite DB)
python manage.py migrate

# Start development server
python manage.py runserver
```

### 3. Open in Browser
```
http://127.0.0.1:8000/
```

---

## 🌾 Features by Screen

| Screen | URL | Description |
|--------|-----|-------------|
| Dashboard | `/` | Live alert strip, stat cards, top crops, recent reviews |
| Crop Reviews | `/reviews/` | Filter by season/region, star ratings, upvote/share |
| Regions | `/regions/` | Clickable AP 26-district SVG map with crop data |
| Water & Climate | `/water/` | Per-crop water need, temperature, rainfall suitability |
| Pest Tracker | `/pest/` | Active outbreaks, severity bars, community remedies |
| Yield & Profit | `/yield/` | Bar charts for yield/profit/ROI, MSP vs market price |
| Farmer Forum | `/forum/` | Q&A with expert/trusted badges, topic filters |
| Upload Field | `/upload/` | Camera upload, AI health analysis simulation |
| Alerts | `/alerts/` | Pest/weather/policy/reply notifications |

---

## 🗺️ Andhra Pradesh Districts Covered (26)

**North Coastal:** Srikakulam, Vizianagaram, Visakhapatnam, Anakapalli  
**Agency:** Alluri Sitarama Raju, Parvathipuram Manyam  
**Godavari Delta:** West Godavari, East Godavari, Kakinada, Konaseema, Eluru  
**Krishna Delta:** Krishna, NTR (Vijayawada), Guntur, Palnadu, Bapatla  
**South Coastal:** Prakasam, Nellore  
**Rayalaseema:** Kurnool, Nandyal, Kadapa, Sri Sathya Sai, Anantapur, Tirupati, Chittoor, Annamayya  

---

## 🎨 Design System

- **Primary:** `#3B6D11` (deep green), `#639922` (mid green)
- **Accent:** `#BA7517` (amber), `#FAC775` (amber light)
- **Font:** DM Sans (Google Fonts)
- **Icons:** Tabler Icons (CDN)
- **Responsive:** Mobile-friendly sidebar collapses to icon-only

---

## 🔌 API Endpoints

```
GET  /api/district/<name>/     → Returns JSON district data
POST /api/upvote/<review_id>/  → Upvote a review (CSRF protected)
```

---

## 📦 Production Notes

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS` with your domain
4. Use PostgreSQL instead of SQLite
5. Serve static files via whitenoise or nginx
6. Connect real AI endpoint in `upload.html` for crop analysis
