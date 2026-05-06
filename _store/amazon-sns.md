---
aid: amazon-sns
name: Amazon SNS
description: Amazon Simple Notification Service (SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It enables pub/sub, SMS, email, and mobile push notifications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-sns/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - AWS
  - Email
  - Messaging
  - Notifications
  - Pub/Sub
  - Push Notifications
  - SMS
apis:
  - name: Amazon SNS API
    description: RESTful API for Amazon Simple Notification Service providing topic management, subscription lifecycle, message publishing, platform application management for mobile push, and SMS messaging operations.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/sns/
    baseURL: https://sns.{region}.amazonaws.com
    tags:
      - AWS
      - Messaging
      - Notifications
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sns/
      - type: OpenAPI
        url: openapi/amazon-sns-api-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/sns/latest/api/welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/sns/pricing/
      - type: FAQ
        url: https://aws.amazon.com/sns/faqs/
      - type: BestPractices
        url: https://docs.aws.amazon.com/sns/latest/dg/sns-best-practices.html
      - type: Features
        url: https://aws.amazon.com/sns/features/
      - type: Security
        url: https://docs.aws.amazon.com/sns/latest/dg/sns-security.html
      - type: RateLimits
        url: https://docs.aws.amazon.com/sns/latest/dg/sns-quotas.html
      - type: CodeExamples
        url: https://github.com/awsdocs/aws-doc-sdk-examples
      - type: SDK
        url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html
        title: Python SDK
      - type: CLI
        url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html
    contact:
      - FN: Amazon Web Services
        url: https://aws.amazon.com/sns/
        email: ''
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/messaging-and-targeting/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Console
    url: https://console.aws.amazon.com/sns/
  - type: Compliance
    url: https://aws.amazon.com/compliance/services-in-scope/
  - type: Support
    url: https://console.aws.amazon.com/support/home
  - type: KnowledgeCenter
    url: https://aws.amazon.com/premiumsupport/knowledge-center/#Amazon_Simple_Notification_Service
  - type: Partners
    url: https://aws.amazon.com/sns/partners/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: GitHubRepository
    url: https://github.com/awsdocs/amazon-sns-developer-guide
  - type: Features
    data:
      - name: Pub/Sub Messaging
        description: Fan-out messages to multiple subscribers through topics supporting HTTP/S, email, SQS, Lambda, and SMS protocols.
      - name: FIFO Topics
        description: Strict message ordering and exactly-once delivery for use cases requiring sequence-preserving fan-out.
      - name: Message Filtering
        description: Subscription filter policies enabling subscribers to receive only the messages relevant to them.
      - name: Mobile Push Notifications
        description: Cross-platform mobile push via APNs, FCM, and other push services through platform applications.
      - name: SMS Messaging
        description: Direct SMS text messaging to phone numbers worldwide with support for transactional and promotional messages.
      - name: Dead-Letter Queues
        description: Capture undeliverable messages for analysis and reprocessing to ensure no messages are lost.
  - type: UseCases
    data:
      - name: Application Event Fan-Out
        description: Broadcast application events to multiple microservices simultaneously using pub/sub topic subscriptions.
      - name: Mobile Push Campaigns
        description: Send targeted push notifications to mobile applications across iOS and Android platforms.
      - name: Alert and Monitoring Systems
        description: Deliver operational alerts via SMS, email, and HTTP endpoints for infrastructure monitoring.
      - name: Order Confirmation Notifications
        description: Send transactional notifications for order confirmations, shipping updates, and account activity.
      - name: Cross-Account Event Distribution
        description: Share events across AWS accounts using SNS topic policies for multi-account architectures.
  - type: Integrations
    data:
      - name: Amazon SQS
        description: Fan out SNS messages to SQS queues for reliable asynchronous processing across multiple consumers.
      - name: AWS Lambda
        description: Invoke Lambda functions directly from SNS notifications for serverless event processing.
      - name: Amazon EventBridge
        description: Route SNS events through EventBridge for complex event-driven routing and filtering.
      - name: AWS CloudFormation
        description: Define and manage SNS topics and subscriptions as infrastructure-as-code resources.
      - name: Amazon Kinesis Data Firehose
        description: Deliver SNS messages to data lakes and analytics services through Kinesis Data Firehose.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
