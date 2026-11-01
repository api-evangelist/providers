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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Unified Scraper API providing endpoints for social media, search engines, e‑commerce platforms and more.
  name: Scavio API
  slug: scavio-api-2
- baseURL: https://api.scavio.dev
  baseurl_source: declared
  description: 'Scavio API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Scavio API
  slug: scavio-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/scavio/plans/scavio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scavio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scavio/rules/scavio-rules.yml
  title: ''
  type: Spectral
  url: rules/scavio-rules.yml
- group: design
  href: https://artifacts.apis.io/scavio/json-ld/scavio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scavio-context.jsonld
- group: design
  href: https://artifacts.apis.io/scavio/vocabulary/scavio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scavio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/scavio/data-model/scavio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scavio-data-model.yml
- group: auth
  href: https://artifacts.apis.io/scavio/authentication/scavio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scavio-authentication.yml
- group: design
  href: https://artifacts.apis.io/scavio/conformance/scavio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scavio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scavio/llms/scavio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scavio-llms.txt
- group: other
  href: https://artifacts.apis.io/scavio/hosts/scavio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scavio-hosts.yml
- group: other
  href: https://artifacts.apis.io/scavio/vendors/scavio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scavio-vendors.yml
- group: build
  href: https://artifacts.apis.io/scavio/packages/scavio-packages.yml
  title: ''
  type: SDKs
  url: packages/scavio-packages.yml
- group: build
  href: https://artifacts.apis.io/scavio/packages/scavio-packages.yml
  title: ''
  type: Packages
  url: packages/scavio-packages.yml
- group: auth
  href: https://artifacts.apis.io/scavio/security/scavio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scavio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scavio.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scavio.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://scavio.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://scavio.dev/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://scavio.dev/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://scavio.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scavio.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scavio.dev/privacy
coverage:
  checked: '2026-10-18'
  detail: The API reference page provides HTML documentation but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://scavio.dev/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Scavio provides a unified Scraper API that gives developers access to structured data from social media, search engines, e‑commerce platforms and more. By offering a single POST endpoint per platform, it eliminates the need for custom scraping, browser automation or handling multiple authentication schemes. The service supports Google Search, YouTube, Amazon, Walmart, Reddit, TikTok, Instagram and other data sources, delivering clean JSON responses suitable for AI agents, analytics pipelines, and rapid application development.
image: https://scavio.dev/en/opengraph-image?2b54e9e16032ebac
json_schemas:
- name: PostApiV1XSearchResponse
  property_count: 18
  slug: scavio-post-api-v1-xsearch-response
- name: PostApiV1XTrendingResponse
  property_count: 7
  slug: scavio-post-api-v1-xtrending-response
- name: PostApiV1XTweetCommentsRequest
  property_count: 3
  slug: scavio-post-api-v1-xtweet-comments-request
- name: PostApiV1XTweetCommentsResponse
  property_count: 18
  slug: scavio-post-api-v1-xtweet-comments-response
- name: PostApiV1XUserTweetsRequest
  property_count: 2
  slug: scavio-post-api-v1-xuser-tweets-request
- name: PostApiV1XUserTweetsResponse
  property_count: 18
  slug: scavio-post-api-v1-xuser-tweets-response
jsonld:
- class_count: 8
  name: Scavio Context
  property_count: 13
  slug: scavio-context
layout: provider
modified: '2026-10-18'
name: Scavio
nav: Providers
network: true
overview: 'Scavio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Scraping, Data, and Artificial Intelligence.


  The Scavio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scavio''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Scavio Plans Pricing
  plan_count: 7
  slug: scavio-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Scavio API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: scavio-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 27.0
    developer_ergonomics: 57.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scavio Authentication
  slug: scavio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Scavio Domain Security
  slug: scavio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scavio
tags:
- Company
- Web Scraping
- Data
- Artificial Intelligence
website: https://scavio.dev/
---
