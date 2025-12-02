# 🛡️ Online Harmful Content Detection & Trend Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Analysis-orange?logo=postgresql)
![Tableau](https://img.shields.io/badge/Tableau-Public-blueviolet?logo=tableau)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


This project analyzes user-generated content to identify harmful behaviors such as harassment, hate speech, spam, misinformation, and violent speech. Using Python, SQL, and Tableau, the project simulates a real Trust & Safety workflow used by content moderation and policy teams.

---

## 📌 Project Overview
- Detect harmful online content using rule-based classification.
- Assign severity scores based on content category.
- Identify high-risk users based on harmful ratio and severity.
- Visualize platform safety trends using an interactive Tableau dashboard.
- Demonstrate data analysis, investigation, and content policy assessment.

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, Matplotlib)
- **SQL** (user-risk metrics, category aggregation)
- **Tableau Public** (dashboard and visualizations)
- **CSV/Excel**
- **VS Code & GitHub**

---

## 📁 Project Structure
├── data/
│ ├── harmful_content_dataset.csv
│ └── user_level_stats.csv
├── scripts/
│ └── harmful_content_analysis.py
├── sql/
│ └── harmful_content_sql_schema_and_queries.sql
├── dashboard/
│ └── (tableau screenshots or workbook link)
└── README.md


---

## 🔍 Methodology

### 1. Dataset Creation
A synthetic dataset of 2,000 comments was generated with labeled categories:
- hate_speech  
- harassment  
- spam  
- misinformation  
- violent_speech  
- safe  

### 2. Severity Scoring
safe = 0
spam = 1
misinformation/harassment = 2
hate_speech/violent_speech = 3

yaml
Copy code

### 3. User-Level Risk Analysis
For each user:
- total comments  
- harmful comments  
- avg severity  
- harmful ratio  

### 4. Visualization
A Tableau dashboard visualizes:
- content category distribution  
- harmful vs safe split  
- top 10 high-risk users  

---

## 📊 Tableau Dashboard (LIVE)
👉 https://public.tableau.com/app/profile/nitish.prasad.shukla/viz/OnlineHarmfulContentDetectionTrendAnalysisDashboard/Dashboard1?publish=yes

---

## 🐍 Running the Python Script
```bash
python harmful_content_analysis.py
Outputs:

user_level_stats.csv

category_distribution.png

🗄 SQL Examples

SELECT category, COUNT(*) AS total
FROM comments
GROUP BY category
ORDER BY total DESC;

📈 Key Insights
Spam and harassment are the most frequent harmful categories.

Several users show harmful_ratio = 1.0 (all comments harmful).

Safe content is still a major portion, but high-severity categories require review.

Top 10 high-risk users can be escalated for moderation.

✨ Author

Nitish Prasad Shukla
