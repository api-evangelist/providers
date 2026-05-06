---
name: Amazon EventBridge Pipes
description: Amazon EventBridge Pipes helps you create point-to-point integrations between event producers and consumers with optional transform, filter, and enrich steps. It reduces the amount of integration code you need to write and maintain when building event-driven applications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/eventbridge/pipes/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Event-Driven
  - Integration
  - Messaging
  - Serverless
apis:
  - name: Amazon EventBridge Pipes API
    description: API for creating and managing pipes that connect event sources to targets with optional filtering, enrichment, and transformation capabilities.
    humanURL: https://aws.amazon.com/eventbridge/pipes/
    baseURL: https://pipes.amazonaws.com
    tags:
      - Event-Driven
      - Integration
      - Messaging
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html
      - type: OpenAPI
        url: openapi/amazon-eventbridge-pipes-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/
      - type: GettingStarted
        url: https://aws.amazon.com/eventbridge/pipes/
      - type: Pricing
        url: https://aws.amazon.com/eventbridge/pricing/
      - type: FAQ
        url: https://aws.amazon.com/eventbridge/faqs/
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-pipes-arn-or-json-path-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-pipes-arn-or-url-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-pipes-arn-schema.json
      - type: JSONLD
        url: json-ld/amazon-eventbridge-pipes-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/eventbridge/
  - type: Documentation
    url: https://docs.aws.amazon.com/eventbridge/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/events/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/eventbridge/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/eventbridge
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-eventbridge-pipes-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-eventbridge-pipes-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-eventbridge-pipes-vocabulary.yaml
  - type: Features
    data:
      - name: Point-to-Point Integration
        description: Connect event sources directly to targets with minimal code
      - name: Event Filtering
        description: Filter events before processing to reduce costs and noise
      - name: Event Enrichment
        description: Enrich events with data from Lambda, Step Functions, or API destinations
      - name: Event Transformation
        description: Transform event payloads using input transformers
      - name: Batching Support
        description: Process events in batches for improved throughput
  - type: UseCases
    data:
      - name: Database Change Data Capture
        description: Stream DynamoDB or Aurora changes to downstream systems
      - name: Queue Processing
        description: Connect SQS queues to Lambda or Step Functions for message processing
      - name: Stream Analytics
        description: Process Kinesis or Kafka streams with filtering and enrichment
      - name: SaaS Integration
        description: Connect SaaS event sources to AWS targets without custom code
  - type: Integrations
    data:
      - name: Amazon DynamoDB Streams
        description: Use DynamoDB Streams as an event source
      - name: Amazon SQS
        description: Connect SQS queues as event sources or targets
      - name: Amazon Kinesis
        description: Process Kinesis data stream events
      - name: AWS Lambda
        description: Use Lambda as enrichment or target for pipe events
      - name: Apache Kafka
        description: Connect Apache Kafka and Amazon MSK as event sources
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
