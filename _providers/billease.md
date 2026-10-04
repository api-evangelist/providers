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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-03'
api_count: 6
apis:
- description: API for Billease fintech services, offering BNPL and personal loans.
  name: Billease API
  slug: billease-api-2
- baseURL: https://trx-test.billease.ph
  baseurl_source: declared
  description: The Be Store Admin Api API from Billease — 1 operation(s) for be store admin api.
  name: Billease Be Store Admin API
  slug: billease-be-store-admin-api-api
- baseURL: https://trx-test.billease.ph
  baseurl_source: declared
  description: The Be Transactions Api API from Billease — 1 operation(s) for be transactions api.
  name: Billease Be Transactions API
  slug: billease-be-transactions-api-api
- baseURL: https://trx-test.billease.ph
  baseurl_source: declared
  description: The Categories API from Billease — 1 operation(s) for categories.
  name: Billease Categories API
  slug: billease-categories-api
- baseURL: https://trx-test.billease.ph
  baseurl_source: declared
  description: The Products API from Billease — 2 operation(s) for products.
  name: Billease Products API
  slug: billease-products-api
- baseURL: https://trx-test.billease.ph
  baseurl_source: declared
  description: The Trx API from Billease — 4 operation(s) for trx.
  name: Billease Trx API
  slug: billease-trx-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/rules/billease-rules.yml
  title: ''
  type: Spectral
  url: rules/billease-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/json-ld/billease-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/billease-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/vocabulary/billease-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/billease-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/data-model/billease-data-model.yml
  title: ''
  type: DataModel
  url: data-model/billease-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/conformance/billease-conformance.yml
  title: ''
  type: Conformance
  url: conformance/billease-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/hosts/billease-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billease-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/vendors/billease-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billease-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://billease.ph/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.billease.ph/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billease/refs/heads/main/security/billease-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billease-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billease.ph
- group: company
  title: ''
  type: Blog
  url: https://billease.ph/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://billease.ph/api/
- group: operate
  title: ''
  type: Support
  url: https://billease.ph/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billease.ph/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billease.ph/privacy
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 200
    url: https://billease.ph/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Billease is a Philippine fintech company offering buy‑now‑pay‑later (BNPL) services and personal loans through its mobile app. Founded in 1969 as a rural bank, it now provides installment financing for online shopping, bill payments, and cash loans, targeting over 10 million users. The platform features zero‑interest credit lines, QR‑code payments, and integrates with thousands of merchants across the Philippines, regulated by the Bangko Sentral ng Pilipinas.
image: https://billease.ph/billease_banner.png
json_schemas:
- name: PostBeStoreAdminApiProductsSyncRequest
  property_count: 3
  slug: billease-post-be-store-admin-api-products-sync-request
- name: PostBeStoreAdminApiProductsSyncResponse
  property_count: 5
  slug: billease-post-be-store-admin-api-products-sync-response
- name: PostProductsSyncRequest
  property_count: 3
  slug: billease-post-products-sync-request
- name: PostTrxIdIdRequest
  property_count: 3
  slug: billease-post-trx-id-id-request
- name: PostTrxIdIdResponse
  property_count: 3
  slug: billease-post-trx-id-id-response
- name: PostTrxTransactionRequest
  property_count: 8
  slug: billease-post-trx-transaction-request
jsonld:
- class_count: 11
  name: Billease Context
  property_count: 28
  slug: billease-context
layout: provider
modified: '2026-09-28'
name: Billease
nav: Providers
network: true
overview: 'Billease publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Be Store Admin API, Be Transactions API, Categories API, and 3 more. Tagged areas include Company, Fintech, Buy Now Pay Later, Philippines, and Loans.


  The Billease catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Billease''s developer surface includes documentation, engineering blog, API reference, support, and 12 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Billease API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: billease-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 23.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Billease Domain Security
  slug: billease-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: billease
tags:
- Company
- Fintech
- Buy Now Pay Later
- Philippines
- Loans
website: https://billease.ph
---
