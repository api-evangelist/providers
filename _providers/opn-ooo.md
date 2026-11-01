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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.omise.co
  baseurl_source: declared
  description: 'Omise API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Omise API
  slug: opn-ooo-api
artifact_total: 12
asyncapis:
- description: ''
  name: Opn Ooo Webhooks
  slug: opn-ooo-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/opn-ooo/well-known/opn-ooo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/opn-ooo-status-security.txt
- group: agent
  href: https://artifacts.apis.io/opn-ooo/well-known/opn-ooo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opn-ooo-well-known.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/rules/opn-ooo-rules.yml
  title: ''
  type: Spectral
  url: rules/opn-ooo-rules.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/json-ld/opn-ooo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opn-ooo-context.jsonld
- group: design
  href: https://artifacts.apis.io/opn-ooo/vocabulary/opn-ooo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opn-ooo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/asyncapi/opn-ooo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/opn-ooo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/data-model/opn-ooo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opn-ooo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/opn-ooo/changelog/opn-ooo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opn-ooo-changelog.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/conventions/opn-ooo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opn-ooo-conventions.yml
- group: auth
  href: https://artifacts.apis.io/opn-ooo/authentication/opn-ooo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opn-ooo-authentication.yml
- group: operate
  href: https://artifacts.apis.io/opn-ooo/lifecycle/opn-ooo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/opn-ooo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/lifecycle/opn-ooo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opn-ooo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/opn-ooo/conformance/opn-ooo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opn-ooo-conformance.yml
- group: other
  href: https://artifacts.apis.io/opn-ooo/hosts/opn-ooo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opn-ooo-hosts.yml
- group: other
  href: https://artifacts.apis.io/opn-ooo/vendors/opn-ooo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opn-ooo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.omise.co/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omise.co/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.omise.co/v2/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://omise.co/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://omise.co/en/newsroom
- group: company
  title: ''
  type: Blog
  url: https://omise.co/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.omise.co/en/docs/international
- group: docs
  title: ''
  type: Documentation
  url: https://docs.omise.co/
- group: auth
  href: https://artifacts.apis.io/opn-ooo/security/opn-ooo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opn-ooo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omise.co
created: '2026-10-25'
description: Omise is a Singapore‑based payments platform that provides a simple, secure API for accepting online payments, managing recurring subscriptions, and handling payouts across multiple currencies. Founded in 2013, Omise serves merchants, developers, and enterprises in Southeast Asia and beyond, offering features such as fraud detection, tokenization, and comprehensive dashboard analytics. The company emphasizes developer‑friendly documentation, robust SDKs, and compliance with regional financial regulations.
image: https://cdn.prod.website-files.com/67481ca1f2e8301c5e5e3895/67d7992fd01eb8fd6ac0c2a1_IMG_4731.png
json_schemas:
- name: GetForexCurrencyResponse
  property_count: 6
  slug: opn-ooo-get-forex-currency-response
- name: GetTokensIdResponse
  property_count: 8
  slug: opn-ooo-get-tokens-id-response
- name: PatchCustomersIdCardsCardidRequest
  property_count: 5
  slug: opn-ooo-patch-customers-id-cards-cardid-request
- name: PostChargesIdRefundsResponse
  property_count: 14
  slug: opn-ooo-post-charges-id-refunds-response
- name: PostChargesRequest
  property_count: 21
  slug: opn-ooo-post-charges-request
- name: PostTokensResponse
  property_count: 8
  slug: opn-ooo-post-tokens-response
jsonld:
- class_count: 12
  name: Opn Ooo Context
  property_count: 58
  slug: opn-ooo-context
layout: provider
modified: '2026-10-25'
name: Omise
nav: Providers
network: true
overview: 'Omise is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, API, FinTech, and Southeast-Asia.


  The Omise catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Omise''s developer surface includes changelog, authentication, signup flow, pricing, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Omise API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: opn-ooo-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 36.1
    developer_ergonomics: 35.7
    discoverability: 67.9
    operational_transparency: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Opn Ooo Authentication
  slug: opn-ooo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Opn Ooo Domain Security
  slug: opn-ooo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opn-ooo
tags:
- Company
- Payments
- API
- FinTech
- Southeast-Asia
website: https://omise.co
---
