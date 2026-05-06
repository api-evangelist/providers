---
aid: step-functions
name: AWS Step Functions
description: AWS Step Functions is a serverless orchestration service that enables developers to compose distributed applications and APIs using visual workflows called state machines. It supports Standard and Express workflows, activities, parallel execution, error handling, and integrates with over 200 AWS services. Step Functions uses the Amazon States Language (ASL) for defining workflow logic as JSON-based state machine definitions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Composition
  - Serverless Orchestration
  - Workflow
  - AWS
  - State Machine
  - Automation
url: https://raw.githubusercontent.com/api-evangelist/step-functions/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: step-functions:step-functions
    name: AWS Step Functions API
    description: The AWS Step Functions API enables creating, managing, and executing state machines and activities. Key operations include creating and deleting state machines, starting and stopping executions, listing execution history, managing state machine versions and aliases, tagging resources, and sending task heartbeats from activity workers. The API uses AWS Signature Version 4 (SigV4) authentication.
    humanURL: https://aws.amazon.com/step-functions/
    baseURL: https://states.{region}.amazonaws.com
    tags:
      - Serverless
      - Workflow
      - State Machine
      - Orchestration
      - AWS
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/step-functions/
      - type: Reference
        url: https://docs.aws.amazon.com/step-functions/latest/apireference/Welcome.html
      - type: Getting Started
        url: https://docs.aws.amazon.com/step-functions/latest/dg/getting-started.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/step-functions/refs/heads/main/openapi/step-functions-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/step-functions/pricing/
common:
  - type: Website
    url: https://aws.amazon.com/step-functions/
  - type: Documentation
    url: https://docs.aws.amazon.com/step-functions/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/states/
  - type: Pricing
    url: https://aws.amazon.com/step-functions/pricing/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/compute/aws-step-functions/
features:
  - name: Standard Workflows
    description: Long-running, durable state machines with exactly-once execution semantics
  - name: Express Workflows
    description: High-volume, event-driven workflows with at-least-once execution
  - name: State Machine Versioning
    description: Publish, manage, and deploy versioned state machine definitions
  - name: State Machine Aliases
    description: Create aliases (e.g., PROD, STAGING) pointing to specific state machine versions
  - name: Activity Workers
    description: Poll for and process work items from Step Functions activity queues
  - name: AWS Service Integrations
    description: Direct integrations with 200+ AWS services via optimized and SDK integrations
  - name: Map State
    description: Parallel iteration over input arrays with distributed map for large-scale processing
  - name: X-Ray Tracing
    description: Built-in AWS X-Ray integration for distributed tracing of workflow executions
  - name: CloudWatch Logging
    description: Configurable execution history logging to CloudWatch Logs
  - name: KMS Encryption
    description: Customer-managed KMS key encryption for state machine definitions and execution history
useCases:
  - name: Microservice Orchestration
    description: Coordinate calls across multiple microservices with error handling and retries
  - name: Data Processing Pipelines
    description: Build ETL and ML data pipelines with parallel processing and error recovery
  - name: Human Approval Workflows
    description: Pause state machine execution waiting for human approval via callback tokens
  - name: Event-Driven Automation
    description: React to AWS events and automate operational workflows
  - name: API Gateway Integration
    description: Expose Step Functions workflows as REST APIs via API Gateway integration
integrations:
  - name: AWS Lambda
    description: Invoke Lambda functions as tasks in workflow state machines
  - name: Amazon SQS
    description: Send and receive messages from SQS queues in workflows
  - name: Amazon SNS
    description: Publish notifications to SNS topics from state machines
  - name: Amazon DynamoDB
    description: Read and write DynamoDB items directly from state machines
  - name: Amazon ECS/Fargate
    description: Run containerized tasks as workflow steps
  - name: AWS Glue
    description: Trigger Glue ETL jobs from state machine executions
  - name: Amazon SageMaker
    description: Train and deploy ML models via SageMaker integrations
  - name: Amazon API Gateway
    description: Expose Step Functions as HTTP REST APIs
solutions:
  - name: Serverless Orchestration
    description: Coordinate serverless function chains without managing servers
  - name: Workflow Automation
    description: Automate complex business processes with visual workflow design
  - name: Distributed Systems Coordination
    description: Manage distributed application state with built-in error handling
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
