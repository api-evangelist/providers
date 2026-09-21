---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Warppay402 Com Agentic Access
  operation_count: 19
  slug: warppay402-com-agentic-access
  summary_line: 19 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.warppay402.com
  baseurl_source: declared
  description: 'REST surface of the WarpPay402 gateway at https://api.warppay402.com: 19 operations (2 GET feeds, 1 GET yield read, 16 POST tools) covering web, browser, PDF and screenshot extraction, structured JSON'
  name: WarpPay402 Monetized MCP Tools API
  slug: warppay402-monetized-mcp-tools-api
- description: Hosted MCP server at https://api.warppay402.com/mcp exposing the same 19 tools as the REST API (public_data_feed, data_feeds, web_scraper, browser_scraper, base_analytics, arc_analytics, arc_network_o
  name: WarpPay402 MCP Server
  slug: warppay402-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://warppay402.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Warppay402
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.warppay402.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.warppay402.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/llms/warppay402-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/warppay402-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.warppay402.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/a2a/warppay402-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/warppay402-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/well-known/warppay402-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/warppay402-com-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/packages/warppay402-com-packages.yml
  title: ''
  type: Packages
  url: packages/warppay402-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/packages/warppay402-com-packages.yml
  title: ''
  type: SDKs
  url: packages/warppay402-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/conformance/warppay402-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/warppay402-com-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/authentication/warppay402-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/warppay402-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/conventions/warppay402-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/warppay402-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/errors/warppay402-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/warppay402-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/lifecycle/warppay402-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/warppay402-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/security/warppay402-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/warppay402-com-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/plans/warppay402-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/warppay402-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/rate-limits/warppay402-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/warppay402-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/agentic-access/warppay402-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/warppay402-com-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/warppay402-com/refs/heads/main/regulatory/warppay402-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/warppay402-com-regulatory-posture.yml
created: '2026-09-19'
description: 'WarpPay402 Studio operates WarpPay402, a non-custodial x402 monetization gateway and hosted MCP tool suite for autonomous AI agents. Nineteen pay-per-use tools — Markdown and headless-browser web scraping, PDF text extraction, full-page screenshots, schema-driven JSON extraction, Base and Arc network analytics, Basescan contract verification, Aerodrome yield, swap, concentrated-liquidity and veAERO routes, contract deployment factories for Base, Solana and Arc, and Circle CCTP bridging — are exposed three ways from one host: a REST API described by an OpenAPI 3.1 document at api.warppay402.com/openapi.json, a hosted MCP server at api.warppay402.com/mcp (Streamable HTTP and legacy SSE, 19 tools listed anonymously), and an agent card at /.well-known/agent.json. There are no API keys: every call answers HTTP 402 with an x402 v2 PAYMENT-REQUIRED challenge and settles in USDC on Base, Solana, Arbitrum One or Arc (prices from $0.0001 to $5.00 per call), with flat-rate access tokens
  offered by email. The company also publishes @warppay402/server, the x402 middleware its Self-Serve Gateway is built on, so other developers can wrap their own APIs and MCP tools in the same 402 challenge, and @warppay402/sdk plus a stdio MCP bridge for Cursor, Windsurf and Claude Desktop. The site is a Google Sites page; all documentation lives on it and in the npm READMEs.'
image: https://raw.githubusercontent.com/golfgolfgolf200/warppay-mcp-skill/master/warppay-real-logo.png
layout: provider
mcp_servers:
- description: WarpPay402 operates a hosted MCP server at https://api.warppay402.com/mcp. It answers Streamable-HTTP JSON-RPC POSTs directly (200 application/json) and also the legacy HTTP+SSE transport (GET /mcp op
  name: WarpPay402 Backend
  slug: warppay402-backend
modified: '2026-09-19'
name: WarpPay402 Studio
nav: Providers
network: true
overview: 'WarpPay402 Studio publishes 1 API on the [APIs.io](https://apis.io/) network: WarpPay402 Monetized MCP Tools API. Tagged areas include x402, Micropayments, AI Agents, MCP, and A2A.


  WarpPay402 Studio''s developer surface includes authentication and 20 more developer resources.'
plans:
- name: Warppay402 Com Plans Pricing
  plan_count: 2
  slug: warppay402-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Warppay402 Com Rate Limits
  slug: warppay402-com-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 38.9
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Warppay402 Com Authentication
  slug: warppay402-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Warppay402 Com Domain Security
  slug: warppay402-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: warppay402-com
tags:
- x402
- Micropayments
- AI Agents
- MCP
- A2A
- agent-native
- Web Scraping
- Data Extraction
- Blockchain
- DeFi
- Base
- Solana
- Smart Contracts
- Data Feed
- Developer Tools
website: https://warppay402.com/
---
