---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Stonex Agentic Access
  operation_count: 15
  slug: stonex-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 8
apis:
- description: The StoneX GF (GAIN Futures) API provides institutional-grade access to futures trading including market data, order management, account and position tracking, margin calculations, contract lookup, an
  name: StoneX GF Futures API
  slug: stonex-gf-api
- description: The StoneX Developer Storefront provides access to all StoneX API products with subscription keys, documentation, and developer resources for integrating with StoneX financial services.
  name: StoneX Developer Portal
  slug: stonex-developer-portal
- description: Account information and management.
  name: StoneX Accounts API
  slug: stonex-accounts-api
- description: OAuth 2.0 token management.
  name: StoneX Authentication API
  slug: stonex-authentication-api
- description: Document retrieval and management.
  name: StoneX Documents API
  slug: stonex-documents-api
- description: Foreign exchange rate queries.
  name: StoneX FX Rates API
  slug: stonex-fx-rates-api
- description: Payment execution and management.
  name: StoneX Payments API
  slug: stonex-payments-api
- description: Trade submission and management.
  name: StoneX Trading API
  slug: stonex-trading-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StoneX Clearing Accounts API
  slug: open-stonex-accounts-api
- collection_type: open
  name: StoneX Clearing Accounts Authentication API
  slug: open-stonex-authentication-api
- collection_type: open
  name: StoneX Clearing API
  slug: open-stonex-clearing
- collection_type: open
  name: StoneX Clearing Accounts Documents API
  slug: open-stonex-documents-api
- collection_type: open
  name: StoneX Clearing Accounts FX Rates API
  slug: open-stonex-fx-rates-api
- collection_type: open
  name: StoneX Clearing Accounts Payments API
  slug: open-stonex-payments-api
- collection_type: open
  name: StoneX Payments API
  slug: open-stonex-payments
- collection_type: open
  name: StoneX Clearing Accounts Trading API
  slug: open-stonex-trading-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stonex-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stonex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stonex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stonex-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stonex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stonex-group
- group: company
  title: ''
  type: Website
  url: https://www.stonex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.stonex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stonex.com/documentation
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.stonex.com/llms.txt
created: '2026-05-02'
description: StoneX Group is a global financial services organization that provides execution, risk management, market intelligence, and post-trade services across asset classes and markets to institutional, commercial, and retail clients. StoneX offers REST APIs for payments, clearing, and futures trading with OAuth 2.0 authentication.
examples:
- key_count: 2
  name: Stonex Create Payment Example
  slug: stonex-create-payment-example
finops:
- name: Stonex Finops
  service_category: Financial Services
  slug: stonex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stonex.png
json_schemas:
- name: StoneX Clearing Account
  property_count: 6
  slug: stonex-clearing-account
- name: StoneX Payment
  property_count: 11
  slug: stonex-payment
json_structures:
- name: Stonex Payment Structure
  property_count: 0
  slug: stonex-payment-structure
jsonld:
- class_count: 25
  name: Stonex Context
  property_count: 0
  slug: stonex-context
layout: provider
modified: '2026-05-19'
name: StoneX
nav: Providers
network: true
overview: 'StoneX publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Documents API, and 3 more. Tagged areas include Finance, Financial-Services, Payments, Clearing, and Futures.


  The StoneX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StoneX''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Stonex Plans Pricing
  plan_count: 1
  slug: stonex-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Stonex Rate Limits
  slug: stonex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: StoneX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stonex-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: StoneX API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: stonex-rules
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 63.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/screenshots/stonex-2026-06-20T194558.png
security:
- kind: authentication
  name: Stonex Authentication
  slug: stonex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stonex Domain Security
  slug: stonex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stonex Vulnerability Disclosure
  slug: stonex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stonex
tags:
- Finance
- Financial-Services
- Payments
- Clearing
- Futures
- Trading
- Risk Management
website: https://www.stonex.com
---
