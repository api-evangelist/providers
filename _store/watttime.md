---
aid: watttime
name: WattTime
description: WattTime is a nonprofit organization that provides real-time, forecast, and historical data for electric grids around the world, enabling carbon-aware computing and clean energy procurement decisions. The WattTime API delivers marginal emissions data (CO2 MOER), health damage signals, average emissions rates, and renewable energy forecasts for 342 grid regions across 210 countries and territories. Developers and organizations use the API to schedule workloads during low-carbon windows, measure actual emissions reductions from clean energy procurement, and meet sustainability reporting requirements.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/watttime/refs/heads/main/apis.yml
tags:
  - Emissions
  - Climate
  - Carbon
  - Energy
  - Electricity Grid
  - Sustainability
  - Clean Energy
created: '2025-05-02'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: watttime:watttime
    name: WattTime API
    description: The WattTime Data API v3 provides access to real-time, forecast, and historical marginal emissions data for electric grids worldwide. Key signals include CO2 MOER (Marginal Operating Emissions Rate), health damage estimates, and CO2 AOER (Average Operating Emissions Rate). The API covers 342 grid regions in 210 countries and territories, with real-time data updated every five minutes via the forecast endpoint.
    humanURL: https://docs.watttime.org/
    baseURL: https://api.watttime.org/v3
    tags:
      - Emissions
      - Carbon
      - Electricity Grid
      - Marginal Emissions
      - Forecasting
      - Climate
    properties:
      - type: Documentation
        url: https://docs.watttime.org/
      - type: Documentation
        url: https://legacy-docs.watttime.org/
        title: Legacy API v2 Documentation
      - type: OpenAPI
        url: openapi/watttime-openapi.yml
      - type: JSONSchema
        url: json-schema/watttime-data-point-schema.json
        title: Data Point Schema
      - type: JSONSchema
        url: json-schema/watttime-data-response-schema.json
        title: Data Response Schema
      - type: JSONSchema
        url: json-schema/watttime-forecast-response-schema.json
        title: Forecast Response Schema
      - type: JSONSchema
        url: json-schema/watttime-region-response-schema.json
        title: Region Response Schema
      - type: JSONStructure
        url: json-structure/watttime-data-point-structure.json
        title: Data Point Structure
      - type: JSONStructure
        url: json-structure/watttime-data-response-structure.json
        title: Data Response Structure
  - aid: watttime:watttime-python-client
    name: WattTime Python Client
    description: Official Python SDK for the WattTime API providing simplified access to real-time, forecast, and historical emissions data.
    humanURL: https://github.com/WattTime/watttime-python-client
    tags:
      - Python
      - SDK
      - Client Library
    properties:
      - type: SDK
        url: https://pypi.org/project/watttime/
        title: Python SDK (PyPI)
      - type: CodeExamples
        url: https://github.com/WattTime/watttime-python-client
        title: Python Client Examples
common:
  - type: Portal
    url: https://watttime.org/
    title: WattTime Website
  - type: Documentation
    url: https://docs.watttime.org/
    title: API Documentation
  - type: ReleaseNotes
    url: https://watttime.org/data-science/release-notes/
    title: API Release Notes
  - type: StatusPage
    url: http://status.watttime.org/
    title: API Status Page
  - type: GitHubOrganization
    url: https://github.com/WattTime
    title: WattTime GitHub Organization
  - type: Support
    url: mailto:support@watttime.org
    title: Support Email
  - type: SpectralRules
    url: rules/watttime-spectral-rules.yml
    title: WattTime Spectral Rules
  - type: NaftikoCapability
    url: capabilities/carbon-aware-computing.yaml
    title: Carbon-Aware Computing Capability
  - type: Vocabulary
    url: vocabulary/watttime-vocabulary.yml
    title: WattTime Vocabulary
  - type: JSON-LD
    url: json-ld/watttime-context.jsonld
    title: WattTime JSON-LD Context
  - type: Features
    data:
      - name: Real-Time Marginal Emissions
        description: CO2 MOER signal providing real-time marginal carbon intensity for local grid regions, updated every 5 minutes via the forecast endpoint.
      - name: Emissions Forecasting
        description: 24-72 hour ahead emissions forecasts enabling applications to schedule energy-intensive workloads during low-carbon grid windows.
      - name: Historical Data Access
        description: Historical MOER data available for up to 32 days via the data endpoint, and multi-year historical datasets downloadable as CSV files.
      - name: Health Damage Signal
        description: Estimates the damage to human life and health caused by emissions from electricity generation based on time and location of consumption.
      - name: Global Grid Coverage
        description: Coverage across 342 grid regions in 210 countries and territories, including North America, Europe, and global expansion with synthetic demand proxy models.
      - name: Grid Region Discovery
        description: Identify the relevant balancing authority for any geographic coordinates and retrieve the list of accessible grid regions.
      - name: Model Versioning
        description: Date-based model versioning (e.g., 2026-03-01) allowing unique versions per region and signal for reproducibility and comparison.
  - type: UseCases
    data:
      - name: Carbon-Aware Computing
        description: Technology companies and cloud providers schedule compute workloads, data transfers, and batch jobs to run during periods of low marginal carbon intensity.
      - name: Clean Energy Procurement
        description: Organizations measure the actual emissions reductions from renewable energy procurement and power purchase agreements using marginal emissions data.
      - name: Sustainability Reporting
        description: Enterprises report Scope 2 emissions more accurately using marginal emissions rates rather than average grid emission factors.
      - name: Smart Building Optimization
        description: Building energy management systems shift heating, cooling, and EV charging to low-emission grid windows to reduce carbon footprint.
      - name: Grid Research and Analysis
        description: Researchers, utilities, and policy makers analyze historical and forecast emissions data to study grid decarbonization trends.
  - type: Integrations
    data:
      - name: Green Software Foundation
        description: WattTime provides the carbon intensity data underlying the Green Software Foundation's Software Carbon Intensity (SCI) specification.
      - name: Climate TRACE
        description: WattTime contributes emissions data and modeling to the Climate TRACE global emissions inventory.
      - name: Impact Framework
        description: Official Green Software Foundation Impact Framework plugin available for integrating WattTime data into software sustainability measurements.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
