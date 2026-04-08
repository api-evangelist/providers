---
aid: amazon-lambda
url: https://raw.githubusercontent.com/api-evangelist/amazon-lambda/refs/heads/main/apis.yml
apis:
- name: Amazon Lambda API
  description: Core API for managing AWS Lambda functions, event source mappings, layers, aliases, versions, and permissions. Enables creating and invoking serverless functions, configuring triggers from AWS services, and managing function deployment packages and runtime configurations.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/lambda/
  baseURL: https://lambda.amazonaws.com
  tags:
  - AWS
  - Compute
  - Event-Driven
  - Functions
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
  - type: OpenAPI
    url: openapi/amazon-lambda-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-lambda-function-schema.json
  - type: JSONLD
    url: json-ld/amazon-lambda-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/lambda/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/lambda/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-auth-and-access-control.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: Best Practices
    url: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
  - type: FAQ
    url: https://aws.amazon.com/lambda/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/lambda/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/lambda/latest/dg/
  - type: API Reference
    url: https://docs.aws.amazon.com/lambda/latest/api/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/lambda/
  - type: Security
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
name: Amazon Lambda
tags:
- AWS
- Compute
- Event-Driven
- FaaS
- Functions
- Serverless
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, automatically scaling and executing your code in response to events from over 200 AWS services and SaaS applications while you pay only for the compute time you consume.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

