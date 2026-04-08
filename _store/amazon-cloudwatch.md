---
aid: amazon-cloudwatch
url: https://raw.githubusercontent.com/api-evangelist/amazon-cloudwatch/refs/heads/main/apis.yml
apis:
- name: Amazon CloudWatch API
  description: Core API for monitoring AWS resources and applications in real time, collecting and tracking metrics, creating alarms, managing dashboards, and automatically reacting to changes in your AWS environment.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/cloudwatch/
  baseURL: https://monitoring.amazonaws.com
  tags:
  - Alarms
  - AWS
  - Logs
  - Metrics
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-cloudwatch-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/monitoring/2010-08-01/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-cloudwatch-alarm-schema.json
  - type: JSONLD
    url: json-ld/amazon-cloudwatch-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/cloudwatch/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/cloudwatch/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/cloudwatch/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/security.html
name: Amazon CloudWatch
tags:
- Alarms
- AWS
- Logs
- Metrics
- Monitoring
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights to monitor applications, respond to system-wide performance changes, and optimize resource utilization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

