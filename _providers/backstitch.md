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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: RESTful JSON API to build and manage backstitch topics — content feeds assembled from social, RSS, video, deals, subreddit, and custom sources with include/exclude/NSFW filters — and to retrieve norma
  name: backstitch Content Curation API
  slug: backstitch-content-curation-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backstitch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.backstitch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.backstit.ch/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.backstit.ch/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backstitch
- group: operate
  title: ''
  type: Support
  url: https://www.backstitch.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.backstitch.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backstitch.io/website-privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.backstitch.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/backstitch-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/backstitch-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/backstitch-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/backstitch-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/backstitch-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/backstitch-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/backstitch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backstitch-llms.txt
created: '2026-07-17'
description: backstitch is a Techstars-backed Kansas City company that operates an employee and total-rewards communications platform (drag-and-drop newsletters, a branded mobile employee app, and personalized total-compensation statements) alongside a developer-facing content-curation API. The backstitch API lets applications build and manage "topics" that aggregate and filter content from social, RSS, video, deals, and custom sources, then retrieve normalized result objects (articles, statuses, photos, videos, products, services, hotels) or embed them with a drop-in JavaScript widget. The API is offered in a legacy v1 and a recommended v2 over REST/JSON, authenticated with an Organization Key plus per-topic tokens.
image: https://www.backstitch.io/hs-fs/hubfs/backstitch_logo_purple_2020.png?width=170&height=36&name=backstitch_logo_purple_2020.png
layout: provider
mcp_servers:
- description: ''
  name: backstitch-mcp.yml
  slug: backstitch-mcpyml
modified: '2026-07-18'
name: backstitch
nav: Providers
network: true
overview: 'backstitch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Curation, Employee Communications, Internal Communications, and Total Rewards.


  backstitch''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backstitch/refs/heads/main/screenshots/backstitch-2026-07-25T202231.png
security:
- kind: authentication
  name: Backstitch Authentication
  slug: backstitch-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Backstitch Domain Security
  slug: backstitch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backstitch
tags:
- Company
- Content Curation
- Employee Communications
- Internal Communications
- Total Rewards
- Content Aggregation
- Newsletters
- Widgets
- REST
website: https://www.backstitch.io/
---
