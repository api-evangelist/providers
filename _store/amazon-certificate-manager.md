---
aid: amazon-certificate-manager
url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/apis.yml
apis:
- name: Amazon Certificate Manager API
  description: API for provisioning, managing, and deploying public and private SSL/TLS certificates for use with AWS services and your internal connected resources. Supports requesting certificates, describing certificate details, listing certificates, importing third-party certificates, and managing certificate tags.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/certificate-manager/
  baseURL: https://acm.amazonaws.com
  tags:
  - AWS
  - Certificates
  - Encryption
  - Security
  - SSL
  - TLS
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/acm/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-certificate-manager-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/acm/2015-12-08/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-certificate-manager-certificate-schema.json
  - type: JSONLD
    url: json-ld/amazon-certificate-manager-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/certificate-manager/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/certificate-manager/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/certificate-manager/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/acm/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/acm/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/acm/
  - type: Security
    url: https://docs.aws.amazon.com/acm/latest/userguide/security.html
name: Amazon Certificate Manager
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications, enabling you to manage certificate lifecycles centrally.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

