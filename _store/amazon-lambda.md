---
name: Amazon Lambda
description: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, automatically scaling and executing your code in response to events from over 200 AWS services and SaaS applications while you pay only for the compute time you consume.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/lambda/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Lambda API
    description: Core API for managing AWS Lambda functions, event source mappings, layers, aliases, versions, and permissions. Enables creating and invoking serverless functions, configuring triggers from AWS services, and managing function deployment packages and runtime configurations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/lambda/
    baseURL: https://lambda.amazonaws.com
    tags:
      - AWS
      - Compute
      - Event-Driven
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
      - type: OpenAPI
        url: openapi/amazon-lambda-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-lambda-function-schema.json
      - type: JSONLD
        url: json-ld/amazon-lambda-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/lambda/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/lambda/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-auth-and-access-control.html
      - type: SDKs
        url: https://aws.amazon.com/tools/
      - type: Status
        url: https://status.aws.amazon.com/
      - type: Best Practices
        url: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
      - type: FAQ
        url: https://aws.amazon.com/lambda/faqs/
      - type: Service Level Agreement
        url: https://aws.amazon.com/lambda/sla/
      - type: User Guide
        url: https://docs.aws.amazon.com/lambda/latest/dg/
      - type: APIReference
        url: https://docs.aws.amazon.com/lambda/latest/api/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/lambda/
      - type: Security
        url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
      - type: JSONSchema
        url: json-schema/amazon-lambda-event-source-mapping-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/lambda/
  - type: Documentation
    url: https://docs.aws.amazon.com/lambda/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/lambda/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Knowledge Center
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/aws-lambda
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Serverless Execution
        description: Run code without provisioning or managing servers — Lambda handles all administration.
      - name: Event-Driven Triggers
        description: Automatically trigger code from over 200 AWS services and SaaS applications.
      - name: Automatic Scaling
        description: Automatically scales to thousands of concurrent executions without configuration.
      - name: Multiple Runtimes
        description: Supports Node.js, Python, Java, Go, Ruby, .NET, and custom runtimes via Lambda layers.
      - name: Lambda Layers
        description: Package and share code, libraries, and configurations across Lambda functions.
      - name: Container Image Support
        description: Deploy Lambda functions as container images up to 10 GB in size.
      - name: SnapStart
        description: Reduce cold starts for Java functions with Lambda SnapStart.
  - type: UseCases
    data:
      - name: API Backends
        description: Build REST and GraphQL API backends with Lambda and API Gateway.
      - name: Data Processing
        description: Process S3 uploads, DynamoDB streams, and Kinesis records in real time.
      - name: Event Automation
        description: Automate operational tasks triggered by CloudWatch events or schedules.
      - name: Machine Learning Inference
        description: Run ML model inference on-demand without managing inference infrastructure.
  - type: Integrations
    data:
      - name: Amazon API Gateway
        description: Build REST and WebSocket APIs backed by Lambda functions.
      - name: Amazon DynamoDB
        description: Trigger Lambda from DynamoDB Streams for real-time data processing.
      - name: Amazon S3
        description: Trigger Lambda on S3 object events for serverless file processing.
      - name: Amazon Kinesis
        description: Process Kinesis data streams with Lambda for real-time analytics.
      - name: AWS Step Functions
        description: Orchestrate Lambda functions in serverless workflows.
      - name: Amazon SQS
        description: Process SQS messages with Lambda for decoupled event processing.
  - type: SpectralRules
    url: rules/amazon-lambda-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-lambda-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-lambda-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Compute
  - Event-Driven
  - FaaS
  - Functions
  - Serverless
---
