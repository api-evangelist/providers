---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Papaya Global Agentic Access
  operation_count: 32
  slug: papaya-global-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api.papayaglobal.com/api/v1
  baseurl_source: declared
  description: Obtain access tokens for API authentication
  name: Papaya Global Authentication API
  slug: papaya-global-authentication-api
- baseURL: https://api.papayaglobal.com/api/v1
  baseurl_source: declared
  description: Manage payment recipients including individuals and organizations
  name: Papaya Global Beneficiaries API
  slug: papaya-global-beneficiaries-api
- baseURL: https://api.papayaglobal.com/api/v1
  baseurl_source: declared
  description: Manage payment groups to consolidate payment requests
  name: Papaya Global Groups API
  slug: papaya-global-groups-api
- baseURL: https://api.papayaglobal.com/api/v1
  baseurl_source: declared
  description: Manage payment instructions and execution
  name: Papaya Global Payments API
  slug: papaya-global-payments-api
- baseURL: https://api.papayaglobal.com/api/v1
  baseurl_source: declared
  description: Manage organizational wallets for payment funding
  name: Papaya Global Wallets API
  slug: papaya-global-wallets-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Papaya Global Workforce Payments Authentication API
  slug: open-papaya-global-authentication-api
- collection_type: open
  name: Papaya Global Workforce Payments Authentication Beneficiaries API
  slug: open-papaya-global-beneficiaries-api
- collection_type: open
  name: Papaya Global Workforce Payments Authentication Groups API
  slug: open-papaya-global-groups-api
- collection_type: open
  name: Papaya Global Workforce Authentication Payments API
  slug: open-papaya-global-payments-api
- collection_type: open
  name: Papaya Global Workforce Payments Authentication Wallets API
  slug: open-papaya-global-wallets-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/papaya-global-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/papaya-global-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/papaya-global-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.papayaglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.papayaglobal.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/papayaglobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/papaya-global
- group: company
  title: ''
  type: Blog
  url: https://www.papayaglobal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.papayaglobal.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/papaya-global-status
- group: other
  title: ''
  type: X
  url: https://twitter.com/Papaya_Global
- group: commercial
  title: ''
  type: Plans
  url: plans/papaya-global-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/papaya-global-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/papaya-global-finops.yml
created: '2026-06-13'
description: Global payroll and workforce management platform with a REST API for managing international payroll, contractor payments, worker records, and compliance across 160+ countries.
examples:
- key_count: 4
  name: Create Beneficiary
  slug: create-beneficiary
- key_count: 4
  name: Create Payment
  slug: create-payment
- key_count: 4
  name: Obtain Token
  slug: obtain-token
finops:
- name: Papaya Global Finops
  service_category: ''
  slug: papaya-global-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/papaya-global.png
json_schemas:
- name: Beneficiary
  property_count: 13
  slug: beneficiary
- name: Payment
  property_count: 13
  slug: payment
- name: Wallet
  property_count: 9
  slug: wallet
jsonld:
- class_count: 8
  name: Papaya Global Context
  property_count: 39
  slug: papaya-global-context
layout: provider
modified: '2026-06-13'
name: Papaya Global
nav: Providers
network: true
overview: 'Papaya Global publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Beneficiaries API, Groups API, and 2 more. Tagged areas include Payroll, Global Workforce, HR, Payments, and Employer of Record.


  The Papaya Global catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Papaya Global''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Papaya Global Plans Pricing
  plan_count: 6
  slug: papaya-global-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Papaya Global Rate Limits
  slug: papaya-global-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Papaya Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: papaya-global-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 73.3
    catalog_earned_first_party: 0.0
    catalog_gap: 41.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 67.4
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/papaya-global/refs/heads/main/screenshots/papaya-global-2026-06-20T191348.png
security:
- kind: authentication
  name: Papaya Global Authentication
  slug: papaya-global-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Papaya Global Domain Security
  slug: papaya-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: papaya-global
tags:
- Payroll
- Global Workforce
- HR
- Payments
- Employer of Record
- Contractor Management
- Compliance
website: https://www.papayaglobal.com/
---
