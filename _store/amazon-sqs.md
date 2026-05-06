---
aid: amazon-sqs
name: Amazon SQS
description: Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-sqs/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - AWS
  - Cloud
  - Distributed Systems
  - Messaging
  - Microservices
  - Queue
apis:
  - name: Amazon SQS API
    description: RESTful API for Amazon Simple Queue Service operations including queue management, message sending and receiving, batch operations, dead-letter queues, and access control.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/sqs/
    baseURL: https://sqs.{region}.amazonaws.com/
    tags:
      - AWS
      - Messaging
      - Queue
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sqs/
      - type: OpenAPI
        url: openapi/amazon-sqs-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/sqs/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/sqs/pricing/
      - type: FAQ
        url: https://aws.amazon.com/sqs/faqs/
      - type: BestPractices
        url: https://docs.aws.amazon.com/sqs/latest/dg/best-practices.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: Tutorials
        url: https://docs.aws.amazon.com/sqs/latest/dg/sqs-tutorials.html
      - type: Features
        url: https://aws.amazon.com/sqs/features/
      - type: Security
        url: https://docs.aws.amazon.com/sqs/latest/dg/sqs-security.html
      - type: Compliance
        url: https://aws.amazon.com/compliance/services-in-scope/
      - type: CLI
        url: https://docs.aws.amazon.com/cli/latest/reference/sqs/
      - type: CodeExamples
        url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/service_code_examples.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.html
      - type: Regions
        url: https://docs.aws.amazon.com/general/latest/gr/sqs-service.html
      - type: ReleaseNotes
        url: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-release-notes.html
    contact:
      - FN: AWS Support
        url: https://aws.amazon.com/contact-us/
        email: ''
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/compute/
  - type: Console
    url: https://console.aws.amazon.com/sqs/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://console.aws.amazon.com/support/home
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: CodeExamples
    url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_code_examples.html
  - type: GitHubRepository
    url: https://github.com/awsdocs/aws-doc-sdk-examples
  - type: Features
    data:
      - name: Standard Queues
        description: Maximum throughput, best-effort ordering, and at-least-once delivery for high-volume messaging workloads.
      - name: FIFO Queues
        description: Exactly-once processing and strict ordering guarantees for applications requiring message sequence preservation.
      - name: Dead-Letter Queues
        description: Automatic routing of failed messages to dead-letter queues for debugging and reprocessing.
      - name: Message Move Tasks
        description: Bulk movement of messages between queues for reprocessing dead-letter queue contents.
      - name: Server-Side Encryption
        description: Automatic encryption of messages at rest using AWS KMS keys for data protection.
      - name: Long Polling
        description: Reduced API costs and latency by allowing consumers to wait for messages to arrive before responding.
  - type: UseCases
    data:
      - name: Microservices Decoupling
        description: Decouple microservices by using SQS queues as asynchronous communication buffers between services.
      - name: Serverless Event Processing
        description: Trigger AWS Lambda functions from SQS messages for event-driven serverless architectures.
      - name: Order Processing Pipelines
        description: Use FIFO queues to ensure ordered processing of e-commerce orders and financial transactions.
      - name: Work Queue Distribution
        description: Distribute compute-intensive tasks across multiple workers using standard queues for parallel processing.
      - name: Batch Job Orchestration
        description: Queue batch processing jobs and manage their execution across distributed compute resources.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Automatically invoke Lambda functions when messages arrive in SQS queues for serverless processing.
      - name: Amazon SNS
        description: Fan out SNS notifications to multiple SQS queues for parallel processing of published messages.
      - name: Amazon EventBridge
        description: Route events from EventBridge to SQS queues for reliable event-driven architectures.
      - name: AWS CloudFormation
        description: Provision and manage SQS queues as infrastructure-as-code using CloudFormation templates.
      - name: Terraform
        description: Create and manage SQS resources using HashiCorp Terraform infrastructure-as-code provider.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
---
