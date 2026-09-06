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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Runa Agentic Access
  operation_count: 10
  slug: runa-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.runa.io/v2
  baseurl_source: declared
  description: Retrieve account balance by currency.
  name: Runa Balance API
  slug: runa-balance-api
- baseURL: https://api.runa.io/v2
  baseurl_source: declared
  description: Create, retrieve, list, and estimate digital reward orders.
  name: Runa Orders API
  slug: runa-orders-api
- baseURL: https://api.runa.io/v2
  baseurl_source: declared
  description: Browse the Runa product catalog by name, category, or country.
  name: Runa Products API
  slug: runa-products-api
- baseURL: https://api.runa.io/v2
  baseurl_source: declared
  description: Utility endpoints for connectivity testing.
  name: Runa Utilities API
  slug: runa-utilities-api
artifact_total: 28
collections:
- collection_type: postman
  name: Runa Payouts Balance API
  slug: postman-runa-balance-api
- collection_type: postman
  name: Runa Payouts Balance Orders API
  slug: postman-runa-orders-api
- collection_type: postman
  name: Runa Payouts Balance Products API
  slug: postman-runa-products-api
- collection_type: postman
  name: Runa Payouts Balance Utilities API
  slug: postman-runa-utilities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Runa Payouts Balance API
  slug: open-runa-balance-api
- collection_type: open
  name: Runa Payouts Balance Orders API
  slug: open-runa-orders-api
- collection_type: open
  name: Runa Payouts API
  slug: open-runa-payouts-api
- collection_type: open
  name: Runa Payouts Balance Products API
  slug: open-runa-products-api
- collection_type: open
  name: Runa Payouts Balance Utilities API
  slug: open-runa-utilities-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/runa/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runa-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runapayouts
- group: start
  title: ''
  type: Portal
  url: https://developer.runa.io/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.runa.io/docs/getting-an-api-key
- group: start
  title: ''
  type: Signup
  url: https://app.runa.io/
- group: start
  title: ''
  type: Sandbox
  url: https://developer.runa.io/docs/playground
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runa.io/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runa.io/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://runa.io/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.runa.io/llms.txt
created: '2025-02-08'
description: Runa is a global digital payouts platform that enables businesses to automate digital reward and gift card distribution through a single API. The platform provides access to over 5,000 gift cards and payout options across 190+ countries, supporting B2C payments, employee rewards, customer incentives, and loyalty programs. The Runa API supports synchronous and asynchronous order modes, balance management, product catalog browsing, and webhook-based event notifications for order completions.
examples:
- key_count: 2
  name: Runa Create Order Example
  slug: runa-create-order-example
- key_count: 2
  name: Runa Get Balance Example
  slug: runa-get-balance-example
finops:
- name: Runa Finops
  service_category: API
  slug: runa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runa.png
json_schemas:
- name: Runa Order
  property_count: 6
  slug: runa-order
json_structures:
- name: Runa Structure
  property_count: 0
  slug: runa-structure
jsonld:
- class_count: 5
  name: Runa Context
  property_count: 14
  slug: runa-context
layout: provider
modified: '2026-05-19'
name: Runa
nav: Providers
network: true
overview: 'Runa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Orders API, Products API, and 1 more. Tagged areas include Gift Cards, Rewards, Payments, Incentives, and Payouts.


  The Runa catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Runa''s developer surface includes authentication, developer portal, signup flow, sandbox, engineering blog, and 9 more developer resources.'
plans:
- name: Runa Plans Pricing
  plan_count: 3
  slug: runa-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Runa Rate Limits
  slug: runa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Runa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: runa-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Runa API Rules
  rule_count: 18
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 15
  slug: runa-spectral-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 67.2
    developer_ergonomics: 41.7
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 43.0
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
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runa/refs/heads/main/screenshots/runa-2026-06-20T193249.png
security:
- kind: authentication
  name: Runa Authentication
  slug: runa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Runa Domain Security
  slug: runa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Runa Trust Center
  slug: runa-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: runa
tags:
- Gift Cards
- Rewards
- Payments
- Incentives
- Payouts
website: https://developer.runa.io/
---
