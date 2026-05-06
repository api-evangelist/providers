---
aid: apache-madlib
name: Apache MADlib
description: Apache MADlib is an open-source library for scalable in-database analytics. It provides data-parallel implementations of mathematical, statistical, and machine learning methods for structured and unstructured data, executed within PostgreSQL or Greenplum Database. MADlib enables data scientists to run machine learning algorithms directly in the database using SQL.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - In-Database Analytics
  - Machine Learning
  - PostgreSQL
  - SQL
  - Statistics
  - Deep Learning
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-madlib/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-madlib:apache-madlib
    name: Apache MADlib
    description: MADlib provides SQL-callable functions for classification, regression, clustering, dimensionality reduction, graph analytics, time series analysis, deep learning with Keras/TensorFlow backend, and other machine learning algorithms running directly within PostgreSQL or Greenplum Database with GPU acceleration support.
    humanURL: https://madlib.apache.org/docs/latest/index.html
    tags:
      - Machine Learning
      - PostgreSQL
      - SQL
      - Deep Learning
      - Statistics
    properties:
      - type: Documentation
        url: https://madlib.apache.org/docs/latest/index.html
      - type: GettingStarted
        url: https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide
      - type: GitHubRepository
        url: https://github.com/apache/madlib
common:
  - type: Portal
    url: https://madlib.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/madlib
  - type: Wiki
    url: https://cwiki.apache.org/confluence/display/MADLIB/
  - type: IssueTracker
    url: https://issues.apache.org/jira/browse/MADLIB
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: In-Database Machine Learning
        description: Run machine learning algorithms directly within PostgreSQL or Greenplum Database using SQL, eliminating data movement overhead.
      - name: Classification and Regression
        description: Support for logistic regression, linear regression, naive Bayes, decision trees, random forests, support vector machines, and more.
      - name: Clustering Algorithms
        description: K-Means, DBSCAN, and other clustering algorithms for unsupervised learning within the database.
      - name: Deep Learning with Keras/TensorFlow
        description: Train and serve deep learning models using Keras and TensorFlow backends with GPU acceleration support.
      - name: Graph Analytics
        description: Built-in graph algorithms for network analysis, path finding, and community detection on graph data stored in the database.
      - name: Time Series Analysis
        description: ARIMA, SARIMA, and other time series forecasting models running in-database.
      - name: Dimensionality Reduction
        description: PCA and SVD implementations for dimensionality reduction and feature extraction.
      - name: Model Selection and Hyperparameter Tuning
        description: Cross-validation and hyperparameter optimization frameworks for model selection.
      - name: Association Rules
        description: FP-Growth and Apriori algorithms for market basket analysis and association rule mining.
  - type: UseCases
    data:
      - name: Predictive Analytics
        description: Build predictive models for churn prediction, fraud detection, and demand forecasting directly on database data.
      - name: Recommendation Systems
        description: Implement collaborative filtering and content-based recommendation algorithms using in-database machine learning.
      - name: Customer Segmentation
        description: Cluster customers using K-Means and other algorithms to identify segments for targeted marketing.
      - name: Anomaly Detection
        description: Detect anomalies in time series and transactional data using statistical models running in-database.
      - name: Network Analysis
        description: Analyze social networks, supply chains, and communication graphs using built-in graph algorithms.
  - type: Integrations
    data:
      - name: PostgreSQL
        description: Primary execution environment supporting PostgreSQL versions 11 through 15.
      - name: Greenplum Database
        description: Native support for Greenplum Database GP6 and GP7 for massively parallel processing.
      - name: TensorFlow
        description: Deep learning backend integration for training neural networks within the database.
      - name: Keras
        description: High-level deep learning API integration for building and training models with GPU acceleration.
      - name: XGBoost
        description: Gradient boosting framework integration for high-performance tree-based models.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
