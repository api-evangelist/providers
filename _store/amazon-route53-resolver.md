---
aid: amazon-route53-resolver
url: https://raw.githubusercontent.com/api-evangelist/amazon-route53-resolver/refs/heads/main/apis.yml
apis:
- name: Amazon Route 53 Resolver API
  description: The Amazon Route 53 Resolver API provides programmatic access to manage DNS resolution across hybrid cloud environments. It enables developers to create and manage resolver endpoints, configure forwarding rules, associate VPCs with resolver rules, and manage DNS firewall rule groups for filtering DNS queries.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/route53/
  baseURL: https://route53resolver.amazonaws.com
  tags:
  - AWS
  - DNS
  - Hybrid Cloud
  - Networking
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html
  - type: OpenAPI
    url: openapi/amazon-route53-resolver-openapi.yml
  - type: Pricing
    url: https://aws.amazon.com/route53/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/route53/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/route53/faqs/
name: Amazon Route 53 Resolver
tags:
- AWS
- DNS
- Hybrid Cloud
- Networking
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Route 53 Resolver provides DNS resolution for hybrid cloud environments, enabling DNS queries between your VPCs and on-premises networks. It allows you to configure DNS forwarding rules, manage resolver endpoints, and set up conditional forwarding to resolve domain names across your hybrid infrastructure seamlessly.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

