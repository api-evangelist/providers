---
aid: amazon-private-ca
url: https://raw.githubusercontent.com/api-evangelist/amazon-private-ca/refs/heads/main/apis.yml
apis:
- aid: amazon-private-ca:aws-private-ca-api
  name: AWS Private CA API
  description: The AWS Private CA API provides programmatic access to create and manage private certificate authorities, certificates, certificate revocation lists, permissions, policies, and tags for private PKI infrastructure.
  humanURL: https://aws.amazon.com/private-ca/
  baseURL: https://acm-pca.amazonaws.com
  tags:
  - Certificates
  - PKI
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/privateca/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/acm-pca/2017-08-22/openapi.yaml
  - type: Getting Started
    url: https://aws.amazon.com/private-ca/getting-started/
  - type: Pricing
    url: https://aws.amazon.com/private-ca/pricing/
  - type: FAQ
    url: https://aws.amazon.com/private-ca/faqs/
name: Amazon Private CA
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Private Certificate Authority (AWS Private CA) is a highly available, fully managed private CA service that helps you easily and securely manage the lifecycle of your private certificates. It allows you to create private CA hierarchies and issue X.509 certificates for your internal resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

