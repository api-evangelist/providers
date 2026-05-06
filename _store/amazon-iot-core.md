---
aid: amazon-iot-core
name: Amazon IoT Core
description: AWS IoT Core is a managed cloud service that lets connected devices easily and securely interact with cloud applications and other devices. It can support billions of devices and trillions of messages, routing those messages to AWS endpoints and other devices reliably and securely.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Device Management
  - IoT
  - MQTT
  - Message Routing
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-core/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-core:aws-iot-api
    name: AWS IoT Core API
    description: The AWS IoT Core API provides programmatic access to manage things, policies, certificates, rules, and MQTT messaging for IoT device connectivity.
    humanURL: https://aws.amazon.com/iot-core/
    baseURL: https://iot.amazonaws.com
    tags:
      - Device Management
      - IoT
      - MQTT
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot/latest/apireference/
      - type: OpenAPI
        url: openapi/amazon-iot-core-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html
      - type: Pricing
        url: https://aws.amazon.com/iot-core/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-core/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-core/
  - type: Website
    url: https://aws.amazon.com/iot-core/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iot/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-core-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-core.yaml
  - type: NaftikoCapability
    url: capabilities/iot-device-connectivity.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-core-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-core-context.jsonld
  - type: Features
    data:
      - name: Secure Device Connectivity
        description: Connects IoT devices to AWS using MQTT, HTTPS, and WebSocket protocols with mutual TLS authentication.
      - name: Message Broker
        description: Scales to billions of messages per day with a fully managed MQTT message broker.
      - name: Rules Engine
        description: Routes device messages to 15+ AWS services based on SQL-like rules.
      - name: Device Shadow
        description: Maintains a persistent virtual representation of each device for state management.
      - name: Fleet Indexing
        description: Index and search all IoT things and their attributes at scale.
  - type: UseCases
    data:
      - name: Industrial IoT
        description: Connect factory equipment to AWS for real-time monitoring and predictive maintenance.
      - name: Smart Home
        description: Build connected home devices with secure two-way communication.
      - name: Asset Tracking
        description: Track vehicles, equipment, and assets with GPS and sensor data.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Trigger serverless functions from IoT device messages with Rules Engine.
      - name: Amazon Kinesis
        description: Stream IoT telemetry data to Kinesis for real-time analytics.
      - name: Amazon S3
        description: Store device messages and data in S3 using IoT Rules.
      - name: Amazon DynamoDB
        description: Write device state data to DynamoDB tables with IoT Rules.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
