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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Grapes Finance Agentic Access
  operation_count: 12
  slug: grapes-finance-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Beneficiary management for third-party payouts
  name: Grapes Finance Contacts API
  slug: grapes-finance-contacts-api
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Identity verification for individuals and businesses
  name: Grapes Finance KYC API
  slug: grapes-finance-kyc-api
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Fiat-to-stablecoin, stablecoin-to-fiat, and payout orders
  name: Grapes Finance Orders API
  slug: grapes-finance-orders-api
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Vineyard Manager API for embedded client management
  name: Grapes Finance Organizations API
  slug: grapes-finance-organizations-api
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Account management for users controlling Grapes wallets
  name: Grapes Finance Users API
  slug: grapes-finance-users-api
- baseURL: https://api.demo.grapesfinance.com
  baseurl_source: declared
  description: Custodial and non-custodial cryptocurrency wallet operations
  name: Grapes Finance Wallets API
  slug: grapes-finance-wallets-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grapes Finance Contacts API
  slug: open-grapes-finance-contacts-api
- collection_type: open
  name: Grapes Finance Contacts KYC API
  slug: open-grapes-finance-kyc-api
- collection_type: open
  name: Grapes Finance Contacts Orders API
  slug: open-grapes-finance-orders-api
- collection_type: open
  name: Grapes Finance Contacts Organizations API
  slug: open-grapes-finance-organizations-api
- collection_type: open
  name: Grapes Finance Contacts Users API
  slug: open-grapes-finance-users-api
- collection_type: open
  name: Grapes Finance Contacts Wallets API
  slug: open-grapes-finance-wallets-api
- collection_type: open
  name: Grapes Finance API
  slug: open-grapes-finance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grapes-finance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grapes-finance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grapes-finance-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.grapesfinance.com/api-user-guide/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/grapes-finance-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/grapes-finance-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/grapes-finance-context.jsonld
- group: design
  title: ''
  type: Rules
  url: grapes-finance-rules.yml
created: '2025-02-24'
description: Grapes is an all-in-one embedded stablecoin onramp and offramp solution that simplifies and streamlines financial transactions. The API enables businesses and developers to integrate fiat-to-stablecoin and stablecoin-to-fiat transactions into their applications, services, and platforms, including buying and selling stablecoins such as QCAD and USDC with CAD and USD across Ethereum, Algorand, and Stellar networks.
finops:
- name: Grapes Finance Finops
  service_category: API
  slug: grapes-finance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grapes-finance.png
json_schemas:
- name: Grapes Finance Order
  property_count: 11
  slug: grapes-finance-order
jsonld:
- class_count: 10
  name: Grapes Finance Context
  property_count: 4
  slug: grapes-finance-context
layout: provider
modified: '2026-05-19'
name: Grapes Finance
nav: Providers
network: true
overview: 'Grapes Finance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, KYC API, Orders API, and 3 more. Tagged areas include Stablecoins, On-Ramp, Off-Ramp, Fiat, and Payments.


  The Grapes Finance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Grapes Finance''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Grapes Finance Plans Pricing
  plan_count: 3
  slug: grapes-finance-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Grapes Finance Rate Limits
  slug: grapes-finance-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Grapes Finance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: grapes-finance-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 50.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grapes-finance/refs/heads/main/screenshots/grapes-finance-2026-06-20T182322.png
security:
- kind: authentication
  name: Grapes Finance Authentication
  slug: grapes-finance-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Grapes Finance Domain Security
  slug: grapes-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grapes-finance
tags:
- Stablecoins
- On-Ramp
- Off-Ramp
- Fiat
- Payments
- Cryptocurrency
- Embedded Finance
---
