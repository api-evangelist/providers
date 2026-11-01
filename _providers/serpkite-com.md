---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.serpkite.com
  baseurl_source: declared
  description: 'serpkite-com API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: serpkite-com API
  slug: serpkite-com-api
artifact_total: 16
asyncapis:
- description: ''
  name: Serpkite Com Webhooks
  slug: serpkite-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/serpkite-com/rate-limits/serpkite-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/serpkite-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/serpkite-com/plans/serpkite-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serpkite-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/rules/serpkite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/serpkite-com-rules.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/json-ld/serpkite-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/serpkite-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/serpkite-com/vocabulary/serpkite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/serpkite-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/serpkite-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/asyncapi/serpkite-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/serpkite-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/data-model/serpkite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/serpkite-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/serpkite-com/changelog/serpkite-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/serpkite-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/conventions/serpkite-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/serpkite-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/serpkite-com/authentication/serpkite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/serpkite-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/serpkite-com/conformance/serpkite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/serpkite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/serpkite-com/llms/serpkite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serpkite-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/serpkite-com/well-known/serpkite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/serpkite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/serpkite-com/hosts/serpkite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/serpkite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/serpkite-com/vendors/serpkite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/serpkite-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/serpkite-com/packages/serpkite-com-packages.yml
  title: ''
  type: SDKs
  url: packages/serpkite-com-packages.yml
- group: build
  href: https://artifacts.apis.io/serpkite-com/packages/serpkite-com-packages.yml
  title: ''
  type: Packages
  url: packages/serpkite-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serpkite
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.serpkite.com`
- group: auth
  href: https://artifacts.apis.io/serpkite-com/security/serpkite-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/serpkite-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/serpkite-com/security/serpkite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serpkite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://serpkite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://serpkite.com/docs
- group: company
  title: ''
  type: Blog
  url: https://serpkite.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://serpkite.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://serpkite.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://serpkite.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://serpkite.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://serpkite.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://serpkite.com/playground
- group: start
  title: ''
  type: GettingStarted
  url: https://serpkite.com/docs/quickstart
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://serpkite.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: SerpKite (serpkite.com) offers a suite of search and data retrieval APIs, including Google Search, Shopping, Scholar, and custom search capabilities. The platform provides comprehensive documentation, quickstart guides, pricing details, and a sandbox playground for developers to test endpoints. It emphasizes transparent security policies, clear terms of service, and privacy practices, supporting developers in building search-driven applications with robust rate‑limit handling and error management.
image: https://serpkite.com/og.png
json_schemas:
- name: GetV1CrawlIdResponse
  property_count: 7
  slug: serpkite-com-get-v1-crawl-id-response
- name: PostV1AnswerResponse
  property_count: 5
  slug: serpkite-com-post-v1-answer-response
- name: PostV1CrawlResponse
  property_count: 12
  slug: serpkite-com-post-v1-crawl-response
- name: PostV1GeminiResponse
  property_count: 8
  slug: serpkite-com-post-v1-gemini-response
- name: PostV1NewsResponse
  property_count: 3
  slug: serpkite-com-post-v1-news-response
- name: PostV1RankResponse
  property_count: 6
  slug: serpkite-com-post-v1-rank-response
jsonld:
- class_count: 21
  name: Serpkite Com Context
  property_count: 42
  slug: serpkite-com-context
layout: provider
modified: '2026-10-31'
name: serpkite-com
nav: Providers
network: true
overview: 'serpkite-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Search, Data Retrieval, API, and Developer Platform.


  The serpkite-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  serpkite-com''s developer surface includes changelog, authentication, documentation, engineering blog, pricing, sandbox, getting-started guide, and 25 more developer resources.'
plans:
- name: Serpkite Com Plans Pricing
  plan_count: 5
  slug: serpkite-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Serpkite Com Rate Limits
  slug: serpkite-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: serpkite-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: serpkite-com-rules
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 55.0
    developer_ergonomics: 66.0
    discoverability: 66.1
    operational_transparency: 67.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Serpkite Com Authentication
  slug: serpkite-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Serpkite Com Domain Security
  slug: serpkite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Serpkite Com Vulnerability Disclosure
  slug: serpkite-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: search
  slug: serpkite-com-search
slug: serpkite-com
tags:
- Company
- Search
- Data Retrieval
- API
- Developer Platform
website: https://serpkite.com/
---
