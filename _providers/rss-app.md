---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://api.rss.app
  baseurl_source: declared
  description: 'RSS.app API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: RSS.app API
  slug: rss-app-api
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/plans/rss-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rss-app-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/rules/rss-app-rules.yml
  title: ''
  type: Spectral
  url: rules/rss-app-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/json-ld/rss-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rss-app-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/vocabulary/rss-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rss-app-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/data-model/rss-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rss-app-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/conformance/rss-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rss-app-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/llms/rss-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rss-app-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/well-known/rss-app-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rss-app-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/well-known/rss-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rss-app-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/hosts/rss-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rss-app-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/vendors/rss-app-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/rss-app/refs/heads/main/security/rss-app-domain-security.yml
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
overview: 'RSS.app publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RSS, No-Code, Automation, and Content.


  The RSS.app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RSS.app''s developer surface includes getting-started guide, documentation, pricing, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Rss App Plans Pricing
  plan_count: 4
  slug: rss-app-plans-pricing
random_paper: 6
rules:
- effective_rule_count: 51
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
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 33.3
    discoverability: 75.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
