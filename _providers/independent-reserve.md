---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.3
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: WebSockets feed for order book and ticker data, documented with samples in the independentreserve/websockets GitHub repository.
  name: Independent Reserve WebSockets API
  slug: independent-reserve-websockets
- baseURL: https://api.independentreserve.com
  baseurl_source: declared
  description: The Private API from Independent Reserve — 18 operation(s) for private.
  name: Independent Reserve Private API
  slug: independent-reserve-private-api
- baseURL: https://api.independentreserve.com
  baseurl_source: declared
  description: The Public API from Independent Reserve — 18 operation(s) for public.
  name: Independent Reserve Public API
  slug: independent-reserve-public-api
artifact_total: 14
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/rules/independent-reserve-rules.yml
  title: ''
  type: Spectral
  url: rules/independent-reserve-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/json-ld/independent-reserve-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/independent-reserve-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/vocabulary/independent-reserve-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/independent-reserve-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/data-model/independent-reserve-data-model.yml
  title: ''
  type: DataModel
  url: data-model/independent-reserve-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/conventions/independent-reserve-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/independent-reserve-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/conventions/independent-reserve-conventions.yml
  title: ''
  type: Conventions
  url: conventions/independent-reserve-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/authentication/independent-reserve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/independent-reserve-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/lifecycle/independent-reserve-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/independent-reserve-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/lifecycle/independent-reserve-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/independent-reserve-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/errors/independent-reserve-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/independent-reserve-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/conformance/independent-reserve-conformance.yml
  title: ''
  type: Conformance
  url: conformance/independent-reserve-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/hosts/independent-reserve-hosts.yml
  title: ''
  type: Hosts
  url: hosts/independent-reserve-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/vendors/independent-reserve-vendors.yml
  title: ''
  type: Vendors
  url: vendors/independent-reserve-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/security/independent-reserve-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/independent-reserve-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/security/independent-reserve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/independent-reserve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.independentreserve.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.independentreserve.com/features/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.independentreserve.com/features/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.independentreserve.com/help/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.independentreserve.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.independentreserve.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.independentreserve.com/help/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.independentreserve.com/help/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.independentreserve.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.independentreserve.com/features/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/independentreserve
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/independent-reserve/refs/heads/main/postman/independent-reserve-api-postman-collection.json
  title: ''
  type: Postman
  url: postman/independent-reserve-api-postman-collection.json
- group: start
  title: ''
  type: Login
  url: https://portal.independentreserve.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://portal.independentreserve.com/mcp
  - status: 200
    url: https://www.independentreserve.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Independent Reserve is an Australian cryptocurrency exchange (also serving New Zealand and Singapore) for personal, business, trust and institutional clients. It publishes a JSON-over-HTTPS trading API at https://api.independentreserve.com with Public (unauthenticated GET) and Private (HMAC-SHA256 signed POST) methods for market data, orders, accounts, deposits and withdrawals, a request-for-quote (RFQ) surface, and a WebSockets market-data feed.
json_schemas:
- name: GetPublicGetmarketsummaryResponse
  property_count: 11
  slug: independent-reserve-get-public-getmarketsummary-response
- name: PostPrivateGetclosedfilledordersRequest
  property_count: 9
  slug: independent-reserve-post-private-getclosedfilledorders-request
- name: PostPrivateGetclosedordersRequest
  property_count: 9
  slug: independent-reserve-post-private-getclosedorders-request
- name: PostPrivateGetopenordersRequest
  property_count: 7
  slug: independent-reserve-post-private-getopenorders-request
- name: PostPrivateGetorderdetailsResponse
  property_count: 12
  slug: independent-reserve-post-private-getorderdetails-response
- name: PostPrivateGettransactionsRequest
  property_count: 10
  slug: independent-reserve-post-private-gettransactions-request
jsonld:
- class_count: 49
  name: Independent Reserve Context
  property_count: 80
  slug: independent-reserve-context
layout: provider
modified: '2026-10-13'
name: Independent Reserve
nav: Providers
network: true
overview: 'Independent Reserve is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Private API, Public API, and 1 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Bitcoin.


  The Independent Reserve catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Independent Reserve''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, and 22 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Independent Reserve API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: independent-reserve-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 51.9
    discoverability: 58.9
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Independent Reserve Authentication
  slug: independent-reserve-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Independent Reserve Domain Security
  slug: independent-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Independent Reserve Vulnerability Disclosure
  slug: independent-reserve-vulnerability-disclosure
  summary_line: no policy recorded
slug: independent-reserve
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Bitcoin
- Financial Services
website: https://www.independentreserve.com
---
