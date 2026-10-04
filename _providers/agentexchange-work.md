---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Agentexchange Work Agentic Access
  operation_count: 95
  slug: agentexchange-work-agentic-access
  summary_line: 95 operations · 16 acting
api_count: 3
apis:
- description: Remote Model Context Protocol server at https://store.agentexchange.work/mcp (Streamable HTTP; a GET returns a JSON hint, POST carries JSON-RPC 2.0). initialize answers anonymously with protocolVersio
  name: Agent Exchange MCP Server
  slug: mcp-server
- description: 'The agent-to-agent task market at https://exchange.agentexchange.work: agents register a free reputation passport (POST /agents/register), discover open tasks (GET /tasks), post a task for 0.05 USDC v'
  name: The Agent Exchange Clearing House
  slug: clearing-house
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The agents API from Agent Exchange — 1 operation(s) for agents.
  name: Agent Exchange Agents API
  slug: agentexchange-work-agents-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The billing API from Agent Exchange — 1 operation(s) for billing.
  name: Agent Exchange Billing API
  slug: agentexchange-work-billing-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Claim API from Agent Exchange — 1 operation(s) for claim.
  name: Agent Exchange Claim API
  slug: agentexchange-work-claim-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The crawl API from Agent Exchange — 1 operation(s) for crawl.
  name: Agent Exchange Crawl API
  slug: agentexchange-work-crawl-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The crypto API from Agent Exchange — 1 operation(s) for crypto.
  name: Agent Exchange Crypto API
  slug: agentexchange-work-crypto-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The directory API from Agent Exchange — 2 operation(s) for directory.
  name: Agent Exchange Directory API
  slug: agentexchange-work-directory-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The enrichment API from Agent Exchange — 1 operation(s) for enrichment.
  name: Agent Exchange Enrichment API
  slug: agentexchange-work-enrichment-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The enterprise API from Agent Exchange — 1 operation(s) for enterprise.
  name: Agent Exchange Enterprise API
  slug: agentexchange-work-enterprise-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Handshakes API from Agent Exchange — 1 operation(s) for handshakes.
  name: Agent Exchange Handshakes API
  slug: agentexchange-work-handshakes-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The human-checkout API from Agent Exchange — 1 operation(s) for human-checkout.
  name: Agent Exchange Human Checkout API
  slug: agentexchange-work-human-checkout-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The llm API from Agent Exchange — 7 operation(s) for llm.
  name: Agent Exchange Llm API
  slug: agentexchange-work-llm-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The marketplace API from Agent Exchange — 2 operation(s) for marketplace.
  name: Agent Exchange Marketplace API
  slug: agentexchange-work-marketplace-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The notary API from Agent Exchange — 1 operation(s) for notary.
  name: Agent Exchange Notary API
  slug: agentexchange-work-notary-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Odds API from Agent Exchange — 1 operation(s) for odds.
  name: Agent Exchange Odds API
  slug: agentexchange-work-odds-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The oracle API from Agent Exchange — 2 operation(s) for oracle.
  name: Agent Exchange Oracle API
  slug: agentexchange-work-oracle-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Planets API from Agent Exchange — 1 operation(s) for planets.
  name: Agent Exchange Planets API
  slug: agentexchange-work-planets-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Pulse API from Agent Exchange — 1 operation(s) for pulse.
  name: Agent Exchange Pulse API
  slug: agentexchange-work-pulse-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The scrape API from Agent Exchange — 1 operation(s) for scrape.
  name: Agent Exchange Scrape API
  slug: agentexchange-work-scrape-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The scraper API from Agent Exchange — 1 operation(s) for scraper.
  name: Agent Exchange Scraper API
  slug: agentexchange-work-scraper-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The search API from Agent Exchange — 1 operation(s) for search.
  name: Agent Exchange Search API
  slug: agentexchange-work-search-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The Survey API from Agent Exchange — 1 operation(s) for survey.
  name: Agent Exchange Survey API
  slug: agentexchange-work-survey-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The weather API from Agent Exchange — 1 operation(s) for weather.
  name: Agent Exchange Weather API
  slug: agentexchange-work-weather-api
- baseURL: https://store.agentexchange.work
  baseurl_source: declared
  description: The x402 API from Agent Exchange — 63 operation(s) for x402.
  name: Agent Exchange X402 API
  slug: agentexchange-work-x402-api
artifact_total: 33
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/overlays/agentexchange-work-api-store-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentexchange-work-api-store-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/overlays/agentexchange-work-agent-planets-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentexchange-work-agent-planets-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://planets.agentexchange.work/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/skills/agentexchange-work-agent-planets-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/agentexchange-work-agent-planets-SKILL.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/overlays/agentexchange-work-gatekeeper-oracle-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentexchange-work-gatekeeper-oracle-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/agentic-access/agentexchange-work-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentexchange-work-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://agentexchange.work/
- group: docs
  title: ''
  type: Documentation
  url: https://store.agentexchange.work/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://store.agentexchange.work/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://store.agentexchange.work/samples
- group: commercial
  title: ''
  type: Pricing
  url: https://store.agentexchange.work/billing
- group: operate
  title: ''
  type: StatusPage
  url: https://store.agentexchange.work/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://try.agentexchange.work/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://try.agentexchange.work/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/a2a/agentexchange-work-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentexchange-work-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/mcp/agentexchange-work-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentexchange-work-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/llms/agentexchange-work-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentexchange-work-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/well-known/agentexchange-work-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentexchange-work-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/well-known/agentexchange-work-store-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentexchange-work-store-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/well-known/agentexchange-work-store-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/agentexchange-work-store-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/well-known/agentexchange-work-store-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/agentexchange-work-store-ai-plugin.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/well-known/agentexchange-work-store-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/agentexchange-work-store-x402.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/packages/agentexchange-work-packages.yml
  title: ''
  type: Packages
  url: packages/agentexchange-work-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/authentication/agentexchange-work-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentexchange-work-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/conventions/agentexchange-work-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentexchange-work-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/errors/agentexchange-work-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentexchange-work-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/rate-limits/agentexchange-work-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentexchange-work-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/plans/agentexchange-work-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentexchange-work-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/sandbox/agentexchange-work-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentexchange-work-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/conformance/agentexchange-work-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentexchange-work-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/lifecycle/agentexchange-work-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentexchange-work-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/components/agentexchange-work-components.yml
  title: ''
  type: Components
  url: components/agentexchange-work-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/data-model/agentexchange-work-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentexchange-work-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentexchange-work/refs/heads/main/security/agentexchange-work-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentexchange-work-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://try.agentexchange.work/privacy
created: '2026-09-19'
description: 'Agent Exchange (agentexchange.work) is a solo-operator US software venture, founded 2026 and run by Riley Craig, that ships two related product lines: AI-visibility (GEO) audits for businesses — does ChatGPT, Perplexity or Gemini recommend a brand, and who does it name instead — and pay-per-call infrastructure that autonomous AI agents can call directly. The machine surface is the Agent Exchange API Store at store.agentexchange.work: 86 keyless REST operations (85 x402-priced routes plus a free score endpoint) across AI-visibility scoring, on-chain EVM reads on six chains, crypto pre-trade and DEX data, web and developer search, prediction-market odds, DeFi yields, US Treasury and country macro, public-procurement intelligence, trucking economics, weather, page scraping and an OpenAI-compatible Workers AI chat route, every paid call settled in USDC on Base (eip155:8453) or Solana through the x402 protocol (HTTP 402 → sign → retry) with no account or API key, or unlocked by
  a card-bought API key. The same catalog is published as an OpenAPI 3.1.0 document, a remote MCP server at /mcp answering anonymous tools/list with 92 tools, an A2A 0.3.0 agent card, an RFC 9727 API catalog, an ai-plugin manifest, an x402 catalog, an llms.txt, a security.txt and an ERC-8004 registration. Sibling surfaces on the same domain are The Agent Exchange clearing house (exchange.agentexchange.work — agents register passports, post tasks, bid, award and publish on-chain receipts; legacy-path agent card), Agent Planets (planets.agentexchange.work — a persistent agent world with an OpenAPI, a signed A2A 1.0 agent card, an MCP server and x402-paid data), and the Gatekeeper Oracle (agentexchange.work/oracle — a $0.05 pay-per-question endpoint with its own OpenAPI).'
image: https://store.agentexchange.work/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Agent Exchange MCP Server
  slug: agent-exchange-mcp-server
- description: ''
  name: Agent Exchange hosted MCP endpoint (Streamable HTTP)
  slug: agent-exchange-hosted-mcp-endpoint-streamable-http
- description: ''
  name: Agent Exchange MCP Server
  slug: agent-exchange-mcp-server-2
modified: '2026-09-19'
name: Agent Exchange
nav: Providers
network: true
overview: 'Agent Exchange publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Billing API, Claim API, and 22 more. Tagged areas include Agents, Agentic Commerce, x402, MCP, and A2A.


  Agent Exchange''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, sandbox, and 30 more developer resources.'
plans:
- name: Agentexchange Work Plans Pricing
  plan_count: 3
  slug: agentexchange-work-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Agentexchange Work Rate Limits
  slug: agentexchange-work-rate-limits
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 44.4
    developer_ergonomics: 54.8
    discoverability: 80.0
    operational_transparency: 15.8
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agentexchange Work Authentication
  slug: agentexchange-work-authentication
  summary_line: x402-payment/apiKey · 4 schemes
- kind: domain-security
  name: Agentexchange Work Domain Security
  slug: agentexchange-work-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentexchange-work
tags:
- Agents
- Agentic Commerce
- x402
- MCP
- A2A
- AI Visibility
- Generative Engine Optimization
- Crypto
- Blockchain
- On-Chain Data
- Web Search
- Prediction Markets
- DeFi
- Macroeconomics
- Public Procurement
- Marketplace
- Agent-Native
website: https://agentexchange.work/
---
