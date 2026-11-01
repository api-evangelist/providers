---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fetcher Sh Agentic Access
  operation_count: 136
  slug: fetcher-sh-agentic-access
  summary_line: 136 operations
api_count: 4
apis:
- baseURL: https://appstore.fetcher.sh
  baseurl_source: declared
  description: Apple App Store app and bundle lookups, reviews, similar apps, and developer catalogs.
  name: fetcher-sh App Store API
  slug: fetcher-sh-app-store-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Place search, place details, and reviews.
  name: fetcher-sh Google Maps API
  slug: fetcher-sh-google-maps-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Headlines by section (world, business, technology, ...), keyword search, topics, and article URL decoding.
  name: fetcher-sh Google News API
  slug: fetcher-sh-google-news-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: App search, app details, reviews, permissions, data safety, and developer catalogs.
  name: fetcher-sh Google Play API
  slug: fetcher-sh-google-play-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Programmatic Google web search results as clean JSON.
  name: fetcher-sh Google Search API
  slug: fetcher-sh-google-search-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Profiles, posts, reels, stories, followers, hashtags, locations, and comment threads.
  name: fetcher-sh Instagram API
  slug: fetcher-sh-instagram-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Search posts, subreddits, and users; pull hot/new/top/best feeds, comment trees, and user history.
  name: fetcher-sh Reddit API
  slug: fetcher-sh-reddit-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Search posts, resolve users by handle, and pull followers, hashtags, music, comments, and replies.
  name: fetcher-sh Tik Tok API
  slug: fetcher-sh-tiktok-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Search tweets, resolve profiles by handle or ID, and pull timelines, replies, followers, lists, and trends.
  name: fetcher-sh Twitter / X API
  slug: fetcher-sh-twitter-x-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Business search by query and location, place details, and reviews.
  name: fetcher-sh Yelp API
  slug: fetcher-sh-yelp-api
- baseURL: https://fetcher.sh
  baseurl_source: declared
  description: Search videos, channels, and playlists; fetch video details, comments, shorts, live streams, and trending.
  name: fetcher-sh YouTube API
  slug: fetcher-sh-youtube-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/fetcher-sh/agentic-access/fetcher-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fetcher-sh-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fetcher-sh/rules/fetcher-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/fetcher-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/fetcher-sh/json-ld/fetcher-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fetcher-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/fetcher-sh/vocabulary/fetcher-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fetcher-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fetcher-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fetcher-sh/data-model/fetcher-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fetcher-sh-data-model.yml
- group: build
  href: https://artifacts.apis.io/fetcher-sh/cli/fetcher-sh-cli.yml
  title: ''
  type: CLI
  url: cli/fetcher-sh-cli.yml
- group: design
  href: https://artifacts.apis.io/fetcher-sh/errors/fetcher-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fetcher-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fetcher-sh/conformance/fetcher-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fetcher-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fetcher-sh/llms/fetcher-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fetcher-sh-llms.txt
- group: other
  href: https://artifacts.apis.io/fetcher-sh/a2a/fetcher-sh-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fetcher-sh-a2a.yml
- group: agent
  href: https://artifacts.apis.io/fetcher-sh/mcp/fetcher-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fetcher-sh-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fetcher-sh/well-known/fetcher-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fetcher-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/fetcher-sh/hosts/fetcher-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fetcher-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/fetcher-sh/vendors/fetcher-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fetcher-sh-vendors.yml
- group: build
  href: https://artifacts.apis.io/fetcher-sh/packages/fetcher-sh-packages.yml
  title: ''
  type: SDKs
  url: packages/fetcher-sh-packages.yml
- group: build
  href: https://artifacts.apis.io/fetcher-sh/packages/fetcher-sh-packages.yml
  title: ''
  type: Packages
  url: packages/fetcher-sh-packages.yml
- group: auth
  href: https://artifacts.apis.io/fetcher-sh/security/fetcher-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetcher-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fetcher.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://fetcher.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fetcher.sh/docs
- group: company
  title: ''
  type: Blog
  url: https://fetcher.sh/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fetcher.sh/prices
- group: start
  title: ''
  type: GettingStarted
  url: https://fetcher.sh/index.md
created: '2026-10-29'
description: fetcher.sh provides a unified web‑data API that aggregates public data from eleven major platforms—including Twitter, YouTube, TikTok, Instagram, Reddit, Google Search, Google Maps, Google News, Google Play, App Store, and Yelp—into a single, no‑account, pay‑per‑call interface. Users can retrieve up to 111 endpoints across these services without OAuth or subscription, paying only per request in USDC (≈ $0.002–$0.005). The service is built on an MCP server architecture, offers transparent pricing, and publishes full OpenAPI 3.1 specifications. Documentation, pricing, and a blog are openly available.
image: https://fetcher.sh/og.png
json_schemas:
- name: Envelope
  property_count: 3
  slug: fetcher-sh-envelope
jsonld:
- class_count: 1
  name: Fetcher Sh Context
  property_count: 3
  slug: fetcher-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at appstore.fetcher.sh.
  name: fetcher-sh MCP Server
  slug: fetcher-sh-mcp-yml
modified: '2026-10-29'
name: fetcher-sh
nav: Providers
network: true
overview: 'fetcher-sh publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Store API, Google Maps API, Google News API, and 8 more. Tagged areas include Company, Web Data, API Aggregation, No Auth, and Pay per Call.


  The fetcher-sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fetcher-sh''s developer surface includes CLI, documentation, API reference, engineering blog, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Fetcher Sh Plans Pricing
  plan_count: 0
  slug: fetcher-sh-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Fetcher Sh Rate Limits
  slug: fetcher-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: fetcher-sh API Rules
  rule_count: 16
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 0
  slug: fetcher-sh-rules
scopes:
- name: Fetcher Sh Scopes
  scope_count: 0
  slug: fetcher-sh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 55.4
    catalog_earned_first_party: 0.0
    catalog_gap: 59.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 54.2
    developer_ergonomics: 47.0
    discoverability: 70.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fetcher Sh Authentication
  slug: fetcher-sh-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fetcher Sh Domain Security
  slug: fetcher-sh-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: get-twitter-handle
  slug: fetcher-sh-get-twitter-handle
slug: fetcher-sh
tags:
- Company
- Web Data
- API Aggregation
- No Auth
- Pay per Call
- MCP
website: https://fetcher.sh/
---
