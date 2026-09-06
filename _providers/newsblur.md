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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Login, logout and signup.
  name: NewsBlur authentication API
  slug: newsblur-authentication-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Intelligence training classifiers.
  name: NewsBlur classifiers API
  slug: newsblur-classifiers-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Subscriptions, folders and organization.
  name: NewsBlur feed-management API
  slug: newsblur-feed-management-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Feed subscription, search and metadata.
  name: NewsBlur feeds API
  slug: newsblur-feeds-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: OPML import and export.
  name: NewsBlur import-export API
  slug: newsblur-import-export-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Blurblogs, sharing, following and comments.
  name: NewsBlur social API
  slug: newsblur-social-api
- baseURL: https://www.newsblur.com
  baseurl_source: declared
  description: Reading, marking and starring stories.
  name: NewsBlur stories API
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
  title: ''
  type: MCPServer
  url: mcp/newsblur-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newsblur-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newsblur-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/newsblur-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newsblur-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newsblur-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newsblur-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newsblur-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/newsblur-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newsblur-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newsblur-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/newsblur-openapi-overlay.yaml
- group: agent
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
overview: 'NewsBlur publishes 7 APIs on the [APIs.io](https://apis.io/) network, including authentication API, classifiers API, feed-management API, and 4 more. Tagged areas include Company, RSS, News, Feed Reader, and Aggregator.


  NewsBlur''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 50.7
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Open-Source
- MCP
website: https://www.newsblur.com/api
---
