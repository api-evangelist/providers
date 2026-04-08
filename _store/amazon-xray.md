---
aid: amazon-xray
url: https://raw.githubusercontent.com/api-evangelist/amazon-xray/refs/heads/main/apis.yml
apis:
- name: Amazon X-Ray REST API
  description: RESTful API for AWS X-Ray distributed tracing operations including trace management, service maps, sampling rules, groups, and insights for application performance analysis.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/xray/
  baseURL: https://xray.amazonaws.com
  tags:
  - AWS
  - Distributed Tracing
  - Observability
  - Tracing
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/xray/latest/api/
  - type: OpenAPI
    url: openapi/amazon-xray-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/xray/2016-04-12/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-xray-trace-schema.json
  - type: JSONLD
    url: json-ld/amazon-xray-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/xray/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/xray/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/xray/latest/api/CommonParameters.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: FAQ
    url: https://aws.amazon.com/xray/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/xray/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html
  - type: API Reference
    url: https://docs.aws.amazon.com/xray/latest/api/Welcome.html
  - type: Code Examples
    url: https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-sample.html
  - type: Security
    url: https://docs.aws.amazon.com/xray/latest/devguide/security.html
name: Amazon X-Ray
tags:
- Application Performance
- AWS
- Debugging
- Distributed Tracing
- Monitoring
- Observability
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS X-Ray is a distributed tracing service that helps developers analyze and debug production applications, providing end-to-end visibility into requests as they travel through the application.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

