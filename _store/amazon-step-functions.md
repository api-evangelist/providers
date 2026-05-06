---
name: Amazon Step Functions
description: Amazon Step Functions is a serverless workflow orchestration service that lets you coordinate distributed applications and microservices using visual workflows, enabling you to build and update state machines that react to events, manage retries, and orchestrate complex business processes.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/step-functions/
created: '2024-01-15'
modified: '2026-04-19'
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
        url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-step-functions.yaml
      - type: GettingStarted
        url: https://aws.amazon.com/step-functions/
      - type: Pricing
        url: https://aws.amazon.com/step-functions/pricing/
      - type: FAQ
        url: https://aws.amazon.com/step-functions/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/step-functions/
  - type: Documentation
    url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/application-services/aws-step-functions/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/states/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-step-functions-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-step-functions-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-step-functions.yaml
  - type: Features
    data:
      - name: Visual Workflow
        description: Design and visualize workflows using Amazon States Language (ASL).
      - name: Serverless Orchestration
        description: Orchestrate Lambda, ECS, Fargate, SNS, SQS, and 220+ AWS services.
      - name: Error Handling
        description: Built-in retry and catch capabilities for fault-tolerant workflows.
      - name: Express Workflows
        description: High-throughput workflows for event processing at scale.
      - name: Standard Workflows
        description: Long-running durable workflows with exactly-once execution.
  - type: UseCases
    data:
      - name: Microservice Orchestration
        description: Coordinate multiple microservices into cohesive workflows.
      - name: Data Processing Pipelines
        description: Build ETL and data transformation pipelines with automatic retries.
      - name: IT Automation
        description: Automate IT and business processes with visual workflow design.
      - name: ML Model Training Pipelines
        description: Orchestrate SageMaker model training, evaluation, and deployment.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Invoke Lambda functions as workflow steps.
      - name: Amazon ECS
        description: Run ECS/Fargate tasks as part of workflows.
      - name: Amazon DynamoDB
        description: Read and write DynamoDB tables directly from workflows.
      - name: Amazon SNS
        description: Publish SNS notifications from workflow steps.
      - name: Amazon SageMaker
        description: Orchestrate ML training and inference pipelines.
      - name: AWS Glue
        description: Run Glue ETL jobs from workflow steps.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Orchestration
  - Serverless
  - State Machine
  - Workflow
x-type: company
---
