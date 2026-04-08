---
aid: amazon-fargate
url: https://raw.githubusercontent.com/api-evangelist/amazon-fargate/refs/heads/main/apis.yml
apis:
- name: Amazon Fargate API
  description: The Amazon Fargate API is accessed through Amazon ECS and enables you to run containers without managing servers or clusters. You can define tasks, configure networking and IAM policies, and deploy containerized applications with serverless compute capacity.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/fargate/
  baseURL: https://ecs.amazonaws.com
  tags:
  - Compute
  - Containers
  - Microservices
  - Serverless
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
  - type: OpenAPI
    url: openapi/amazon-fargate-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.json
  - type: JSON Schema
    url: json-schema/amazon-fargate-schema.json
  - type: JSON-LD
    url: json-ld/amazon-fargate-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/fargate/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/fargate/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/fargate/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/security.html
name: Amazon Fargate
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate removes the need to provision and manage servers, letting you specify and pay for resources per application, and improves security through application isolation by design.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

