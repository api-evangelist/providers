---
aid: amazon-guardduty
url: https://raw.githubusercontent.com/api-evangelist/amazon-guardduty/refs/heads/main/apis.yml
apis:
- name: Amazon GuardDuty API
  description: The Amazon GuardDuty API enables programmatic access to manage threat detection across your AWS accounts. You can create and manage detectors, configure threat intelligence feeds, manage findings, set up member accounts, and create IP sets and threat intelligence lists.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/guardduty/
  baseURL: https://guardduty.amazonaws.com
  tags:
  - Findings
  - Monitoring
  - Security
  - Threat Detection
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html
  - type: OpenAPI
    url: openapi/amazon-guardduty-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/guardduty/2017-11-28/openapi.json
  - type: JSON Schema
    url: json-schema/amazon-guardduty-schema.json
  - type: JSON-LD
    url: json-ld/amazon-guardduty-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/guardduty/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/guardduty/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/guardduty/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html
  - type: API Reference
    url: https://docs.aws.amazon.com/guardduty/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/guardduty/
  - type: Security
    url: https://docs.aws.amazon.com/guardduty/latest/ug/security.html
name: Amazon GuardDuty
tags:
- Anomaly Detection
- AWS
- Compliance
- Machine Learning
- Monitoring
- Security
- Threat Detection
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon GuardDuty is an intelligent threat detection service that continuously monitors your AWS accounts, workloads, and data for malicious activity. It uses machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats to your AWS environment.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

