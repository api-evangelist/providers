---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Wisdomtree Agentic Access
  operation_count: 35
  slug: wisdomtree-agentic-access
  summary_line: 35 operations · 9 acting
api_count: 2
apis:
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Accruals API from WisdomTree — 1 operation(s) for accruals.
  name: WisdomTree Accruals API
  slug: wisdomtree-accruals-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Dividend Payment Preferences API from WisdomTree — 4 operation(s) for dividend payment preferences.
  name: WisdomTree Dividend Payment Preferences API
  slug: wisdomtree-dividend-payment-preferences-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: WisdomTree DataSpan fund NAV, aggregates and accrual data.
  name: WisdomTree Fund Data API
  slug: wisdomtree-fund-data-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Orders API from WisdomTree — 17 operation(s) for orders.
  name: WisdomTree Orders API
  slug: wisdomtree-orders-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Organizations API from WisdomTree — 1 operation(s) for organizations.
  name: WisdomTree Organizations API
  slug: wisdomtree-organizations-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Statements API from WisdomTree — 2 operation(s) for statements.
  name: WisdomTree Statements API
  slug: wisdomtree-statements-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Users API from WisdomTree — 2 operation(s) for users.
  name: WisdomTree Users API
  slug: wisdomtree-users-api
- baseURL: https://app.wisdomtreeconnect.com
  baseurl_source: declared
  description: The Wallets API from WisdomTree — 5 operation(s) for wallets.
  name: WisdomTree Wallets API
  slug: wisdomtree-wallets-api
artifact_total: 20
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/agentic-access/wisdomtree-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wisdomtree-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/rules/wisdomtree-rules.yml
  title: ''
  type: Spectral
  url: rules/wisdomtree-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/json-ld/wisdomtree-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wisdomtree-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/vocabulary/wisdomtree-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wisdomtree-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/data-model/wisdomtree-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wisdomtree-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/conventions/wisdomtree-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/wisdomtree-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/conventions/wisdomtree-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wisdomtree-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/errors/wisdomtree-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wisdomtree-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/conformance/wisdomtree-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wisdomtree-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/hosts/wisdomtree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wisdomtree-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/vendors/wisdomtree-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wisdomtree-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/scopes/wisdomtree-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wisdomtree-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/authentication/wisdomtree-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wisdomtree-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wisdomtree/refs/heads/main/security/wisdomtree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wisdomtree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wisdomtree.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wisdomtreeconnect.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wisdomtreeconnect.com/
created: '2026-10-13'
description: WisdomTree is a global asset manager issuing ETFs and tokenized funds. Through WisdomTree Connect it offers an OAuth2-secured REST API for institutions to create subscription and redemption orders, manage wallets and track settlement of regulated tokenized assets, plus a DataSpan Fund Data API for NAV, aggregates, accruals and shares outstanding per fund ticker.
json_schemas:
- name: APIKeyCreateResponse
  property_count: 11
  slug: wisdomtree-apikey-create-response
- name: DividendPaymentPreferenceDetail
  property_count: 9
  slug: wisdomtree-dividend-payment-preference-detail
- name: OrderReviewResponse
  property_count: 30
  slug: wisdomtree-order-review-response
- name: Order
  property_count: 19
  slug: wisdomtree-order
- name: WTC
  property_count: 12
  slug: wisdomtree-wtc
- name: WTCOrderDetailsResponse
  property_count: 34
  slug: wisdomtree-wtcorder-details-response
jsonld:
- class_count: 93
  name: Wisdomtree Context
  property_count: 260
  slug: wisdomtree-context
layout: provider
modified: '2026-10-14'
name: WisdomTree
nav: Providers
network: true
overview: 'WisdomTree publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accruals API, Dividend Payment Preferences API, Fund Data API, and 5 more. Tagged areas include Company, Asset Management, ETFs, Tokenization, and Tokenized Funds.


  The WisdomTree catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WisdomTree''s developer surface includes authentication, documentation, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: WisdomTree API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: wisdomtree-rules
scopes:
- name: Wisdomtree Scopes
  scope_count: 3
  slug: wisdomtree-scopes
  summary_line: 3 scopes · password
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 51.9
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 22.2
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Wisdomtree Authentication
  slug: wisdomtree-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wisdomtree Domain Security
  slug: wisdomtree-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wisdomtree
tags:
- Company
- Asset Management
- ETFs
- Tokenization
- Tokenized Funds
- Financial Services
- Fund Data
website: https://www.wisdomtree.com
---
