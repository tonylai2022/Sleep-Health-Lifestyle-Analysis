import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Configure Streamlit page
st.set_page_config(
    page_title="Sleep Health & Lifestyle Analysis Dashboard",
    page_icon="😴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(90deg, #e3f2fd, #f8f9fa);
        border-radius: 10px;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .insight-box {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #4caf50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load and cache data
@st.cache_data
def load_data():
    """Load and preprocess the sleep health dataset"""
    try:
        df = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
        
        # Feature engineering
        def categorize_age(age):
            if age < 30:
                return '18-29'
            elif age < 40:
                return '30-39'
            elif age < 50:
                return '40-49'
            elif age < 60:
                return '50-59'
            else:
                return '60+'

        def categorize_activity(steps):
            if steps < 5000:
                return 'Low Activity'
            elif steps < 8000:
                return 'Moderate Activity'
            else:
                return 'High Activity'

        def categorize_sleep_quality(quality):
            if quality <= 4:
                return 'Poor'
            elif quality <= 6:
                return 'Fair'
            elif quality <= 8:
                return 'Good'
            else:
                return 'Excellent'

        def categorize_stress(stress):
            if stress <= 3:
                return 'Low (1-3)'
            elif stress <= 6:
                return 'Medium (4-6)'
            else:
                return 'High (7-10)'

        # Apply feature engineering
        df['Age Group'] = df['Age'].apply(categorize_age)
        df['Sleep Efficiency'] = df['Sleep Duration'] / 8 * 100
        df['Activity Level'] = df['Daily Steps'].apply(categorize_activity)
        df['Sleep Quality Category'] = df['Quality of Sleep'].apply(categorize_sleep_quality)
        df['Stress Category'] = df['Stress Level'].apply(categorize_stress)
        df['Sleep Disorder Status'] = df['Sleep Disorder'].fillna('No Disorder')
        
        return df
    except FileNotFoundError:
        st.error("Dataset file not found! Please ensure 'Sleep_health_and_lifestyle_dataset.csv' is in the same directory.")
        return None

# Main dashboard function
def main():
    # Header
    st.markdown('<h1 class="main-header">😴 Sleep Health & Lifestyle Analysis Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters & Controls")
    
    # Age group filter
    age_groups = ['All'] + list(df['Age Group'].unique())
    selected_age = st.sidebar.selectbox("Select Age Group", age_groups)
    
    # Occupation filter
    occupations = ['All'] + list(df['Occupation'].unique())
    selected_occupation = st.sidebar.selectbox("Select Occupation", occupations)
    
    # Sleep disorder filter
    disorders = ['All'] + list(df['Sleep Disorder Status'].unique())
    selected_disorder = st.sidebar.selectbox("Select Sleep Disorder Status", disorders)
    
    # Apply filters
    filtered_df = df.copy()
    if selected_age != 'All':
        filtered_df = filtered_df[filtered_df['Age Group'] == selected_age]
    if selected_occupation != 'All':
        filtered_df = filtered_df[filtered_df['Occupation'] == selected_occupation]
    if selected_disorder != 'All':
        filtered_df = filtered_df[filtered_df['Sleep Disorder Status'] == selected_disorder]
    
    # Display dataset overview
    st.sidebar.markdown("---")
    st.sidebar.write(f"**Filtered Dataset:** {len(filtered_df)} participants")
    st.sidebar.write(f"**Total Dataset:** {len(df)} participants")
    
    # Main dashboard layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_sleep = filtered_df['Sleep Duration'].mean()
        st.metric("Average Sleep Duration", f"{avg_sleep:.2f} hours", 
                 delta=f"{avg_sleep - df['Sleep Duration'].mean():.2f}h vs overall")
    
    with col2:
        avg_quality = filtered_df['Quality of Sleep'].mean()
        st.metric("Average Sleep Quality", f"{avg_quality:.1f}/10",
                 delta=f"{avg_quality - df['Quality of Sleep'].mean():.1f} vs overall")
    
    with col3:
        avg_stress = filtered_df['Stress Level'].mean()
        st.metric("Average Stress Level", f"{avg_stress:.1f}/10",
                 delta=f"{avg_stress - df['Stress Level'].mean():.1f} vs overall")
    
    with col4:
        disorder_rate = (filtered_df['Sleep Disorder Status'] != 'No Disorder').mean() * 100
        overall_rate = (df['Sleep Disorder Status'] != 'No Disorder').mean() * 100
        st.metric("Sleep Disorder Rate", f"{disorder_rate:.1f}%",
                 delta=f"{disorder_rate - overall_rate:.1f}% vs overall")
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "🏢 Occupation Analysis", "📈 Correlations", 
        "👥 Demographics", "🔍 Individual Explorer"
    ])
    
    with tab1:
        overview_tab(filtered_df, df)
    
    with tab2:
        occupation_tab(filtered_df, df)
    
    with tab3:
        correlation_tab(filtered_df, df)
    
    with tab4:
        demographics_tab(filtered_df, df)
    
    with tab5:
        individual_explorer_tab(filtered_df, df)

def overview_tab(filtered_df, full_df):
    """Overview tab with key insights and distributions"""
    st.header("📊 Sleep Health Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sleep Disorder Distribution")
        disorder_counts = filtered_df['Sleep Disorder Status'].value_counts()
        fig = px.pie(values=disorder_counts.values, names=disorder_counts.index,
                    title="Sleep Disorder Distribution",
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sleep Quality Distribution")
        quality_counts = filtered_df['Sleep Quality Category'].value_counts()
        fig = px.bar(x=quality_counts.index, y=quality_counts.values,
                    title="Sleep Quality Distribution",
                    color=quality_counts.values,
                    color_continuous_scale='viridis')
        fig.update_layout(xaxis_title="Sleep Quality", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)
    
    # Sleep duration distribution
    st.subheader("Sleep Duration Distribution")
    fig = px.histogram(filtered_df, x='Sleep Duration', nbins=20,
                      title="Sleep Duration Distribution",
                      color_discrete_sequence=['#1f77b4'])
    fig.add_vline(x=filtered_df['Sleep Duration'].mean(), line_dash="dash",
                  annotation_text=f"Mean: {filtered_df['Sleep Duration'].mean():.2f}h")
    st.plotly_chart(fig, use_container_width=True)
    
    # Key insights
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.subheader("🔑 Key Insights")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        best_occupation = filtered_df.groupby('Occupation')['Sleep Duration'].mean().idxmax()
        best_sleep = filtered_df.groupby('Occupation')['Sleep Duration'].mean().max()
        st.write(f"**Best Sleeping Occupation:** {best_occupation} ({best_sleep:.2f}h)")
    
    with col2:
        highest_stress_disorder = filtered_df[filtered_df['Sleep Disorder Status'] != 'No Disorder'].groupby('Sleep Disorder Status')['Stress Level'].mean().idxmax()
        stress_value = filtered_df[filtered_df['Sleep Disorder Status'] != 'No Disorder'].groupby('Sleep Disorder Status')['Stress Level'].mean().max()
        st.write(f"**Highest Stress Disorder:** {highest_stress_disorder} ({stress_value:.1f}/10)")
    
    with col3:
        best_age = filtered_df.groupby('Age Group')['Sleep Duration'].mean().idxmax()
        best_age_sleep = filtered_df.groupby('Age Group')['Sleep Duration'].mean().max()
        st.write(f"**Best Sleeping Age Group:** {best_age} ({best_age_sleep:.2f}h)")
    
    st.markdown('</div>', unsafe_allow_html=True)

def occupation_tab(filtered_df, full_df):
    """Occupation analysis tab"""
    st.header("🏢 Occupation Analysis")
    
    # Sleep duration by occupation
    occupation_sleep = filtered_df.groupby('Occupation')['Sleep Duration'].agg(['mean', 'count']).reset_index()
    occupation_sleep.columns = ['Occupation', 'Average Sleep', 'Count']
    occupation_sleep = occupation_sleep.sort_values('Average Sleep', ascending=True)
    
    fig = px.bar(occupation_sleep, x='Average Sleep', y='Occupation',
                orientation='h', title="Average Sleep Duration by Occupation",
                color='Average Sleep', color_continuous_scale='viridis',
                hover_data=['Count'])
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sleep Quality by Occupation")
        quality_by_occ = filtered_df.groupby('Occupation')['Quality of Sleep'].mean().sort_values(ascending=False)
        fig = px.bar(x=quality_by_occ.values, y=quality_by_occ.index,
                    orientation='h', title="Average Sleep Quality by Occupation",
                    color=quality_by_occ.values, color_continuous_scale='plasma')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Stress Level by Occupation")
        stress_by_occ = filtered_df.groupby('Occupation')['Stress Level'].mean().sort_values(ascending=True)
        fig = px.bar(x=stress_by_occ.values, y=stress_by_occ.index,
                    orientation='h', title="Average Stress Level by Occupation",
                    color=stress_by_occ.values, color_continuous_scale='reds')
        st.plotly_chart(fig, use_container_width=True)
    
    # Occupation vs Sleep Disorder
    st.subheader("Sleep Disorders by Occupation")
    occ_disorder = pd.crosstab(filtered_df['Occupation'], filtered_df['Sleep Disorder Status'], normalize='index') * 100
    fig = px.bar(occ_disorder, title="Sleep Disorder Percentage by Occupation",
                color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_layout(yaxis_title="Percentage (%)", xaxis_title="Occupation")
    st.plotly_chart(fig, use_container_width=True)

def correlation_tab(filtered_df, full_df):
    """Correlation analysis tab"""
    st.header("📈 Correlation Analysis")
    
    # Correlation matrix
    numeric_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                   'Stress Level', 'Heart Rate', 'Daily Steps', 'Sleep Efficiency']
    
    correlation_matrix = filtered_df[numeric_cols].corr()
    
    # Interactive correlation heatmap
    fig = px.imshow(correlation_matrix, 
                   title="Sleep Health Correlation Matrix",
                   color_continuous_scale='RdBu_r',
                   color_continuous_midpoint=0,
                   text_auto='.2f')
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sleep Duration Correlations")
        sleep_corrs = correlation_matrix['Sleep Duration'].drop('Sleep Duration').sort_values(key=abs, ascending=False)
        
        fig = px.bar(x=sleep_corrs.values, y=sleep_corrs.index,
                    orientation='h', title="Correlations with Sleep Duration",
                    color=sleep_corrs.values, color_continuous_scale='RdBu_r',
                    color_continuous_midpoint=0)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sleep Quality Correlations")
        quality_corrs = correlation_matrix['Quality of Sleep'].drop('Quality of Sleep').sort_values(key=abs, ascending=False)
        
        fig = px.bar(x=quality_corrs.values, y=quality_corrs.index,
                    orientation='h', title="Correlations with Sleep Quality",
                    color=quality_corrs.values, color_continuous_scale='RdBu_r',
                    color_continuous_midpoint=0)
        st.plotly_chart(fig, use_container_width=True)
    
    # Scatter plots for key relationships
    st.subheader("Key Relationships")
    
    scatter_options = st.selectbox("Select Relationship to Explore:",
                                  ["Sleep Duration vs Quality", "Stress vs Sleep Duration",
                                   "Daily Steps vs Sleep Duration", "Age vs Sleep Duration"])
    
    if scatter_options == "Sleep Duration vs Quality":
        fig = px.scatter(filtered_df, x='Sleep Duration', y='Quality of Sleep',
                        color='Sleep Disorder Status', size='Physical Activity Level',
                        hover_data=['Age', 'Occupation'], title="Sleep Duration vs Quality")
    elif scatter_options == "Stress vs Sleep Duration":
        fig = px.scatter(filtered_df, x='Stress Level', y='Sleep Duration',
                        color='Sleep Disorder Status', size='Age',
                        hover_data=['Occupation'], title="Stress Level vs Sleep Duration")
    elif scatter_options == "Daily Steps vs Sleep Duration":
        fig = px.scatter(filtered_df, x='Daily Steps', y='Sleep Duration',
                        color='Activity Level', size='Physical Activity Level',
                        hover_data=['Age', 'Occupation'], title="Daily Steps vs Sleep Duration")
    else:
        fig = px.scatter(filtered_df, x='Age', y='Sleep Duration',
                        color='Sleep Disorder Status', size='Quality of Sleep',
                        hover_data=['Occupation'], title="Age vs Sleep Duration")
    
    st.plotly_chart(fig, use_container_width=True)

def demographics_tab(filtered_df, full_df):
    """Demographics analysis tab"""
    st.header("👥 Demographics Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sleep Patterns by Age Group")
        age_sleep = filtered_df.groupby('Age Group')[['Sleep Duration', 'Quality of Sleep', 'Stress Level']].mean()
        
        fig = px.bar(age_sleep, title="Sleep Metrics by Age Group",
                    barmode='group', color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sleep Disorders by Age Group")
        age_disorder = pd.crosstab(filtered_df['Age Group'], filtered_df['Sleep Disorder Status'], normalize='index') * 100
        
        fig = px.bar(age_disorder, title="Sleep Disorder Distribution by Age Group",
                    color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig, use_container_width=True)
    
    # Gender analysis if gender column exists
    if 'Gender' in filtered_df.columns:
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("Sleep Duration by Gender")
            gender_sleep = filtered_df.groupby('Gender')['Sleep Duration'].mean()
            fig = px.bar(x=gender_sleep.index, y=gender_sleep.values,
                        title="Average Sleep Duration by Gender",
                        color=gender_sleep.values, color_continuous_scale='viridis')
            st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            st.subheader("Sleep Disorders by Gender")
            gender_disorder = pd.crosstab(filtered_df['Gender'], filtered_df['Sleep Disorder Status'], normalize='index') * 100
            fig = px.bar(gender_disorder, title="Sleep Disorder Rate by Gender",
                        color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(fig, use_container_width=True)
    
    # Activity level analysis
    st.subheader("Physical Activity Impact")
    activity_metrics = filtered_df.groupby('Activity Level')[['Sleep Duration', 'Quality of Sleep', 'Stress Level']].mean()
    
    fig = px.bar(activity_metrics, title="Sleep Metrics by Activity Level",
                barmode='group', color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig, use_container_width=True)

def individual_explorer_tab(filtered_df, full_df):
    """Individual data explorer tab"""
    st.header("🔍 Individual Data Explorer")
    
    st.subheader("Custom Analysis Builder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        x_axis = st.selectbox("Select X-axis:", 
                             ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                              'Stress Level', 'Heart Rate', 'Daily Steps'])
        
        chart_type = st.selectbox("Select Chart Type:", 
                                 ['Scatter Plot', 'Box Plot', 'Histogram', 'Bar Chart'])
    
    with col2:
        if chart_type == 'Scatter Plot':
            y_axis = st.selectbox("Select Y-axis:", 
                                 ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                                  'Stress Level', 'Heart Rate', 'Daily Steps', 'Age'])
            color_by = st.selectbox("Color by:", 
                                   ['Sleep Disorder Status', 'Age Group', 'Occupation', 
                                    'Activity Level', 'Sleep Quality Category'])
        else:
            y_axis = None
            color_by = st.selectbox("Group by:", 
                                   ['Sleep Disorder Status', 'Age Group', 'Occupation', 
                                    'Activity Level', 'Sleep Quality Category'])
    
    # Generate custom chart
    if chart_type == 'Scatter Plot':
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color=color_by,
                        hover_data=['Occupation', 'Age'], title=f"{x_axis} vs {y_axis}")
    elif chart_type == 'Box Plot':
        fig = px.box(filtered_df, x=color_by, y=x_axis, title=f"{x_axis} by {color_by}")
    elif chart_type == 'Histogram':
        fig = px.histogram(filtered_df, x=x_axis, color=color_by, title=f"{x_axis} Distribution")
    else:  # Bar Chart
        grouped_data = filtered_df.groupby(color_by)[x_axis].mean().reset_index()
        fig = px.bar(grouped_data, x=color_by, y=x_axis, title=f"Average {x_axis} by {color_by}")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Data table
    st.subheader("Filtered Data Table")
    
    # Display options
    show_columns = st.multiselect("Select columns to display:",
                                 filtered_df.columns.tolist(),
                                 default=['Occupation', 'Age', 'Sleep Duration', 'Quality of Sleep', 
                                         'Stress Level', 'Sleep Disorder Status'])
    
    if show_columns:
        st.dataframe(filtered_df[show_columns], use_container_width=True)
    
    # Download filtered data
    if st.button("Download Filtered Data"):
        csv = filtered_df.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv, file_name="filtered_sleep_data.csv", mime="text/csv")

if __name__ == "__main__":
    main()
