---
aid: amazon-forecast
name: Amazon Forecast
description: Amazon Forecast is a fully managed service that uses machine learning to deliver highly accurate forecasts. It analyzes your historical time-series data and automatically selects the right machine learning algorithms to generate accurate forecasts with no machine learning expertise required.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Forecasting
  - Machine Learning
  - Predictive Analytics
  - Time Series
url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-forecast:amazon-forecast-api
    name: Amazon Forecast API
    description: The Amazon Forecast API provides programmatic access to create and manage datasets, predictors, forecasts, and export jobs for time-series forecasting using machine learning models.
    humanURL: https://aws.amazon.com/forecast/
    baseURL: https://forecast.amazonaws.com
    tags:
      - Forecasting
      - Machine Learning
      - Time Series
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html
      - type: OpenAPI
        url: openapi/amazon-forecast-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-forecast-dataset-schema.json
      - type: JSONSchema
        url: json-schema/amazon-forecast-predictor-schema.json
      - type: JSONSchema
        url: json-schema/amazon-forecast-forecast-schema.json
      - type: JSONSchema
        url: json-schema/amazon-forecast-dataset-group-schema.json
      - type: JSONSchema
        url: json-schema/amazon-forecast-tag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-forecast-dataset-structure.json
      - type: JSONStructure
        url: json-structure/amazon-forecast-predictor-structure.json
      - type: JSONStructure
        url: json-structure/amazon-forecast-forecast-structure.json
      - type: JSONStructure
        url: json-structure/amazon-forecast-dataset-group-structure.json
      - type: JSONStructure
        url: json-structure/amazon-forecast-tag-structure.json
      - type: Example
        url: examples/amazon-forecast-dataset-example.json
      - type: Example
        url: examples/amazon-forecast-dataset-group-example.json
      - type: Example
        url: examples/amazon-forecast-predictor-example.json
      - type: Example
        url: examples/amazon-forecast-forecast-example.json
      - type: Example
        url: examples/amazon-forecast-tag-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/forecast/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/forecast/pricing/
      - type: FAQ
        url: https://aws.amazon.com/forecast/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/forecast/latest/dg/API_Operations.html
common:
  - type: Portal
    url: https://aws.amazon.com/forecast/
  - type: Website
    url: https://aws.amazon.com/forecast/
  - type: Documentation
    url: https://docs.aws.amazon.com/forecast/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/forecast/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-forecast
  - type: SpectralRules
    url: rules/amazon-forecast-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/forecast.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-forecast-time-series-prediction.yaml
  - type: Vocabulary
    url: vocabulary/amazon-forecast-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-forecast-context.jsonld
  - type: Features
    data:
      - name: AutoML
        description: Automatically evaluates and selects from over 60 ML algorithms to find the best fit for your time-series data.
      - name: Probabilistic Forecasts
        description: Generates quantile forecasts (p10, p50, p90) to estimate demand uncertainty and plan inventory buffers.
      - name: Domain-Specific Models
        description: Pre-built domain configurations for retail, workforce, traffic, and cloud capacity forecasting.
      - name: Related Time Series
        description: Incorporate external factors (price, promotions, holidays) as related time-series data to improve accuracy.
      - name: HPO (Hyperparameter Optimization)
        description: Automatic tuning of model hyperparameters to maximize forecast accuracy.
      - name: Explainability
        description: Forecast Explainability reports show which features most impact each individual forecast.
      - name: S3 Export
        description: Export forecast results to Amazon S3 in CSV format for downstream consumption.
  - type: UseCases
    data:
      - name: Retail Demand Forecasting
        description: Predict item-level sales for inventory planning and replenishment across stores.
      - name: Workforce Capacity Planning
        description: Forecast staffing needs for contact centers and seasonal workforce management.
      - name: Cloud Resource Forecasting
        description: Predict EC2 capacity requirements to optimize reserved instance purchases.
      - name: Supply Chain Optimization
        description: Forecast component and raw material demand to reduce stockouts and carrying costs.
      - name: Financial Revenue Forecasting
        description: Project revenue by product, region, and channel for financial planning.
      - name: Energy Load Forecasting
        description: Predict electricity load and generation requirements for grid balancing.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Import training datasets and export forecast results to S3.
      - name: AWS Glue
        description: Transform and prepare time-series data for Forecast using AWS Glue ETL jobs.
      - name: Amazon SageMaker
        description: Combine Amazon Forecast with SageMaker for custom ML pipelines.
      - name: AWS IAM
        description: Control access to Forecast datasets, predictors, and forecasts with IAM policies.
      - name: Amazon CloudWatch
        description: Monitor Forecast job status, errors, and API usage metrics.
      - name: AWS KMS
        description: Encrypt Forecast datasets and training data with customer-managed KMS keys.
      - name: Amazon QuickSight
        description: Visualize exported forecast data in QuickSight dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
