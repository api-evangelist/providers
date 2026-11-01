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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Vezgo API provides access to balances, positions and transaction history across crypto exchanges, blockchains and wallets.
  name: Vezgo API
  slug: vezgo-api-2
- baseURL: https://api.vezgo.com
  baseurl_source: declared
  description: 'Vezgo API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Vezgo API
  slug: vezgo-api
artifact_total: 15
asyncapis:
- description: ''
  name: Vezgo Webhooks
  slug: vezgo-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/vezgo/plans/vezgo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vezgo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vezgo/rules/vezgo-rules.yml
  title: ''
  type: Spectral
  url: rules/vezgo-rules.yml
- group: design
  href: https://artifacts.apis.io/vezgo/json-ld/vezgo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vezgo-context.jsonld
- group: design
  href: https://artifacts.apis.io/vezgo/vocabulary/vezgo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vezgo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vezgo/asyncapi/vezgo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vezgo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/vezgo/data-model/vezgo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vezgo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/vezgo/changelog/vezgo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vezgo-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://vezgo.com/security/
- group: auth
  href: https://artifacts.apis.io/vezgo/authentication/vezgo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vezgo-authentication.yml
- group: design
  href: https://artifacts.apis.io/vezgo/conformance/vezgo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vezgo-conformance.yml
- group: other
  href: https://artifacts.apis.io/vezgo/hosts/vezgo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vezgo-hosts.yml
- group: other
  href: https://artifacts.apis.io/vezgo/vendors/vezgo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vezgo-vendors.yml
- group: build
  href: https://artifacts.apis.io/vezgo/packages/vezgo-packages.yml
  title: ''
  type: SDKs
  url: packages/vezgo-packages.yml
- group: build
  href: https://artifacts.apis.io/vezgo/packages/vezgo-packages.yml
  title: ''
  type: Packages
  url: packages/vezgo-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vezgo.com/
- group: auth
  title: ''
  type: Security
  url: https://vezgo.com/security/
- group: other
  title: ''
  type: Leadership
  url: https://vezgo.com/team/
- group: operate
  title: ''
  type: ChangeLog
  url: https://vezgo.com/docs/changelog/
- group: auth
  href: https://artifacts.apis.io/vezgo/security/vezgo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vezgo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vezgo/security/vezgo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vezgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vezgo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vezgo.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://vezgo.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://vezgo.com/docs/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://vezgo.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vezgo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vezgo.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://vezgo.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://vezgo.com/blog/
coverage:
  checked: '2026-10-19'
  detail: The Vezgo API documentation is publicly available but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://vezgo.com/docs/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Vezgo provides a Crypto Data API for digital assets, offering secure, real‑time access to wallet and exchange holdings, transaction histories, NFT data, and event streams. Their platform enables developers to build portfolio trackers, tax software, compliance tools, lending solutions, and AI agents by delivering comprehensive crypto asset information through a single, unified API.
image: https://vezgo.com/vezgo-og-image.png
json_schemas:
- name: PostAccountsRequest
  property_count: 1
  slug: vezgo-post-accounts-request
- name: PostAuthTokenRequest
  property_count: 2
  slug: vezgo-post-auth-token-request
- name: PostV1AuthTokenRequest
  property_count: 2
  slug: vezgo-post-v1-auth-token-request
- name: PostVezgoAuthRequest
  property_count: 2
  slug: vezgo-post-vezgo-auth-request
- name: PostVezgoWebhooksRequest
  property_count: 4
  slug: vezgo-post-vezgo-webhooks-request
- name: PutAccountsIdRequest
  property_count: 2
  slug: vezgo-put-accounts-id-request
jsonld:
- class_count: 12
  name: Vezgo Context
  property_count: 9
  slug: vezgo-context
layout: provider
modified: '2026-10-19'
name: Vezgo
nav: Providers
network: true
overview: 'Vezgo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Data API, Digital Assets, Fintech, and Portfolio Tracking.


  The Vezgo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Vezgo''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 22 more developer resources.'
plans:
- name: Vezgo Plans Pricing
  plan_count: 2
  slug: vezgo-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Vezgo API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: vezgo-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 22.0
    contract_quality: 31.5
    developer_ergonomics: 54.8
    discoverability: 58.9
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vezgo Authentication
  slug: vezgo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vezgo Domain Security
  slug: vezgo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vezgo Trust Center
  slug: vezgo-trust-center
  summary_line: SOC 2, GDPR
slug: vezgo
tags:
- Cryptocurrency
- Data API
- Digital Assets
- Fintech
- Portfolio Tracking
website: https://vezgo.com/
---
