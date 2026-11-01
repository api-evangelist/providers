---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: 'Form 13F holdings data as a REST API: who holds a ticker, what a manager holds, quarter-over-quarter changes, and Schedule 13D/13G beneficial owners. SEC EDGAR source.'
  name: 13F holdings API
  slug: 13f-holdings-api
- description: 'Restated and revised figures from SEC filings as an API: original value, revised value, both EDGAR accessions, and the change type. Companion to the public restatements page.'
  name: Restatements API
  slug: restatements-api
- description: 'REST API for SEC EDGAR filings by ticker: form type, filing date, accession number, document URL and 8-K item codes. Free key, JSON, US domestic filers.'
  name: SEC filings API
  slug: sec-filings-api
- description: 'XBRL financial data from SEC 10-K and 10-Q filings as a REST API: latest fundamentals per ticker, trailing-year aggregates, and the XBRL concept behind every number.'
  name: XBRL financial data API
  slug: xbrl-financial-data-api
- baseURL: https://api.distillmarkets.com
  baseurl_source: declared
  description: 'distillmarkets-com API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: distillmarkets-com API
  slug: distillmarkets-com-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/distillmarkets-com/plans/distillmarkets-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/distillmarkets-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/distillmarkets-com/rules/distillmarkets-com-rules.yml
  title: ''
  type: Spectral
  url: rules/distillmarkets-com-rules.yml
- group: design
  href: https://artifacts.apis.io/distillmarkets-com/json-ld/distillmarkets-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/distillmarkets-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/distillmarkets-com/vocabulary/distillmarkets-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/distillmarkets-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/distillmarkets-com/data-model/distillmarkets-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/distillmarkets-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/distillmarkets-com/changelog/distillmarkets-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/distillmarkets-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/distillmarkets-com/conformance/distillmarkets-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/distillmarkets-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/distillmarkets-com/llms/distillmarkets-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/distillmarkets-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/distillmarkets-com/well-known/distillmarkets-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/distillmarkets-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/distillmarkets-com/hosts/distillmarkets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distillmarkets-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/distillmarkets-com/vendors/distillmarkets-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/distillmarkets-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.distillmarkets.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.distillmarkets.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.distillmarkets.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.distillmarkets.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.distillmarkets.com\\\
- group: auth
  href: https://artifacts.apis.io/distillmarkets-com/security/distillmarkets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distillmarkets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distillmarkets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.distillmarkets.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.distillmarkets.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.distillmarkets.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://www.distillmarkets.com/docs
coverage:
  checked: '2026-10-30'
  detail: API spec endpoints on https://api.distillmarkets.com return 401 Unauthorized, indicating authentication is required to access contracts.
  evidence:
  - status: 401
    url: https://api.distillmarkets.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Distill Markets provides point-in-time SEC fundamentals and 13F institutional ownership data via a robust API, delivering the entire universe of filings as they stood at any quarter-end since 2009, with survivorship completeness and benchmarked accuracy against EDGAR.
image: https://www.distillmarkets.com/og.png
json_schemas:
- name: GetApiV1AnonymousAsofResponse
  property_count: 6
  slug: distillmarkets-com-get-api-v1-anonymous-asof-response
- name: GetApiV1SecFactsAaplResponse
  property_count: 5
  slug: distillmarkets-com-get-api-v1-sec-facts-aapl-response
- name: GetApiV1SecFilingsAaplResponse
  property_count: 8
  slug: distillmarkets-com-get-api-v1-sec-filings-aapl-response
- name: GetApiV1SecFundamentalsFundamentalidResponse
  property_count: 12
  slug: distillmarkets-com-get-api-v1-sec-fundamentals-fundamentalid-response
- name: GetApiV1SecFundamentalsKhcAsOf20190131Response
  property_count: 6
  slug: distillmarkets-com-get-api-v1-sec-fundamentals-khc-as-of20190131-response
- name: GetApiV1SecManagersVanguardResponse
  property_count: 9
  slug: distillmarkets-com-get-api-v1-sec-managers-vanguard-response
jsonld:
- class_count: 6
  name: Distillmarkets Com Context
  property_count: 36
  slug: distillmarkets-com-context
layout: provider
modified: '2026-10-30'
name: distillmarkets-com
nav: Providers
network: true
overview: 'distillmarkets-com is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, SEC, and API.


  The distillmarkets-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  distillmarkets-com''s developer surface includes changelog, documentation, support, pricing, API reference, and 17 more developer resources.'
plans:
- name: Distillmarkets Com Plans Pricing
  plan_count: 4
  slug: distillmarkets-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: distillmarkets-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: distillmarkets-com-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 91.5
    catalog_earned_first_party: 0.0
    catalog_gap: 23.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 55.6
    developer_ergonomics: 31.0
    discoverability: 71.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Distillmarkets Com Domain Security
  slug: distillmarkets-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: distillmarkets-com
tags:
- Company
- Finance
- Data
- SEC
- API
- AI
website: https://distillmarkets.com/
---
