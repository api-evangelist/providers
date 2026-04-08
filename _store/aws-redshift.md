---
aid: aws-redshift
url: https://raw.githubusercontent.com/api-evangelist/aws-redshift/refs/heads/main/apis.yml
apis:
- aid: aws-redshift:amazon-redshift-api
  name: Amazon Redshift API
  description: The Amazon Redshift API provides programmatic access to create and manage Amazon Redshift clusters and their associated resources.
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
    url: https://api.apis.guru/v2/specs/amazonaws.com/redshift/2012-12-01/openapi.json
- aid: aws-redshift:amazon-redshift-data-api
  name: Amazon Redshift Data API
  description: The Amazon Redshift Data API enables you to run SQL statements without managing connections via a secure HTTP endpoint.
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
    url: https://api.apis.guru/v2/specs/amazonaws.com/redshift-data/2019-12-20/openapi.json
- aid: aws-redshift:amazon-redshift-serverless-api
  name: Amazon Redshift Serverless API
  description: API for Amazon Redshift Serverless, which makes it easy to run analytics workloads without managing data warehouse infrastructure.
  humanURL: https://aws.amazon.com/redshift/redshift-serverless/
  baseURL: https://redshift-serverless.{region}.amazonaws.com
  tags:
  - Analytics
  - Auto-Scaling
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/Welcome.html
name: AWS Redshift
tags:
- Analytics
- Big Data
- Cloud Database
- Data Warehouse
- SQL
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to analyze all your data using standard SQL and existing Business Intelligence tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

