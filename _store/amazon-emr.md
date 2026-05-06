---
name: Amazon EMR
description: Amazon EMR is a cloud big data platform for running large-scale distributed data processing jobs, interactive SQL queries, and machine learning applications using open-source analytics frameworks such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/emr/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - Analytics
  - Apache Spark
  - AWS
  - Big Data
  - Data Processing
  - Hadoop
apis:
  - name: Amazon EMR API
    description: API for creating and managing Amazon EMR clusters, steps, instance groups, and running distributed big data processing workloads.
    humanURL: https://aws.amazon.com/emr/
    baseURL: https://elasticmapreduce.amazonaws.com
    tags:
      - Analytics
      - Big Data
      - Data Processing
      - Spark
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/
      - type: OpenAPI
        url: openapi/amazon-emr-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/emr/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/emr/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/emr/pricing/
      - type: FAQ
        url: https://aws.amazon.com/emr/faqs/
      - type: JSONSchema
        url: json-schema/amazon-emr-schema.json
      - type: JSONLD
        url: json-ld/amazon-emr-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/emr/
  - type: Documentation
    url: https://docs.aws.amazon.com/emr/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/emr/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/emr/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/emr
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-emr-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-emr-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-emr-vocabulary.yaml
  - type: Features
    data:
      - name: Apache Spark Support
        description: Run Apache Spark jobs for large-scale data processing and machine learning
      - name: Auto Scaling
        description: Automatically adjust cluster size based on workload demand
      - name: Spot Instance Integration
        description: Use EC2 Spot instances to reduce costs up to 90%
      - name: EMR Serverless
        description: Run analytics without provisioning or managing clusters
      - name: Studio Notebooks
        description: Develop and debug jobs using EMR Studio Jupyter notebooks
  - type: UseCases
    data:
      - name: ETL Data Processing
        description: Extract, transform, and load large datasets across data lakes and warehouses
      - name: Machine Learning
        description: Train machine learning models on large datasets using Spark MLlib
      - name: Log Analytics
        description: Process and analyze application logs at petabyte scale
      - name: Financial Risk Analysis
        description: Run Monte Carlo simulations and risk models on large datasets
  - type: Integrations
    data:
      - name: Amazon S3
        description: Use S3 as data lake storage for EMR clusters
      - name: AWS Glue
        description: Integrate with Glue Data Catalog for metadata management
      - name: Amazon Athena
        description: Query data processed by EMR using Athena SQL
      - name: Amazon SageMaker
        description: Hand off processed data to SageMaker for model training
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
