# Create a figure with subplots
plt.figure(figsize=(18, 12))

# 1. Annual Temperature Anomaly Time Series
plt.subplot(2, 2, 1)
plt.plot(clean_df['Year'], clean_df['J-D'], 'r-', label='Annual Mean')
plt.plot(clean_df['Year'], clean_df['5yr_Moving_Avg'], 'k-', linewidth=2, label='5-yr Moving Average')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
plt.title('Global Temperature Anomaly (Annual Mean)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# 2. Seasonal Temperature Anomalies
plt.subplot(2, 2, 2)
plt.plot(clean_df['Year'], clean_df['DJF'], 'b-', label='Winter (DJF)')
plt.plot(clean_df['Year'], clean_df['MAM'], 'g-', label='Spring (MAM)')
plt.plot(clean_df['Year'], clean_df['JJA'], 'r-', label='Summer (JJA)')
plt.plot(clean_df['Year'], clean_df['SON'], 'orange', label='Fall (SON)')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
plt.title('Seasonal Temperature Anomalies', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# 3. Monthly Anomalies for Recent Years
recent_years = clean_df[clean_df['Year'] >= 2010].copy()
plt.subplot(2, 2, 3)

# Get monthly data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
last_year = recent_years['Year'].max()
for year in range(last_year-4, last_year+1):
    if year in recent_years['Year'].values:
        year_data = recent_years[recent_years['Year'] == year]
        plt.plot(months, year_data[months].values[0], 'o-', label=str(int(year)))

plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
plt.title('Monthly Temperature Anomalies (Recent Years)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

# 4. Heatmap of monthly anomalies since 1980
plt.subplot(2, 2, 4)
recent_df = clean_df[clean_df['Year'] >= 1980].copy()
data_for_heatmap = recent_df[['Year'] + months].set_index('Year')

plt.imshow(data_for_heatmap.T, aspect='auto', cmap='coolwarm', 
           interpolation='nearest', vmin=-1, vmax=2)
plt.colorbar(label='Temperature Anomaly (°C)')
plt.title('Monthly Temperature Anomalies Since 1980', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Month', fontsize=12)
plt.yticks(range(12), months)
plt.xticks(range(0, len(recent_df), 5), recent_df['Year'].iloc[::5])

# Add text labels to show milestone years
plt.tight_layout()
plt.suptitle('NASA GISTEMP Global Temperature Analysis', fontsize=16, y=1.02)
plt.savefig('nasa_temperature_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Bonus: Decade Averages Bar Chart
plt.figure(figsize=(12, 6))
# Create decade column
clean_df['Decade'] = (clean_df['Year'] // 10) * 10
decade_means = clean_df.groupby('Decade')['J-D'].mean()

bars = plt.bar(decade_means.index.astype(str), decade_means, color='maroon')
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
plt.title('Global Temperature Anomaly by Decade', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Average Temperature Anomaly (°C)', fontsize=12)
plt.grid(True, axis='y', alpha=0.3)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{height:.2f}°C', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('nasa_temperature_by_decade.png', dpi=300)
plt.show()