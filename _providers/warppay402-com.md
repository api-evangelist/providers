---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Warppay402 Com Agentic Access
  operation_count: 19
  slug: warppay402-com-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 2
apis:
- description: Hosted MCP server at https://api.warppay402.com/mcp exposing the same 19 tools as the REST API (public_data_feed, data_feeds, web_scraper, browser_scraper, base_analytics, arc_analytics, arc_network_o
  name: WarpPay402 MCP Server
  slug: warppay402-mcp-server
- baseURL: https://api.warppay402.com
  baseurl_source: declared
  description: The Feeds API from WarpPay402 Studio — 1 operation(s) for feeds.
  name: WarpPay402 Studio Feeds API
  slug: warppay402-com-feeds-api
- baseURL: https://api.warppay402.com
  baseurl_source: declared
  description: The Public Data Feed API from WarpPay402 Studio — 1 operation(s) for public data feed.
  name: WarpPay402 Studio Public Data Feed API
  slug: warppay402-com-public-data-feed-api
- baseURL: https://api.warppay402.com
  baseurl_source: declared
  description: The Tools API from WarpPay402 Studio — 17 operation(s) for tools.
  name: WarpPay402 Studio Tools API
  slug: warppay402-com-tools-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/warppay402-com/overlays/warppay402-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/warppay402-com-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/warppay402-com/llms/warppay402-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/warppay402-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.warppay402.com/llms.txt
- group: other
  href: https://artifacts.apis.io/warppay402-com/a2a/warppay402-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/warppay402-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/warppay402-com/well-known/warppay402-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/warppay402-com-well-known.yml
- group: build
  href: https://artifacts.apis.io/warppay402-com/packages/warppay402-com-packages.yml
  title: ''
  type: Packages
  url: packages/warppay402-com-packages.yml
- group: build
  href: https://artifacts.apis.io/warppay402-com/packages/warppay402-com-packages.yml
  title: ''
  type: SDKs
  url: packages/warppay402-com-packages.yml
- group: design
  href: https://artifacts.apis.io/warppay402-com/conformance/warppay402-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/warppay402-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/warppay402-com/authentication/warppay402-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/warppay402-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/warppay402-com/conventions/warppay402-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/warppay402-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/warppay402-com/errors/warppay402-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/warppay402-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/warppay402-com/lifecycle/warppay402-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/warppay402-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/warppay402-com/security/warppay402-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/warppay402-com-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/warppay402-com/plans/warppay402-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/warppay402-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/warppay402-com/rate-limits/warppay402-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/warppay402-com-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/warppay402-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/warppay402-com/agentic-access/warppay402-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/warppay402-com-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/warppay402-com/regulatory/warppay402-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/warppay402-com-regulatory-posture.yml
created: '2026-09-19'
description: 'WarpPay402 Studio operates WarpPay402, a non-custodial x402 monetization gateway and hosted MCP tool suite for autonomous AI agents. Nineteen pay-per-use tools — Markdown and headless-browser web scraping, PDF text extraction, full-page screenshots, schema-driven JSON extraction, Base and Arc network analytics, Basescan contract verification, Aerodrome yield, swap, concentrated-liquidity and veAERO routes, contract deployment factories for Base, Solana and Arc, and Circle CCTP bridging — are exposed three ways from one host: a REST API described by an OpenAPI 3.1 document at api.warppay402.com/openapi.json, a hosted MCP server at api.warppay402.com/mcp (Streamable HTTP and legacy SSE, 19 tools listed anonymously), and an agent card at /.well-known/agent.json. There are no API keys: every call answers HTTP 402 with an x402 v2 PAYMENT-REQUIRED challenge and settles in USDC on Base, Solana, Arbitrum One or Arc (prices from $0.0001 to $5.00 per call), with flat-rate access tokens
  offered by email. The company also publishes @warppay402/server, the x402 middleware its Self-Serve Gateway is built on, so other developers can wrap their own APIs and MCP tools in the same 402 challenge, and @warppay402/sdk plus a stdio MCP bridge for Cursor, Windsurf and Claude Desktop. The site is a Google Sites page; all documentation lives on it and in the npm READMEs.'
finops:
- has_sources: true
  method: derived
  name: Warppay402 Com Finops
  primary_unit: call
  service_category: ''
  slug: warppay402-com-finops
  template: false
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
overview: 'WarpPay402 Studio publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Feeds API, Public Data Feed API, Tools API, and 1 more. Tagged areas include x402, Micropayments, AI Agents, MCP, and A2A.


  The WarpPay402 Studio catalog on APIs.io includes 1 Spectral governance ruleset.


  WarpPay402 Studio''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Warppay402 Com Plans Pricing
  plan_count: 11
  slug: warppay402-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Warppay402 Com Rate Limits
  slug: warppay402-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: WarpPay402 Studio API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: warppay402-com-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 39.8
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/warppay402-com/warppay402-com-2026-10-11T195520.png
security:
- kind: authentication
  name: Warppay402 Com Authentication
  slug: warppay402-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Warppay402 Com Domain Security
  slug: warppay402-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Read on-chain state before any DeFi or deployment write
  slug: warppay402-com-chain-read-before-write
- name: Call a WarpPay402 tool with an x402 micropayment
  slug: warppay402-com-pay-per-call-x402
- name: Extract web, browser, PDF and screenshot content
  slug: warppay402-com-web-intelligence
slug: warppay402-com
tags:
- x402
- Micropayments
- AI Agents
- MCP
- A2A
- Agent-Native
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
