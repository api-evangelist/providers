---
access_model:
  confidence: high
  label: Freemium, self-service
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://alphai.io/pricing
  - https://alphai.io/account/api-keys
  - https://alphai.io/developers
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: verified
    openapi_examples: documented
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 70.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alphaai Agentic Access
  operation_count: 15
  slug: alphaai-agentic-access
  summary_line: 15 operations
api_count: 3
apis:
- description: REST API for relevance-scored, ticker-linked financial news. Fifteen read-only operations across news feeds, trending, macro, an economic calendar, SEC Form 4 insider data, symbols, and per-ticker sen
  name: AlphaAI REST API
  slug: alphaai-rest-api
- description: Hosted MCP server over Streamable HTTP exposing fifteen tools for news search, ticker news, trending, actionable-now, macro, economic calendar, insider news, pair analysis, article retrieval, ticker d
  name: AlphaAI MCP Server
  slug: alphaai-mcp-server
- description: 'Provider-published open-source pack of five Claude Code agent skills wrapping the MCP tools into ready-made workflows: one-ticker brief, market pulse, insider-activity scan, two-ticker read-across, an'
  name: AlphaAI Claude Code Skills
  slug: alphaai-claude-code-skills
artifact_total: 14
asyncapis:
- description: ''
  name: Alphaai Webhooks
  slug: alphaai-webhooks
collections:
- collection_type: open
  name: alphai REST API
  slug: open-alphaai-rest-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alphai.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://alphai.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.alphai.io/api/schema/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://alphai.io/developers
- group: build
  title: ''
  type: Examples
  url: https://alphai.io/examples
- group: operate
  title: ''
  type: Support
  url: https://alphai.io/contact
- group: company
  title: ''
  type: Blog
  url: https://alphai.io/research
- group: company
  title: ''
  type: BlogRSS
  url: https://alphai.io/research/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeev
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mmakeevs-team/alphaai-financial-news-api
- group: commercial
  title: ''
  type: Pricing
  url: https://alphai.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://alphai.io/account/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphai.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alphai.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://alphai.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alphaai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alphaai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alphaai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alphaai-scopes.yml
- group: auth
  title: ''
  type: Security
  url: https://api.alphai.io/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/alphaai-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alphaai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphaai-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alphaai-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alphaai-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alphaai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alphaai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alphaai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/alphaai-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alphaai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/alphaai-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/alphaai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alphaai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/alphaai-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alphaai-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alphaai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alphaai-agentic-access.yml
created: '2026-07-05'
description: A REST API and agent-native platform for relevance-scored, ticker-linked financial news, built for trading bots, agent backends, and dashboards. Every article is enriched at ingest with a 1-10 relevance score, one of fourteen categories, validated ticker links, and per-ticker sentiment with an impact analysis and confidence rating, plus structured SEC Form 4 insider data sourced from EDGAR. The same data core is served three ways — an OpenAPI 3.1 REST API at api.alphai.io, a hosted MCP server with OAuth 2.1 and dynamic client registration at mcp.alphai.io, and HMAC-signed webhooks on the Pro tier — alongside first-party Python, TypeScript and Rust clients and a provider-published pack of Claude Code agent skills.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphaai.png
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: alphaai-mcp.yml
  slug: alphaai-mcpyml
modified: '2026-08-11'
name: AlphaAI
nav: Providers
network: true
overview: 'AlphaAI publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Financial News, Stock Market, SEC Filings, Insider Trading, and Fintech.


  The AlphaAI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AlphaAI''s developer surface includes documentation, API reference, getting-started guide, code examples, support, engineering blog, pricing, and 32 more developer resources.'
plans:
- name: Alphaai Plans Pricing
  plan_count: 4
  slug: alphaai-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 6
  name: Alphaai Rate Limits
  slug: alphaai-rate-limits
scopes:
- name: Alphaai Scopes
  scope_count: 2
  slug: alphaai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.4
  delta: 1.3
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 16.7
    contract_quality: 67.1
    developer_ergonomics: 85.7
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 84.2
  previous_composite: 72.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 71.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphaai/refs/heads/main/screenshots/alphaai-2026-08-17T080047.png
security:
- kind: authentication
  name: Alphaai Authentication
  slug: alphaai-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Alphaai Domain Security
  slug: alphaai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Alphaai Vulnerability Disclosure
  slug: alphaai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: alphaai
tags:
- Financial News
- Stock Market
- SEC Filings
- Insider Trading
- Fintech
- Market Data
- Sentiment
- AI Agents
- MCP
- LLM
- Trading
website: https://alphai.io/developers
---
