---
aid: resilinc
name: Resilinc
description: Resilinc is a cloud/SaaS-based supply chain risk management platform that provides REST APIs for accessing supply chain data, disruption events, supplier risk assessments, and mitigation planning. The platform offers real-time visibility into global supply chain disruptions, AI-powered risk analysis, and integrations with ERP systems, Snowflake, and Microsoft Azure. Resilinc serves enterprise customers with agentic AI capabilities for autonomous supply chain resilience.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Supply Chain
  - Risk Management
  - Supplier Intelligence
  - Disruption Monitoring
  - AI
url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: resilinc:resilinc
    name: Resilinc API
    description: The Resilinc REST API provides programmatic access to supply chain risk data including supplier information, disruption events, risk assessments, and mitigation planning data. The API enables integration with ERP systems, analytics platforms, and custom applications for offline analysis and real-time supply chain monitoring.
    humanURL: https://resilinc.ai/solutions/developer-api/
    tags:
      - Supply Chain
      - Risk Management
      - Suppliers
      - Events
      - Disruptions
      - Mitigation
    properties:
      - type: Documentation
        url: https://resilinc.ai/solutions/developer-api/
      - type: About
        url: https://resilinc.ai/about/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/json-schema/resilinc-supplier-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/json-schema/resilinc-disruption-event-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/json-structure/resilinc-supplier-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/json-ld/resilinc-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/vocabulary/resilinc-vocabulary.yml
    contact:
      - FN: Resilinc
        url: https://resilinc.ai/contact/
common:
  - type: Website
    url: https://resilinc.ai/
  - type: Documentation
    url: https://resilinc.ai/solutions/developer-api/
  - type: About
    url: https://resilinc.ai/about/
  - type: Products
    url: https://resilinc.ai/products/agentic-supply-chain-risk-management/
  - type: SupplyChainRisk
    url: https://resilinc.ai/solutions/supply-chain-risk-management/
  - type: Compliance
    url: https://resilinc.ai/solutions/supply-chain-compliance/
  - type: Blog
    url: https://resilinc.ai/blog/
  - type: AzureMarketplace
    url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/resilinc.resilinc_ai
  - type: SnowflakeIntegration
    url: https://resilinc.ai/blog/resilincs-agentic-ai-supply-chain-risk-platform-now-available-on-microsoft-azure-marketplace/
  - type: ParabolaIntegration
    url: https://parabola.io/parabolas-apis/parabolas-resilinc-api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
