---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.debyko.com
  baseurl_source: declared
  description: 'DEBYKO API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DEBYKO API
  slug: debyko-com-api
artifact_total: 12
asyncapis:
- description: ''
  name: Debyko Com Webhooks
  slug: debyko-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/debyko-com/plans/debyko-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/debyko-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/debyko-com/rules/debyko-com-rules.yml
  title: ''
  type: Spectral
  url: rules/debyko-com-rules.yml
- group: design
  href: https://artifacts.apis.io/debyko-com/json-ld/debyko-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/debyko-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/debyko-com/vocabulary/debyko-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/debyko-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/debyko-com/asyncapi/debyko-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/debyko-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/debyko-com/data-model/debyko-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/debyko-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/debyko-com/changelog/debyko-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/debyko-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/debyko-com/conformance/debyko-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/debyko-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/debyko-com/llms/debyko-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/debyko-com-llms.txt
- group: other
  href: https://artifacts.apis.io/debyko-com/hosts/debyko-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/debyko-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/debyko-com/vendors/debyko-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/debyko-com-vendors.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://debyko.com/roadmap/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.debyko.com/dql/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.debyko.com/start/first-request/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.debyko.com/api/reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/debyko
- group: auth
  href: https://artifacts.apis.io/debyko-com/security/debyko-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/debyko-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://debyko.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.debyko.com
- group: commercial
  title: ''
  type: Pricing
  url: https://debyko.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://debyko.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://debyko.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://debyko.com/support/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://debyko.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DEBYKO provides perpetual futures market data from 19 exchanges, including funding rates, open interest, order books and trades. The data is stored as published and sealed daily on Base, offering developers reliable, up-to-date market information for building trading applications and analytics.
image: https://debyko.com/og/debyko-og-1200x630.png?v=3
json_schemas:
- name: GetV1ProfileResponse
  property_count: 4
  slug: debyko-com-get-v1-profile-response
- name: GetV2AnchorsProofResponse
  property_count: 1
  slug: debyko-com-get-v2-anchors-proof-response
- name: GetV2AnchorsResponse
  property_count: 1
  slug: debyko-com-get-v2-anchors-response
- name: GetV2DqlCatalogueResponse
  property_count: 1
  slug: debyko-com-get-v2-dql-catalogue-response
- name: PostV1TradesRequest
  property_count: 18
  slug: debyko-com-post-v1-trades-request
- name: PutV1ProfileResponse
  property_count: 3
  slug: debyko-com-put-v1-profile-response
jsonld:
- class_count: 15
  name: Debyko Com Context
  property_count: 31
  slug: debyko-com-context
layout: provider
modified: '2026-11-05'
name: DEBYKO
nav: Providers
network: true
overview: 'DEBYKO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Market Data, Futures, and Cryptocurrency.


  The DEBYKO catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DEBYKO''s developer surface includes changelog, getting-started guide, API reference, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Debyko Com Plans Pricing
  plan_count: 5
  slug: debyko-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: DEBYKO API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: debyko-com-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 34.2
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
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Debyko Com Domain Security
  slug: debyko-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: debyko-com
tags:
- Finance
- Market Data
- Futures
- Cryptocurrency
website: https://debyko.com/
---
