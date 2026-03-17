---
name: Amazon ECS
description: Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications.
url: https://aws.amazon.com/ecs/
created: '2024'
modified: '2026-03-16'
specificationVersion: '0.18'
apis:
- name: Amazon ECS API
  description: The Amazon ECS API provides programmatic access to manage containerized applications using Docker containers.
  image: https://aws.amazon.com/favicon.ico
  humanURL: https://aws.amazon.com/ecs/
  baseURL: https://ecs.amazonaws.com
  tags:
  - containers
  - orchestration
  - docker
  - microservices
  - cloud
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/ecs/
  - type: OpenAPI
    url: openapi/amazon-ecs-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.yaml
  - type: JSON Schema
    url: json-schema/amazon-ecs-task-definition-schema.json
  - type: JSON-LD Context
    url: json-ld/amazon-ecs-context.jsonld
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html
  - type: Pricing
    url: https://aws.amazon.com/ecs/pricing/
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
  - type: FAQ
    url: https://aws.amazon.com/ecs/faqs/
  - type: Best Practices
    url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
  - type: Service Health
    url: https://status.aws.amazon.com/
  - type: API Operations
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Operations.html
  - type: Developer Guide
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
  - type: Features
    url: https://aws.amazon.com/ecs/features/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html
  - type: Troubleshooting
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
  - type: Service Quotas
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
  - type: Monitoring
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html
  - type: CloudWatch
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html
  - type: Container Insights
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html
  - type: Document History
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
  - type: Partners
    url: https://aws.amazon.com/ecs/partners/
  - type: Resources
    url: https://aws.amazon.com/ecs/resources/
  - type: Blog
    url: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/
  - type: Knowledge Center
    url: https://repost.aws/knowledge-center/ecs-troubleshoot-failed-deployments
  - type: Compliance
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html
  - type: Endpoints and Quotas
    url: https://docs.aws.amazon.com/general/latest/gr/ecs-service.html
- name: Amazon ECS Service Connect API
  description: Amazon ECS Service Connect provides management of service-to-service communication as Amazon ECS configuration, building both service discovery and a service mesh for connecting services within and across clusters and VPCs.
  image: https://aws.amazon.com/favicon.ico
  humanURL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html
  baseURL: https://ecs.amazonaws.com
  tags:
  - containers
  - service-mesh
  - service-discovery
  - microservices
  - networking
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html
  - type: API Reference
    url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectConfiguration.html
  - type: Concepts
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts.html
  - type: Components
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts-deploy.html
  - type: CLI Configuration
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-connect.html
  - type: Blog
    url: https://aws.amazon.com/blogs/aws/new-amazon-ecs-service-connect-enabling-easy-communication-between-microservices/
  - type: GitHub
    url: https://github.com/aws/amazon-ecs-service-connect-agent
- name: Amazon ECS Anywhere API
  description: Amazon ECS Anywhere extends Amazon ECS to support registering external instances such as on-premises servers or virtual machines to your Amazon ECS cluster, allowing you to run and manage containerized workloads on your own infrastructure.
  image: https://aws.amazon.com/favicon.ico
  humanURL: https://aws.amazon.com/ecs/anywhere/
  baseURL: https://ecs.amazonaws.com
  tags:
  - containers
  - hybrid-cloud
  - on-premises
  - orchestration
  - edge
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html
  - type: Getting Started
    url: https://aws.amazon.com/ecs/anywhere/getting-started/
  - type: Launch Type
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-external.html
  - type: Troubleshooting
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-troubleshooting.html
  - type: FAQ
    url: https://aws.amazon.com/ecs/anywhere/faqs/
  - type: Tutorial
    url: https://github.com/aws-containers/ecs-anywhere-tutorial
- name: AWS Copilot CLI
  description: AWS Copilot is an open source command line interface that simplifies building, releasing, and operating production-ready containerized applications on Amazon ECS and AWS Fargate, providing common cloud architectures and workflows.
  image: https://aws.amazon.com/favicon.ico
  humanURL: https://aws.amazon.com/containers/copilot/
  baseURL: https://ecs.amazonaws.com
  tags:
  - containers
  - cli
  - devops
  - deployment
  - fargate
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html
  - type: Website
    url: https://aws.github.io/copilot-cli/
  - type: GitHub
    url: https://github.com/aws/copilot-cli
  - type: Getting Started
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-aws-copilot-cli.html
  - type: Installation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-install.html
  - type: Overview
    url: https://aws.github.io/copilot-cli/docs/overview/
common:
- type: Documentation
  url: https://docs.aws.amazon.com/ecs/
- type: Pricing
  url: https://aws.amazon.com/ecs/pricing/
- type: FAQ
  url: https://aws.amazon.com/ecs/faqs/
- type: Features
  url: https://aws.amazon.com/ecs/features/
- type: Getting Started
  url: https://aws.amazon.com/ecs/getting-started/
- type: Resources
  url: https://aws.amazon.com/ecs/resources/
- type: Partners
  url: https://aws.amazon.com/ecs/partners/
- type: Blog
  url: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/
- type: Service Health
  url: https://status.aws.amazon.com/
- type: SDKs
  url: https://aws.amazon.com/tools/
- type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
- type: Security
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html
- type: Compliance
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html
- type: Best Practices
  url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
- type: Service Quotas
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
- type: Monitoring
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html
- type: Troubleshooting
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
- type: Console
  url: https://console.aws.amazon.com/ecs/home
- type: Knowledge Center
  url: https://repost.aws/tags/TAd-wgX2x3QgSxyelEN6raFg/amazon-elastic-container-service
- type: Change Log
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
- type: Fargate
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
- type: Platform Versions
  url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html
- type: Agent Releases
  url: https://github.com/aws/amazon-ecs-agent/releases
maintainers:
- name: Kin Lane
  email: kin@apievangelist.com
  url: https://apievangelist.com
- name: Amazon Web Services
  email: support@aws.amazon.com
  url: https://aws.amazon.com
tags:
- aws
- amazon
- containers
- ecs
- docker
- orchestration
---