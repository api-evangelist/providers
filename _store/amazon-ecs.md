---
name: Amazon ECS
description: Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that makes it easy to deploy, manage, and scale containerized applications.
url: https://aws.amazon.com/ecs/
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
apis:
  - name: Amazon ECS API
    description: The Amazon ECS API provides programmatic access to manage containerized applications using Docker containers.
    image: https://aws.amazon.com/favicon.ico
    humanURL: https://aws.amazon.com/ecs/
    baseURL: https://ecs.amazonaws.com
    tags:
      - Cloud
      - Containers
      - Docker
      - Microservices
      - Orchestration
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ecs/
      - type: OpenAPI
        url: openapi/amazon-ecs-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/ecs/2014-11-13/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-ecs-task-definition-schema.json
      - type: JSONLD
        url: json-ld/amazon-ecs-context.jsonld
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/ecs/pricing/
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
      - type: FAQ
        url: https://aws.amazon.com/ecs/faqs/
      - type: BestPractices
        url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Operations.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
      - type: Features
        url: https://aws.amazon.com/ecs/features/
      - type: Security
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html
      - type: Troubleshooting
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html
      - type: ChangeLog
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
      - type: Partners
        url: https://aws.amazon.com/ecs/partners/
      - type: Resources
        url: https://aws.amazon.com/ecs/resources/
      - type: Blog
        url: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/
      - type: KnowledgeCenter
        url: https://repost.aws/knowledge-center/ecs-troubleshoot-failed-deployments
      - type: Compliance
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html
      - type: Documentation
        url: https://docs.aws.amazon.com/general/latest/gr/ecs-service.html
  - name: Amazon ECS Service Connect API
    description: Amazon ECS Service Connect provides management of service-to-service communication as Amazon ECS configuration, building both service discovery and a service mesh for connecting services within and across clusters and VPCs.
    image: https://aws.amazon.com/favicon.ico
    humanURL: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html
    baseURL: https://ecs.amazonaws.com
    tags:
      - Containers
      - Microservices
      - Networking
      - Service-Discovery
      - Service-Mesh
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectConfiguration.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts-deploy.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-connect.html
      - type: Blog
        url: https://aws.amazon.com/blogs/aws/new-amazon-ecs-service-connect-enabling-easy-communication-between-microservices/
      - type: GitHubRepository
        url: https://github.com/aws/amazon-ecs-service-connect-agent
  - name: Amazon ECS Anywhere API
    description: Amazon ECS Anywhere extends Amazon ECS to support registering external instances such as on-premises servers or virtual machines to your Amazon ECS cluster, allowing you to run and manage containerized workloads on your own infrastructure.
    image: https://aws.amazon.com/favicon.ico
    humanURL: https://aws.amazon.com/ecs/anywhere/
    baseURL: https://ecs.amazonaws.com
    tags:
      - Containers
      - Edge
      - Hybrid-Cloud
      - On-Premises
      - Orchestration
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html
      - type: GettingStarted
        url: https://aws.amazon.com/ecs/anywhere/getting-started/
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-external.html
      - type: Troubleshooting
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-troubleshooting.html
      - type: FAQ
        url: https://aws.amazon.com/ecs/anywhere/faqs/
      - type: Tutorials
        url: https://github.com/aws-containers/ecs-anywhere-tutorial
  - name: AWS Copilot CLI
    description: AWS Copilot is an open source command line interface that simplifies building, releasing, and operating production-ready containerized applications on Amazon ECS and AWS Fargate, providing common cloud architectures and workflows.
    image: https://aws.amazon.com/favicon.ico
    humanURL: https://aws.amazon.com/containers/copilot/
    baseURL: https://ecs.amazonaws.com
    tags:
      - Cli
      - Containers
      - Deployment
      - Devops
      - Fargate
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html
      - type: Documentation
        url: https://aws.github.io/copilot-cli/
      - type: GitHubRepository
        url: https://github.com/aws/copilot-cli
      - type: GettingStarted
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-aws-copilot-cli.html
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-install.html
      - type: Documentation
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
  - type: GettingStarted
    url: https://aws.amazon.com/ecs/getting-started/
  - type: Resources
    url: https://aws.amazon.com/ecs/resources/
  - type: Partners
    url: https://aws.amazon.com/ecs/partners/
  - type: Blog
    url: https://aws.amazon.com/blogs/aws/category/compute/amazon-elastic-container-service/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: SDK
    url: https://aws.amazon.com/tools/
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/ecs/
  - type: Security
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html
  - type: Compliance
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html
  - type: BestPractices
    url: https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html
  - type: Troubleshooting
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html
  - type: Console
    url: https://console.aws.amazon.com/ecs/home
  - type: KnowledgeCenter
    url: https://repost.aws/tags/TAd-wgX2x3QgSxyelEN6raFg/amazon-elastic-container-service
  - type: ChangeLog
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html
  - type: GitHubRepository
    url: https://github.com/aws/amazon-ecs-agent/releases
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Features
    data:
      - name: Fully Managed Container Orchestration
        description: Run and manage Docker containers at scale without managing the underlying infrastructure or control plane.
      - name: AWS Fargate Integration
        description: Run containers serverlessly without provisioning or managing EC2 instances using AWS Fargate launch type.
      - name: Service Auto Scaling
        description: Automatically scale container workloads based on CloudWatch metrics, target tracking, or step scaling policies.
      - name: Service Connect
        description: Built-in service discovery and service mesh for connecting containerized services within and across clusters.
      - name: ECS Anywhere
        description: Extend ECS to on-premises and edge infrastructure to run containers on your own servers and virtual machines.
      - name: Capacity Providers
        description: Manage compute capacity with capacity provider strategies for optimal resource allocation across EC2 and Fargate.
      - name: Task Definitions
        description: Define containerized applications as task definitions with CPU, memory, networking, and IAM role configurations.
      - name: Container Insights
        description: Monitor container performance metrics and logs with CloudWatch Container Insights for operational visibility.
  - type: UseCases
    data:
      - name: Microservices Architecture
        description: Deploy and manage microservices with independent scaling, deployment, and lifecycle management per service.
      - name: Batch Processing
        description: Run batch computing workloads using ECS tasks with automatic scaling and job scheduling.
      - name: CI/CD Pipeline Deployment
        description: Integrate with AWS CodePipeline and CodeDeploy for automated blue/green and rolling deployments of containerized applications.
      - name: Hybrid Cloud Workloads
        description: Run containerized workloads across AWS cloud and on-premises environments using ECS Anywhere.
      - name: Machine Learning Inference
        description: Deploy ML models as containerized inference endpoints with auto-scaling based on demand.
  - type: Integrations
    data:
      - name: AWS Fargate
        description: Serverless compute engine for running containers without managing underlying EC2 instances.
      - name: Amazon ECR
        description: Private container registry for storing, managing, and deploying Docker container images.
      - name: AWS CloudFormation
        description: Infrastructure as code for provisioning and managing ECS clusters, services, and task definitions.
      - name: Elastic Load Balancing
        description: Distribute traffic across containers with Application Load Balancer and Network Load Balancer integration.
      - name: Amazon CloudWatch
        description: Monitor container metrics, logs, and alarms with CloudWatch and Container Insights.
      - name: AWS IAM
        description: Fine-grained access control for ECS tasks and services using IAM roles and policies.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
  - name: Amazon Web Services
    email: support@aws.amazon.com
    url: https://aws.amazon.com
tags:
  - Amazon
  - Aws
  - Containers
  - Docker
  - Ecs
  - Orchestration
---
