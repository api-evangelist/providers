---
aid: baker-hughes
url: https://raw.githubusercontent.com/api-evangelist/baker-hughes/refs/heads/main/apis.yml
name: Baker Hughes
description: Baker Hughes is an energy technology company providing solutions to energy and industrial customers worldwide. Their digital portfolio includes the Cordant industrial software platform for asset performance management, process optimization, and emissions management, along with the BHC3 AI Suite (in alliance with C3.ai) for enterprise AI applications in oil and gas. Baker Hughes operates across oilfield services, industrial equipment, and digital solutions segments globally.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy Technology
  - Industrial IoT
  - Oil And Gas
  - Asset Performance Management
  - Digital Energy
created: '2026-03-21'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: baker-hughes:cordant-platform
    name: Baker Hughes Cordant Industrial Platform
    description: Cordant is Baker Hughes' modular AI-enabled industrial enterprise software platform for asset performance management (APM), process optimization, and emissions management. It provides a digital thread across energy and industrial operations, connecting data, automating decision-making, and delivering predictive insights. Cordant offers APIs for integration with existing enterprise systems including OT/IT connectivity for asset data.
    humanURL: https://www.bakerhughes.com/cordant
    tags:
      - Asset Performance Management
      - Industrial IoT
      - Process Optimization
      - Emissions Management
    properties:
      - type: Documentation
        url: https://www.bakerhughes.com/cordant/platform
      - type: APIReference
        url: https://www.bakerhughes.com/cordant
  - aid: baker-hughes:bhc3-ai-suite
    name: Baker Hughes BHC3 AI Suite
    description: The BHC3 AI Suite is a joint product from Baker Hughes and C3.ai providing pre-built, configurable AI applications for the energy industry. Applications cover predictive maintenance, reliability, production optimization, inventory optimization, well placement, well integrity, and yield optimization. The platform runs on Microsoft Azure and uses C3.ai's model-driven architecture enabling enterprise AI application development.
    humanURL: https://www.bakerhughes.com/bhc3
    tags:
      - Artificial Intelligence
      - Energy
      - Oil And Gas
      - Predictive Maintenance
    properties:
      - type: Documentation
        url: https://www.bakerhughes.com/bhc3
      - type: APIReference
        url: https://www.bakerhughes.com/ai-bakerhughesc3ai/
common:
  - type: Website
    url: https://www.bakerhughes.com
  - type: Portal
    url: https://www.bakerhughes.com/company/digital
  - type: Blog
    url: https://www.bakerhughes.com/company/news
  - type: Support
    url: https://www.bakerhughes.com/contact-us
  - type: PrivacyPolicy
    url: https://www.bakerhughes.com/privacy-policy
  - type: TermsOfService
    url: https://www.bakerhughes.com/terms-and-conditions
  - type: SpectralRules
    url: rules/baker-hughes-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/baker-hughes-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/baker-hughes-industrial-platform.yaml
  - type: JSON-LD
    url: json-ld/baker-hughes-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Asset Performance Management
        description: AI-powered predictive maintenance and reliability for industrial assets.
      - name: Process Optimization
        description: Real-time process monitoring and optimization for energy and industrial operations.
      - name: Emissions Management
        description: Track, measure, and reduce greenhouse gas emissions across operations.
      - name: Enterprise AI Applications
        description: Pre-built AI applications for oil and gas use cases including production optimization and well integrity.
      - name: OT/IT Integration
        description: Connectivity between operational technology (OT) sensor data and enterprise IT systems.
      - name: Digital Thread
        description: Connected data fabric linking assets, processes, and enterprise systems across operations.
      - name: Well Integrity Monitoring
        description: Continuous monitoring of well barrier status and integrity for safe operations.
      - name: Production Optimization
        description: AI-driven optimization of oil and gas production rates from well and reservoir data.
  - name: UseCases
    type: UseCases
    data:
      - name: Predictive Maintenance
        description: Predict equipment failures before they occur to reduce unplanned downtime and maintenance costs.
      - name: Production Optimization
        description: Optimize oil and gas production rates using AI-driven insights from well and reservoir data.
      - name: Sustainability Reporting
        description: Monitor and report on emissions, energy consumption, and ESG metrics across facilities.
      - name: Industrial Process Control
        description: Automate and optimize industrial processes using real-time sensor data and AI recommendations.
      - name: Well Lifecycle Management
        description: Monitor and optimize oil and gas well performance across the full production lifecycle.
      - name: Inventory Optimization
        description: Optimize spare parts inventory for maintenance operations using AI demand forecasting.
  - name: Integrations
    type: Integrations
    data:
      - name: Microsoft Azure
        description: BHC3 AI Suite is optimized to run on Microsoft Azure cloud infrastructure.
      - name: C3.ai
        description: Strategic AI alliance providing enterprise AI platform capabilities for BHC3.
      - name: SAP
        description: Integration with SAP ERP for asset and maintenance management data.
      - name: OSIsoft PI
        description: Integration with OSIsoft PI data historian for real-time process data.
      - name: Maximo
        description: Integration with IBM Maximo asset management for work order lifecycle.
      - name: Honeywell
        description: Integration with Honeywell process control and DCS systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
