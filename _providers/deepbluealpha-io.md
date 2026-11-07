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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Real-time Ethereum whale tracking API providing wallet activity, token holdings, and market signals.
  name: Deep Blue Alpha API
  slug: deep-blue-alpha-api
- description: 'Deep Blue Alpha API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Deep Blue Alpha API
  slug: deepbluealpha-io-api
artifact_total: 13
asyncapis:
- description: ''
  name: Deepbluealpha Io Webhooks
  slug: deepbluealpha-io-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/deepbluealpha-io/plans/deepbluealpha-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepbluealpha-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/rules/deepbluealpha-io-rules.yml
  title: ''
  type: Spectral
  url: rules/deepbluealpha-io-rules.yml
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/json-ld/deepbluealpha-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deepbluealpha-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/vocabulary/deepbluealpha-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepbluealpha-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/asyncapi/deepbluealpha-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deepbluealpha-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/data-model/deepbluealpha-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deepbluealpha-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/deepbluealpha-io/conformance/deepbluealpha-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deepbluealpha-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deepbluealpha-io/llms/deepbluealpha-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deepbluealpha-io-llms.txt
- group: other
  href: https://artifacts.apis.io/deepbluealpha-io/hosts/deepbluealpha-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepbluealpha-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepbluealpha-io/vendors/deepbluealpha-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepbluealpha-io-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://deepbluealpha.io/api-docs/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepbluealpha.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepbluealpha.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://deepbluealpha.io/news
- group: auth
  href: https://artifacts.apis.io/deepbluealpha-io/security/deepbluealpha-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepbluealpha-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepbluealpha.io/
- group: docs
  title: ''
  type: APIReference
  url: https://deepbluealpha.io/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://deepbluealpha.io/api-docs
- group: operate
  title: ''
  type: Roadmap
  url: https://deepbluealpha.io/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://deepbluealpha.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://deepbluealpha.io/register
coverage:
  checked: '2026-11-05'
  detail: Provider docs are behind Cloudflare JS challenge, preventing machine‑readable spec retrieval.
  evidence:
  - status: 403
    url: https://deepbluealpha.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Deep Blue Alpha provides real-time Ethereum whale tracking and intelligence. The platform offers live dashboards, whale flow visualizations, trend analysis, and smart‑money insights for crypto investors. Users can explore wallet activity, token holdings, and market signals across multiple plans, with API access for developers to integrate whale data into their applications.
image: https://deepbluealpha.io/static/img/og/home.png
json_schemas:
- name: GetApiV1TokenSymbolFlowResponse
  property_count: 2
  slug: deepbluealpha-io-get-api-v1-token-symbol-flow-response
- name: GetApiV1TopTokensResponse
  property_count: 2
  slug: deepbluealpha-io-get-api-v1-top-tokens-response
- name: GetApiV1TopWalletsResponse
  property_count: 2
  slug: deepbluealpha-io-get-api-v1-top-wallets-response
- name: GetApiV1TransactionsResponse
  property_count: 2
  slug: deepbluealpha-io-get-api-v1-transactions-response
- name: GetApiV1WatchlistResponse
  property_count: 2
  slug: deepbluealpha-io-get-api-v1-watchlist-response
- name: GetV1TransactionsResponse
  property_count: 2
  slug: deepbluealpha-io-get-v1-transactions-response
jsonld:
- class_count: 11
  name: Deepbluealpha Io Context
  property_count: 9
  slug: deepbluealpha-io-context
layout: provider
modified: '2026-11-05'
name: Deep Blue Alpha
nav: Providers
network: true
overview: 'Deep Blue Alpha is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ethereum, WhaleTracking, Crypto-Analytics, and Real-Time Data.


  The Deep Blue Alpha catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Deep Blue Alpha''s developer surface includes API reference, documentation, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Deepbluealpha Io Plans Pricing
  plan_count: 4
  slug: deepbluealpha-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Deep Blue Alpha API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: deepbluealpha-io-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 30.8
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepbluealpha Io Domain Security
  slug: deepbluealpha-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deepbluealpha-io
tags:
- Company
- Ethereum
- WhaleTracking
- Crypto-Analytics
- Real-Time Data
website: https://deepbluealpha.io/
---
