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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: The Data Import API allows you to import mentions from external sources into YouScan topics. This feature enables you to bring historical data or mentions from sources not natively supported by YouSca
  name: YouScan Data Import API
  slug: youscan-data-import-api
- description: Manage historical data collection for a topic. Starting a collection can return `400` if a collection is already running, if the date range is invalid, or if the requested depth exceeds your plan's hi
  name: YouScan History API
  slug: youscan-history-api
- description: 'Retrieve and update mentions collected in a topic. ### How to effectively retrieve large sets of mentions Common scenarios are: * Load all the mentions from a given topic for a given period * Periodic'
  name: YouScan Mentions API
  slug: youscan-mentions-api
- description: Spaces available to the authenticated user and categories configured in them.
  name: YouScan Spaces API
  slug: youscan-spaces-api
- description: 'Aggregated statistics for mentions of a topic. ### Dates `from` and `to` are dates (`yyyy-MM-dd`); `to` is inclusive. Day boundaries are computed in the API key owner''s time zone (see *Dates and time '
  name: YouScan Statistics API
  slug: youscan-statistics-api
- description: Manage tags created in your topic.
  name: YouScan Tags API
  slug: youscan-tags-api
- description: 'Create and manage topics — the monitoring entities that collect mentions matching your queries. ### Topic query structure A topic query consists of a `textQuery` and/or `viQuery` (at least one is requ'
  name: YouScan Topics API
  slug: youscan-topics-api
- description: Webhooks push new mentions to your own server in real time, so you don't have to poll the API. Every time a new mention is found and saved to a topic, YouScan sends an HTTP `POST` with the mention pay
  name: YouScan Webhook API
  slug: youscan-webhook-api
artifact_total: 12
asyncapis:
- description: ''
  name: Youscan Mentions Webhooks
  slug: youscan-mentions-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://youscan.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.youscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.youscan.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.youscan.io/api/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.youscan.io
- group: operate
  title: ''
  type: Support
  url: https://help.youscan.io/en/collections/76280-integrations-and-api
- group: company
  title: ''
  type: Blog
  url: https://youscan.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://youscan.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.youscan.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://youscan.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://youscan.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/youscan
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/youscan-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/youscan-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/youscan-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/youscan-mentions-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/youscan-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/youscan-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/youscan-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/youscan-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/youscan-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/youscan-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/youscan-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/youscan-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: YouScan is an AI-powered social media listening and consumer-intelligence platform that monitors mentions, conversations, and images across social networks, news, blogs, forums, and review sites. It provides sentiment analysis, trend and topic detection, visual insights via image recognition, and an AI Insights Copilot for querying data in natural language. YouScan exposes a REST API (documented with an OpenAPI 3.1 specification) to manage monitoring topics, retrieve and stream mentions, manage tags, run data imports, and query statistics, plus outbound webhooks that push new mentions to subscriber endpoints in real time.
image: https://youscan.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: youscan-mcp.yml
  slug: youscan-mcpyml
modified: '2026-07-21'
name: YouScan
nav: Providers
network: true
overview: 'YouScan publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data Import API, History API, Mentions API, and 5 more. Tagged areas include Company, Social Media Listening, Social Intelligence, Consumer Insights, and Sentiment Analysis.


  The YouScan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  YouScan''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 18 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 52.0
  delta: -2.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 74.7
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 54.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Youscan Authentication
  slug: youscan-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Youscan Domain Security
  slug: youscan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: youscan
tags:
- Company
- Social Media Listening
- Social Intelligence
- Consumer Insights
- Sentiment Analysis
- Media Monitoring
- Analytics
- Artificial Intelligence
website: https://youscan.io
---
