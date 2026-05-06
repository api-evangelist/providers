---
aid: aladdin-studio
url: https://raw.githubusercontent.com/api-evangelist/aladdin-studio/refs/heads/main/apis.yml
name: Aladdin Studio
tags:
  - Financial
  - Investment Management
  - Portfolio Analytics
  - Risk Management
  - Asset Management
  - BlackRock
  - Data Cloud
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: Aladdin Studio is BlackRock's developer platform enabling institutional investors, asset managers, and wealth managers to build custom solutions on top of the Aladdin investment operating system. APIs provide access to portfolio data, risk analytics, trading, investment research, and the Aladdin Data Cloud, supporting approximately $25 trillion in assets managed on the platform.
created: '2024-03-05'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aladdin-studio:graph-api
    name: Aladdin Graph API
    tags:
      - Portfolio Data
      - Investment Management
      - REST
    properties:
      - url: https://www.blackrock.com/aladdin/products/apis
        type: Documentation
      - url: https://www.blackrock.com/aladdin/products/apis
        type: APIReference
      - url: openapi/aladdin-studio-graph-openapi.yaml
        type: OpenAPI
      - url: json-schema/aladdin-studio-graph-portfolio-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-portfolio-list-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-position-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-position-list-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-factor-exposure-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-portfolio-risk-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-graph-security-schema.json
        type: JSONSchema
      - url: json-structure/aladdin-studio-graph-portfolio-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-graph-position-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-graph-portfolio-risk-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-graph-security-structure.json
        type: JSONStructure
      - url: examples/aladdin-studio-graph-portfolio-example.json
        type: Example
      - url: examples/aladdin-studio-graph-position-example.json
        type: Example
      - url: examples/aladdin-studio-graph-portfolio-risk-example.json
        type: Example
      - url: examples/aladdin-studio-graph-security-example.json
        type: Example
    humanURL: https://www.blackrock.com/aladdin/products/apis
    baseURL: https://api.blackrock.com/v1
    description: The Aladdin Graph API provides RESTful access to portfolio data, securities, positions, risk analytics, and other Aladdin platform capabilities. Powers the AladdinSDK Python client with OAuth and Basic Auth authentication.
  - aid: aladdin-studio:data-cloud-api
    name: Aladdin Data Cloud API
    tags:
      - Data Cloud
      - Snowflake
      - Analytics
    properties:
      - url: https://www.blackrock.com/aladdin/products/apis
        type: Documentation
      - url: openapi/aladdin-studio-data-cloud-openapi.yaml
        type: OpenAPI
      - url: json-schema/aladdin-studio-data-cloud-connection-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-data-cloud-query-request-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-data-cloud-query-result-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-data-cloud-dataset-schema.json
        type: JSONSchema
      - url: json-structure/aladdin-studio-data-cloud-connection-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-data-cloud-query-result-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-data-cloud-dataset-structure.json
        type: JSONStructure
      - url: examples/aladdin-studio-data-cloud-connection-example.json
        type: Example
      - url: examples/aladdin-studio-data-cloud-query-result-example.json
        type: Example
      - url: examples/aladdin-studio-data-cloud-dataset-example.json
        type: Example
    humanURL: https://www.blackrock.com/aladdin/products/apis
    baseURL: https://api.blackrock.com/adc/v1
    description: The Aladdin Data Cloud API provides access to Snowflake-based analytics data warehousing with OAuth and JWT authentication. Enables large-scale portfolio analytics and data science workflows using Snowflake connectors and Snowpark.
  - aid: aladdin-studio:trading-api
    name: Aladdin Trading API
    tags:
      - Trading
      - Order Management
      - Financial
    properties:
      - url: https://www.blackrock.com/aladdin/products/apis
        type: Documentation
      - url: openapi/aladdin-studio-trading-openapi.yaml
        type: OpenAPI
      - url: https://pypi.org/project/asdk-plugin-trading/
        type: SDK
        title: Python Trading Plugin
      - url: json-schema/aladdin-studio-trading-order-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-trading-order-request-schema.json
        type: JSONSchema
      - url: json-structure/aladdin-studio-trading-order-structure.json
        type: JSONStructure
      - url: examples/aladdin-studio-trading-order-example.json
        type: Example
    humanURL: https://www.blackrock.com/aladdin/products/apis
    baseURL: https://api.blackrock.com/trading/v1
    description: The Aladdin Trading API enables order management and trading workflow integration. Available as the asdk_plugin_trading Python package built on the AladdinSDK framework.
  - aid: aladdin-studio:investment-research-api
    name: Aladdin Investment Research API
    tags:
      - Investment Research
      - Analytics
      - Portfolio
    properties:
      - url: https://www.blackrock.com/aladdin/products/apis
        type: Documentation
      - url: openapi/aladdin-studio-investment-research-openapi.yaml
        type: OpenAPI
      - url: https://pypi.org/project/asdk-plugin-investment-research/
        type: SDK
        title: Python Investment Research Plugin
      - url: json-schema/aladdin-studio-investment-research-security-research-schema.json
        type: JSONSchema
      - url: json-schema/aladdin-studio-investment-research-portfolio-analytics-schema.json
        type: JSONSchema
      - url: json-structure/aladdin-studio-investment-research-security-research-structure.json
        type: JSONStructure
      - url: json-structure/aladdin-studio-investment-research-portfolio-analytics-structure.json
        type: JSONStructure
      - url: examples/aladdin-studio-investment-research-security-research-example.json
        type: Example
      - url: examples/aladdin-studio-investment-research-portfolio-analytics-example.json
        type: Example
    humanURL: https://www.blackrock.com/aladdin/products/apis
    baseURL: https://api.blackrock.com/research/v1
    description: The Aladdin Investment Research API provides access to research data, analyst insights, and quantitative analytics built on Aladdin's data infrastructure. Available as the asdk_plugin_investment_research Python package.
common:
  - url: https://www.blackrock.com/aladdin/products/apis
    type: Portal
  - url: https://www.blackrock.com/aladdin/products/aladdin-studio
    type: Documentation
  - url: https://github.com/blackrock
    type: GitHubOrganization
  - url: https://github.com/blackrock/aladdinsdk
    type: SDK
    title: Python SDK (AladdinSDK)
  - url: https://pypi.org/project/aladdinsdk/
    type: SDK
    title: Python SDK (PyPI)
  - url: https://github.com/blackrock/aladdinsdk-plugin-builder
    type: SDK
    title: Plugin Builder
  - url: rules/aladdin-studio-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/aladdin-studio-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/aladdin-studio-context.jsonld
    type: JSONLD
  - url: capabilities/shared/graph-api.yaml
    type: NaftikoCapability
    title: Aladdin Graph API Shared Capability
  - url: capabilities/shared/data-cloud-api.yaml
    type: NaftikoCapability
    title: Aladdin Data Cloud API Shared Capability
  - url: capabilities/portfolio-analytics.yaml
    type: NaftikoCapability
    title: Portfolio Analytics Workflow
  - type: Features
    data:
      - name: Portfolio Data Access
        description: Retrieve comprehensive portfolio data including positions, holdings, securities, and performance metrics across asset classes.
      - name: Risk Analytics
        description: Access Aladdin's institutional-grade risk analytics including factor exposures, VaR, scenario analysis, and stress testing across public and private markets.
      - name: Aladdin Data Cloud
        description: Snowflake-based data warehousing providing access to large-scale portfolio analytics with OAuth and JWT authentication supporting both Snowflake connectors and Snowpark.
      - name: Trading Integration
        description: Order management and trading workflow APIs enabling integration with Aladdin's trading platform for order creation, tracking, and execution.
      - name: Investment Research Access
        description: APIs for accessing investment research data, analyst insights, and quantitative analytics built on Aladdin's data infrastructure.
      - name: Long-Running Operations
        description: Support for long-running operation (LRO) patterns with configurable polling, enabling asynchronous processing of computationally intensive analytics requests.
      - name: Batch Processing
        description: Batch API support with sequential and parallel execution capabilities for processing large volumes of portfolio data operations efficiently.
      - name: Multi-Auth Support
        description: Flexible authentication supporting Basic Auth with API tokens, OAuth client credentials flow, OAuth refresh token flow, and Snowflake JWT for Data Cloud access.
      - name: Plugin Architecture
        description: Extensible SDK plugin architecture enabling domain-specific packages (trading, investment research) built on top of the core AladdinSDK.
      - name: Jupyter Notebook Integration
        description: Downloadable Python Jupyter Notebooks and code samples in multiple languages for rapid solution development and prototyping.
  - type: UseCases
    data:
      - name: Custom Portfolio Analytics
        description: Build bespoke portfolio analysis tools using Aladdin's risk and performance data to generate custom insights for investment teams.
      - name: Automated Risk Reporting
        description: Automate generation of risk reports, factor exposure summaries, and stress test results using Aladdin's risk analytics APIs.
      - name: Trading Workflow Automation
        description: Integrate Aladdin trading data into proprietary order management systems and automate trading workflow processes.
      - name: Investment Research Integration
        description: Connect internal research platforms to Aladdin's investment research data for unified analyst workflow tooling.
      - name: Data Science and Quantitative Research
        description: Access Aladdin Data Cloud from Snowflake-based data science environments for quantitative model development and backtesting.
      - name: Client Reporting Automation
        description: Build automated client reporting solutions pulling portfolio performance, risk, and holdings data from Aladdin APIs.
      - name: Multi-Asset Class Analytics
        description: Analyze portfolios across public equities, fixed income, alternatives, and private markets using Aladdin's unified data platform.
  - type: Integrations
    data:
      - name: Snowflake
        description: Native Aladdin Data Cloud integration with Snowflake for large-scale analytics, supporting both standard connectors and Snowpark for Python-based data science workflows.
      - name: Amazon Web Services
        description: Aladdin available on AWS infrastructure (general availability expected second half of 2026) complementing existing Azure deployment.
      - name: Microsoft Azure
        description: Primary cloud infrastructure for Aladdin platform, supporting enterprise deployments across institutional clients.
      - name: Preqin
        description: Private markets data integrated into Aladdin ecosystem following BlackRock's acquisition for alternatives and private market analytics.
      - name: Python Ecosystem
        description: First-class Python support via AladdinSDK on PyPI, with Jupyter Notebook examples and plugin architecture for domain extensions.
      - name: RepRisk
        description: ESG risk data integrated into Aladdin portfolio management for reputational and environmental risk analysis.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
