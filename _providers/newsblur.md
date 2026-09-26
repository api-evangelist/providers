---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Login, logout and signup.
  name: NewsBlur Authentication API
  slug: newsblur-authentication-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Intelligence training classifiers.
  name: NewsBlur Classifiers API
  slug: newsblur-classifiers-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Subscriptions, folders and organization.
  name: NewsBlur Feed Management API
  slug: newsblur-feed-management-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Feed subscription, search and metadata.
  name: NewsBlur Feeds API
  slug: newsblur-feeds-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: OPML import and export.
  name: NewsBlur Import Export API
  slug: newsblur-import-export-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Blurblogs, sharing, following and comments.
  name: NewsBlur Social API
  slug: newsblur-social-api
- baseURL: https://www.newsblur.com
  baseurl_source: spec
  description: Reading, marking and starring stories.
  name: NewsBlur Stories API
  slug: newsblur-stories-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NewsBlur authentication API
  slug: open-newsblur-authentication-api
- collection_type: open
  name: NewsBlur authentication classifiers API
  slug: open-newsblur-classifiers-api
- collection_type: open
  name: NewsBlur authentication feed-management API
  slug: open-newsblur-feed-management-api
- collection_type: open
  name: NewsBlur authentication feeds API
  slug: open-newsblur-feeds-api
- collection_type: open
  name: NewsBlur authentication import-export API
  slug: open-newsblur-import-export-api
- collection_type: open
  name: NewsBlur authentication social API
  slug: open-newsblur-social-api
- collection_type: open
  name: NewsBlur authentication stories API
  slug: open-newsblur-stories-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.newsblur.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.newsblur.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.newsblur.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.newsblur.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/samuelclay/NewsBlur
- group: operate
  title: ''
  type: Support
  url: https://forum.newsblur.com
- group: company
  title: ''
  type: Blog
  url: https://blog.newsblur.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newsblur.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newsblur.com/tos
- group: start
  title: ''
  type: SignUp
  url: https://www.newsblur.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/mcp/newsblur-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/newsblur-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/authentication/newsblur-authentication.yml
  title: ''
  type: Authentication
  url: authentication/newsblur-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/conventions/newsblur-conventions.yml
  title: ''
  type: Conventions
  url: conventions/newsblur-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/packages/newsblur-packages.yml
  title: ''
  type: Packages
  url: packages/newsblur-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/llms/newsblur-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/newsblur-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/well-known/newsblur-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/newsblur-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/lifecycle/newsblur-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/newsblur-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/security/newsblur-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newsblur-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/data-model/newsblur-data-model.yml
  title: ''
  type: DataModel
  url: data-model/newsblur-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/errors/newsblur-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/newsblur-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/conformance/newsblur-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newsblur-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/overlays/newsblur-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/newsblur-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: NewsBlur is a personal news reader that brings people together to talk about the world. It is an RSS/Atom feed aggregator with training-based intelligence (hide or highlight stories per feed), original-site and original-text views, saved (starred) stories, folders, OPML import/export, and a social layer of shareable "blurblogs" with following, comments and likes. NewsBlur is open source (MIT, github.com/samuelclay/NewsBlur), runs native iOS, macOS and Android apps, and exposes a documented HTTP API plus an official hosted Model Context Protocol (MCP) server at newsblur.com/mcp for AI agents. This profile captures NewsBlur's public API surface for the API Evangelist network.
image: https://www.newsblur.com/media/img/logo_512.png
layout: provider
mcp_servers:
- description: 'NewsBlur ships an official hosted Model Context Protocol (MCP) server that lets AI agents (Claude Desktop, Claude Code, Cursor, or any MCP-compatible client) interact with a user''s feeds, stories and '
  name: NewsBlur MCP Server
  slug: newsblur-mcp-server
modified: '2026-07-20'
name: NewsBlur
nav: Providers
network: true
overview: 'NewsBlur publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Classifiers API, Feed Management API, and 4 more. Tagged areas include Company, RSS, News, Feed Reader, and Aggregator.


  NewsBlur''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.7
    developer_ergonomics: 47.0
    discoverability: 60.0
    operational_transparency: 2.6
  previous_composite: 35.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/newsblur/refs/heads/main/screenshots/newsblur-2026-08-07T185129.png
security:
- kind: authentication
  name: Newsblur Authentication
  slug: newsblur-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Newsblur Domain Security
  slug: newsblur-domain-security
  summary_line: TLSv1.3 · HSTS
slug: newsblur
tags:
- Company
- RSS
- News
- Feed Reader
- Aggregator
- Social
- Content
- Media
- Open Source
- MCP
website: https://www.newsblur.com/
---
