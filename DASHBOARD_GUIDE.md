# 🚀 Streamlit Dashboard Quick Start Guide

## Sleep Health & Lifestyle Analysis Interactive Dashboard

### 📋 Overview
This interactive dashboard provides real-time exploration of sleep health data with filtering, visualization, and analysis capabilities.

### 🎯 Dashboard Features

#### 🔍 **Interactive Filters** (Left Sidebar)
- **Age Group:** Filter by age ranges (18-29, 30-39, 40-49, 50-59, 60+)
- **Occupation:** Select specific professions or view all
- **Sleep Disorder Status:** Filter by disorder type or show all participants

#### 📊 **Main Dashboard Tabs**

1. **📊 Overview Tab**
   - Key metrics dashboard with real-time calculations
   - Sleep disorder and quality distributions
   - Sleep duration histogram with mean indicator
   - Key insights box with filtered data

2. **🏢 Occupation Analysis Tab**
   - Sleep duration ranking by occupation
   - Sleep quality comparisons across professions
   - Stress level analysis by job type
   - Sleep disorder prevalence by occupation

3. **📈 Correlations Tab**
   - Interactive correlation heatmap
   - Sleep duration and quality correlation charts
   - Customizable scatter plots for relationship exploration
   - Four relationship options to explore

4. **👥 Demographics Tab**
   - Age group analysis with sleep metrics
   - Sleep disorder distribution by age
   - Physical activity level impact analysis
   - Gender-based comparisons (if available)

5. **🔍 Individual Explorer Tab**
   - Custom chart builder with multiple options
   - Scatter plots, box plots, histograms, bar charts
   - Flexible axis and grouping selections
   - Filtered data table viewer
   - Data export functionality

### 🚀 How to Start

#### **Option 1: Double-Click Launch (Windows)**
1. Navigate to the project folder
2. Double-click `run_dashboard.bat`
3. Wait for browser to open automatically
4. If browser doesn't open, go to: http://localhost:8501

#### **Option 2: Command Line**
```bash
# Navigate to project directory
cd "c:\Users\mingw\OneDrive\桌面\cap1\Sleep-Health-Lifestyle-Analysis"

# Start dashboard
streamlit run streamlit_dashboard.py
```

#### **Option 3: VS Code Terminal**
1. Open terminal in VS Code
2. Run: `streamlit run streamlit_dashboard.py`
3. Click the link that appears in terminal

### 💡 Usage Tips

#### **Getting Started**
1. **Start with Overview Tab** - Get familiar with your data
2. **Apply Filters** - Use sidebar to focus on specific groups
3. **Explore Occupation Tab** - See profession-specific patterns
4. **Check Correlations** - Understand relationships between variables
5. **Use Individual Explorer** - Create custom analyses

#### **Filter Tips**
- **Multiple Filters:** Combine age, occupation, and disorder filters
- **Real-time Updates:** All charts update instantly when filters change
- **Reset Filters:** Select "All" to remove any filter
- **Data Counter:** Check sidebar for filtered vs total participant count

#### **Visualization Tips**
- **Hover for Details:** Most charts show additional info on hover
- **Interactive Elements:** Click legend items to show/hide data
- **Zoom & Pan:** Use plotly controls to explore charts in detail
- **Full Screen:** Click expand icon on charts for larger view

### 📈 Sample Analysis Workflows

#### **Workflow 1: Occupation Health Assessment**
1. Go to **Occupation Analysis** tab
2. Identify lowest sleep duration professions
3. Check stress levels for same professions
4. Look at sleep disorder rates
5. **Insight:** Target high-stress, low-sleep occupations for interventions

#### **Workflow 2: Age-Based Risk Analysis**
1. Go to **Demographics** tab
2. Filter by different age groups in sidebar
3. Compare sleep disorder rates across ages
4. Check correlation with stress levels
5. **Insight:** Identify high-risk age groups for preventive care

#### **Workflow 3: Custom Factor Analysis**
1. Go to **Individual Explorer** tab
2. Select variables of interest for x/y axes
3. Choose grouping variable (occupation, age group, etc.)
4. Try different chart types
5. **Insight:** Discover unique patterns in your data

#### **Workflow 4: Stress-Sleep Investigation**
1. Go to **Correlations** tab
2. Select "Stress vs Sleep Duration" relationship
3. Use filters to examine specific groups
4. Check correlation values
5. **Insight:** Quantify stress impact on sleep for different populations

### 🔧 Troubleshooting

#### **Dashboard Won't Start**
- Check if all packages are installed: `pip install -r requirements.txt`
- Ensure you're in the correct directory
- Try running: `streamlit --version` to verify installation

#### **Charts Not Loading**
- Check internet connection (some plotly features need internet)
- Refresh browser page (Ctrl+F5)
- Check terminal for error messages

#### **Filters Not Working**
- Refresh the page
- Check if dataset loaded properly (look for error messages)
- Ensure `Sleep_health_and_lifestyle_dataset.csv` is in project folder

#### **Performance Issues**
- Close other browser tabs to free memory
- Reduce number of participants with filters
- Restart dashboard if it becomes slow

### 📊 Data Export

#### **Download Filtered Data**
1. Go to **Individual Explorer** tab
2. Apply desired filters in sidebar
3. Select columns to include
4. Click "Download Filtered Data" button
5. Use downloaded CSV for external analysis

### 🎨 Customization Options

#### **Chart Types Available**
- **Scatter Plots:** Relationship exploration
- **Box Plots:** Distribution comparisons  
- **Histograms:** Single variable distributions
- **Bar Charts:** Category comparisons
- **Heatmaps:** Correlation visualization
- **Pie Charts:** Composition analysis

#### **Color Coding**
- **Sleep Disorder Status:** Different colors for each condition
- **Age Groups:** Distinct colors for age ranges
- **Occupations:** Unique colors for professions
- **Activity Levels:** Color-coded by physical activity

### 🏁 Next Steps

After exploring the dashboard:
1. **Identify Key Patterns** from your exploration
2. **Export Insights** using the data download feature
3. **Create Reports** based on filtered analyses
4. **Share Findings** with stakeholders
5. **Plan Interventions** based on discovered risk factors

### 📞 Support

If you encounter issues:
1. Check the PROJECT_README.md for detailed documentation
2. Verify all requirements are installed
3. Ensure dataset file is present and accessible
4. Check terminal output for error messages

---

**🎯 Goal:** Use this dashboard to discover actionable insights about sleep health patterns and make data-driven recommendations for improving sleep quality across different populations.

**💡 Remember:** The dashboard updates in real-time as you apply filters, so experiment with different combinations to uncover hidden patterns in the data!
