---
aid: amazon-iot-device-management
name: Amazon IoT Device Management
description: AWS IoT Device Management makes it easy to securely onboard, organize, monitor, and remotely manage your IoT devices at scale. You can register your connected devices individually or in bulk, and easily manage permissions so your devices remain secure throughout their lifecycle.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Device Management
  - Fleet Management
  - IoT
  - OTA Updates
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-device-management/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-device-management:aws-iot-management-api
    name: AWS IoT Device Management API
    description: The AWS IoT Device Management API provides access to thing groups, jobs, bulk registration, fleet indexing, and remote device management capabilities.
    humanURL: https://aws.amazon.com/iot-device-management/
    baseURL: https://iot.amazonaws.com
    tags:
      - Device Management
      - Fleet Management
      - IoT
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html
      - type: OpenAPI
        url: openapi/amazon-iot-device-management-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html
      - type: Pricing
        url: https://aws.amazon.com/iot-device-management/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-device-management/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-device-management/
  - type: Website
    url: https://aws.amazon.com/iot-device-management/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html
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
    url: rules/amazon-iot-device-management-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-device-management.yaml
  - type: NaftikoCapability
    url: capabilities/iot-fleet-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-device-management-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-device-management-context.jsonld
  - type: Features
    data:
      - name: Bulk Device Registration
        description: Register thousands of devices simultaneously using bulk registration templates.
      - name: Fleet Indexing
        description: Search and query your entire device fleet based on attributes and shadow state.
      - name: Remote Jobs
        description: Deploy firmware updates, configuration changes, and software remotely at scale.
      - name: Thing Groups
        description: Organize devices into hierarchical groups for policies and bulk operations.
      - name: Tunnel Secure
        description: Create secure bidirectional tunnels to devices behind firewalls for remote troubleshooting.
  - type: UseCases
    data:
      - name: OTA Firmware Updates
        description: Deploy firmware updates to thousands of devices simultaneously with rollback.
      - name: Device Onboarding
        description: Automate device provisioning and certificate management at manufacturing.
      - name: Fleet Monitoring
        description: Monitor device connectivity, metadata, and shadow state across the entire fleet.
  - type: Integrations
    data:
      - name: AWS IoT Core
        description: All device management operations integrate with IoT Core connectivity.
      - name: AWS Lambda
        description: Trigger automation workflows based on job status changes.
      - name: Amazon S3
        description: Store firmware and configuration files for remote deployment.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
