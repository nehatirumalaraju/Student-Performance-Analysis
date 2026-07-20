
📊 Student Performance Analysis

**Automated Student Performance Analysis using Python, Pandas, and Streamlit**  
Generates Excel reports and visualizes key factors affecting exam scores.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

🚀 Project Overview
This project analyzes a student dataset with 32+ attributes to identify what impacts academic performance the most. 

It includes:
- **Exploratory Data Analysis** to find correlations and patterns
- **Data Visualizations** for gender, parental education, study time vs performance
- **Automated Excel Report Generation** for quick, shareable insights
- **Optional Streamlit Dashboard** to interactively explore the data

The goal: Help educators and institutions make data-driven decisions to improve student outcomes.

---

🛠️ Tech Stack
- **Language**: Python 3.9+
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn
- **Analysis**: Jupyter Notebook
- **Reporting**: OpenPyXL / XlsxWriter for Excel automation
- **Dashboard**: Streamlit

---

📁 Project Structure
Student-Performance-Analysis/
│
├── http://Untitled5.ipynb                # Main analysis notebook - EDA, Visualizations, Insights
├── http://StudentPerformanceFactors.csv  # Dataset with 32+ student attributes
├── Student_Reports/               # Folder for automated generated Excel reports
│   └── Automated_Student_Report.xlsx
├── .gitignore
└── http://README.md

---

⚡ How to Run

1. **Clone the repo**
```bash
git clone https://github.com/nehatirumalraju/Student-Performance-Analysis.git
cd Student-Performance-Analysis
2. *Install dependencies*
pip install pandas numpy matplotlib seaborn jupyter openpyxl streamlit
3. *Run the analysis*
Open the notebook:
jupyter notebook Untitled5.ipynb
4. *Run Streamlit Dashboard* - if added
streamlit run app.py
---

📈 Key Insights
- *Top Factors Identified*: Study time, parental education level, and previous grades have the highest correlation with final exam scores
- *Visualizations Created*: Gender vs performance, study time vs scores, parental support impact
- *Automation*: Generates `Automated_Student_Report.xlsx` with summary stats and charts for stakeholders

---

📊 Sample Visualizations
_
---

🎯 Future Improvements
- [ ] Deploy interactive Streamlit dashboard
- [ ] Add ML model to predict student performance
- [ ] Include more demographic and socio-economic factors

---

👩‍💻 Author
*Neha Tirumalaraju*
- GitHub: https://github.com/nehatirumalraju

---

📄 License
This project is licensed under the MIT License.
---
