# Sleep Health & Lifestyle Analysis Project

## 🔷 Project Overview

**Title:** Sleep Health & Lifestyle Analysis: Exploring Factors That Influence Sleep Duration and Quality

**Objective:** Analyze and visualize trends in sleep health based on lifestyle choices (exercise, stress level, physical activity) and demographics (age, occupation) to identify key factors correlated with poor or high-quality sleep.

## 📊 Dataset Information

- **Source:** Kaggle - Sleep Health and Lifestyle Dataset
- **Size:** 374 participants with 13 features
- **Age Range:** 27-59 years
- **Sleep Duration Range:** 5.8-8.5 hours

### Dataset Features:
- Person ID, Gender, Age
- Occupation (11 different jobs)
- Sleep Duration & Quality of Sleep
- Physical Activity Level & Daily Steps
- Stress Level (1-10 scale)
- BMI Category & Blood Pressure
- Heart Rate
- Sleep Disorder (None, Insomnia, Sleep Apnea)

## 🧭 Analysis Structure

### 1. **Data Preparation**
- Load dataset using Pandas
- Handle missing values (Sleep Disorder column has NaN values)
- Create derived features:
  - Age Groups: 18-29, 30-39, 40-49, 50-59, 60+
  - Sleep Efficiency: (Sleep Duration / 8) * 100
  - Activity Level: Low/Moderate/High based on daily steps
  - Sleep Quality Category: Poor/Fair/Good/Excellent

### 2. **Exploratory Data Analysis (EDA)**
- Descriptive statistics by occupation and age group
- Stress level distribution among sleep disorder types
- Correlation analysis between numeric variables

### 3. **Key Visualizations**

#### 📌 Sleep Duration vs Occupation
- **Type:** Horizontal bar chart
- **Insight:** Identifies which professions get more/less sleep
- **Key Finding:** Significant variation in sleep patterns across occupations

#### 📌 Sleep Disorder Distribution
- **Type:** Pie chart and bar chart
- **Insight:** Shows prevalence of sleep disorders in population
- **Key Finding:** Percentage breakdown of None, Insomnia, and Sleep Apnea

#### 📌 Stress Level vs Sleep Disorder
- **Type:** Stacked bar chart
- **Insight:** Examines stress-disorder relationship
- **Key Finding:** Higher stress levels correlate with sleep disorder presence

#### 📌 Daily Steps vs Sleep Duration
- **Type:** Scatter plot with regression line
- **Insight:** Relationship between physical activity and sleep
- **Key Finding:** Correlation coefficient and activity level impact

#### 📌 Correlation Matrix Heatmap
- **Type:** Heatmap
- **Variables:** Sleep Duration, Stress, Physical Activity, BMI, Quality
- **Insight:** Comprehensive view of all variable relationships

#### 📌 Age Group vs Sleep Disorder
- **Type:** Grouped bar chart
- **Insight:** Age-related sleep disorder patterns
- **Key Finding:** Identifies which age groups are most at risk

## 🔍 Key Insights & Findings

### 🏢 Occupation Impact
- Significant variation in sleep duration across professions
- Some occupations show consistently higher stress levels
- Work-related factors influence sleep quality

### 😰 Stress & Sleep Disorders
- Strong correlation between stress levels and sleep disorder presence
- People with sleep disorders have higher average stress scores
- Stress management could be key intervention point

### 🏃‍♂️ Physical Activity Benefits
- Correlation between daily steps and sleep duration
- Activity level categories show different sleep patterns
- Regular physical activity associated with better sleep

### 👥 Age-Related Patterns
- Sleep disorder prevalence varies by age group
- Sleep duration and quality change with age
- Different age groups may need targeted interventions

### 🔗 Strongest Correlations
- Quality of Sleep ↔ Sleep Duration
- Stress Level ↔ Sleep Disorders
- Physical Activity ↔ Sleep Quality
- Age ↔ Sleep Patterns

## 💡 Recommendations

### 1. **For Individuals:**
- **High-Stress Occupations:** Focus on stress management techniques
- **Low Activity Levels:** Increase daily steps (target: >8000 steps)
- **Poor Sleep Quality:** Consider lifestyle modifications based on findings
- **Age-Specific:** Follow recommendations based on age group patterns

### 2. **For Healthcare Providers:**
- **Risk Assessment:** Use occupation and stress level as screening factors
- **Intervention Design:** Target high-risk age groups and occupations
- **Lifestyle Counseling:** Emphasize physical activity and stress management
- **Monitoring:** Track sleep quality alongside other health metrics

### 3. **For Employers:**
- **Workplace Wellness:** Address occupation-specific sleep challenges
- **Stress Reduction:** Implement stress management programs
- **Health Initiatives:** Promote physical activity and work-life balance
- **Education:** Raise awareness about sleep health importance

## 🧰 Technical Implementation

### **Tools Used:**
- **Python Libraries:** pandas, numpy, matplotlib, seaborn, plotly, streamlit
- **Analysis:** Statistical analysis, correlation studies
- **Visualization:** Interactive and static charts
- **Environment:** Jupyter Notebook + Streamlit Dashboard
- **Dashboard:** Real-time interactive web application

### **File Structure:**
```
Sleep-Health-Lifestyle-Analysis/
├── Sleep_health_and_lifestyle_dataset.csv    # Original dataset
├── sleep_health_analysis.ipynb               # Main analysis notebook
├── streamlit_dashboard.py                    # Interactive dashboard
├── run_dashboard.bat                         # Dashboard launcher script
├── requirements.txt                          # Python dependencies
├── PROJECT_README.md                         # This documentation
└── README.md                                 # Repository overview
```

## 📈 Usage Instructions

### **Option 1: Interactive Dashboard (Recommended)**
1. **Setup Environment:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Dashboard:**
   - **Windows:** Double-click `run_dashboard.bat`
   - **Command Line:** `streamlit run streamlit_dashboard.py`
   - **Browser:** Navigate to http://localhost:8501

3. **Dashboard Features:**
   - 🔍 Interactive filters (Age, Occupation, Sleep Disorder)
   - 📊 Real-time data visualization
   - 📈 Custom chart builder
   - 👥 Demographics analysis
   - 💾 Data export capabilities

### **Option 2: Jupyter Notebook Analysis**
1. **Setup Environment:**
   ```bash
   pip install pandas numpy matplotlib seaborn plotly jupyter
   ```

2. **Run Analysis:**
   - Open `sleep_health_analysis.ipynb` in Jupyter Notebook
   - Execute all cells sequentially
   - Review visualizations and insights

3. **Customization:**
   - Modify age group categories in Step 3
   - Adjust correlation analysis variables in Step 5
   - Create additional visualizations as needed

## 📊 Expected Outcomes

After running the complete analysis, you will have:
- ✅ Comprehensive dataset understanding
- ✅ Visual insights into sleep patterns
- ✅ Statistical correlations between lifestyle factors
- ✅ Interactive dashboard for real-time exploration
- ✅ Actionable recommendations for sleep improvement
- ✅ Data-driven insights for health interventions
- ✅ Custom analysis capabilities through dashboard

## 🎯 Project Applications

### **Academic Research:**
- Sleep health studies
- Lifestyle factor analysis
- Occupational health research

### **Healthcare:**
- Patient risk assessment
- Treatment planning
- Health promotion programs

### **Corporate Wellness:**
- Employee health initiatives
- Workplace health assessments
- Wellness program design

### **Personal Health:**
- Individual sleep improvement
- Lifestyle modification guidance
- Health tracking insights

---

**Note:** This analysis provides insights based on the specific dataset and should be interpreted within the context of the sample population. For clinical or medical decisions, consult healthcare professionals.

## 📞 Support

For questions about the analysis methodology, code implementation, or interpretation of results, refer to the detailed comments and documentation within the Jupyter notebook.

---
*Analysis completed using evidence-based data science methodologies to provide actionable insights for sleep health improvement.*
