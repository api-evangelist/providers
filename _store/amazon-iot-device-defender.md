---
aid: amazon-iot-device-defender
name: Amazon IoT Device Defender
description: AWS IoT Device Defender is a security service that lets you continuously audit your IoT configurations to detect deviations from security best practices. It also lets you detect abnormal device behavior through ML-based anomaly detection and take actions to mitigate security risks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Compliance
  - IoT
  - Security
  - Vulnerability Management
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-device-defender/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-device-defender:aws-iot-defender-api
    name: AWS IoT Device Defender API
    description: The AWS IoT Device Defender API provides programmatic access to security profiles, audit configurations, anomaly detection, and violation management for IoT fleet security.
    humanURL: https://aws.amazon.com/iot-device-defender/
    baseURL: https://iot.amazonaws.com
    tags:
      - Compliance
      - IoT
      - Security
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html
      - type: OpenAPI
        url: openapi/amazon-iot-device-defender-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/iot-device-defender/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-device-defender/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-device-defender/
  - type: Website
    url: https://aws.amazon.com/iot-device-defender/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-device-defender/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iot/home#/devicedefender
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-device-defender-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-device-defender.yaml
  - type: NaftikoCapability
    url: capabilities/iot-security-monitoring.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-device-defender-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-device-defender-context.jsonld
  - type: Features
    data:
      - name: Configuration Audit
        description: Continuously audit IoT configurations against security best practices.
      - name: ML Anomaly Detection
        description: Detect abnormal device behavior using machine learning models.
      - name: Security Profiles
        description: Define expected behaviors for device metrics and receive alerts on violations.
      - name: Automated Mitigation
        description: Automatically take actions to mitigate security violations.
  - type: UseCases
    data:
      - name: IoT Compliance
        description: Ensure IoT deployments meet security compliance requirements.
      - name: Threat Detection
        description: Detect compromised devices exhibiting abnormal communication patterns.
      - name: Security Auditing
        description: Audit IoT policies and certificates against security best practices.
  - type: Integrations
    data:
      - name: AWS IoT Core
        description: Monitors all IoT Core device connections and policies.
      - name: Amazon CloudWatch
        description: Sends security metrics and alerts to CloudWatch.
      - name: AWS Security Hub
        description: Publishes IoT security findings to Security Hub.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
