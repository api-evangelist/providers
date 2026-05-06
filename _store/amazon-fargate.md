---
name: Amazon Fargate
description: Amazon Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. Fargate removes the need to provision and manage servers, letting you specify and pay for resources per application, and improves security through application isolation by design.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/fargate/
type: Index
created: '2024-01-15'
modified: '2026-04-19'
tags:
  - AWS
  - Compute
  - Containers
  - ECS
  - EKS
  - Microservices
  - Serverless
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
      - type: JSONSchema
        url: json-schema/amazon-fargate-cluster-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fargate-task-definition-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fargate-task-schema.json
      - type: JSONSchema
        url: json-schema/amazon-fargate-service-schema.json
      - type: JSONStructure
        url: json-structure/amazon-fargate-cluster-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fargate-task-definition-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fargate-task-structure.json
      - type: JSONStructure
        url: json-structure/amazon-fargate-service-structure.json
      - type: Example
        url: examples/amazon-fargate-cluster-example.json
      - type: Example
        url: examples/amazon-fargate-task-definition-example.json
      - type: Example
        url: examples/amazon-fargate-task-example.json
      - type: Example
        url: examples/amazon-fargate-service-example.json
      - type: Pricing
        url: https://aws.amazon.com/fargate/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/fargate/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/fargate/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html
common:
  - type: Portal
    url: https://console.aws.amazon.com/
  - type: Website
    url: https://aws.amazon.com/fargate/
  - type: Documentation
    url: https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/containers/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/ecs
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/aws-fargate
  - type: SpectralRules
    url: rules/amazon-fargate-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/fargate.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-fargate-container-orchestration.yaml
  - type: Vocabulary
    url: vocabulary/amazon-fargate-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-fargate-context.jsonld
  - type: Features
    data:
      - name: Serverless Compute
        description: Run containers without provisioning or managing servers. Fargate handles capacity, OS updates, and scaling automatically.
      - name: ECS and EKS Integration
        description: Works seamlessly with both Amazon ECS task definitions and Amazon EKS pods.
      - name: Workload Isolation
        description: Each task runs in its own dedicated single-tenant compute environment for improved security.
      - name: VPC Networking
        description: Tasks receive ENIs with full VPC networking support including security groups and VPC Flow Logs.
      - name: Auto Scaling
        description: Supports Application Auto Scaling with target tracking, step scaling, and scheduled scaling.
      - name: Persistent Storage
        description: Integration with Amazon EFS for stateful workloads requiring persistent storage.
      - name: Compliance Support
        description: HIPAA, PCI, FedRAMP, and GovCloud (US) region support for regulated workloads.
      - name: CloudWatch Integration
        description: Built-in Container Insights for metrics, logs, and observability.
      - name: ARM64/Graviton Support
        description: Run workloads on AWS Graviton processors for improved price-performance.
      - name: Spot Instances
        description: Run fault-tolerant workloads on Fargate Spot for significant cost savings.
  - type: UseCases
    data:
      - name: Web Applications and APIs
        description: Deploy microservices-based web applications and REST APIs without infrastructure management.
      - name: Batch Data Processing
        description: Run parallel data processing jobs and ETL workloads using AWS Batch with Fargate.
      - name: Application Modernization
        description: Lift-and-shift containerized workloads to serverless infrastructure for reduced operational burden.
      - name: AI/ML Workloads
        description: Run training, inference, and data preparation containers in flexible serverless environments.
      - name: CI/CD Pipelines
        description: Execute build, test, and deployment pipelines as ephemeral Fargate tasks.
      - name: Scheduled Jobs
        description: Run time-based container workloads using Amazon EventBridge and Fargate tasks.
  - type: Integrations
    data:
      - name: Amazon ECS
        description: Primary orchestration engine for running Fargate tasks and services.
      - name: Amazon EKS
        description: Run Kubernetes pods serverlessly using Fargate profiles.
      - name: AWS IAM
        description: Fine-grained task-level IAM roles for container security and least privilege.
      - name: Amazon CloudWatch
        description: Container Insights, metrics, logs, and alarms for Fargate workloads.
      - name: AWS Application Auto Scaling
        description: Automatically scale Fargate services based on CloudWatch metrics.
      - name: Amazon EFS
        description: Persistent shared file storage for stateful Fargate workloads.
      - name: AWS Batch
        description: Run high-scale batch workloads using Fargate compute environments.
      - name: Application Load Balancer
        description: Route HTTP/HTTPS traffic to Fargate services using ALB target groups.
      - name: AWS Secrets Manager
        description: Inject secrets and configuration into Fargate task containers securely.
      - name: Amazon ECR
        description: Store and deploy container images from Amazon Elastic Container Registry.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
