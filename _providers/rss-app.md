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
    auth_clarity: false
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
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.rss.app
  baseurl_source: declared
  description: The Bundles API from RSS.app — 2 operation(s) for bundles.
  name: RSS.app Bundles API
  slug: rss-app-bundles-api
- baseURL: https://api.rss.app
  baseurl_source: declared
  description: The Feed API from RSS.app — 1 operation(s) for feed.
  name: RSS.app Feed API
  slug: rss-app-feed-api
- baseURL: https://api.rss.app
  baseurl_source: declared
  description: The RSS.app API API from RSS.app — 2 operation(s) for rss.app api.
  name: RSS.app RSS.app API
  slug: rss-app-rss-app-api-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/rss-app/plans/rss-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rss-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rss-app/rules/rss-app-rules.yml
  title: ''
  type: Spectral
  url: rules/rss-app-rules.yml
- group: design
  href: https://artifacts.apis.io/rss-app/json-ld/rss-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rss-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/rss-app/vocabulary/rss-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rss-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rss-app/data-model/rss-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rss-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/rss-app/conformance/rss-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rss-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rss-app/llms/rss-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rss-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/rss-app/well-known/rss-app-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rss-app-help-security.txt
- group: agent
  href: https://artifacts.apis.io/rss-app/well-known/rss-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rss-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/rss-app/hosts/rss-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rss-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/rss-app/vendors/rss-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rss-app-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://rss.app/discover/security
- group: company
  title: ''
  type: Newsroom
  url: https://rss.app/rss-feed/categories/news
- group: start
  title: ''
  type: GettingStarted
  url: https://help.rss.app/en/articles/11124064-how-to-use-rss-app-your-quick-start-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.rss.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.rss.app</code
- group: auth
  href: https://artifacts.apis.io/rss-app/security/rss-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rss-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rss.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://rss.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://rss.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rss.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rss.app/privacy
- group: start
  title: ''
  type: SignUp
  url: https://rss.app/signup
coverage:
  checked: 2026-09-22
  detail: API documentation at https://rss.app/docs/api returns HTML rendered by JavaScript, preventing machine‑readable extraction.
  evidence:
  - status: 200
    url: https://rss.app/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: RSS.app provides a no‑code platform that lets users generate RSS feeds from any website or social media source, create embeddable widgets, and automate content distribution via bots to Discord, Slack, Telegram, and email. It offers a suite of tools for monitoring brands, competitors, and news, with customizable widgets, news walls, and alerts, targeting marketers, developers, and businesses seeking automated content streams without writing code.
finops:
- has_sources: true
  method: derived
  name: Rss App Finops
  primary_unit: ''
  service_category: ''
  slug: rss-app-finops
  template: true
image: https://rss.app/static/img/images/rss-app.png
json_schemas:
- name: GetV1V1IdIdResponse
  property_count: 8
  slug: rss-app-get-v1-v1-id-id-response
- name: GetV1V1IdResponse
  property_count: 4
  slug: rss-app-get-v1-v1-id-response
- name: PatchV1FeedRequest
  property_count: 3
  slug: rss-app-patch-v1-feed-request
- name: PatchV1FeedResponse
  property_count: 7
  slug: rss-app-patch-v1-feed-response
- name: PostV1V1IdRequest
  property_count: 2
  slug: rss-app-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 7
  slug: rss-app-post-v1-v1-id-response
jsonld:
- class_count: 7
  name: Rss App Context
  property_count: 15
  slug: rss-app-context
layout: provider
modified: '2026-09-22'
name: RSS.app
nav: Providers
network: true
overview: 'RSS.app is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Bundles API, Feed API, and RSS.app API. Tagged areas include Company, RSS, No-Code, Automation, and Content.


  The RSS.app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RSS.app''s developer surface includes getting-started guide, documentation, pricing, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Rss App Plans Pricing
  plan_count: 4
  slug: rss-app-plans-pricing
- name: Rss App Price Estimates
  plan_count: 0
  slug: rss-app-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: RSS.app API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: rss-app-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 16.7
    discoverability: 79.5
    operational_transparency: 5.3
  previous_composite: 39.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rss-app/rss-app-2026-10-11T125438.png
security:
- kind: domain-security
  name: Rss App Domain Security
  slug: rss-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rss-app
tags:
- Company
- RSS
- No-Code
- Automation
- Content
website: https://rss.app/
---
