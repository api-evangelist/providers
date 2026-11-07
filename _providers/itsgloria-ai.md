---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Itsgloria Ai Agentic Access
  operation_count: 20
  slug: itsgloria-ai-agentic-access
  summary_line: 20 operations · 5 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'Pay-per-request access to Gloria news over the x402 protocol with no account or API key: GET /news ($0.03), /news-ticker-summary ($0.031), /news-by-keyword ($0.05) and /recaps ($0.10), each answering '
  name: Gloria X402 API
  slug: gloria-x402-api
- description: Hosted, remote MCP server (Streamable HTTP at https://mcp.itsgloria.ai/mcp, serverInfo "Gloria AI" 1.26.0, protocol 2025-06-18) exposing seven tools - five free (get_latest_news, get_news_recap, searc
  name: Gloria MCP Server
  slug: gloria-mcp-server
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Manage long-lived API tokens
  name: Gloria API Keys API
  slug: itsgloria-ai-api-keys-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Long-form articles generated from news events
  name: Gloria Articles API
  slug: itsgloria-ai-articles-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Wallet-based authentication (SIWE) and token management
  name: Gloria Authentication API
  slug: itsgloria-ai-authentication-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Social platform bot registration (Telegram, Discord)
  name: Gloria Bots API
  slug: itsgloria-ai-bots-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Available feed categories
  name: Gloria Categories API
  slug: itsgloria-ai-categories-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Service health checks
  name: Gloria Health API
  slug: itsgloria-ai-health-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Market narrative threads grouping related news
  name: Gloria Narratives API
  slug: itsgloria-ai-narratives-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Real-time crypto news feed with sentiment analysis
  name: Gloria News API
  slug: itsgloria-ai-news-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Periodic summaries per feed category
  name: Gloria Recaps API
  slug: itsgloria-ai-recaps-api
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: Real-time news feed via WebSocket
  name: Gloria WebSocket API
  slug: itsgloria-ai-websocket-api
artifact_total: 26
asyncapis:
- description: ''
  name: Itsgloria Ai Websocket Feed
  slug: itsgloria-ai-websocket-feed
common:
- group: other
  href: https://artifacts.apis.io/itsgloria-ai/capabilities/itsgloria-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/itsgloria-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/itsgloria-ai/overlays/itsgloria-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/itsgloria-ai-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/itsgloria-ai/security/itsgloria-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/itsgloria-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itsgloria.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.itsgloria.ai/api-keys-new
- group: docs
  title: ''
  type: Documentation
  url: https://docs.itsgloria.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.itsgloria.ai/gloria-data-platform/api-integration/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.itsgloria.ai/gloria-data-platform/overview/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.itsgloria.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itsgloria.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itsgloria.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/UFa4HK2Vjv
- group: operate
  title: ''
  type: Contact
  url: https://www.itsgloria.ai/contact
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.itsgloria.ai/roadmap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cryptobriefing-labs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/itsgloria_ai
- group: other
  title: ''
  type: Telegram
  url: https://t.me/itsgloria_ai
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/UFa4HK2Vjv
- group: build
  href: https://artifacts.apis.io/itsgloria-ai/packages/itsgloria-ai-packages.yml
  title: ''
  type: Packages
  url: packages/itsgloria-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/itsgloria-ai/well-known/itsgloria-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/itsgloria-ai-well-known.yml
- group: build
  href: https://artifacts.apis.io/itsgloria-ai/well-known/itsgloria-ai-ai-plugin.json
  title: ''
  type: PluginManifest
  url: well-known/itsgloria-ai-ai-plugin.json
- group: agent
  href: https://artifacts.apis.io/itsgloria-ai/llms/itsgloria-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/itsgloria-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/itsgloria-ai/conformance/itsgloria-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itsgloria-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/itsgloria-ai/lifecycle/itsgloria-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/itsgloria-ai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/itsgloria-ai/authentication/itsgloria-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/itsgloria-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/itsgloria-ai/conventions/itsgloria-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/itsgloria-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/itsgloria-ai/errors/itsgloria-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/itsgloria-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/itsgloria-ai/data-model/itsgloria-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/itsgloria-ai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/itsgloria-ai/plans/itsgloria-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/itsgloria-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/itsgloria-ai/rate-limits/itsgloria-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/itsgloria-ai-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/itsgloria-ai/regulatory/itsgloria-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/itsgloria-ai-regulatory-posture.yml
- group: agent
  href: https://artifacts.apis.io/itsgloria-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/itsgloria-ai/agentic-access/itsgloria-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/itsgloria-ai-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/itsgloria-ai/x402/itsgloria-ai-x402.yml
  title: ''
  type: X-X402
  url: x402/itsgloria-ai-x402.yml
created: '2026-09-19'
description: 'Gloria (Gloria AI Ltd., a Crypto Briefing product) is an AI-powered crypto and prediction-market news intelligence platform: a real-time feed of curated headlines scraped from crypto Twitter and newswires, filtered by a multi-stage LLM pipeline and enriched with sentiment, entity extraction, narratives, category recaps and long-form articles. The same data core is exposed four ways - a 20-operation REST API (OpenAPI 3.0.3 at itsgloria.ai/openapi.json, base https://ai-hub.cryptobriefing.com) authenticated by SIWE wallet signature or long-lived API tokens, a WebSocket push feed, a hosted MCP server at mcp.itsgloria.ai with seven tools that answers an anonymous tools/list, and an x402 pay-per-request API at api.itsgloria.ai settled in USDC on Base - plus Telegram and Discord bots.'
finops:
- has_sources: true
  method: derived
  name: Itsgloria Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: itsgloria-ai-finops
  template: false
image: https://docs.itsgloria.ai/img/gloria-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.itsgloria.ai over HTTP; 7 tools listed.
  name: Gloria AI
  slug: gloria-ai
modified: '2026-09-19'
name: Gloria
nav: Providers
network: true
overview: 'Gloria publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Articles API, Authentication API, and 9 more. Tagged areas include Company, News, Cryptocurrency, Market Intelligence, and Sentiment Analysis.


  The Gloria catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gloria''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, and 28 more developer resources.'
plans:
- name: Itsgloria Ai Plans Pricing
  plan_count: 4
  slug: itsgloria-ai-plans-pricing
- name: Itsgloria Ai Price Estimates
  plan_count: 0
  slug: itsgloria-ai-price-estimates
random_paper: 21
rate_limits:
- limit_count: 1
  name: Itsgloria Ai Rate Limits
  slug: itsgloria-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Gloria API Rules
  rule_count: 65
  severity_counts:
    error: 57
    hint: 0
    info: 3
    warn: 5
  slug: itsgloria-ai-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 54.5
    developer_ergonomics: 35.1
    discoverability: 68.3
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/itsgloria-ai/itsgloria-ai-2026-10-11T105903.png
security:
- kind: authentication
  name: Itsgloria Ai Authentication
  slug: itsgloria-ai-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Itsgloria Ai Domain Security
  slug: itsgloria-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Read the latest curated news
  slug: itsgloria-ai-read-latest-news
- name: Get a category recap and a ticker summary
  slug: itsgloria-ai-recap-and-ticker-summary
- name: Stream news in real time over WebSocket
  slug: itsgloria-ai-stream-news-websocket
- name: Authenticate with a wallet and manage API tokens
  slug: itsgloria-ai-wallet-auth-and-api-tokens
slug: itsgloria-ai
tags:
- Company
- News
- Cryptocurrency
- Market Intelligence
- Sentiment Analysis
- Prediction Markets
- Artificial Intelligence
- MCP
- x402
- WebSocket
- Agents
website: https://itsgloria.ai/
---
