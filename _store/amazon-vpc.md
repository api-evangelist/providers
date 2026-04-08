---
aid: amazon-vpc
url: https://raw.githubusercontent.com/api-evangelist/amazon-vpc/refs/heads/main/apis.yml
apis:
- name: Amazon VPC API
  description: Core API for managing Amazon Virtual Private Cloud resources including VPCs, subnets, internet gateways, NAT gateways, route tables, and network ACLs. VPC operations are part of the Amazon EC2 API.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/vpc/
  baseURL: https://ec2.amazonaws.com
  tags:
  - AWS
  - Networking
  - Private Cloud
  - Security
  - Subnets
  - VPC
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-vpc.html
  - type: OpenAPI
    url: openapi/amazon-vpc-openapi.yml
  - type: JSONSchema
    url: json-schema/amazon-vpc-schema.json
  - type: JSONLD
    url: json-ld/amazon-vpc-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/vpc/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/vpc/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/vpc/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/vpc/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
  - type: Security
    url: https://docs.aws.amazon.com/vpc/latest/userguide/security.html
name: Amazon VPC
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Virtual Private Cloud (VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define, with complete control over IP addressing, subnets, routing, and network gateways.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

