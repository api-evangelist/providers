---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: DePay's Web3 API provides endpoints for payments, links, and token transfers.
  name: DePay API
  slug: depay-api
- baseURL: https://api.depay.com
  baseurl_source: declared
  description: 'Depay API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Depay API
  slug: depayapp-com-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/depayapp-com/rate-limits/depayapp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/depayapp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/depayapp-com/plans/depayapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/depayapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/depayapp-com/rules/depayapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/depayapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/depayapp-com/json-ld/depayapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/depayapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/depayapp-com/vocabulary/depayapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/depayapp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/depayapp-com/data-model/depayapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/depayapp-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/depayapp-com/authentication/depayapp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/depayapp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/depayapp-com/conformance/depayapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/depayapp-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/depayapp-com/hosts/depayapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depayapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/depayapp-com/vendors/depayapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/depayapp-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/depayapp-com/packages/depayapp-com-packages.yml
  title: ''
  type: SDKs
  url: packages/depayapp-com-packages.yml
- group: build
  href: https://artifacts.apis.io/depayapp-com/packages/depayapp-com-packages.yml
  title: ''
  type: Packages
  url: packages/depayapp-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/depayapp-com/security/depayapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depayapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://depay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://depay.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://depay.com/docs/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://depay.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://app.depay.com/
- group: company
  title: ''
  type: Blog
  url: https://depay.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DePayFi
- group: commercial
  title: ''
  type: Pricing
  url: https://depay.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://depay.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://depay.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.depay.com/
coverage:
  checked: '2026-10-29'
  detail: The DePay documentation is publicly readable but provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://depay.com/docs/apis/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Depay is a Swiss‑based crypto payments platform that enables businesses and developers to accept stablecoins, tokens, and other Web3 assets across multiple blockchains. It offers non‑custodial payment links, plugins for Shopify, WooCommerce, WordPress, and APIs for seamless integration. Founded in 2020 and backed by Techstars, DePay provides auto‑conversion, multi‑chain support, and a developer portal with comprehensive documentation.
image: https://depay.com/brand/DePay%20Logo.png
json_schemas:
- name: GetAppsCheckoutsShopifyResponse
  property_count: 1
  slug: depayapp-com-get-apps-checkouts-shopify-response
- name: GetAppsPaymentsShopifyIdResponse
  property_count: 12
  slug: depayapp-com-get-apps-payments-shopify-id-response
- name: GetLinksLinkidPaymentsResponse
  property_count: 12
  slug: depayapp-com-get-links-linkid-payments-response
- name: GetPaymentsShopifyIdResponse
  property_count: 12
  slug: depayapp-com-get-payments-shopify-id-response
- name: PostPaymentsDepayCallbackRequest
  property_count: 24
  slug: depayapp-com-post-payments-depay-callback-request
jsonld:
- class_count: 5
  name: Depayapp Com Context
  property_count: 25
  slug: depayapp-com-context
layout: provider
modified: '2026-10-29'
name: Depay
nav: Providers
network: true
overview: 'Depay is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cryptocurrency, Web3, and Fintech.


  The Depay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Depay''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Depayapp Com Plans Pricing
  plan_count: 1
  slug: depayapp-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Depayapp Com Rate Limits
  slug: depayapp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Depay API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: depayapp-com-rules
scopes:
- name: Depayapp Com Scopes
  scope_count: 0
  slug: depayapp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 36.9
    discoverability: 66.1
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.4
  provenance:
    conformance: derived
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
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/depayapp-com/depayapp-com-2026-11-03T130535.png
security:
- kind: authentication
  name: Depayapp Com Authentication
  slug: depayapp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Depayapp Com Domain Security
  slug: depayapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: depayapp-com
tags:
- Company
- Payments
- Cryptocurrency
- Web3
- Fintech
website: https://depay.com/
---
