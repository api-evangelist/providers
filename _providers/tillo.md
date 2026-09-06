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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tillo Agentic Access
  operation_count: 12
  slug: tillo-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://app.tillo.io
  baseurl_source: declared
  description: Balance checking operations
  name: Tillo Balance API
  slug: tillo-balance-api
- baseURL: https://app.tillo.io
  baseurl_source: declared
  description: Brand catalog and information
  name: Tillo Brands API
  slug: tillo-brands-api
- baseURL: https://app.tillo.io
  baseurl_source: declared
  description: Digital gift card issuance
  name: Tillo Digital Cards API
  slug: tillo-digital-cards-api
- baseURL: https://app.tillo.io
  baseurl_source: declared
  description: Float account management
  name: Tillo Float API
  slug: tillo-float-api
- baseURL: https://app.tillo.io
  baseurl_source: declared
  description: Order management and status
  name: Tillo Orders API
  slug: tillo-orders-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tillo Gift Card Balance API
  slug: open-tillo-balance-api
- collection_type: open
  name: Tillo Gift Card Balance Brands API
  slug: open-tillo-brands-api
- collection_type: open
  name: Tillo Gift Card Balance Digital Cards API
  slug: open-tillo-digital-cards-api
- collection_type: open
  name: Tillo Gift Card Balance Float API
  slug: open-tillo-float-api
- collection_type: open
  name: Tillo Gift Card API
  slug: open-tillo-gift-card
- collection_type: open
  name: Tillo Gift Card Balance Orders API
  slug: open-tillo-orders-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tilloops/tillo/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tillo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tillo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tillo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tillo
- group: company
  title: ''
  type: Website
  url: https://www.tillo.io/
- group: start
  title: ''
  type: Portal
  url: https://www.tillo.io/gift-card-api
- group: docs
  title: ''
  type: Documentation
  url: https://tillo.tech/v2_docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tillo.tech/v2_docs/getting_started.html
- group: auth
  title: ''
  type: Authentication
  url: https://tillo.tech/v2_docs/authentication.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tilloops
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tilloops/tillo
- group: company
  title: ''
  type: Blog
  url: https://www.tillo.io/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.tillo.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tillo.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tillo.io/legal
- group: build
  title: ''
  type: PostmanCollection
  url: https://api.tillo.tech/
- group: start
  title: ''
  type: Signup
  url: https://app.tillo.io/
created: '2025-02-08'
description: Tillo is an award-winning gift card API platform connecting businesses to 4,000+ global brands across 37 markets and 16 currencies. The REST API supports digital and physical gift card issuance, balance checking, float management, and brand catalog access. Authentication uses HMAC-SHA256 signatures.
examples:
- key_count: 2
  name: Tillo Issuedigitalcard Example
  slug: tillo-issueDigitalCard-example
- key_count: 2
  name: Tillo Listbrands Example
  slug: tillo-listBrands-example
finops:
- name: Tillo Finops
  service_category: API
  slug: tillo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tillo.png
json_schemas:
- name: Tillo Brand
  property_count: 12
  slug: tillo-brand
- name: Tillo Gift Card
  property_count: 11
  slug: tillo-gift-card
json_structures:
- name: Tillo Brand Structure
  property_count: 0
  slug: tillo-brand-structure
jsonld:
- class_count: 15
  name: Tillo Context
  property_count: 0
  slug: tillo-context
layout: provider
modified: '2026-05-19'
name: Tillo
nav: Providers
network: true
overview: 'Tillo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Brands API, Digital Cards API, and 2 more. Tagged areas include Finance, Gift Cards, Payments, Rewards, and Incentives.


  The Tillo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tillo''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Tillo Plans Pricing
  plan_count: 3
  slug: tillo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Tillo Rate Limits
  slug: tillo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tillo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tillo-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Tillo API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: tillo-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 60.8
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 39.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/tillo/refs/heads/main/screenshots/tillo-2026-06-20T195353.png
security:
- kind: authentication
  name: Tillo Authentication
  slug: tillo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tillo Domain Security
  slug: tillo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tillo
tags:
- Finance
- Gift Cards
- Payments
- Rewards
- Incentives
website: https://www.tillo.io/
---
