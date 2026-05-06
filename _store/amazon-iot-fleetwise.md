---
aid: amazon-iot-fleetwise
name: Amazon IoT FleetWise
description: AWS IoT FleetWise is a managed service that makes it easy for automotive manufacturers to collect, transform, and transfer vehicle data to the cloud in near-real time. It provides tools for vehicle data modeling, intelligent data collection, and cloud-based analytics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - AWS
  - Connected Vehicles
  - IoT
  - Telematics
  - Vehicle Data
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-fleetwise/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-fleetwise:aws-iot-fleetwise-api
    name: AWS IoT FleetWise API
    description: The AWS IoT FleetWise API provides access to vehicle data modeling, fleet management, signal catalogs, campaigns, and data collection for connected vehicle platforms.
    humanURL: https://aws.amazon.com/iot-fleetwise/
    baseURL: https://iotfleetwise.amazonaws.com
    tags:
      - Automotive
      - IoT
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-iot-fleetwise-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/iot-fleetwise/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-fleetwise/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-fleetwise/
  - type: Website
    url: https://aws.amazon.com/iot-fleetwise/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot-fleetwise/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-fleetwise/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iotfleetwise/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-fleetwise-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-fleetwise.yaml
  - type: NaftikoCapability
    url: capabilities/vehicle-fleet-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-fleetwise-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-fleetwise-context.jsonld
  - type: Features
    data:
      - name: Vehicle Signal Catalog
        description: Model vehicle signals using VSS and OEM-specific data dictionaries.
      - name: Intelligent Data Collection
        description: Collect vehicle data conditionally based on events, time windows, or triggers.
      - name: Fleet-Wide Campaigns
        description: Deploy data collection campaigns across thousands of vehicles simultaneously.
      - name: Cloud Analytics
        description: Analyze collected vehicle data using Amazon Timestream and QuickSight.
  - type: UseCases
    data:
      - name: OBD Data Collection
        description: Collect and analyze vehicle diagnostic data from CAN bus.
      - name: Driver Behavior Analysis
        description: Analyze driving patterns for safety scoring and insurance.
      - name: Predictive Maintenance
        description: Monitor vehicle health and predict maintenance needs.
  - type: Integrations
    data:
      - name: Amazon Timestream
        description: Stores vehicle time-series telemetry data for analysis.
      - name: Amazon S3
        description: Stores raw vehicle data files for batch analytics.
      - name: AWS IoT Core
        description: Provides connectivity for vehicle data transmission.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
