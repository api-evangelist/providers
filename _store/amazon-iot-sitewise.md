---
aid: amazon-iot-sitewise
name: Amazon IoT SiteWise
description: AWS IoT SiteWise is a managed service that makes it easy to collect, store, organize, and monitor industrial data at scale. It provides tools to create asset models representing your industrial operations and analyze equipment performance across your facilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Asset Management
  - Industrial IoT
  - IoT
  - Time Series Data
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-sitewise/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-sitewise:aws-iot-sitewise-api
    name: AWS IoT SiteWise API
    description: The AWS IoT SiteWise API provides access to asset model management, asset data ingestion, time-series data queries, portals, and dashboards for industrial IoT monitoring.
    humanURL: https://aws.amazon.com/iot-sitewise/
    baseURL: https://iotsitewise.amazonaws.com
    tags:
      - Asset Management
      - Industrial IoT
      - IoT
      - Time Series
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-iot-sitewise-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started.html
      - type: Pricing
        url: https://aws.amazon.com/iot-sitewise/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-sitewise/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-sitewise/
  - type: Website
    url: https://aws.amazon.com/iot-sitewise/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot-sitewise/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-sitewise/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iotsitewise/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-sitewise-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-sitewise.yaml
  - type: NaftikoCapability
    url: capabilities/industrial-asset-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-sitewise-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-sitewise-context.jsonld
  - type: Features
    data:
      - name: Asset Modeling
        description: Create hierarchical asset models that represent your industrial equipment and processes.
      - name: Time-Series Data Storage
        description: Ingest and store industrial sensor data with automatic data quality classification.
      - name: SiteWise Monitor
        description: Build no-code dashboards for industrial operations visualization.
      - name: Edge Processing
        description: Process data locally at industrial sites using SiteWise Edge.
      - name: Computed Properties
        description: Define metrics and transforms on asset data using built-in formula engine.
  - type: UseCases
    data:
      - name: Equipment Performance Monitoring
        description: Track OEE and equipment health across multiple manufacturing facilities.
      - name: Energy Management
        description: Monitor and optimize energy consumption across industrial sites.
      - name: Process Optimization
        description: Analyze production line data to identify bottlenecks and inefficiencies.
  - type: Integrations
    data:
      - name: AWS IoT Greengrass
        description: Collects industrial data from OPC-UA, Modbus, and Ethernet/IP sources at the edge.
      - name: Amazon Kinesis
        description: Streams asset property data for real-time analytics.
      - name: Amazon QuickSight
        description: Visualizes SiteWise industrial data in business dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
