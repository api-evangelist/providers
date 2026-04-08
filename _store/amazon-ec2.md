---
aid: amazon-ec2
url: https://raw.githubusercontent.com/api-evangelist/amazon-ec2/refs/heads/main/apis.yml
apis:
- name: Amazon EC2 API
  description: Core API for managing Amazon EC2 instances, AMIs, key pairs, security groups, Elastic IPs, launch templates, spot instances, capacity reservations, and other compute resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/ec2/
  baseURL: https://ec2.amazonaws.com
  tags:
  - AWS
  - Cloud Computing
  - Compute
  - Instances
  - Virtual Machines
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: openapi/amazon-ec2-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ec2/2016-11-15/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-ec2-instance-schema.json
  - type: JSONLD
    url: json-ld/amazon-ec2-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/ec2/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/ec2/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: Best Practices
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html
  - type: FAQ
    url: https://aws.amazon.com/ec2/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/ec2/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/
  - type: API Reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
  - type: Security
    url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
name: Amazon EC2
tags:
- AWS
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, allowing you to launch virtual server instances, manage networking, and configure storage with complete control over your computing resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

