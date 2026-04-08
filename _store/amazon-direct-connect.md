---
aid: amazon-direct-connect
url: https://raw.githubusercontent.com/api-evangelist/amazon-direct-connect/refs/heads/main/apis.yml
apis:
- name: Amazon Direct Connect API
  description: The AWS Direct Connect API provides programmatic access to create and manage dedicated network connections between your on-premises network and AWS, including connections, virtual interfaces, gateways, and link aggregation groups.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/directconnect/
  baseURL: https://directconnect.amazonaws.com
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/directconnect/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-direct-connect-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/directconnect/2012-10-25/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-direct-connect-connection-schema.json
  - type: JSONLD
    url: json-ld/amazon-direct-connect-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/directconnect/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/directconnect/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/directconnect/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/
  - type: API Reference
    url: https://docs.aws.amazon.com/directconnect/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/directconnect/
  - type: Security
    url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/security.html
name: Amazon Direct Connect
tags:
- AWS
- Dedicated Connection
- Direct Connect
- Hybrid Cloud
- Networking
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect location provides access to AWS in the region with which it is associated, providing reduced network costs, increased bandwidth throughput, and a more consistent network experience.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

