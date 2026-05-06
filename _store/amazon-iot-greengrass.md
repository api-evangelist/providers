---
aid: amazon-iot-greengrass
name: Amazon IoT Greengrass
description: AWS IoT Greengrass extends AWS compute, messaging, data management, sync, and ML inference capabilities to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Edge Computing
  - IoT
  - Lambda
  - Machine Learning
  - Real-Time Processing
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-greengrass/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-greengrass:aws-iot-greengrass-api
    name: AWS IoT Greengrass API
    description: The AWS IoT Greengrass V2 API provides access to component management, core device management, and deployment orchestration for edge computing workloads.
    humanURL: https://aws.amazon.com/greengrass/
    baseURL: https://greengrass.amazonaws.com
    tags:
      - Edge Computing
      - IoT
      - Lambda
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/greengrass/v2/APIReference/
      - type: OpenAPI
        url: openapi/amazon-iot-greengrass-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/greengrass/pricing/
      - type: FAQ
        url: https://aws.amazon.com/greengrass/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/greengrass/
  - type: Website
    url: https://aws.amazon.com/greengrass/
  - type: Documentation
    url: https://docs.aws.amazon.com/greengrass/v2/developerguide/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-greengrass/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/greengrass/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-greengrass-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-greengrass.yaml
  - type: NaftikoCapability
    url: capabilities/edge-device-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-greengrass-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-greengrass-context.jsonld
  - type: Features
    data:
      - name: Edge Computing
        description: Run Lambda functions and containers on edge devices with local compute.
      - name: Component System
        description: Deploy reusable software components to edge devices from a component catalog.
      - name: Local ML Inference
        description: Run machine learning inference locally with SageMaker model deployment.
      - name: Deployment Management
        description: Deploy and update software components to thousands of edge devices.
      - name: Local Messaging
        description: Enable MQTT messaging between local IoT devices without cloud round-trips.
  - type: UseCases
    data:
      - name: Industrial Edge Processing
        description: Process sensor data locally to reduce latency and bandwidth.
      - name: Edge ML Inference
        description: Run computer vision and anomaly detection models at the edge.
      - name: Offline Operation
        description: Continue processing and storing data when disconnected from the cloud.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Run Lambda functions on edge devices for local processing.
      - name: Amazon SageMaker
        description: Deploy trained ML models to edge devices for local inference.
      - name: AWS IoT Core
        description: Syncs device state and routes messages between edge and cloud.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
