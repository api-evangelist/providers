---
aid: amazon-data-pipeline
name: Amazon Data Pipeline
description: AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. With AWS Data Pipeline, you can regularly access your data where it is stored, transform and process it at scale, and efficiently transfer the results to AWS services such as Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR. It supports data-driven workflows with retry, failure handling, and scheduling capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Data Processing
  - ETL
  - Workflows
  - Data Pipeline
  - Automation
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-data-pipeline:aws-data-pipeline-api
    name: AWS Data Pipeline API
    description: The AWS Data Pipeline API provides a web service for processing and moving data between different AWS compute and storage services as well as on-premises data sources at specified intervals. The API allows you to create pipeline definitions, schedule data transformations, configure retry and failure handling logic, and monitor pipeline execution across Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR.
    humanURL: https://aws.amazon.com/datapipeline/
    baseURL: https://datapipeline.amazonaws.com
    tags:
      - AWS
      - Data Processing
      - ETL
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/datapipeline/
      - type: OpenAPI
        url: openapi/amazon-data-pipeline-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/datapipeline/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/datapipeline/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/datapipeline/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/
      - type: JSONSchema
        url: json-schema/pipeline-object-schema.json
      - type: JSONSchema
        url: json-schema/pipeline-description-schema.json
      - type: JSONLD
        url: json-ld/amazon-data-pipeline-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/datapipeline/
  - type: DeveloperPortal
    url: https://aws.amazon.com/datapipeline/
  - type: Documentation
    url: https://docs.aws.amazon.com/datapipeline/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/datapipeline/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-data-pipeline-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-data-pipeline-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/etl-pipeline-operations.yaml
  - type: NaftikoCapability
    url: capabilities/shared/data-pipeline.yaml
  - type: Features
    data:
      - name: Data-Driven Workflows
        description: Define complex data processing workflows with activities, data nodes, schedules, and preconditions using a declarative pipeline definition.
      - name: Multi-Service Integration
        description: Move and transform data between Amazon S3, Amazon RDS, Amazon DynamoDB, Amazon Redshift, and Amazon EMR in a single pipeline.
      - name: Flexible Scheduling
        description: Schedule pipeline runs at fixed intervals (hourly, daily, weekly) or trigger them based on data availability preconditions.
      - name: Automated Retry and Failure Handling
        description: Configure automatic retries for failed activities with configurable retry intervals, timeout settings, and failure notifications.
      - name: On-Premises Data Support
        description: Process data from on-premises databases and file systems using the Data Pipeline Task Runner agent installed locally.
      - name: EMR Integration
        description: Launch and manage Amazon EMR clusters as pipeline resources to run Hive, Pig, and MapReduce jobs as part of data workflows.
      - name: Pipeline Versioning
        description: Manage active and latest pipeline definition versions, enabling updates to running pipelines without disrupting current execution.
  - type: UseCases
    data:
      - name: Daily ETL Workflows
        description: Schedule daily extraction, transformation, and loading of data from relational databases into S3 or Redshift for analytics processing.
      - name: Log Processing Pipelines
        description: Process application and server log files from S3 using EMR activities to generate aggregated reports and analytics datasets.
      - name: Database Migration
        description: Migrate data between on-premises databases and AWS managed database services using scheduled pipeline activities.
      - name: Data Lake Ingestion
        description: Automate the ingestion and transformation of raw data into structured formats in S3 data lakes for downstream analytics.
      - name: Cross-Region Data Replication
        description: Replicate DynamoDB tables or S3 data across AWS regions using scheduled pipeline copy activities for disaster recovery.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Primary data node type for reading input data and writing output data in pipeline ETL activities using S3DataNode.
      - name: Amazon EMR
        description: Managed Hadoop/Spark cluster resource for running large-scale data processing activities including Hive, Pig, and MapReduce jobs.
      - name: Amazon RDS
        description: Relational database data node for SQL-based data extraction and loading between RDS instances and S3 or Redshift.
      - name: Amazon DynamoDB
        description: NoSQL data node for importing and exporting DynamoDB table data in pipeline activities for batch processing workflows.
      - name: Amazon Redshift
        description: Data warehouse target for loading processed pipeline output data for business intelligence and analytics queries.
      - name: AWS Glue
        description: Modern alternative managed ETL service that can complement or replace Data Pipeline for serverless data transformation workflows.
      - name: Amazon CloudWatch
        description: Monitor pipeline execution status, set up alarms for pipeline failures, and track activity completion metrics.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
