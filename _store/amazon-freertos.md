---
aid: amazon-freertos
name: Amazon FreeRTOS
description: Amazon FreeRTOS is an open source, real-time operating system for microcontrollers that makes it easy to program, deploy, secure, connect, and manage small, low-power edge devices. It extends the FreeRTOS kernel with libraries for secure connectivity, over-the-air updates, and more.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Embedded Systems
  - IoT
  - Microcontrollers
  - RTOS
url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-freertos:amazon-freertos-api
    name: Amazon FreeRTOS API
    description: The Amazon FreeRTOS API provides programmatic access to manage FreeRTOS software configurations and over-the-air update jobs for IoT devices running FreeRTOS.
    humanURL: https://aws.amazon.com/freertos/
    baseURL: https://iot.amazonaws.com
    tags:
      - Embedded Systems
      - IoT
      - RTOS
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/freertos/latest/userguide/what-is-amazon-freertos.html
      - type: OpenAPI
        url: openapi/amazon-freertos-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-freertos-software-configuration-schema.json
      - type: JSONSchema
        url: json-schema/amazon-freertos-ota-update-schema.json
      - type: JSONSchema
        url: json-schema/amazon-freertos-device-schema.json
      - type: JSONSchema
        url: json-schema/amazon-freertos-ota-file-schema.json
      - type: JSONSchema
        url: json-schema/amazon-freertos-tag-schema.json
      - type: JSONStructure
        url: json-structure/amazon-freertos-software-configuration-structure.json
      - type: JSONStructure
        url: json-structure/amazon-freertos-ota-update-structure.json
      - type: JSONStructure
        url: json-structure/amazon-freertos-device-structure.json
      - type: JSONStructure
        url: json-structure/amazon-freertos-ota-file-structure.json
      - type: JSONStructure
        url: json-structure/amazon-freertos-tag-structure.json
      - type: Example
        url: examples/amazon-freertos-software-configuration-example.json
      - type: Example
        url: examples/amazon-freertos-ota-update-example.json
      - type: Example
        url: examples/amazon-freertos-device-example.json
      - type: Example
        url: examples/amazon-freertos-ota-file-example.json
      - type: Example
        url: examples/amazon-freertos-tag-example.json
      - type: GettingStarted
        url: https://aws.amazon.com/freertos/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/freertos/pricing/
      - type: FAQ
        url: https://aws.amazon.com/freertos/faqs/
      - type: APIReference
        url: https://docs.aws.amazon.com/freertos/latest/userguide/freertos-lib-ota-api.html
common:
  - type: Portal
    url: https://aws.amazon.com/freertos/
  - type: Website
    url: https://aws.amazon.com/freertos/
  - type: Documentation
    url: https://docs.aws.amazon.com/freertos/
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
  - type: GitHubRepository
    url: https://github.com/aws/amazon-freertos
  - type: Console
    url: https://console.aws.amazon.com/iot/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-freertos
  - type: SpectralRules
    url: rules/amazon-freertos-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/freertos.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-freertos-device-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-freertos-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/amazon-freertos-context.jsonld
  - type: Features
    data:
      - name: FreeRTOS Kernel
        description: Open-source real-time operating system kernel with preemptive multitasking for microcontrollers.
      - name: OTA Update Management
        description: Over-the-air firmware update delivery with code signing verification and rollback support.
      - name: Secure Connectivity
        description: TLS 1.2/1.3 encrypted MQTT and HTTP connectivity using AWS IoT Core.
      - name: Device Provisioning
        description: Zero-touch device provisioning using AWS IoT Fleet Provisioning and Just-In-Time Registration.
      - name: corePKCS11
        description: Cryptographic library for secure key storage and operations on embedded devices.
      - name: FreeRTOS+TCP
        description: IPv4/IPv6 TCP/IP networking stack optimized for embedded systems.
      - name: Qualified Hardware
        description: Over 100 partner-qualified hardware platforms from major MCU vendors including Espressif, ST, NXP, Renesas.
  - type: UseCases
    data:
      - name: Industrial IoT Sensors
        description: Deploy FreeRTOS on industrial sensors for secure cloud connectivity and remote firmware updates.
      - name: Smart Home Devices
        description: Build connected home devices with low-power FreeRTOS firmware and AWS IoT integration.
      - name: Asset Tracking
        description: Develop GPS and location tracking devices with FreeRTOS for fleet and supply chain monitoring.
      - name: Predictive Maintenance
        description: Collect vibration, temperature, and current data from FreeRTOS devices for ML-based maintenance prediction.
      - name: Medical IoT
        description: Build FDA-validated medical devices with FreeRTOS for remote patient monitoring and diagnostics.
      - name: Energy Management
        description: Deploy smart meters and grid sensors running FreeRTOS for utility data collection and OTA updates.
  - type: Integrations
    data:
      - name: AWS IoT Core
        description: Primary cloud backend for FreeRTOS device messaging, shadow state, and job management.
      - name: AWS IoT Greengrass
        description: Extend cloud intelligence to FreeRTOS edge devices for local compute and ML inference.
      - name: AWS IoT Device Management
        description: Register, organize, monitor, and remotely manage FreeRTOS device fleets.
      - name: AWS IoT Device Defender
        description: Audit and monitor FreeRTOS device security posture for anomalies and policy violations.
      - name: Amazon S3
        description: Store firmware binaries for OTA update delivery to FreeRTOS devices.
      - name: AWS KMS
        description: Manage code signing keys for secure firmware distribution.
      - name: AWS CloudFormation
        description: Automate FreeRTOS fleet infrastructure provisioning with infrastructure-as-code templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
