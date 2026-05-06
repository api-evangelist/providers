---
aid: amazon-iot-twinmaker
name: Amazon IoT TwinMaker
description: AWS IoT TwinMaker makes it easier for developers to create digital twins of real-world systems such as buildings, factories, and industrial equipment. You can use AWS IoT TwinMaker to build operational digital twin applications to visualize, monitor, and diagnose complex operational systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - 3D Visualization
  - Digital Twin
  - Industrial IoT
  - IoT
url: https://raw.githubusercontent.com/api-evangelist/amazon-iot-twinmaker/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iot-twinmaker:aws-iot-twinmaker-api
    name: AWS IoT TwinMaker API
    description: The AWS IoT TwinMaker API provides access to workspaces, scenes, entities, components, and sync jobs for building and managing digital twin applications.
    humanURL: https://aws.amazon.com/iot-twinmaker/
    baseURL: https://iottwinmaker.amazonaws.com
    tags:
      - 3D Visualization
      - Digital Twin
      - IoT
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/
      - type: OpenAPI
        url: openapi/amazon-iot-twinmaker-openapi-original.yml
      - type: GettingStarted
        url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html
      - type: Pricing
        url: https://aws.amazon.com/iot-twinmaker/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iot-twinmaker/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/iot-twinmaker/
  - type: Website
    url: https://aws.amazon.com/iot-twinmaker/
  - type: Documentation
    url: https://docs.aws.amazon.com/iot-twinmaker/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/iot/tag/aws-iot-twinmaker/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/iottwinmaker/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iot-twinmaker-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/iot-twinmaker.yaml
  - type: NaftikoCapability
    url: capabilities/digital-twin-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iot-twinmaker-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iot-twinmaker-context.jsonld
  - type: Features
    data:
      - name: Digital Twin Modeling
        description: Model physical systems as entities with components and property relationships.
      - name: 3D Scene Integration
        description: Build interactive 3D visualization scenes connected to live IoT data.
      - name: Data Connectors
        description: Connect to existing data sources with built-in and custom data connectors.
      - name: Knowledge Graph
        description: Explore entity relationships and property graphs for complex systems.
  - type: UseCases
    data:
      - name: Smart Building Management
        description: Create digital twins of buildings for energy optimization and maintenance.
      - name: Factory Digital Twin
        description: Visualize production lines and equipment in 3D for operators.
      - name: Remote Operations
        description: Enable remote monitoring and diagnosis of industrial equipment.
  - type: Integrations
    data:
      - name: AWS IoT SiteWise
        description: Connects SiteWise asset data to TwinMaker entity components.
      - name: Amazon Grafana
        description: Visualizes TwinMaker data in Grafana dashboards.
      - name: AWS IoT Core
        description: Receives real-time device data for digital twin updates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
