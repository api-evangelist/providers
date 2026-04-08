---
aid: amazon-waf
url: https://raw.githubusercontent.com/api-evangelist/amazon-waf/refs/heads/main/apis.yml
apis:
- name: Amazon WAF REST API
  description: RESTful API for AWS WAF operations including web ACL management, rule groups, IP sets, regex pattern sets, and logging configurations for protecting web applications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/waf/
  baseURL: https://wafv2.amazonaws.com
  tags:
  - AWS
  - Security
  - WAF
  - Web Application Firewall
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/waf/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-waf-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/wafv2/2019-07-29/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-waf-web-acl-schema.json
  - type: JSONLD
    url: json-ld/amazon-waf-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/waf/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/waf/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/waf/latest/APIReference/CommonParameters.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: FAQ
    url: https://aws.amazon.com/waf/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/waf/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
  - type: API Reference
    url: https://docs.aws.amazon.com/waf/latest/APIReference/Welcome.html
  - type: Code Examples
    url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-examples.html
  - type: Security
    url: https://docs.aws.amazon.com/waf/latest/developerguide/security.html
name: Amazon WAF
tags:
- AWS
- Bot Management
- DDoS Protection
- Security
- WAF
- Web Application Firewall
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS WAF is a web application firewall that helps protect web applications and APIs from common web exploits and bots that may affect availability, compromise security, or consume excessive resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

