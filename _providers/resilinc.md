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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
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
overview: 'Resilinc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Risk Management, Supplier Intelligence, Disruption Monitoring, and Artificial Intelligence.


  The Resilinc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Resilinc''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Resilinc Plans Pricing
  plan_count: 3
  slug: resilinc-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Resilinc Rate Limits
  slug: resilinc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Resilinc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: resilinc-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 25.0
    contract_quality: 24.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 24.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Artificial Intelligence
website: https://resilinc.ai/
---
