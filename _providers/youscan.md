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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: The Data Import API allows you to import mentions from external sources into YouScan topics. This feature enables you to bring historical data or mentions from sources not natively supported by YouSca
  name: YouScan Data Import API
  slug: youscan-data-import-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: Manage historical data collection for a topic. Starting a collection can return `400` if a collection is already running, if the date range is invalid, or if the requested depth exceeds your plan's hi
  name: YouScan History API
  slug: youscan-history-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: 'Retrieve and update mentions collected in a topic. ### How to effectively retrieve large sets of mentions Common scenarios are: * Load all the mentions from a given topic for a given period * Periodic'
  name: YouScan Mentions API
  slug: youscan-mentions-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: Spaces available to the authenticated user and categories configured in them.
  name: YouScan Spaces API
  slug: youscan-spaces-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: 'Aggregated statistics for mentions of a topic. ### Dates `from` and `to` are dates (`yyyy-MM-dd`); `to` is inclusive. Day boundaries are computed in the API key owner''s time zone (see *Dates and time '
  name: YouScan Statistics API
  slug: youscan-statistics-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: Manage tags created in your topic.
  name: YouScan Tags API
  slug: youscan-tags-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: 'Create and manage topics — the monitoring entities that collect mentions matching your queries. ### Topic query structure A topic query consists of a `textQuery` and/or `viQuery` (at least one is requ'
  name: YouScan Topics API
  slug: youscan-topics-api
- baseURL: https://api.youscan.io/api/external
  baseurl_source: declared
  description: Webhooks push new mentions to your own server in real time, so you don't have to poll the API. Every time a new mention is found and saved to a topic, YouScan sends an HTTP `POST` with the mention pay
  name: YouScan Webhook API
  slug: youscan-webhook-api
artifact_total: 25
asyncapis:
- description: ''
  name: Youscan Mentions Webhooks
  slug: youscan-mentions-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: YouScan Data Import API
  slug: open-youscan-data-import-api
- collection_type: open
  name: YouScan Data Import History API
  slug: open-youscan-history-api
- collection_type: open
  name: YouScan Data Import Mentions API
  slug: open-youscan-mentions-api
- collection_type: open
  name: YouScan Data Import Spaces API
  slug: open-youscan-spaces-api
- collection_type: open
  name: YouScan Data Import Statistics API
  slug: open-youscan-statistics-api
- collection_type: open
  name: YouScan Data Import Tags API
  slug: open-youscan-tags-api
- collection_type: open
  name: YouScan Data Import Topics API
  slug: open-youscan-topics-api
- collection_type: open
  name: YouScan Data Import Webhook API
  slug: open-youscan-webhook-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/youscan-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/youscan-openapi-overlay.yaml
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
- group: start
  title: ''
  type: GettingStarted
  url: https://help.youscan.io/en/articles/2754452-how-to-use-youscan-api
- group: auth
  title: ''
  type: Security
  url: security/youscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/youscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/youscan-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/youscan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/youscan-rate-limits.yml
created: '2026-07-17'
description: YouScan is an AI-powered social media listening and consumer-intelligence platform that monitors mentions, conversations, and images across social networks, news, blogs, forums, and review sites. It provides sentiment analysis, trend and topic detection, visual insights via image recognition, and an AI Insights Copilot for querying data in natural language. YouScan exposes a REST API (documented with an OpenAPI 3.1 specification) to manage monitoring topics, retrieve and stream mentions, manage tags, run data imports, and query statistics, plus outbound webhooks that push new mentions to subscriber endpoints in real time.
image: https://youscan.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: YouScan MCP Server
  slug: youscan-mcp-server
modified: '2026-08-13'
name: YouScan
nav: Providers
network: true
overview: 'YouScan publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data Import API, History API, Mentions API, and 5 more. Tagged areas include Company, Social Media Listening, Social Intelligence, Consumer Insights, and Sentiment Analysis.


  The YouScan catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  YouScan''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Youscan Plans Pricing
  plan_count: 2
  slug: youscan-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Youscan Rate Limits
  slug: youscan-rate-limits
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 66.2
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 57.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/youscan/refs/heads/main/screenshots/youscan-2026-08-17T080440.png
security:
- kind: authentication
  name: Youscan Authentication
  slug: youscan-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Youscan Domain Security
  slug: youscan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Youscan Vulnerability Disclosure
  slug: youscan-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Youscan Trust Center
  slug: youscan-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, GDPR
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
