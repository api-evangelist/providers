---
aid: amazon-privatelink
url: https://raw.githubusercontent.com/api-evangelist/amazon-privatelink/refs/heads/main/apis.yml
apis:
- aid: amazon-privatelink:aws-privatelink-api
  name: AWS PrivateLink API
  description: The AWS PrivateLink API (part of Amazon VPC) provides programmatic access to create and manage VPC endpoint services, VPC endpoints, and endpoint connections for private AWS service connectivity.
  humanURL: https://aws.amazon.com/privatelink/
  baseURL: https://ec2.amazonaws.com
  tags:
  - Networking
  - Private Connectivity
  - VPC
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
  - type: Getting Started
    url: https://aws.amazon.com/privatelink/getting-started/
  - type: Pricing
    url: https://aws.amazon.com/privatelink/pricing/
  - type: FAQ
    url: https://aws.amazon.com/privatelink/faqs/
name: Amazon PrivateLink
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), AWS services, and your on-premises networks without exposing your traffic to the public internet. It makes it easy to connect services across different accounts and VPCs to simplify your network architecture.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

