---
aid: amazon-redshift
name: Amazon Redshift
description: Amazon Redshift is a fast, fully managed cloud data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-redshift/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Analytics
  - Big Data
  - Cloud
  - Data Lake
  - Data Warehouse
  - ETL
  - Machine Learning
  - Serverless
  - SQL
apis:
  - name: Amazon Redshift API
    description: The Amazon Redshift API for managing clusters, snapshots, and configurations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/redshift/
    baseURL: https://redshift.amazonaws.com
    tags:
      - Clusters
      - Data Warehouse
      - Snapshots
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/redshift/2012-12-01/openapi.yaml
      - type: APIReference
        url: https://docs.aws.amazon.com/redshift/latest/APIReference/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/redshift/pricing/
      - type: Console
        url: https://console.aws.amazon.com/redshift/
      - type: SDK
        url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html
        title: Python SDK
      - type: SDK
        url: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/redshift/
        title: JavaScript SDK
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/redshift/
      - type: BestPractices
        url: https://docs.aws.amazon.com/redshift/latest/dg/best-practices.html
      - type: Security
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/security.html
      - type: FAQ
        url: https://aws.amazon.com/redshift/faqs/
      - type: ReleaseNotes
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html
      - type: ChangeLog
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/document-history.html
  - name: Amazon Redshift Data API
    description: The Amazon Redshift Data API for running SQL statements without managing connections. Supports asynchronous execution with IAM and Secrets Manager authentication.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html
    baseURL: https://redshift-data.amazonaws.com
    tags:
      - Data API
      - Serverless
      - SQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html
      - type: APIReference
        url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-redshift-data-api-openapi.yml
      - type: SDK
        url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-data.html
        title: Python SDK
      - type: SDK
        url: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/redshift-data/
        title: JavaScript SDK
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/redshift-data/
      - type: GettingStarted
        url: https://aws.amazon.com/blogs/big-data/get-started-with-the-amazon-redshift-data-api/
  - name: Amazon Redshift Serverless API
    description: The Amazon Redshift Serverless API for managing serverless data warehouse workgroups, namespaces, and capacity without provisioning clusters.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html
    baseURL: https://redshift-serverless.amazonaws.com
    tags:
      - Data Warehouse
      - Namespaces
      - Serverless
      - Workgroups
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html
      - type: APIReference
        url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/Welcome.html
      - type: SDK
        url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift-serverless.html
        title: Python SDK
      - type: SDK
        url: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/redshift-serverless/
        title: JavaScript SDK
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/redshift-serverless/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html
      - type: Pricing
        url: https://aws.amazon.com/redshift/pricing/
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/big-data/category/database/amazon-redshift/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Documentation
    url: https://docs.aws.amazon.com/redshift/
  - type: GettingStarted
    url: https://aws.amazon.com/redshift/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/redshift/faqs/
  - type: Pricing
    url: https://aws.amazon.com/redshift/pricing/
  - type: Console
    url: https://console.aws.amazon.com/redshift/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Features
    data:
      - name: Massively Parallel Processing
        description: Distributed query execution across multiple nodes for petabyte-scale analytics with sub-second response times.
      - name: Serverless Data Warehouse
        description: Auto-scaling compute capacity without cluster provisioning, paying only for compute used during queries.
      - name: Data API
        description: Run SQL statements without managing database connections using IAM-based authentication and asynchronous execution.
      - name: Federated Query
        description: Query data across Amazon RDS, Aurora, and S3 data lakes without moving data using federated query capabilities.
      - name: Machine Learning Integration
        description: Build, train, and deploy ML models directly in Redshift using SQL with Amazon SageMaker integration.
      - name: Concurrency Scaling
        description: Automatically add transient capacity to handle bursts of concurrent queries without performance degradation.
  - type: UseCases
    data:
      - name: Business Intelligence Analytics
        description: Run complex analytical queries across petabytes of structured data for BI dashboards and reporting.
      - name: Data Lake Analytics
        description: Query data directly in Amazon S3 using Redshift Spectrum without loading it into the warehouse.
      - name: Real-Time Analytics
        description: Ingest streaming data and run near-real-time analytics on operational data for instant insights.
      - name: ETL Pipeline Processing
        description: Transform and load large datasets using SQL-based ETL operations within the data warehouse.
      - name: Serverless Ad-Hoc Queries
        description: Run on-demand analytical queries without provisioning clusters using Redshift Serverless and Data API.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Load data from and query data in S3 using COPY commands, Redshift Spectrum, and data lake integration.
      - name: AWS Glue
        description: Automated ETL job orchestration and data catalog integration for data warehouse loading.
      - name: Amazon QuickSight
        description: Connect QuickSight directly to Redshift for serverless BI dashboards and visualizations.
      - name: AWS Lambda
        description: Trigger Lambda functions from Redshift Data API results for event-driven data processing workflows.
      - name: Terraform
        description: Provision and manage Redshift clusters and serverless workgroups using Terraform infrastructure-as-code.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
