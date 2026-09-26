---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://cymetica.com/api/v1
  baseurl_source: declared
  description: 'Curated public REST surface of EventTrader, Cymetica''s perpetual prediction market and CLOB exchange: register and mint API keys, OAuth 2.0 (PKCE) token flows, list markets and exchange pairs, read or'
  name: EventTrader Public API
  slug: eventtrader-public-api
- description: Hosted Streamable-HTTP MCP endpoint at https://cymetica.com/mcp/v1 (protocol 2025-03-26) answering anonymous tools/list with 57 annotated tools — markets, orderbooks, funds research, ontology, agent r
  name: EventTrader MCP Server
  slug: eventtrader-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Cymetica Com Webhooks
  slug: cymetica-com-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://cymetica.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cymetica.com/build
- group: docs
  title: ''
  type: Documentation
  url: https://cymetica.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cymetica.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://cymetica.com/contact
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/JCn76KcVmk
- group: company
  title: ''
  type: Blog
  url: https://cymetica.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://cymetica.com/press
- group: other
  title: ''
  type: Leadership
  url: https://cymetica.com/about
- group: start
  title: ''
  type: SignUp
  url: https://cymetica.com/signup
- group: start
  title: ''
  type: Login
  url: https://cymetica.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cymetica.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cymetica.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/llms/cymetica-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cymetica-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/a2a/cymetica-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cymetica-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/well-known/cymetica-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cymetica-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/well-known/cymetica-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cymetica-com-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/security/cymetica-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cymetica-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/security/cymetica-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cymetica-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/security/cymetica-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cymetica-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/authentication/cymetica-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cymetica-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/scopes/cymetica-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cymetica-com-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/packages/cymetica-com-packages.yml
  title: ''
  type: Packages
  url: packages/cymetica-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/packages/cymetica-com-packages.yml
  title: ''
  type: SDKs
  url: packages/cymetica-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/conformance/cymetica-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cymetica-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cymetica-com/refs/heads/main/lifecycle/cymetica-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cymetica-com-lifecycle.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://cymetica.com/privacy
- group: other
  title: ''
  type: AITransparency
  url: https://cymetica.com/privacy
created: '2026-09-19'
description: 'Cymetica (Berkeley, California; founded November 2025 by Kasian Franks) is the company behind EventTrader, an AI-native perpetual prediction market and hybrid CEX-DEX exchange: a central limit order book with 500+ pairs, EVCDX event-card index markets, clonable AI trading agent species, AI-managed funds and a token launchpad, with off-chain matching and on-chain settlement on Base L2 and Ethereum. It publishes an unusually complete agent-facing surface from one origin — a curated OpenAPI 3.1 REST contract, a hosted MCP server with an open tools/list, an A2A agent card, an AsyncAPI 3.0 WebSocket description, llms.txt, OAuth 2.0 with PKCE and RFC 8414/9728 discovery, UCP/ACP/x402 commerce manifests, security.txt and TypeScript/Python SDKs.'
image: https://cymetica.com/static/img/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: Cymetica MCP Server
  slug: cymetica-mcp-server
modified: '2026-09-19'
name: Cymetica
nav: Providers
network: true
overview: 'Cymetica publishes 2 APIs on the [APIs.io](https://apis.io/) network, including EventTrader Public API, and 1 more. Tagged areas include Prediction Markets, Cryptocurrency Exchange, Trading, AI Agents, and MCP.


  The Cymetica catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cymetica''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Cymetica Com Plans Pricing
  plan_count: 4
  slug: cymetica-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 13
  name: Cymetica Com Rate Limits
  slug: cymetica-com-rate-limits
scopes:
- name: Cymetica Com Scopes
  scope_count: 3
  slug: cymetica-com-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 62.0
    developer_ergonomics: 78.6
    discoverability: 78.3
    operational_transparency: 50.0
  previous_composite: 67.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 47.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cymetica Com Authentication
  slug: cymetica-com-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Cymetica Com Domain Security
  slug: cymetica-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cymetica Com Vulnerability Disclosure
  slug: cymetica-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cymetica-com
tags:
- Prediction Markets
- Cryptocurrency Exchange
- Trading
- AI Agents
- MCP
- Agent-Native
- Blockchain
- DeFi
- Financial Services
- Market Data
- A2A
- Real-Time
website: https://cymetica.com/
---
