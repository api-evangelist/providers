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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Public REST API for running AirOps Workflows/Apps (synchronous, asynchronous, and webhook execution), managing executions, interacting with Knowledge Bases (Memory Stores), and reading AEO analytics, '
  name: AirOps API
  slug: airops-api
artifact_total: 6
asyncapis:
- description: ''
  name: Airops Webhooks
  slug: airops-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.airops.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airops.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airops.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airops.com/api-reference/api-reference/executions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airops.com/getting-started/readme
- group: auth
  title: ''
  type: Authentication
  url: authentication/airops-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airops-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airops-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airops-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/airops-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airops-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/airops-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/airops-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airops-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airops-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airops-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airops.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/airops-conformance.yml
- group: company
  title: ''
  type: Blog
  url: https://www.airops.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airops.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.airops.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.airops.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airops.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airops.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airopshq
- group: operate
  title: ''
  type: Support
  url: https://university.airops.com/
created: '2026-07-17'
description: AirOps is a growth platform for AI search and answer engine optimization (AEO) that helps brands measure and improve their visibility across AI assistants and search engines including ChatGPT, Perplexity, Gemini, Claude, and Google. The platform pairs Insights (citation tracking, share-of-voice, sentiment, and competitor intelligence) with Action (Playbooks, Workflows, Grids, and Campaigns that draft and ship content at scale) and Context (Brand Kits and Knowledge Bases). AirOps exposes a public REST API at api.airops.com for executing Workflows/Apps, managing Knowledge Bases, and pulling AEO analytics, a hosted Model Context Protocol (MCP) server at app.airops.com/mcp with roughly ninety tools, incoming webhook triggers, and first-party JavaScript and Python SDKs. It was surfaced as a portfolio company of Greylock and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/61fae48cb5979577435753f6/69fe76ac41d8f24a95a59e72_1200x630-Homepage.jpg
layout: provider
mcp_servers:
- description: ''
  name: airops-mcp.yml
  slug: airops-mcpyml
modified: '2026-07-17'
name: AirOps
nav: Providers
network: true
overview: 'AirOps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applications, AI, Content, and SEO.


  The AirOps catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AirOps'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 38
scopes:
- name: Airops Scopes
  scope_count: 4
  slug: airops-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 49.3
  delta: 8.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/airops/refs/heads/main/screenshots/airops-2026-07-25T195431.png
security:
- kind: authentication
  name: Airops Authentication
  slug: airops-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Airops Domain Security
  slug: airops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airops
tags:
- Company
- Applications
- AI
- Content
- SEO
- AEO
- Answer Engine Optimization
- Generative Engine Optimization
- Workflows
- MCP
- Analytics
website: https://www.airops.com/
---
