---
aid: aws-app-runner
name: AWS App Runner
description: AWS App Runner is a fully managed service that makes it easy to build, deploy, and run containerized web applications and APIs at scale. It automatically builds and deploys applications from container images or source code, load balances traffic with encryption, and scales to meet traffic needs without requiring infrastructure management. App Runner integrates with ECR, GitHub, Bitbucket, VPC, IAM, and CloudWatch for complete application delivery.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - CI/CD
  - Containers
  - Deployment
  - Microservices
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/aws-app-runner/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-app-runner:aws-app-runner
    name: AWS App Runner
    description: AWS App Runner is a fully managed service that makes it easy to build, deploy, and run containerized web applications and APIs at scale. It automatically builds and deploys applications, load balances traffic with encryption, and scales to meet traffic needs without requiring infrastructure management.
    humanURL: https://aws.amazon.com/apprunner/
    baseURL: https://apprunner.{region}.amazonaws.com
    tags:
      - AWS
      - Containers
      - Deployment
      - Microservices
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/apprunner/latest/dg/getting-started.html
      - type: APIReference
        url: https://docs.aws.amazon.com/apprunner/latest/api/Welcome.html
      - type: Authentication
        url: https://docs.aws.amazon.com/apprunner/latest/dg/security-iam.html
      - type: OpenAPI
        url: openapi/aws-app-runner-openapi.yml
common:
  - type: Website
    url: https://aws.amazon.com/apprunner/
  - type: Documentation
    url: https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html
  - type: Features
    url: https://aws.amazon.com/apprunner/features/
  - type: Pricing
    url: https://aws.amazon.com/apprunner/pricing/
  - type: FAQ
    url: https://aws.amazon.com/apprunner/faqs/
  - type: Customers
    url: https://aws.amazon.com/apprunner/customers/
  - type: Console
    url: https://console.aws.amazon.com/apprunner/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/containers/category/compute/aws-app-runner/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: SpectralRules
    url: rules/aws-app-runner-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-app-runner-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/app-deployment-workflow.yaml
  - type: Features
    data:
      - name: Automatic Build and Deploy
        description: Automatically builds container images from source code and deploys with zero configuration.
      - name: Auto-Scaling
        description: Scales automatically based on incoming request volume, with configurable min/max instances.
      - name: Load Balancing
        description: Built-in load balancing with HTTPS encryption for all traffic to deployed services.
      - name: Custom Domains
        description: Associate custom domain names with SSL/TLS certificates for branded endpoints.
      - name: VPC Integration
        description: Connect to private VPC resources like RDS, ElastiCache, and internal services.
      - name: Pause and Resume
        description: Pause services to stop billing during idle periods and resume instantly when needed.
      - name: Observability
        description: Integration with CloudWatch and X-Ray for metrics, logs, and distributed tracing.
      - name: GitHub and ECR Integration
        description: Deploy directly from GitHub repositories or Amazon ECR container registries.
  - type: UseCases
    data:
      - name: Web Application Deployment
        description: Deploy containerized web applications without managing servers, load balancers, or scaling.
      - name: API Backend Deployment
        description: Host REST or GraphQL API backends with automatic scaling and HTTPS termination.
      - name: Microservices Hosting
        description: Deploy individual microservices with isolated scaling and custom domain routing.
      - name: Development and Staging Environments
        description: Quickly spin up and tear down environments using pause/resume to minimize costs.
  - type: Integrations
    data:
      - name: Amazon ECR
        description: Pull container images from Amazon Elastic Container Registry for deployment.
      - name: GitHub
        description: Connect GitHub repositories for automatic builds and continuous deployment.
      - name: AWS IAM
        description: Control access to App Runner APIs and service resources using IAM policies.
      - name: Amazon CloudWatch
        description: Monitor service metrics, CPU usage, request counts, and response latency.
      - name: AWS X-Ray
        description: Enable distributed tracing for request flows through App Runner services.
      - name: Amazon VPC
        description: Access private VPC resources from App Runner services via VPC connectors.
      - name: AWS Certificate Manager
        description: Automatic SSL/TLS certificate provisioning for custom domain names.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
