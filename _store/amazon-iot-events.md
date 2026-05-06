---
aid: amazon-iot-events
name: Amazon IoT Events
description: AWS IoT Events is a managed service that makes it easy to detect and respond to events from IoT sensors and applications. You can use it to build complex event detection logic, create state machines for IoT workflows, and trigger alerts or actions when specific conditions are met.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Event Detection
  - IoT
  - State Machine
  - Automation
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-events/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-events:aws-iot-events-api
    name: AWS IoT Events API
    description: The AWS IoT Events API provides access to detector models, inputs, alarms, and event detection configurations for building IoT event-driven workflows.
    humanURL: https://aws.amazon.com/iot-events/
    baseURL: https://iotevents.amazonaws.com
    tags:
      - Event Detection
      - IoT
      - State Machine
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iotevents/latest/apireference/
      - type: OpenAPI
        url: openapi/amazon-iot-events-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iotevents/latest/developerguide/getting-started-iotevents.html
      - type: Pricing
        url: https://aws.amazon.com/iot-events/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-events/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-events/
  - type: Website
    url: https://aws.amazon.com/iot-events/
  - type: Documentation
    url: https://docs.aws.amazon.com/iotevents/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-events/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iotevents/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-events-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-events.yaml
  - type: NaftikoCapability
    url: capabilities/iot-event-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-events-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-events-context.jsonld
  - type: Features
    data:
      - name: Detector Models
        description: Create state machines to detect complex event patterns across IoT data streams.
      - name: Alarm Management
        description: Built-in alarm management for monitoring IoT sensor thresholds.
      - name: Event Inputs
        description: Define structured event inputs and route IoT data to detector models.
      - name: Multi-Trigger Actions
        description: Trigger actions to SNS, SQS, Lambda, and other services when events are detected.
  - type: UseCases
    data:
      - name: Industrial Alarm Management
        description: Detect equipment failures and trigger maintenance workflows automatically.
      - name: Complex Event Processing
        description: Detect patterns across multiple sensor streams over time.
      - name: Predictive Maintenance
        description: Alert operations teams when device metrics indicate impending failure.
  - type: Integrations
    data:
      - name: AWS IoT Core
        description: Receives message data from IoT Core for event detection.
      - name: Amazon SNS
        description: Sends alerts and notifications when events are detected.
      - name: AWS Lambda
        description: Triggers Lambda functions to execute response workflows.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
