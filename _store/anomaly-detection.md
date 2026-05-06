---
name: Anomaly Detection
description: A curated collection of APIs, tools, and platforms for detecting anomalies in data streams, time series, and multivariate metrics. Covers cloud ML services, observability platforms, and open-source frameworks used for fraud detection, predictive maintenance, IoT monitoring, and security analytics.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: 2024-01-15T00:00:00.000Z
modified: 2026-04-19T00:00:00.000Z
specificationVersion: '0.16'
url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/apis.yml
apis:
  - name: Azure AI Anomaly Detector
    description: Azure AI Anomaly Detector is a managed REST API service that enables monitoring and detection of anomalies in time series data without requiring machine learning expertise. Supports univariate batch and streaming detection, multivariate detection using Graph Attention Networks for up to 300 correlated signals, and change-point detection. The service is being retired on 1 October 2026 in favor of Microsoft Fabric real-time intelligence.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview
    baseURL: https://api.cognitive.microsoft.com
    tags:
      - Anomaly Detection
      - Azure
      - Machine Learning
      - Microsoft
      - Multivariate
      - Time Series
      - Univariate
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/anomalydetector/
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/quickstarts/client-libraries
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/azure/ai-services/anomaly-detector/tutorials/batch-anomaly-detection-powerbi
      - type: GitHubRepository
        url: https://github.com/microsoft/anomaly-detector
    contact:
      - FN: Microsoft Azure Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Elasticsearch Anomaly Detection API
    description: Elasticsearch Machine Learning APIs provide a comprehensive suite of anomaly detection capabilities for time series data stored in Elasticsearch indices. Supports creating and managing anomaly detection jobs and datafeeds, accessing bucket, record, category, and influencer results, model snapshots, calendars, scheduled events, and forecasting. Part of the Elastic Stack ML feature set available in subscriptions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.elastic.co/guide/en/elasticsearch/reference/current/ml-apis.html
    baseURL: https://your-elasticsearch-host:9200
    tags:
      - Anomaly Detection
      - Elasticsearch
      - Machine Learning
      - Monitoring
      - Time Series
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/elasticsearch/reference/current/ml-apis.html
      - type: APIReference
        url: https://www.elastic.co/guide/en/elasticsearch/reference/current/ml-ad-apis.html
      - type: GettingStarted
        url: https://www.elastic.co/guide/en/machine-learning/current/ml-ad-overview.html
      - type: GitHubOrganization
        url: https://github.com/elastic
    contact:
      - FN: Elastic Support
        url: https://www.elastic.co/support
  - name: Datadog Anomaly Monitor API
    description: Datadog's Monitors API supports anomaly detection monitors that identify unusual metric behavior using historical pattern analysis including trends, day-of-week, and time-of-day seasonality. Offers three detection algorithms — Basic, Agile (SARIMA), and Robust (seasonal-trend decomposition) — configurable via REST API. Available across regional endpoints for US, EU, AP1, AP2, GOV, US3, and US5 deployments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.datadoghq.com/monitors/types/anomaly/
    baseURL: https://api.datadoghq.com
    tags:
      - Anomaly Detection
      - Datadog
      - Monitoring
      - Observability
      - Time Series
    properties:
      - type: Documentation
        url: https://docs.datadoghq.com/monitors/types/anomaly/
      - type: APIReference
        url: https://docs.datadoghq.com/api/latest/monitors/
      - type: Authentication
        url: https://docs.datadoghq.com/api/latest/authentication/
      - type: GitHubOrganization
        url: https://github.com/DataDog
    contact:
      - FN: Datadog Support
        url: https://www.datadoghq.com/support/
  - name: AWS Lookout for Metrics
    description: Amazon Lookout for Metrics is a fully managed ML service that automatically detects anomalies in business and operational data. It connects to data sources including Amazon S3, Amazon Redshift, Amazon CloudWatch, and SaaS applications, learns each metric's normal behavior, and sends alerts when anomalies are detected. Provides root cause analysis grouping related anomalies for faster diagnosis.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://aws.amazon.com/lookout-for-metrics/
    baseURL: https://lookoutmetrics.us-east-1.amazonaws.com
    tags:
      - Amazon Web Services
      - Anomaly Detection
      - AWS
      - Business Metrics
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lookoutmetrics/latest/dev/lookoutmetrics-welcome.html
      - type: APIReference
        url: https://docs.aws.amazon.com/lookoutmetrics/latest/api/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/lookoutmetrics/latest/dev/lookoutmetrics-gettingstarted.html
      - type: Pricing
        url: https://aws.amazon.com/lookout-for-metrics/pricing/
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
  - name: PyOD (Python Outlier Detection)
    description: PyOD is a comprehensive and scalable Python library for detecting outliers/anomalies in multivariate data. It includes more than 40 detection algorithms including deep learning approaches (AutoEncoder, VAE), proximity-based methods (LOF, CBLOF), linear models (PCA, OCSVM), and ensemble methods (IForest, LOCI). Widely used in research and production for fraud detection, intrusion detection, medical anomaly detection, and data quality monitoring.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://pyod.readthedocs.io/
    baseURL: https://pypi.org/project/pyod/
    tags:
      - Anomaly Detection
      - Data Science
      - Machine Learning
      - Open Source
      - Outlier Detection
      - Python
    properties:
      - type: Documentation
        url: https://pyod.readthedocs.io/en/latest/
      - type: APIReference
        url: https://pyod.readthedocs.io/en/latest/pyod.html
      - type: GitHubRepository
        url: https://github.com/yzhao062/pyod
      - type: SDK
        url: https://pypi.org/project/pyod/
    contact:
      - FN: PyOD Maintainers
        url: https://github.com/yzhao062/pyod/issues
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
tags:
  - Anomaly Detection
  - Artificial Intelligence
  - Data Science
  - Fraud Detection
  - Machine Learning
  - Monitoring
  - Observability
  - Outlier Detection
  - Pattern Recognition
  - Security
  - Time Series
include: []
common:
  - type: GitHubOrganization
    url: https://github.com/api-evangelist/anomaly-detection
  - type: BestPractices
    url: https://pyod.readthedocs.io/en/latest/faq.html
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/AI-Customer-Engineering-Team/Introducing-Azure-Anomaly-Detector-API/ba-p/490162
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-anomaly-schema.json
    title: Anomaly Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-time-series-schema.json
    title: Time Series Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-detection-job-schema.json
    title: Detection Job Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/vocabulary/anomaly-detection-vocabulary.yaml
  - type: Features
    data:
      - name: Univariate Time Series Detection
        description: Detect anomalies in a single time series metric using statistical algorithms, SARIMA models, and SR-CNN approaches for both batch and real-time streaming use cases.
      - name: Multivariate Detection
        description: Identify anomalies across multiple correlated metrics simultaneously using graph attention networks and correlation analysis, capturing system-level failures invisible in individual metrics.
      - name: Streaming and Batch Modes
        description: Support for both real-time streaming anomaly detection on incoming data points and batch retrospective analysis across historical datasets.
      - name: Change Point Detection
        description: Identify structural breaks and trend changes in time series data beyond point anomalies, enabling detection of regime shifts and concept drift.
      - name: Root Cause Analysis
        description: Group related anomalies and surface likely contributing factors to accelerate diagnosis and response.
      - name: Algorithm Diversity
        description: Access to a wide range of detection algorithms from statistical methods to deep learning, including IForest, LOF, OCSVM, AutoEncoder, VAE, and SARIMA.
  - type: UseCases
    data:
      - name: Fraud Detection
        description: Identify fraudulent transactions, account takeovers, and suspicious behavioral patterns in financial and e-commerce systems.
      - name: Predictive Maintenance
        description: Detect early signs of equipment failure in industrial IoT systems by identifying anomalous sensor readings before breakdowns occur.
      - name: IT and Security Operations
        description: Detect unusual network traffic, unauthorized access patterns, and security incidents in real time using behavioral baselines.
      - name: Business Metrics Monitoring
        description: Alert on unexpected drops or spikes in KPIs such as revenue, conversion rates, user engagement, or API error rates.
      - name: Healthcare Monitoring
        description: Monitor patient vitals, lab values, and medical device readings for out-of-range or clinically significant anomalies.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Connect anomaly detection pipelines to S3 data lakes for batch analysis of historical metric data.
      - name: Elasticsearch / OpenSearch
        description: Use Elasticsearch ML datafeeds to continuously analyze indices for anomalous patterns using built-in anomaly detection jobs.
      - name: Amazon CloudWatch
        description: Pipe CloudWatch metrics into AWS Lookout for Metrics for automated operational anomaly alerting.
      - name: Microsoft Fabric / Real-Time Intelligence
        description: Migration target for Azure Anomaly Detector users, providing integrated real-time anomaly detection within the Microsoft Fabric analytics platform.
      - name: Grafana
        description: Visualize anomaly scores and detected anomalies from Elasticsearch ML and Datadog within Grafana dashboards.
---
