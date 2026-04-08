---
aid: amazon-global-accelerator
url: https://raw.githubusercontent.com/api-evangelist/amazon-global-accelerator/refs/heads/main/apis.yml
apis:
- name: Amazon Global Accelerator API
  description: The Amazon Global Accelerator API enables programmatic access to create and manage accelerators, listeners, and endpoint groups. You can configure traffic routing, health checks, and client IP address preservation to optimize application performance across AWS Regions.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/global-accelerator/
  baseURL: https://globalaccelerator.amazonaws.com
  tags:
  - Global
  - Networking
  - Performance
  - Traffic Management
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html
  - type: OpenAPI
    url: openapi/amazon-global-accelerator-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/globalaccelerator/2018-08-08/openapi.json
  - type: JSON Schema
    url: json-schema/amazon-global-accelerator-schema.json
  - type: JSON-LD
    url: json-ld/amazon-global-accelerator-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/global-accelerator/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/global-accelerator/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/global-accelerator/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html
  - type: API Reference
    url: https://docs.aws.amazon.com/global-accelerator/latest/api/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/
  - type: Security
    url: https://docs.aws.amazon.com/global-accelerator/latest/dg/security.html
name: Amazon Global Accelerator
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Global Accelerator is a networking service that improves the performance and availability of applications with local or global users. It provides static IP addresses that act as a fixed entry point to your applications and uses the AWS global network to optimize the path from users to applications, improving performance by up to 60%.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

