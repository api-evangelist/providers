---
aid: amazon-ecr
url: https://raw.githubusercontent.com/api-evangelist/amazon-ecr/refs/heads/main/apis.yml
apis:
- name: Amazon ECR API
  description: API for managing Amazon ECR repositories, images, and related resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/ecr/
  baseURL: https://api.ecr.amazonaws.com
  properties:
  - type: documentation
    url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/
  - type: openapi
    url: openapi/amazon-ecr-openapi.yml
  - type: openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecr/2015-09-21/openapi.yaml
  - type: json-schema
    url: json-schema/amazon-ecr-repository-schema.json
  - type: json-ld
    url: json-ld/amazon-ecr-context.jsonld
  - type: pricing
    url: https://aws.amazon.com/ecr/pricing/
  - type: getting-started
    url: https://aws.amazon.com/ecr/getting-started/
  - type: faq
    url: https://aws.amazon.com/ecr/faqs/
  - type: user-guide
    url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/
  - type: api-reference
    url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/
  - type: cli-reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ecr/
  - type: security
    url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/security.html
name: Amazon ECR
tags:
- Amazon Web Services
- AWS
- Container Images
- Container Registry
- Containers
- Docker
- ECR
- OCI
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Elastic Container Registry (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy container images and artifacts. ECR eliminates the need to operate your own container repositories or worry about scaling the underlying infrastructure, and integrates with Amazon ECS and Amazon EKS for simplified development to production workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

