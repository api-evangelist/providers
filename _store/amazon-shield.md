---
aid: amazon-shield
url: https://raw.githubusercontent.com/api-evangelist/amazon-shield/refs/heads/main/apis.yml
apis:
- name: AWS Shield API
  description: The AWS Shield API provides programmatic access to manage DDoS protection for your AWS resources. It enables developers to create and manage protections, subscribe to Shield Advanced, configure emergency contacts, view attack details and statistics, and manage protection groups for coordinated defense across multiple resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/shield/
  baseURL: https://shield.amazonaws.com
  tags:
  - AWS
  - DDoS Protection
  - Networking
  - Security
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
  - type: OpenAPI
    url: openapi/amazon-shield-openapi.yml
  - type: Pricing
    url: https://aws.amazon.com/shield/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/shield/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/shield/faqs/
name: Amazon Shield
tags:
- AWS
- DDoS Protection
- Networking
- Security
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. It provides always-on detection and automatic inline mitigations that minimize application downtime and latency, with two tiers of protection - Shield Standard for automatic defense against common attacks and Shield Advanced for enhanced detection and 24/7 access to the DDoS Response Team.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

