---
aid: amazon-transit-gateway
url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/apis.yml
apis:
- name: Amazon Transit Gateway REST API
  description: RESTful API for Amazon Transit Gateway operations including creating and managing transit gateways, VPC attachments, route tables, peering connections, and multicast domains.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/transit-gateway/
  baseURL: https://ec2.amazonaws.com
  tags:
  - AWS
  - Networking
  - Transit Gateway
  - VPC
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-tgw.html
  - type: OpenAPI
    url: openapi/amazon-transit-gateway-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-transit-gateway-schema.json
  - type: JSONLD
    url: json-ld/amazon-transit-gateway-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/transit-gateway/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/transit-gateway/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: FAQ
    url: https://aws.amazon.com/transit-gateway/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/ec2/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html
  - type: API Reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-tgw.html
  - type: Code Examples
    url: https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html
  - type: Security
    url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-security.html
name: Amazon Transit Gateway
tags:
- AWS
- Cloud Networking
- Network Hub
- Networking
- Transit Gateway
- VPC
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Transit Gateway connects VPCs and on-premises networks through a central hub, simplifying network architecture and reducing operational complexity for large-scale cloud deployments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

