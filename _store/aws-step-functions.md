---
aid: aws-step-functions
name: AWS Step Functions
description: AWS Step Functions is a serverless orchestration service that lets you coordinate distributed applications and microservices using visual workflows, integrating with AWS services and supporting error handling and retries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - iPaaS
  - Orchestration
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/aws-step-functions/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aws-step-functions:aws-step-functions
    name: AWS Step Functions
    description: AWS Step Functions is a serverless orchestration service that lets you coordinate distributed applications and microservices using visual workflows, integrating with AWS services and supporting error handling and retries. Define workflows in Amazon States Language with standard and express workflow types.
    humanURL: https://aws.amazon.com/step-functions/
    baseURL: https://states.{region}.amazonaws.com
    tags:
      - iPaaS
      - Orchestration
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/step-functions/
      - type: GettingStarted
        url: https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html
      - type: OpenAPI
        url: openapi/aws-step-functions-openapi.json
      - type: APIReference
        url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
common:
  - type: Website
    url: https://aws.amazon.com/step-functions/
  - type: Documentation
    url: https://docs.aws.amazon.com/step-functions/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Pricing
    url: https://aws.amazon.com/step-functions/pricing/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/application-services/aws-step-functions/
  - type: ChangeLog
    url: https://aws.amazon.com/releasenotes/aws-step-functions/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: SpectralRules
    url: rules/aws-step-functions-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-step-functions-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/orchestration-workflow.yaml
  - type: Features
    data:
      - name: Visual Workflow Design
        description: Design and visualize workflows using the Workflow Studio drag-and-drop interface.
      - name: Amazon States Language
        description: Define workflows in a JSON-based structured language with built-in error handling and retry logic.
      - name: AWS Service Integrations
        description: Natively integrate with over 220 AWS services without writing custom code.
      - name: Standard Workflows
        description: Long-running, durable workflows with exactly-once task execution semantics.
      - name: Express Workflows
        description: High-volume, short-duration workflows optimized for cost with at-least-once execution.
      - name: Error Handling
        description: Built-in retry logic and catch blocks for graceful error handling and fallback paths.
      - name: Parallel Execution
        description: Run parallel branches simultaneously within the same state machine execution.
      - name: Map State
        description: Process arrays of items in parallel using the Map state for dynamic fan-out.
      - name: Wait for Callback
        description: Pause workflows waiting for external events using task tokens.
      - name: X-Ray Integration
        description: Built-in tracing via AWS X-Ray for end-to-end visibility into workflow executions.
  - type: UseCases
    data:
      - name: Microservice Orchestration
        description: Coordinate multiple microservices in a reliable, fault-tolerant workflow.
      - name: Data Processing Pipelines
        description: Build ETL pipelines that process data in parallel across multiple services.
      - name: Human Approval Workflows
        description: Implement approval workflows that wait for human decisions via task tokens.
      - name: Event-Driven Automation
        description: Automate complex multi-step processes triggered by events.
      - name: Machine Learning Pipelines
        description: Orchestrate ML model training, evaluation, and deployment using SageMaker integrations.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Invoke Lambda functions as Task states in workflows.
      - name: Amazon SQS
        description: Send and receive messages from SQS queues as part of workflows.
      - name: Amazon DynamoDB
        description: Read and write DynamoDB records directly from workflow states.
      - name: Amazon ECS
        description: Run ECS tasks and Fargate containers as workflow steps.
      - name: Amazon SageMaker
        description: Orchestrate ML training, processing, and deployment workflows.
      - name: AWS Glue
        description: Trigger and monitor Glue ETL jobs from Step Functions workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
