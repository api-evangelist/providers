---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Trioptima Agentic Access
  operation_count: 8
  slug: trioptima-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 5
apis:
- description: Trioptima triResolve is a web-based portfolio reconciliation service for OTC derivatives. It normalizes trade data, reconciles all fields using an algorithmic match engine, and provides break workflow
  name: Trioptima triResolve Portfolio Reconciliation
  slug: triresolve
- description: Compression cycle discovery and management
  name: Trioptima Cycles API
  slug: trioptima-cycles-api
- description: Compression results and reports
  name: Trioptima Results API
  slug: trioptima-results-api
- description: Risk data submission and delta ladder management
  name: Trioptima Risk API
  slug: trioptima-risk-api
- description: Trade data submission and retrieval
  name: Trioptima Trades API
  slug: trioptima-trades-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trioptima triReduce Cycles API
  slug: open-trioptima-cycles-api
- collection_type: open
  name: Trioptima triReduce Cycles Results API
  slug: open-trioptima-results-api
- collection_type: open
  name: Trioptima triReduce Cycles Risk API
  slug: open-trioptima-risk-api
- collection_type: open
  name: Trioptima triReduce Cycles Trades API
  slug: open-trioptima-trades-api
- collection_type: open
  name: Trioptima triReduce API
  slug: open-trioptima-trireduce-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trioptima-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trioptima-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trioptima-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trioptima-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://osttra.com/insights/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trioptima
- group: company
  title: ''
  type: Website
  url: https://osttra.com
- group: company
  title: ''
  type: Website
  url: https://osttra.com/login/trioptima-logins/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cmegroup.com/education/brochures-and-handbooks/trireduce-api
- group: docs
  title: ''
  type: Documentation
  url: https://osttra.com/services/optimisation/portfolio-compression/
- group: docs
  title: ''
  type: Documentation
  url: https://osttra.com/services/trade-lifecycle-services/portfolio-reconciliation/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TriOptima
- group: build
  title: ''
  type: GitHub
  url: https://github.com/osttra
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/trioptima-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trioptima-compression-cycle-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trioptima-trade-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trioptima-vocabulary.yml
created: '2026-05-03'
description: Trioptima provides post-trade infrastructure services for the OTC derivatives market, including portfolio compression (triReduce), portfolio reconciliation (triResolve), and risk mitigation services. Originally founded in 2000, Trioptima became part of OSTTRA in 2021 — a joint venture combining MarkitServ, Traiana, TriOptima, and Reset to form a comprehensive post-trade services platform. Trioptima's services help financial institutions reduce counterparty risk, optimize capital requirements, and meet regulatory obligations across interest rate, credit, FX, and equity derivatives.
examples:
- key_count: 2
  name: Trioptima Get Cycle Results Example
  slug: trioptima-get-cycle-results-example
- key_count: 2
  name: Trioptima List Compression Cycles Example
  slug: trioptima-list-compression-cycles-example
- key_count: 2
  name: Trioptima Submit Cycle Trades Example
  slug: trioptima-submit-cycle-trades-example
features:
- name: Portfolio Compression (triReduce)
- name: Portfolio Reconciliation (triResolve)
- name: Collateral Management (triResolve Margin)
- name: Risk Mitigation
- name: Multilateral Compression
- name: Bilateral Compression
- name: Cleared IRS Compression
- name: Credit Default Swap Compression
- name: FX Forward Compression
- name: Break Workflow Management
- name: Dispute Resolution
- name: SWIFT Integration
- name: SFTP Data Transfer
- name: OAuth 2.0 Authentication
finops:
- name: Trioptima Finops
  service_category: API
  slug: trioptima-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trioptima.png
integrations:
- name: SWIFT
- name: CLS (FX compression)
- name: LCH
- name: CME Clearing
- name: Eurex
- name: Bloomberg
- name: Traiana
- name: MarkitServ
json_schemas:
- name: Trioptima Compression Cycle
  property_count: 10
  slug: trioptima-compression-cycle
- name: Trioptima Trade
  property_count: 10
  slug: trioptima-trade
json_structures:
- name: Trioptima Compression Cycle Structure
  property_count: 0
  slug: trioptima-compression-cycle-structure
jsonld:
- class_count: 16
  name: Trioptima Context
  property_count: 17
  slug: trioptima-context
layout: provider
modified: '2026-05-19'
name: Trioptima
nav: Providers
network: true
overview: 'Trioptima publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cycles API, Results API, Risk API, and 1 more. Tagged areas include CME Group, Derivatives, Financial-Services, OSTTRA, and Portfolio Compression.


  The Trioptima catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trioptima''s developer surface includes authentication, engineering blog, documentation, GitHub presence, and 13 more developer resources.'
plans:
- name: Trioptima Plans Pricing
  plan_count: 3
  slug: trioptima-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Trioptima Rate Limits
  slug: trioptima-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trioptima API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trioptima-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Trioptima API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: trioptima-rules
scopes:
- name: Trioptima Scopes
  scope_count: 2
  slug: trioptima-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 39.8
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 65.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trioptima/refs/heads/main/screenshots/trioptima-2026-06-20T195722.png
security:
- kind: authentication
  name: Trioptima Authentication
  slug: trioptima-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Trioptima Domain Security
  slug: trioptima-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trioptima
solutions:
- name: Interest Rate Derivatives Post-Trade
- name: Credit Derivatives Post-Trade
- name: FX Derivatives Post-Trade
- name: Regulatory Compliance (EMIR, Dodd-Frank)
- name: Capital Optimization
- name: Counterparty Risk Reduction
tags:
- CME Group
- Derivatives
- Financial-Services
- OSTTRA
- Portfolio Compression
- Post-Trade Services
- Reconciliation
- Risk Management
website: https://osttra.com
---
