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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Valueray Agentic Access
  operation_count: 1
  slug: valueray-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Aggregated technical, quantitative, and sentiment data for a single symbol.
  name: ValueRay Symbol Data API
  slug: valueray-symbol-data-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ValueRay Symbol Data API
  slug: open-valueray-symbol-data-api
- collection_type: open
  name: ValueRay Symbol Data API
  slug: open-valueray-symbol-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valueray-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/valueray-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valueray-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.valueray.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.valueray.com/api
- group: other
  title: ''
  type: FieldDefinitions
  url: https://www.valueray.com/prompts/_explanations.md
- group: other
  title: ''
  type: Screener
  url: https://www.valueray.com/presets/long-setups
- group: commercial
  title: ''
  type: Plans
  url: plans/valueray-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/valueray-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/valueray-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/valueray-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/valueray-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://www.valueray.com/llms.txt
created: '2026-05-06'
description: AI-ready financial data API for stocks and ETFs. ValueRay aggregates technical, quantitative, and sentiment data with risk metrics, peer percentiles, and market regime signals into AI/LLM-friendly responses optimized for agents that need explainable financial overviews of specific symbols.
examples:
- key_count: 2
  name: Valueray Getsymboldata Example
  slug: valueray-getSymbolData-example
finops:
- name: Valueray Finops
  service_category: Market Data
  slug: valueray-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valueray.png
json_schemas:
- name: ValueRay Symbol Data
  property_count: 23
  slug: valueray-symbol-data
json_structures:
- name: Valueray Symbol Data Structure
  property_count: 0
  slug: valueray-symbol-data-structure
jsonld:
- class_count: 76
  name: Valueray Context
  property_count: 1
  slug: valueray-context
layout: provider
modified: '2026-05-19'
name: ValueRay
nav: Providers
network: true
overview: 'ValueRay publishes 1 API on the [APIs.io](https://apis.io/) network: Symbol Data API. Tagged areas include AI/LLM, ETFs, Financial Data, Quantitative, and Stocks.


  The ValueRay catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ValueRay''s developer surface includes documentation and 12 more developer resources.'
plans:
- name: Valueray Plans Pricing
  plan_count: 2
  slug: valueray-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Valueray Rate Limits
  slug: valueray-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ValueRay API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: valueray-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: ValueRay API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 2
  slug: valueray-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 61.2
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valueray/refs/heads/main/screenshots/valueray-2026-06-20T200802.png
security:
- kind: domain-security
  name: Valueray Domain Security
  slug: valueray-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Valueray Vulnerability Disclosure
  slug: valueray-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: valueray
tags:
- AI/LLM
- ETFs
- Financial Data
- Quantitative
- Stocks
- Technical Analysis
website: https://www.valueray.com/
---
