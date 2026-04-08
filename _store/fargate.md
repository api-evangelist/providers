---
aid: fargate
url: https://raw.githubusercontent.com/api-evangelist/fargate/refs/heads/main/apis.yml
apis:
- name: Amazon ECS API (Fargate)
  description: The Amazon ECS API provides programmatic access to manage Fargate tasks and services through Amazon Elastic Container Service. It supports creating and managing clusters, task definitions, services, and container instances using the Fargate launch type for serverless container execution.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  baseURL: https://ecs.{region}.amazonaws.com
  humanURL: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html
  - type: API Operations
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Operations.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html
  - type: Pricing
    url: https://aws.amazon.com/fargate/pricing/
  - type: Developer Guide
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Platform Versions
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-fargate.html
  - type: Change Log
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html
  - type: Service Quotas
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
  - type: Security
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-fargate.html
  - type: Monitoring
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-fargate-usage.html
  - type: Container Insights
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html
  - type: Troubleshooting
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
  - type: Best Practices
    url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
  - type: Windows Containers
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-considerations.html
  - type: ECS Exec
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html
  tags:
  - Containers
  - ECS
  - Fargate
  - Orchestration
  - Serverless
- name: Amazon EKS API (Fargate)
  description: The Amazon EKS API provides programmatic access to manage Fargate pods through Amazon Elastic Kubernetes Service. It supports creating Fargate profiles that define which Kubernetes pods run on Fargate infrastructure, enabling serverless Kubernetes workloads without managing nodes.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  baseURL: https://eks.{region}.amazonaws.com
  humanURL: https://docs.aws.amazon.com/eks/latest/APIReference/
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/eks/latest/userguide/fargate.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/eks/2017-11-01/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/eks/latest/APIReference/Welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html
  - type: Pricing
    url: https://aws.amazon.com/fargate/pricing/
  - type: Fargate Profiles
    url: https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html
  - type: Pod Configuration
    url: https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-configuration.html
  - type: Pod Execution Role
    url: https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/eks/create-fargate-profile.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  tags:
  - Containers
  - EKS
  - Fargate
  - Kubernetes
  - Serverless
name: AWS Fargate
tags:
- Compute
- Containers
- Docker
- Kubernetes
- Serverless
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS Fargate is a serverless, pay-as-you-go compute engine for containers that works with Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). It removes the need to provision and manage servers, letting you focus on building and running applications without managing infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

