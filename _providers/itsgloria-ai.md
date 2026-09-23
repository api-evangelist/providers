---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Itsgloria Ai Agentic Access
  operation_count: 20
  slug: itsgloria-ai-agentic-access
  summary_line: 20 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ai-hub.cryptobriefing.com
  baseurl_source: declared
  description: REST API for curated crypto news with sentiment analysis, per-category AI recaps, narrative story arcs, long-form articles and feed categories, plus API-token and social-bot management. Authentication
  name: Gloria Data Platform REST API
  slug: gloria-data-platform-rest-api
- description: 'Pay-per-request access to Gloria news over the x402 protocol with no account or API key: GET /news ($0.03), /news-ticker-summary ($0.031), /news-by-keyword ($0.05) and /recaps ($0.10), each answering '
  name: Gloria x402 API
  slug: gloria-x402-api
- description: Hosted, remote MCP server (Streamable HTTP at https://mcp.itsgloria.ai/mcp, serverInfo "Gloria AI" 1.26.0, protocol 2025-06-18) exposing seven tools - five free (get_latest_news, get_news_recap, searc
  name: Gloria MCP Server
  slug: gloria-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Itsgloria Ai Websocket Feed
  slug: itsgloria-ai-websocket-feed
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/security/itsgloria-ai-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/packages/itsgloria-ai-packages.yml
  title: ''
  type: Packages
  url: packages/itsgloria-ai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/well-known/itsgloria-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/itsgloria-ai-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/well-known/itsgloria-ai-ai-plugin.json
  title: ''
  type: PluginManifest
  url: well-known/itsgloria-ai-ai-plugin.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/llms/itsgloria-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/itsgloria-ai-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/conformance/itsgloria-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itsgloria-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/lifecycle/itsgloria-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/itsgloria-ai-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/authentication/itsgloria-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/itsgloria-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/conventions/itsgloria-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/itsgloria-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/errors/itsgloria-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/itsgloria-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/data-model/itsgloria-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/itsgloria-ai-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/plans/itsgloria-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/itsgloria-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/rate-limits/itsgloria-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/itsgloria-ai-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/regulatory/itsgloria-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/itsgloria-ai-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/agentic-access/itsgloria-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/itsgloria-ai-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/itsgloria-ai/refs/heads/main/x402/itsgloria-ai-x402.yml
  title: ''
  type: X-X402
  url: x402/itsgloria-ai-x402.yml
created: '2026-09-19'
description: 'Gloria (Gloria AI Ltd., a Crypto Briefing product) is an AI-powered crypto and prediction-market news intelligence platform: a real-time feed of curated headlines scraped from crypto Twitter and newswires, filtered by a multi-stage LLM pipeline and enriched with sentiment, entity extraction, narratives, category recaps and long-form articles. The same data core is exposed four ways - a 20-operation REST API (OpenAPI 3.0.3 at itsgloria.ai/openapi.json, base https://ai-hub.cryptobriefing.com) authenticated by SIWE wallet signature or long-lived API tokens, a WebSocket push feed, a hosted MCP server at mcp.itsgloria.ai with seven tools that answers an anonymous tools/list, and an x402 pay-per-request API at api.itsgloria.ai settled in USDC on Base - plus Telegram and Discord bots.'
image: https://docs.itsgloria.ai/img/gloria-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Gloria AI
  slug: gloria-ai
- description: ''
  name: Live remote endpoint (Streamable HTTP)
  slug: live-remote-endpoint-streamable-http
modified: '2026-09-19'
name: Gloria
nav: Providers
network: true
overview: 'Gloria publishes 1 API on the [APIs.io](https://apis.io/) network: Data Platform REST API. Tagged areas include Company, News, Crypto, Cryptocurrency, and Market Intelligence.


  The Gloria catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gloria''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, and 26 more developer resources.'
plans:
- name: Itsgloria Ai Plans Pricing
  plan_count: 5
  slug: itsgloria-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Itsgloria Ai Rate Limits
  slug: itsgloria-ai-rate-limits
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 56.0
    developer_ergonomics: 56.5
    discoverability: 68.5
    operational_transparency: 31.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Itsgloria Ai Authentication
  slug: itsgloria-ai-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Itsgloria Ai Domain Security
  slug: itsgloria-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: itsgloria-ai
tags:
- Company
- News
- Crypto
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
