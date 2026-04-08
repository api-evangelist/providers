---
aid: amazon-step-functions
url: https://raw.githubusercontent.com/api-evangelist/amazon-step-functions/refs/heads/main/apis.yml
apis:
- name: Amazon Step Functions API
  description: Core API for creating and managing state machines and executions in AWS Step Functions, enabling serverless workflow orchestration for coordinating distributed applications and microservices.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/step-functions/
  baseURL: https://states.amazonaws.com
  tags:
  - AWS
  - Orchestration
  - Serverless
  - State Machine
  - Workflow
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/step-functions/latest/apireference/
  - type: OpenAPI
    url: openapi/amazon-step-functions-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/states/2016-11-23/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-step-functions-state-machine-schema.json
  - type: JSONLD
    url: json-ld/amazon-step-functions-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/step-functions/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/step-functions/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/step-functions/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/step-functions/latest/dg/
  - type: API Reference
    url: https://docs.aws.amazon.com/step-functions/latest/apireference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/
  - type: Security
    url: https://docs.aws.amazon.com/step-functions/latest/dg/security.html
name: Amazon Step Functions
tags:
- AWS
- Orchestration
- Serverless
- State Machine
- Workflow
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Step Functions is a serverless workflow orchestration service that lets you coordinate distributed applications and microservices using visual workflows, enabling you to build and update state machines that react to events, manage retries, and orchestrate complex business processes.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

