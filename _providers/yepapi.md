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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-10-17'
api_count: 5
apis:
- baseURL: https://api.yepapi.com
  baseurl_source: declared
  description: The Email API from YepAPI — 1 operation(s) for email.
  name: YepAPI Email API
  slug: yepapi-email-api
- baseURL: https://api.yepapi.com
  baseurl_source: declared
  description: The Maps API from YepAPI — 1 operation(s) for maps.
  name: YepAPI Maps API
  slug: yepapi-maps-api
- baseURL: https://api.yepapi.com
  baseurl_source: declared
  description: The Seo API from YepAPI — 3 operation(s) for seo.
  name: YepAPI Seo API
  slug: yepapi-seo-api
- baseURL: https://api.yepapi.com
  baseurl_source: declared
  description: The Serp API from YepAPI — 1 operation(s) for serp.
  name: YepAPI Serp API
  slug: yepapi-serp-api
- baseURL: https://api.yepapi.com
  baseurl_source: declared
  description: The Tiktok API from YepAPI — 1 operation(s) for tiktok.
  name: YepAPI Tiktok API
  slug: yepapi-tiktok-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/rules/yepapi-rules.yml
  title: ''
  type: Spectral
  url: rules/yepapi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/json-ld/yepapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yepapi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/vocabulary/yepapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yepapi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/data-model/yepapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yepapi-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/authentication/yepapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yepapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/conformance/yepapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yepapi-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/llms/yepapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yepapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/well-known/yepapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yepapi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/hosts/yepapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yepapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/vendors/yepapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yepapi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yepapi.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.yepapi.com/skills/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yepapi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yepapi.com/skills/pricing-pages
- group: start
  title: ''
  type: Login
  url: https://www.yepapi.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.yepapi.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.yepapi.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yepapi.com/getting-started/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://docs.yepapi.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yepapi/refs/heads/main/security/yepapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yepapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yepapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yepapi.com/
created: '2026-10-08'
description: YepAPI provides a unified API gateway that aggregates and resells a wide range of data services, including SEO and SERP analytics, web scraping, and access to over 180 third‑party AI models such as OpenAI, Claude, and Gemini through a single OpenAI‑compatible endpoint. The platform offers endpoints for keyword research, backlink analysis, real‑time search results, social media data from TikTok and Instagram (via scraping), YouTube analytics, and AI‑driven content extraction. Customers can obtain data on a per‑call basis with no subscription tiers, making it suitable for marketers, developers, and AI agents seeking comprehensive web and AI data without managing multiple vendor integrations.
image: https://www.yepapi.com/api/og?title=YepAPI+-+Unified+API+gateway+for+vibe+coders.&description=Web+scraping%2C+SEO+data%2C+SERP+results%2C+AI+models+%E2%80%94+130%2B+API+endpoints+under+one+key.+Pay+per+call+from+%240.01.+No+monthly+fees.
json_schemas:
- name: PostV1EmailCountResponse
  property_count: 2
  slug: yepapi-post-v1-email-count-response
- name: PostV1MapsMapidResponse
  property_count: 2
  slug: yepapi-post-v1-maps-mapid-response
- name: PostV1SeoKeywordsRequest
  property_count: 3
  slug: yepapi-post-v1-seo-keywords-request
- name: PostV1SeoSeoidKeywordsRequest
  property_count: 3
  slug: yepapi-post-v1-seo-seoid-keywords-request
- name: PostV1SerpSerpidResponse
  property_count: 2
  slug: yepapi-post-v1-serp-serpid-response
- name: PostV1TiktokUserResponse
  property_count: 2
  slug: yepapi-post-v1-tiktok-user-response
jsonld:
- class_count: 6
  name: Yepapi Context
  property_count: 3
  slug: yepapi-context
layout: provider
modified: '2026-10-08'
name: YepAPI
nav: Providers
network: true
overview: 'YepAPI is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Email API, Maps API, Seo API, and 2 more. Tagged areas include SEO, SERP, WebScraping, AIModels, and Marketing.


  The YepAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  YepAPI''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, API reference, documentation, and 15 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: YepAPI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: yepapi-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 42.9
    discoverability: 78.6
    operational_transparency: 26.3
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
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Yepapi Authentication
  slug: yepapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Yepapi Domain Security
  slug: yepapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: yepapi
tags:
- SEO
- SERP
- WebScraping
- AIModels
- Marketing
website: https://www.yepapi.com/
---
