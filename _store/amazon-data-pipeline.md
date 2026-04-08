---
aid: amazon-data-pipeline
url: https://raw.githubusercontent.com/api-evangelist/amazon-data-pipeline/refs/heads/main/apis.yml
apis:
- name: AWS Data Pipeline API
  description: The AWS Data Pipeline API provides a web service for processing and moving data between different AWS compute and storage services as well as on-premises data sources at specified intervals. The API allows you to create pipeline definitions, schedule data transformations, set up retry and failure handling logic, and monitor pipeline execution. It supports data-driven workflows that can access data from Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
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
  - type: Getting Started
    url: https://aws.amazon.com/datapipeline/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/datapipeline/faqs/
name: Amazon Data Pipeline
tags:
- AWS
- Data Processing
- ETL
- Workflows
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals. With AWS Data Pipeline, you can regularly access your data where it is stored, transform and process it at scale, and efficiently transfer the results to AWS services such as Amazon S3, Amazon RDS, Amazon DynamoDB, and Amazon EMR.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

