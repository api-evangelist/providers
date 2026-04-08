---
aid: aws-x-ray
url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/apis.yml
apis:
- aid: aws-x-ray:aws-x-ray
  name: AWS X-Ray
  description: AWS X-Ray is a service that helps developers analyze and debug distributed applications by providing end-to-end tracing of requests as they travel through the application, identifying performance bottlenecks and errors. It is now part of Amazon CloudWatch Application Signals for unified observability.
  humanURL: https://aws.amazon.com/xray/
  tags:
  - AWS
  - Debugging
  - Distributed Tracing
  - Microservices
  - Observability
  properties:
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/openapi/aws-x-ray-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/aws-x-ray/refs/heads/main/json-schema/aws-x-ray-trace-segment.yml
name: AWS X-Ray
tags:
- AWS
- Debugging
- Distributed Tracing
- Microservices
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS X-Ray is a service that helps developers analyze and debug distributed applications by providing end-to-end tracing of requests as they travel through the application, identifying performance bottlenecks and errors. It is now part of Amazon CloudWatch Application Signals for unified observability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

