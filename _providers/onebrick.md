---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://sandbox.onebrick.io
  baseurl_source: declared
  description: 'Brick API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Brick API
  slug: onebrick-api
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/onebrick/well-known/onebrick-onebrick-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onebrick-onebrick-security.txt
- group: commercial
  href: https://artifacts.apis.io/onebrick/plans/onebrick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onebrick-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/onebrick/rules/onebrick-rules.yml
  title: ''
  type: Spectral
  url: rules/onebrick-rules.yml
- group: design
  href: https://artifacts.apis.io/onebrick/json-ld/onebrick-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/onebrick-context.jsonld
- group: design
  href: https://artifacts.apis.io/onebrick/vocabulary/onebrick-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/onebrick-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/onebrick/data-model/onebrick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onebrick-data-model.yml
- group: design
  href: https://artifacts.apis.io/onebrick/conventions/onebrick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onebrick-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.onebrick.io/bug-report
- group: auth
  href: https://artifacts.apis.io/onebrick/authentication/onebrick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onebrick-authentication.yml
- group: design
  href: https://artifacts.apis.io/onebrick/conformance/onebrick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onebrick-conformance.yml
- group: agent
  href: https://artifacts.apis.io/onebrick/llms/onebrick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onebrick-llms.txt
- group: auth
  href: https://artifacts.apis.io/onebrick/well-known/onebrick-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onebrick-www-security.txt
- group: auth
  href: https://artifacts.apis.io/onebrick/well-known/onebrick-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onebrick-security.txt
- group: agent
  href: https://artifacts.apis.io/onebrick/well-known/onebrick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onebrick-well-known.yml
- group: other
  href: https://artifacts.apis.io/onebrick/hosts/onebrick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onebrick-hosts.yml
- group: other
  href: https://artifacts.apis.io/onebrick/vendors/onebrick-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onebrick-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onebrick.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onebrick.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onebrick.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onebrick.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onebrick.io/transaction-history/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onebrick.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.onebrick.io</option
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onebrick.io/api/authentication
- group: auth
  href: https://artifacts.apis.io/onebrick/security/onebrick-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/onebrick-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/onebrick/security/onebrick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onebrick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onebrick.io/
created: '2026-10-21'
description: Brick builds payment infrastructure for modern money movement across Southeast Asia, starting with payouts and payment acceptance in Indonesia. It offers APIs for payments, payouts, compliance, and financial services, targeting businesses and developers seeking seamless integration of modern payment solutions in the region.
image: https://www.onebrick.io/images/og.png
json_schemas:
- name: GetV2PaymentsAuthTokenResponse
  property_count: 4
  slug: onebrick-get-v2-payments-auth-token-response
- name: GetV2PaymentsGsBalanceResponse
  property_count: 4
  slug: onebrick-get-v2-payments-gs-balance-response
- name: GetV2PaymentsGsGetTopUpHistoryResponse
  property_count: 20
  slug: onebrick-get-v2-payments-gs-get-top-up-history-response
- name: GetV2PaymentsGsLedgerResponse
  property_count: 4
  slug: onebrick-get-v2-payments-gs-ledger-response
- name: GetV2PaymentsGsTopUpBankListResponse
  property_count: 4
  slug: onebrick-get-v2-payments-gs-top-up-bank-list-response
- name: PostV2PaymentsGsAcceptanceEwalletRequest
  property_count: 4
  slug: onebrick-post-v2-payments-gs-acceptance-ewallet-request
jsonld:
- class_count: 7
  name: Onebrick Context
  property_count: 16
  slug: onebrick-context
layout: provider
modified: '2026-10-21'
name: Brick
nav: Providers
network: true
overview: 'Brick is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Southeast Asia, and B2B.


  The Brick catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Brick''s developer surface includes authentication, pricing, getting-started guide, documentation, API reference, and 22 more developer resources.'
plans:
- name: Onebrick Plans Pricing
  plan_count: 3
  slug: onebrick-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Brick API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: onebrick-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 33.3
    contract_quality: 26.6
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 43.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/onebrick/onebrick-2026-11-03T140554.png
security:
- kind: authentication
  name: Onebrick Authentication
  slug: onebrick-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onebrick Domain Security
  slug: onebrick-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onebrick Vulnerability Disclosure
  slug: onebrick-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: onebrick
tags:
- Fintech
- Payments
- Southeast Asia
- B2B
website: https://onebrick.io/
---
