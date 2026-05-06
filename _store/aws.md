---
aid: aws
name: Amazon Web Services (AWS)
description: Amazon Web Services is a comprehensive collection of cloud computing services and APIs provided by Amazon, offering infrastructure as a service, platform as a service, and software as a service solutions globally.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Computing
  - IaaS
  - Infrastructure
  - PaaS
  - Platform as a Service
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/aws/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: aws:amazon-ec2
    name: Amazon EC2
    description: Scalable virtual servers in the cloud.
    humanURL: https://aws.amazon.com/ec2/
    baseURL: https://ec2.amazonaws.com
    tags:
      - Compute
      - Infrastructure
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ec2/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
  - aid: aws:amazon-s3
    name: Amazon S3
    description: Scalable object storage service for data backup, archival, and analytics.
    humanURL: https://aws.amazon.com/s3/
    baseURL: https://s3.amazonaws.com
    tags:
      - Data Lake
      - Object Storage
      - Storage
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/s3/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/s3/2006-03-01/openapi.yaml
  - aid: aws:amazon-lambda
    name: Amazon Lambda
    description: Run code without thinking about servers or clusters.
    humanURL: https://aws.amazon.com/lambda/
    baseURL: https://lambda.amazonaws.com
    tags:
      - Compute
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.yaml
  - aid: aws:amazon-dynamodb
    name: Amazon DynamoDB
    description: Fast and flexible NoSQL database service for any scale.
    humanURL: https://aws.amazon.com/dynamodb/
    baseURL: https://dynamodb.amazonaws.com
    tags:
      - Database
      - Key-Value
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/dynamodb/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.yaml
  - aid: aws:amazon-rds
    name: Amazon RDS
    description: Managed relational database service for MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB.
    humanURL: https://aws.amazon.com/rds/
    baseURL: https://rds.amazonaws.com
    tags:
      - Database
      - Managed Service
      - Relational
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/rds/
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/rds/2014-10-31/openapi.yaml
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Documentation
    url: https://docs.aws.amazon.com/
  - type: Authentication
    url: https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Pricing
    url: https://aws.amazon.com/pricing/
  - type: Console
    url: https://console.aws.amazon.com/
  - type: ChangeLog
    url: https://aws.amazon.com/new/
  - type: Features
    data:
      - 'Amazon Web Services (AWS): hundreds of services across Cloud Infrastructure'
      - 'Detailed pricing: see https://aws.amazon.com/pricing/'
      - 'Service: EC2 (compute)'
      - 'Service: S3 (object storage)'
      - 'Service: EBS (block storage)'
      - 'Service: RDS (managed SQL)'
      - 'Service: DynamoDB (NoSQL)'
      - 'Service: Lambda (serverless)'
      - 'Service: API Gateway'
      - 'Service: CloudFront (CDN)'
      - 'Service: Route 53 (DNS)'
      - 'Service: VPC (networking)'
      - 'Service: IAM (identity)'
      - 'Service: KMS (encryption)'
      - 'Service: Secrets Manager'
      - 'Service: CloudWatch (monitoring)'
      - 'Service: EKS (Kubernetes)'
      - 'Service: ECS (containers)'
      - 'Service: ECR (container registry)'
      - 'Service: SQS (queue)'
      - 'Service: SNS (pub-sub)'
      - 'Service: SES (email)'
      - 'Service: Bedrock (AI/ML)'
      - 'Service: SageMaker (ML)'
      - 'Service: Comprehend (NLP)'
      - 'Service: Rekognition (vision)'
      - 'Service: Polly (TTS)'
      - 'Service: Transcribe (STT)'
      - 'Service: Translate'
      - 'Service: Athena (SQL on S3)'
      - 'Service: Redshift (data warehouse)'
      - 'Service: Glue (ETL)'
      - 'Service: EMR (Hadoop)'
      - 'Service: Kinesis (streaming)'
      - 'Service: MSK (managed Kafka)'
      - 'Service: OpenSearch'
      - 'Service: QuickSight (BI)'
    sources:
      - https://aws.amazon.com/pricing/
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Web Application Hosting
        description: Host scalable web applications with EC2, S3, CloudFront, and RDS.
      - name: Data Analytics
        description: Process and analyze large datasets using EMR, Redshift, Athena, and Glue.
      - name: Machine Learning
        description: Build and deploy ML models at scale using SageMaker, Rekognition, and Comprehend.
      - name: Disaster Recovery
        description: Implement multi-region disaster recovery strategies with minimal RPO and RTO.
      - name: IoT Applications
        description: Collect, process, and analyze IoT device data with AWS IoT Core and related services.
  - type: Integrations
    data:
      - name: Terraform
        description: Manage AWS infrastructure as code using the official AWS Terraform provider.
      - name: Kubernetes
        description: Deploy and manage Kubernetes workloads on AWS using Amazon EKS.
      - name: GitHub Actions
        description: Automate CI/CD pipelines deploying to AWS using GitHub Actions and OIDC.
      - name: Datadog
        description: Monitor AWS infrastructure and applications using the Datadog AWS integration.
      - name: Snowflake
        description: Integrate data workflows between Snowflake and AWS S3, Glue, and Lake Formation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
