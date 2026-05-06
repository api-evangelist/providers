---
aid: aws-redshift
name: AWS Redshift
description: Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to analyze all your data using standard SQL and existing Business Intelligence tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Big Data
  - Cloud Database
  - Data Warehouse
  - SQL
url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-redshift:amazon-redshift-api
    name: Amazon Redshift API
    description: The Amazon Redshift API provides programmatic access to create and manage Amazon Redshift clusters and their associated resources including snapshots, parameter groups, subnet groups, and reserved nodes.
    humanURL: https://aws.amazon.com/redshift/
    baseURL: https://redshift.{region}.amazonaws.com
    tags:
      - Clusters
      - Data Warehouse
      - Snapshots
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/aws-redshift-openapi.json
  - aid: aws-redshift:amazon-redshift-data-api
    name: Amazon Redshift Data API
    description: The Amazon Redshift Data API enables you to run SQL statements without managing connections via a secure HTTP endpoint. It supports both synchronous and asynchronous SQL execution against Redshift clusters and Redshift Serverless workgroups.
    humanURL: https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html
    baseURL: https://redshift-data.{region}.amazonaws.com
    tags:
      - Data Access
      - Serverless
      - SQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/aws-redshift-data-openapi.json
  - aid: aws-redshift:amazon-redshift-serverless-api
    name: Amazon Redshift Serverless API
    description: API for Amazon Redshift Serverless, which makes it easy to run analytics workloads without managing data warehouse infrastructure. Automatically provisions and scales data warehouse capacity on demand.
    humanURL: https://aws.amazon.com/redshift/redshift-serverless/
    baseURL: https://redshift-serverless.{region}.amazonaws.com
    tags:
      - Analytics
      - Auto-Scaling
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/Welcome.html
common:
  - type: Website
    url: https://aws.amazon.com/redshift/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/database/amazon-redshift/
  - type: ChangeLog
    url: https://aws.amazon.com/releasenotes/Amazon-Redshift/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Pricing
    url: https://aws.amazon.com/redshift/pricing/
  - type: GettingStarted
    url: https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
  - type: Documentation
    url: https://docs.aws.amazon.com/redshift/
  - type: SpectralRules
    url: rules/aws-redshift-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-redshift-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-warehouse-workflow.yaml
  - type: Features
    data:
      - name: Petabyte-Scale Storage
        description: Store and query petabytes of structured and semi-structured data with columnar storage.
      - name: Standard SQL Support
        description: Query data using standard SQL and connect with existing BI tools via JDBC/ODBC.
      - name: Massively Parallel Processing
        description: Distribute SQL operations across multiple nodes for high-performance query execution.
      - name: Columnar Storage
        description: Store data in columnar format for efficient analytical query performance and compression.
      - name: Automated Snapshots
        description: Automated and manual snapshots for point-in-time recovery of your cluster data.
      - name: Data Sharing
        description: Share live data across Redshift clusters and accounts without copying data.
      - name: ML Integration
        description: Run Amazon Redshift ML to create, train, and deploy machine learning models using SQL.
      - name: Serverless Mode
        description: Run analytics workloads without managing cluster infrastructure with Redshift Serverless.
      - name: Federated Query
        description: Query data across operational databases, data warehouses, and data lakes.
      - name: AQUA
        description: Advanced Query Accelerator for up to 10x faster query performance using distributed hardware-accelerated cache.
  - type: UseCases
    data:
      - name: Business Intelligence
        description: Power BI dashboards and reports with fast analytical queries over large datasets.
      - name: Log Analytics
        description: Analyze application logs and clickstream data for operational insights.
      - name: Financial Analytics
        description: Process financial transactions and generate regulatory reports over historical data.
      - name: Data Lake Analytics
        description: Query data in Amazon S3 data lakes using Redshift Spectrum without loading.
      - name: Machine Learning
        description: Build and deploy ML models directly within the warehouse using SQL with Redshift ML.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Load data from S3 and query data lake files using Redshift Spectrum.
      - name: Amazon Glue
        description: Catalog and ETL data into Redshift from various data sources.
      - name: Amazon QuickSight
        description: Connect QuickSight for BI visualization directly to Redshift.
      - name: AWS Lake Formation
        description: Manage fine-grained data access controls across Redshift and S3.
      - name: Amazon SageMaker
        description: Export training data and import ML model results from SageMaker.
      - name: dbt
        description: Transform data in Redshift using dbt data transformation framework.
      - name: Tableau
        description: Connect Tableau via JDBC/ODBC for interactive data visualization.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
