---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Stonex Agentic Access
  operation_count: 15
  slug: stonex-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 2
apis:
- description: The StoneX GF (GAIN Futures) API provides institutional-grade access to futures trading including market data, order management, account and position tracking, margin calculations, contract lookup, an
  name: StoneX GF Futures API
  slug: stonex-gf-api
- description: The StoneX Developer Storefront provides access to all StoneX API products with subscription keys, documentation, and developer resources for integrating with StoneX financial services.
  name: StoneX Developer Portal
  slug: stonex-developer-portal
- baseURL: https://api.clearing.stonex.com
  baseurl_source: spec
  description: Account information and management.
  name: StoneX Accounts API
  slug: stonex-accounts-api
- baseURL: https://api.clearing.stonex.com
  baseurl_source: spec
  description: OAuth 2.0 token management.
  name: StoneX Authentication API
  slug: stonex-authentication-api
- baseURL: https://api.clearing.stonex.com
  baseurl_source: spec
  description: Document retrieval and management.
  name: StoneX Documents API
  slug: stonex-documents-api
- baseURL: https://fx-api.payments.stonex.com
  baseurl_source: spec
  description: Foreign exchange rate queries.
  name: StoneX FX Rates API
  slug: stonex-fx-rates-api
- baseURL: https://fx-api.payments.stonex.com
  baseurl_source: spec
  description: Payment execution and management.
  name: StoneX Payments API
  slug: stonex-payments-api
- baseURL: https://api.clearing.stonex.com
  baseurl_source: spec
  description: Trade submission and management.
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/plans/stonex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stonex-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/rate-limits/stonex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stonex-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/finops/stonex-finops.yml
  title: ''
  type: FinOps
  url: finops/stonex-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/capabilities/stonex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stonex-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/agentic-access/stonex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stonex-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/security/stonex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stonex-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/security/stonex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stonex-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stonex/refs/heads/main/authentication/stonex-authentication.yml
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
- has_sources: true
  method: generated
  name: Stonex Finops
  primary_unit: ''
  service_category: Financial Services
  slug: stonex-finops
  template: false
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
overview: 'StoneX publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Documents API, and 5 more. Tagged areas include Finance, Financial Services, Payments, Clearing, and Futures.


  The StoneX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StoneX''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Stonex Plans Pricing
  plan_count: 1
  slug: stonex-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Stonex Rate Limits
  slug: stonex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: StoneX — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stonex-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 48
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
  composite: 30.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 55.5
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 31.7
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
    score: 20.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Financial Services
- Payments
- Clearing
- Futures
- Trading
- Risk Management
website: https://www.stonex.com
---
