---
aid: amazon-codedeploy
url: https://raw.githubusercontent.com/api-evangelist/amazon-codedeploy/refs/heads/main/apis.yml
apis:
- name: Amazon CodeDeploy API
  description: API for automating code deployments to any instance, including Amazon EC2 instances, on-premises servers, Lambda functions, and ECS services. Supports creating applications and deployment groups, managing deployment configurations, triggering deployments, and monitoring deployment status with automatic rollback capabilities.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/codedeploy/
  baseURL: https://codedeploy.amazonaws.com
  tags:
  - Automation
  - AWS
  - CI/CD
  - Deployment
  - DevOps
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-codedeploy-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/codedeploy/2014-10-06/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-codedeploy-deployment-schema.json
  - type: JSONLD
    url: json-ld/amazon-codedeploy-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/codedeploy/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/codedeploy/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/codedeploy/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/codedeploy/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/deploy/
  - type: Security
    url: https://docs.aws.amazon.com/codedeploy/latest/userguide/security.html
name: Amazon CodeDeploy
tags:
- Automation
- AWS
- CI/CD
- Deployment
- DevOps
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and on-premises servers.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

