---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The Resilinc REST API provides programmatic access to supply chain risk data including supplier information, disruption events, risk assessments, and mitigation planning data. The API enables integrat
  name: Resilinc API
  slug: resilinc
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resilinc-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resilinc-corp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resilinc
- group: company
  title: ''
  type: Website
  url: https://resilinc.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://resilinc.ai/solutions/developer-api/
- group: company
  title: ''
  type: About
  url: https://resilinc.ai/about/
- group: other
  title: ''
  type: Products
  url: https://resilinc.ai/products/agentic-supply-chain-risk-management/
- group: other
  title: ''
  type: SupplyChainRisk
  url: https://resilinc.ai/solutions/supply-chain-risk-management/
- group: auth
  title: ''
  type: Compliance
  url: https://resilinc.ai/solutions/supply-chain-compliance/
- group: company
  title: ''
  type: Blog
  url: https://resilinc.ai/blog/
- group: other
  title: ''
  type: AzureMarketplace
  url: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/resilinc.resilinc_ai
- group: build
  title: ''
  type: SnowflakeIntegration
  url: https://resilinc.ai/blog/resilincs-agentic-ai-supply-chain-risk-platform-now-available-on-microsoft-azure-marketplace/
- group: build
  title: ''
  type: ParabolaIntegration
  url: https://parabola.io/parabolas-apis/parabolas-resilinc-api
- group: agent
  title: ''
  type: LlmsText
  url: https://resilinc.ai/llms.txt
created: '2025-03-01'
description: Resilinc is a cloud/SaaS-based supply chain risk management platform that provides REST APIs for accessing supply chain data, disruption events, supplier risk assessments, and mitigation planning. The platform offers real-time visibility into global supply chain disruptions, AI-powered risk analysis, and integrations with ERP systems, Snowflake, and Microsoft Azure. Resilinc serves enterprise customers with agentic AI capabilities for autonomous supply chain resilience.
examples:
- key_count: 3
  name: Resilinc Disruption Event Example
  slug: resilinc-disruption-event-example
finops:
- name: Resilinc Finops
  service_category: API
  slug: resilinc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resilinc.png
json_schemas:
- name: Resilinc Disruption Event
  property_count: 13
  slug: resilinc-disruption-event
- name: Resilinc Supplier
  property_count: 13
  slug: resilinc-supplier
json_structures:
- name: Resilinc Supplier Structure
  property_count: 0
  slug: resilinc-supplier-structure
jsonld:
- class_count: 14
  name: Resilinc Context
  property_count: 0
  slug: resilinc-context
layout: provider
modified: '2026-05-02'
name: Resilinc
nav: Providers
network: true
overview: 'Resilinc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Risk Management, Supplier Intelligence, Disruption Monitoring, and AI.


  The Resilinc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Resilinc''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Resilinc Plans Pricing
  plan_count: 3
  slug: resilinc-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Resilinc Rate Limits
  slug: resilinc-rate-limits
rules:
- name: Resilinc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: resilinc-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 34.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 41.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resilinc/refs/heads/main/screenshots/resilinc-2026-06-20T192948.png
security:
- kind: domain-security
  name: Resilinc Domain Security
  slug: resilinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resilinc
tags:
- Supply Chain
- Risk Management
- Supplier Intelligence
- Disruption Monitoring
- AI
website: https://resilinc.ai/
---
