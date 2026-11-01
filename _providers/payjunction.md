---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: PayJunction offers a payment processing API suite covering transactions, recurring billing, ACH, and card‑on‑file capabilities. Documentation and a sandbox are provided via the developer portal.
  name: PayJunction API
  slug: payjunction-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/payjunction/plans/payjunction-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payjunction-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/payjunction/conformance/payjunction-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payjunction-conformance.yml
- group: auth
  href: https://artifacts.apis.io/payjunction/well-known/payjunction-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payjunction-status-security.txt
- group: agent
  href: https://artifacts.apis.io/payjunction/well-known/payjunction-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payjunction-well-known.yml
- group: other
  href: https://artifacts.apis.io/payjunction/hosts/payjunction-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payjunction-hosts.yml
- group: other
  href: https://artifacts.apis.io/payjunction/vendors/payjunction-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payjunction-vendors.yml
- group: build
  href: https://artifacts.apis.io/payjunction/packages/payjunction-packages.yml
  title: ''
  type: SDKs
  url: packages/payjunction-packages.yml
- group: build
  href: https://artifacts.apis.io/payjunction/packages/payjunction-packages.yml
  title: ''
  type: Packages
  url: packages/payjunction-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.payjunction.com/
- group: auth
  href: https://artifacts.apis.io/payjunction/security/payjunction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payjunction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payjunction.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.payjunction.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.payjunction.com/hc/en-us/articles/216477407-POST-transactions
- group: docs
  title: ''
  type: APIReference
  url: https://developer.payjunction.com/hc/en-us/articles/216477407-POST-transactions
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.payjunction.com/hc/en-us/articles/216477397-Development-Sandbox
- group: operate
  title: ''
  type: Support
  url: https://support.payjunction.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.payjunction.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PayJunction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.payjunction.com/payments/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payjunction.com/
created: '2026-10-27'
description: PayJunction provides payment processing solutions for businesses, offering a suite of APIs for transactions, recurring billing, ACH, and card‑on‑file capabilities. Their platform includes a developer portal with API documentation, sandbox environments, and integration guides for various industries such as veterinary, dental, and automotive.
json_schemas:
- name: GetDeposits88888888444444444444CcccccccccccResponse
  property_count: 11
  slug: payjunction-get-deposits88888888444444444444-cccccccccccc-response
- name: GetSettlementsSettlementidResponse
  property_count: 6
  slug: payjunction-get-settlements-settlementid-response
- name: PostPlaidItemPublicTokenExchangeResponse
  property_count: 4
  slug: payjunction-post-plaid-item-public-token-exchange-response
- name: PostSmartterminalsSmartterminalidRequestPaymentResponse
  property_count: 1
  slug: payjunction-post-smartterminals-smartterminalid-request-payment-response
- name: PostTransactionsResponse
  property_count: 4
  slug: payjunction-post-transactions-response
- name: PutTransactionsResponse
  property_count: 11
  slug: payjunction-put-transactions-response
jsonld:
- class_count: 6
  name: Payjunction Context
  property_count: 34
  slug: payjunction-context
layout: provider
modified: '2026-10-27'
name: PayJunction
nav: Providers
network: true
overview: 'PayJunction is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, FinTech, API, SaaS, and B2B.


  The PayJunction catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PayJunction''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Payjunction Plans Pricing
  plan_count: 3
  slug: payjunction-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: PayJunction API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: payjunction-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 12.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 29.5
    contract_quality: 18.2
    developer_ergonomics: 52.4
    discoverability: 53.6
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Payjunction Domain Security
  slug: payjunction-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payjunction
tags:
- Payments
- FinTech
- API
- SaaS
- B2B
website: https://payjunction.com/
---
