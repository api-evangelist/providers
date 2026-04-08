---
aid: amazon-verified-access
url: https://raw.githubusercontent.com/api-evangelist/amazon-verified-access/refs/heads/main/apis.yml
apis:
- aid: amazon-verified-access:amazon-verified-access-api
  name: AWS Verified Access API
  description: The AWS Verified Access API provides programmatic access to create and manage Verified Access instances, groups, endpoints, and trust providers. It enables configuring zero-trust network access policies that evaluate user identity and device security posture for each application request.
  humanURL: https://aws.amazon.com/verified-access/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Access Management
  - AWS
  - Security
  - Zero Trust
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/verified-access/latest/ug/
  - type: Reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-verified-access.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/verified-access/latest/ug/getting-started.html
  - type: Pricing
    url: https://aws.amazon.com/verified-access/pricing/
  - type: FAQ
    url: https://aws.amazon.com/verified-access/faqs/
name: Amazon Verified Access
tags:
- Access Management
- AWS
- Security
- Zero Trust
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Verified Access provides secure access to corporate applications without requiring a VPN. It evaluates each application request in real time using security signals like identity, device posture, and contextual data to grant granular access only to users who meet the specified requirements.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

