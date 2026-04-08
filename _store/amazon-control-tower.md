---
aid: amazon-control-tower
url: https://raw.githubusercontent.com/api-evangelist/amazon-control-tower/refs/heads/main/apis.yml
apis:
- aid: amazon-control-tower:aws-control-tower-api
  name: AWS Control Tower API
  description: The AWS Control Tower API provides programmatic access to manage landing zones, organizational units, accounts, and controls (guardrails) within your AWS environment, enabling automated governance at scale.
  humanURL: https://aws.amazon.com/controltower/
  baseURL: https://controltower.amazonaws.com
  tags:
  - Governance
  - Landing Zone
  - Multi-Account
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/controltower/2018-11-28/openapi.yaml
  - type: Getting Started
    url: https://aws.amazon.com/controltower/getting-started/
  - type: Pricing
    url: https://aws.amazon.com/controltower/pricing/
  - type: FAQ
    url: https://aws.amazon.com/controltower/faqs/
name: Amazon Control Tower
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Control Tower provides the easiest way to set up and govern a secure, multi-account AWS environment based on best practices. It establishes a landing zone with pre-configured governance and guardrails, enabling organizations to maintain compliance and manage accounts at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

