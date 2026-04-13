# 📊 EDA Mobile Price Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on a mobile price dataset to understand patterns, relationships, and trends between different features like price, RAM, storage, and camera.

---

## 🛠️ Tools & Technologies Used

* Python 🐍
* Pandas
* Matplotlib
* Seaborn

---

## 📂 Dataset

* Mobile Price Dataset (`mobile_price_dataset.csv`)
* Contains features like:

  * Price (USD)
  * RAM
  * Storage
  * Camera
  * Battery
  * Year

---

## 📊 EDA Steps Performed

1. Data loading and inspection
2. Summary statistics (mean, median, std)
3. Data visualization:

   * Histograms
   * Boxplots
   * Correlation Heatmap
   * Pairplot
4. Identifying patterns and trends

---

## 🔍 Key Insights

* 📈 Higher RAM → Higher price
* 📷 Better camera → Slight increase in price
* 💰 Most phones fall in the mid-range (200–600 USD)
* 📱 Majority devices have 4GB–8GB RAM

---
## 🚀 How to Run the Project

1. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```
2. Run the Python file:

   ```bash
   python eda_analysis.py
   ```

---

## 📁 Project Structure

```
EDA-Mobile-Price-Analysis/
│
├── mobile_price_dataset.csv
├── eda_analysis.py
├── eda_report.md
├── requirements.txt
├── README.md

## 🧠 Conclusion

EDA helps in understanding the dataset and reveals important relationships between features. This analysis can be used for future machine learning models.

---
