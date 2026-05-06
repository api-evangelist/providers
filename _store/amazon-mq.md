---
aid: amazon-mq
name: Amazon MQ
description: Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud, enabling you to migrate to a message broker without writing the code that typically enables interoperability with existing applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-mq/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-mq:mq-api
    name: Amazon MQ API
    description: Amazon MQ is a managed message broker service for Apache ActiveMQ and RabbitMQ that makes it easy to set up and operate message brokers in the cloud, enabling you to migrate to a message broker without writing the code that typically enables interoperability with existing applications.
    humanURL: https://aws.amazon.com/mq/
    baseURL: http://mq.{region}.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/mq/
      - type: OpenAPI
        url: openapi/amazon-mq-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/mq/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/mq/pricing/
      - type: FAQ
        url: https://aws.amazon.com/mq/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/mq/
  - type: Documentation
    url: https://docs.aws.amazon.com/mq/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/mq/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-mq-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-mq-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-mq-media-workflow.yaml
  - type: Features
    data:
      - name: Managed Message Brokers
        description: Fully managed Apache ActiveMQ and RabbitMQ brokers with automated provisioning and maintenance.
      - name: Protocol Support
        description: Supports AMQP, MQTT, OpenWire, STOMP, and WebSocket protocols for broad compatibility.
      - name: High Availability
        description: Active/standby configurations with automatic failover for high availability.
      - name: Network of Brokers
        description: Create networks of brokers for distributed messaging across regions and availability zones.
      - name: Broker Management API
        description: Programmatically create, configure, and manage brokers and configurations.
      - name: Security
        description: Encryption at rest and in transit, VPC isolation, and IAM integration.
  - type: UseCases
    data:
      - name: Application Migration
        description: Migrate on-premises ActiveMQ or RabbitMQ workloads to AWS without code changes.
      - name: Microservices Decoupling
        description: Use message queues to decouple microservices for improved reliability and scalability.
      - name: Enterprise Integration
        description: Connect enterprise applications using standard messaging protocols.
      - name: Event-Driven Architecture
        description: Build event-driven applications with reliable message delivery.
  - type: Integrations
    data:
      - name: Amazon VPC
        description: Deploy brokers within a VPC for network isolation and security.
      - name: Amazon CloudWatch
        description: Monitor broker metrics, queue depths, and consumer lag.
      - name: AWS KMS
        description: Encrypt broker data at rest using AWS KMS keys.
      - name: AWS IAM
        description: Control access to Amazon MQ resources with IAM policies.
      - name: Amazon CloudFormation
        description: Provision and manage brokers using CloudFormation templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
