---
aid: aws-lambda
name: AWS Lambda
description: AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. Lambda runs your code on high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/aws-lambda/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
apis:
  - aid: aws-lambda:aws-lambda-api
    name: AWS Lambda API
    description: The AWS Lambda REST API enables you to create, manage, and invoke Lambda functions programmatically. Supports function management, event source mappings, aliases, versions, and layer operations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/lambda/
    baseURL: https://lambda.{region}.amazonaws.com
    tags:
      - Compute
      - Event-Driven
      - FaaS
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/lambda/2015-03-31/openapi.json
      - type: OpenAPI
        url: openapi/aws-lambda-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/aws-lambda-event-triggers-asyncapi.yml
      - type: JSONSchema
        url: json-schema/aws-lambda-function-schema.json
      - type: JSONLD
        url: json-ld/aws-lambda-context.jsonld
      - type: APIReference
        url: https://docs.aws.amazon.com/lambda/latest/api/welcome.html
      - type: Pricing
        url: https://aws.amazon.com/lambda/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/lambda/getting-started/
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: Console
        url: https://console.aws.amazon.com/lambda/
      - type: StatusPage
        url: https://health.aws.amazon.com/health/status
      - type: RateLimits
        url: https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
      - type: BestPractices
        url: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
      - type: Security
        url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html
      - type: Tutorials
        url: https://aws.amazon.com/lambda/resources/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/lambda/
      - type: CodeExamples
        url: https://docs.aws.amazon.com/lambda/latest/dg/service_code_examples.html
      - type: Versioning
        url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html
      - type: Troubleshooting
        url: https://docs.aws.amazon.com/lambda/latest/dg/troubleshooting-deployment.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
      - type: X
        url: https://twitter.com/awscloud
  - aid: aws-lambda:aws-lambda-extensions-api
    name: AWS Lambda Extensions API
    description: The Lambda Extensions API enables you to create extensions that integrate with the Lambda execution environment lifecycle. Extensions can run as companion processes alongside your function, enabling use cases such as capturing diagnostic information, sending telemetry data, and integrating with monitoring and observability tools.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html
    baseURL: https://lambda.{region}.amazonaws.com
    tags:
      - Extensions
      - Monitoring
      - Observability
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html
      - type: APIReference
        url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html
      - type: Partners
        url: https://docs.aws.amazon.com/lambda/latest/dg/extensions-api-partners.html
      - type: CodeExamples
        url: https://github.com/aws-samples/aws-lambda-extensions
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - aid: aws-lambda:aws-lambda-telemetry-api
    name: AWS Lambda Telemetry API
    description: The Lambda Telemetry API lets you collect telemetry data directly from the Lambda execution environment. Extensions can subscribe to telemetry streams for platform telemetry, function logs, and extension logs to send data to custom destinations for monitoring and observability.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html
    baseURL: https://lambda.{region}.amazonaws.com
    tags:
      - Logging
      - Monitoring
      - Observability
      - Serverless
      - Telemetry
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html
      - type: APIReference
        url: https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api-reference.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - aid: aws-lambda:aws-lambda-runtime-api
    name: AWS Lambda Runtime API
    description: The Lambda Runtime API enables you to use custom runtimes to run functions in any programming language. The runtime API provides an HTTP API for custom runtimes to receive invocation events from Lambda and send response data back within the Lambda execution environment.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html
    baseURL: https://lambda.{region}.amazonaws.com
    tags:
      - Custom Runtime
      - Functions
      - Runtime
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html
      - type: APIReference
        url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - aid: aws-lambda:aws-lambda-logs-api
    name: AWS Lambda Logs API
    description: The Lambda Logs API enables extensions to subscribe to log streams generated by the Lambda platform, function code, and extensions within the execution environment, providing access to log data for processing and forwarding.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-logs-api.html
    baseURL: https://lambda.{region}.amazonaws.com
    tags:
      - Logging
      - Monitoring
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/dg/runtimes-logs-api.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
common:
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: FAQ
    url: https://aws.amazon.com/lambda/faqs/
  - type: Partners
    url: https://aws.amazon.com/lambda/partners/
  - type: KnowledgeCenter
    url: https://repost.aws/tags/TA5uNafDy2TpGNjidWLMSxDw/aws-lambda
  - type: ChangeLog
    url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-releases.html
  - type: GitHubRepository
    url: https://github.com/awsdocs/aws-lambda-developer-guide
  - type: SpectralRules
    url: rules/aws-lambda-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aws-lambda-vocabulary.yaml
  - type: Features
    url: https://aws.amazon.com/lambda/features/
    data:
      - name: Serverless Compute
        description: Run code without provisioning or managing servers, paying only for the compute time consumed.
      - name: Event-Driven Execution
        description: Automatically trigger functions from over 200 AWS services and SaaS applications via event source mappings.
      - name: Auto Scaling
        description: Automatically scale from zero to thousands of concurrent executions in response to incoming events.
      - name: Function URLs
        description: Dedicated HTTPS endpoints for Lambda functions that can be invoked directly without API Gateway.
      - name: Lambda Layers
        description: Package shared libraries, custom runtimes, and dependencies as layers reusable across multiple functions.
      - name: Provisioned Concurrency
        description: Pre-initialize function instances to reduce cold start latency for latency-sensitive workloads.
      - name: SnapStart
        description: Improve startup performance for Java functions by caching initialized snapshots of the execution environment.
      - name: Lambda Extensions
        description: Integrate monitoring, observability, and security tools directly into the Lambda execution environment.
      - name: Container Image Support
        description: Package and deploy Lambda functions as container images up to 10 GB in size.
      - name: Graviton2 Support
        description: Run functions on ARM-based AWS Graviton2 processors for better price-performance.
  - type: UseCases
    url: https://aws.amazon.com/lambda/
    data:
      - name: Real-Time File Processing
        description: Automatically process files uploaded to S3, such as image resizing, video transcoding, or document indexing.
      - name: Real-Time Stream Processing
        description: Process real-time streaming data from Kinesis or DynamoDB Streams for analytics, monitoring, or ETL pipelines.
      - name: Web Application Backends
        description: Build scalable API backends using Lambda with API Gateway or Function URLs for web and mobile applications.
      - name: IoT Backends
        description: Process IoT device data from AWS IoT Core for device management, telemetry analysis, and alerting.
      - name: Scheduled Tasks
        description: Run periodic tasks like database cleanup, report generation, or data synchronization using EventBridge rules.
      - name: CI/CD Automation
        description: Automate build, test, and deployment workflows by triggering Lambda functions from CodePipeline or GitHub events.
  - type: Integrations
    url: https://aws.amazon.com/lambda/
    data:
      - name: Amazon S3
        description: Trigger functions on object creation, deletion, or modification events in S3 buckets.
      - name: Amazon API Gateway
        description: Create RESTful and WebSocket APIs that invoke Lambda functions as backend handlers.
      - name: Amazon DynamoDB
        description: Process DynamoDB Streams events to react to table changes in real time.
      - name: Amazon SQS
        description: Poll SQS queues and invoke Lambda functions with batches of messages for asynchronous processing.
      - name: Amazon SNS
        description: Subscribe Lambda functions to SNS topics for fan-out event processing patterns.
      - name: Amazon Kinesis
        description: Process real-time streaming data from Kinesis Data Streams with configurable batch sizes and parallelization.
      - name: Amazon EventBridge
        description: Route events from AWS services, SaaS applications, and custom sources to Lambda functions based on rules.
      - name: AWS Step Functions
        description: Orchestrate Lambda functions into complex workflows with branching, error handling, and parallel execution.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
