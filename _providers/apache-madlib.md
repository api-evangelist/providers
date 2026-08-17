---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: MADlib provides SQL-callable functions for classification, regression, clustering, dimensionality reduction, graph analytics, time series analysis, deep learning with Keras/TensorFlow backend, and oth
  name: Apache MADlib
  slug: apache-madlib
artifact_total: 25
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/madlib/blob/madlib2-master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-madlib-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-madlib-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://madlib.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/madlib
- group: other
  title: ''
  type: Wiki
  url: https://cwiki.apache.org/confluence/display/MADLIB/
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/browse/MADLIB
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache MADlib is an open-source library for scalable in-database analytics. It provides data-parallel implementations of mathematical, statistical, and machine learning methods for structured and unstructured data, executed within PostgreSQL or Greenplum Database. MADlib enables data scientists to run machine learning algorithms directly in the database using SQL.
features:
- description: Run machine learning algorithms directly within PostgreSQL or Greenplum Database using SQL, eliminating data movement overhead.
  name: In-Database Machine Learning
- description: Support for logistic regression, linear regression, naive Bayes, decision trees, random forests, support vector machines, and more.
  name: Classification and Regression
- description: K-Means, DBSCAN, and other clustering algorithms for unsupervised learning within the database.
  name: Clustering Algorithms
- description: Train and serve deep learning models using Keras and TensorFlow backends with GPU acceleration support.
  name: Deep Learning with Keras/TensorFlow
- description: Built-in graph algorithms for network analysis, path finding, and community detection on graph data stored in the database.
  name: Graph Analytics
- description: ARIMA, SARIMA, and other time series forecasting models running in-database.
  name: Time Series Analysis
- description: PCA and SVD implementations for dimensionality reduction and feature extraction.
  name: Dimensionality Reduction
- description: Cross-validation and hyperparameter optimization frameworks for model selection.
  name: Model Selection and Hyperparameter Tuning
- description: FP-Growth and Apriori algorithms for market basket analysis and association rule mining.
  name: Association Rules
finops:
- name: Apache Madlib Finops
  service_category: API
  slug: apache-madlib-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-madlib.png
integrations:
- description: Primary execution environment supporting PostgreSQL versions 11 through 15.
  name: PostgreSQL
- description: Native support for Greenplum Database GP6 and GP7 for massively parallel processing.
  name: Greenplum Database
- description: Deep learning backend integration for training neural networks within the database.
  name: TensorFlow
- description: High-level deep learning API integration for building and training models with GPU acceleration.
  name: Keras
- description: Gradient boosting framework integration for high-performance tree-based models.
  name: XGBoost
layout: provider
modified: '2026-04-19'
name: Apache MADlib
nav: Providers
network: true
overview: 'Apache MADlib publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include In-Database Analytics, Machine Learning, PostgreSQL, SQL, and Statistics.


  Apache MADlib''s developer surface includes developer portal and 9 more developer resources.'
plans:
- name: Apache Madlib Plans Pricing
  plan_count: 3
  slug: apache-madlib-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 5
  name: Apache Madlib Rate Limits
  slug: apache-madlib-rate-limits
score:
  band: emerging
  composite: 14.6
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-madlib/refs/heads/main/screenshots/apache-madlib-2026-06-20T172118.png
security:
- kind: domain-security
  name: Apache Madlib Domain Security
  slug: apache-madlib-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Madlib Vulnerability Disclosure
  slug: apache-madlib-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-madlib
tags:
- In-Database Analytics
- Machine Learning
- PostgreSQL
- SQL
- Statistics
- Deep Learning
use_cases:
- description: Build predictive models for churn prediction, fraud detection, and demand forecasting directly on database data.
  name: Predictive Analytics
- description: Implement collaborative filtering and content-based recommendation algorithms using in-database machine learning.
  name: Recommendation Systems
- description: Cluster customers using K-Means and other algorithms to identify segments for targeted marketing.
  name: Customer Segmentation
- description: Detect anomalies in time series and transactional data using statistical models running in-database.
  name: Anomaly Detection
- description: Analyze social networks, supply chains, and communication graphs using built-in graph algorithms.
  name: Network Analysis
website: https://madlib.apache.org/
---
