# Industrial-Human-Resources
1. Problem Statement
Describe the challenge of analyzing the industrial classification of workers across different states in India.
Mention the goal of geo-visualization to provide insights into the workforce distribution by industries, considering different types of workers and their geographic locations.
2. Tools Used
Programming Language: Python
Libraries: Pandas, Numpy, Seaborn, Matplotlib, Scipy, Sklearn, TfidfVectorizer, KMeans, PCA, RandomForestClassifier
Technologies: Streamlit for dashboard app development, GitHub for version control, LinkedIn for sharing the project.
3. Approaches
Data Collection: Merging multiple CSV files using Python's glob and Pandas.
Data Cleaning: Removing non-numeric characters, handling missing values, and converting data types.
Outlier Detection and Handling: Using Z-score and IQR methods to clean the data.
Feature Engineering: Transforming features like logarithmic transformation, scaling, and OneHotEncoding.
Clustering: Applying KMeans clustering on text data and numerical data to group industries and workers.
Modeling: Building a Random Forest classifier to predict industry clusters based on the dataset.
Visualization: Utilizing Seaborn, Matplotlib, and PCA for visualizing data distributions and clusters.
4. EDA Insights

Present distributions of workers by different categories such as Main Workers and Marginal Workers, both Rural and Urban.
Show boxplots before and after outlier removal, histograms of log-transformed features, and PCA plots to visualize clustering.
Discuss the industry clusters identified by KMeans and their significance in understanding the workforce distribution across different regions.
