---
aid: aws
url: https://raw.githubusercontent.com/api-evangelist/aws/refs/heads/main/apis.yml
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
name: Amazon Web Services (AWS)
tags:
- Cloud Computing
- IaaS
- Infrastructure
- PaaS
- Platform as a Service
- Serverless
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Web Services is a comprehensive collection of cloud computing services and APIs provided by Amazon, offering infrastructure as a service, platform as a service, and software as a service solutions globally.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

