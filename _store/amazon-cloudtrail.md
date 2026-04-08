---
aid: amazon-cloudtrail
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudtrail/refs/heads/main/apis.yml
apis:
- name: Amazon CloudTrail API
  description: API for recording and monitoring AWS API calls made on your account. CloudTrail provides event history of API activity, enabling security analysis, resource change tracking, and compliance auditing. Supports creating and managing trails, looking up events, querying event data stores, and configuring insights.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudtrail/
  baseURL: https://cloudtrail.amazonaws.com
  tags:
  - Audit
  - AWS
  - Compliance
  - Governance
  - Logging
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-cloudtrail-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/cloudtrail/2013-11-01/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-cloudtrail-event-schema.json
  - type: JSONLD
    url: json-ld/amazon-cloudtrail-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/cloudtrail/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/cloudtrail/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/cloudtrail/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/
  - type: Security
    url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security.html
name: Amazon CloudTrail
tags:
- Audit
- AWS
- Compliance
- Governance
- Logging
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account by recording API calls and delivering log files containing API activity for your account.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

