---
name: Amazon EventBridge
description: Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, SaaS applications, and AWS services and routes that data to targets such as Lambda, SNS, SQS, and more.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/eventbridge/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Event Bus
  - Event-Driven
  - Events
  - Integration
  - Serverless
apis:
  - name: Amazon EventBridge API
    description: API for creating and managing event buses, rules, targets, and connections for routing events across applications, microservices, and SaaS integrations.
    humanURL: https://aws.amazon.com/eventbridge/
    baseURL: https://events.amazonaws.com
    tags:
      - Event Bus
      - Event-Driven
      - Events
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/eventbridge/latest/userguide/
      - type: OpenAPI
        url: openapi/amazon-eventbridge-openapi.yml
      - type: AsyncAPI
        url: asyncapi/amazon-eventbridge-asyncapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/eventbridge/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/eventbridge/pricing/
      - type: FAQ
        url: https://aws.amazon.com/eventbridge/faqs/
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-create-archive-request-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-create-archive-response-schema.json
      - type: JSONSchema
        url: json-schema/amazon-eventbridge-create-event-bus-request-schema.json
      - type: JSONLD
        url: json-ld/amazon-eventbridge-context.jsonld
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
    url: rules/amazon-eventbridge-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-eventbridge-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-eventbridge-vocabulary.yaml
  - type: Features
    data:
      - name: Event Bus
        description: Central event bus for routing events between AWS services and applications
      - name: Event Rules
        description: Create rules to filter and route events to specific targets
      - name: Schema Registry
        description: Discover, create, and manage event schemas with code binding generation
      - name: SaaS Integrations
        description: Receive events from SaaS partners like Zendesk, Datadog, and PagerDuty
      - name: API Destinations
        description: Send events to external HTTP endpoints via API Destinations
  - type: UseCases
    data:
      - name: Microservices Decoupling
        description: Decouple microservices by routing events through a central event bus
      - name: Application Monitoring
        description: React to CloudWatch alarms and AWS service events in real time
      - name: SaaS Event Processing
        description: Receive and process events from SaaS applications without polling
      - name: Multi-Account Event Routing
        description: Route events across AWS accounts and regions for enterprise architectures
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Invoke Lambda functions in response to events
      - name: Amazon SNS
        description: Fan out events to multiple subscribers via SNS topics
      - name: Amazon SQS
        description: Queue events for reliable processing with SQS
      - name: AWS Step Functions
        description: Start state machine executions in response to events
      - name: Zendesk
        description: Receive Zendesk support ticket and activity events
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
