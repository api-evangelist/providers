---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Login, logout and signup.
  name: NewsBlur authentication API
  slug: newsblur-authentication-api
- description: Intelligence training classifiers.
  name: NewsBlur classifiers API
  slug: newsblur-classifiers-api
- description: Subscriptions, folders and organization.
  name: NewsBlur feed-management API
  slug: newsblur-feed-management-api
- description: Feed subscription, search and metadata.
  name: NewsBlur feeds API
  slug: newsblur-feeds-api
- description: OPML import and export.
  name: NewsBlur import-export API
  slug: newsblur-import-export-api
- description: Blurblogs, sharing, following and comments.
  name: NewsBlur social API
  slug: newsblur-social-api
- description: Reading, marking and starring stories.
  name: NewsBlur stories API
  slug: newsblur-stories-api
artifact_total: 10
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
- description: ''
  name: newsblur-mcp.yml
  slug: newsblur-mcpyml
modified: '2026-07-20'
name: NewsBlur
nav: Providers
network: true
overview: 'NewsBlur publishes 7 APIs on the [APIs.io](https://apis.io/) network, including authentication API, classifiers API, feed-management API, and 4 more. Tagged areas include Company, RSS, News, Feed Reader, and Aggregator.


  NewsBlur''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 62
score:
  band: developing
  composite: 42.0
  delta: 0.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 53.9
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
website: https://www.newsblur.com/api
---
