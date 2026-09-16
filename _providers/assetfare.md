---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://api.assetfare.dev
  baseurl_source: declared
  description: Public REST API for the solana:SOL -> base:ETH corridor. Public no-auth quote/status/manifest endpoints plus bearer-protected session and execution workflow. Includes hosted MCP server, llms.txt agent
  name: AssetFare Agent-native Route API
  slug: assetfare-agent-native-route-api
arazzos:
- description: Verify AssetFare and obtain a fresh Solana SOL to Base or Arbitrum ETH quote.
  name: AssetFare read-only route evaluation
  slug: assetfare-route-evaluation-arazzo
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/security/assetfare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetfare-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/security/assetfare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/assetfare-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/authentication/assetfare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/assetfare-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/well-known/assetfare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assetfare-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/well-known/assetfare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assetfare-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/well-known/assetfare-security.txt
  title: ''
  type: Security
  url: well-known/assetfare-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assetfare/refs/heads/main/mcp/assetfare-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/assetfare-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://assetfare.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://assetfare.dev/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assetfare.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assetfare.dev/privacy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/odaiin/assetfare-mcp
- group: company
  title: ''
  type: Website
  url: https://assetfare.dev/
created: '2026-09-14'
description: A capped, non-custodial routing API for a single corridor — Solana SOL to Base native ETH — aimed at AI agents. It returns fee-inclusive quotes and bounded unsigned actions; the caller's agent verifies, signs, and submits every transaction. AssetFare never receives private keys and never signs or submits, framing itself as one route candidate rather than a market-wide best-price aggregator.
layout: provider
mcp_servers:
- description: ''
  name: AssetFare MCP Server
  slug: assetfare-mcp-server
- description: Official hosted, non-custodial MCP server for the capped Solana SOL to Base/Arbitrum ETH corridors. Listed in the official MCP Registry (status active). tools/list is anonymous; read tools are open, e
  name: AssetFare
  slug: assetfare
modified: '2026-09-14'
name: AssetFare
nav: Providers
network: true
overview: 'AssetFare publishes 1 API on the [APIs.io](https://apis.io/) network: Agent-native Route API. Tagged areas include AI Agents, Asset Transfer, Bridge, Cross-Chain, and Non-Custodial.


  AssetFare''s developer surface includes authentication, pricing, and 12 more developer resources.'
plans:
- name: Assetfare Plans Pricing
  plan_count: 1
  slug: assetfare-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Assetfare Rate Limits
  slug: assetfare-rate-limits
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 45.2
    discoverability: 72.2
    operational_transparency: 63.2
  previous_composite: 45.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Assetfare Authentication
  slug: assetfare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Assetfare Domain Security
  slug: assetfare-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Assetfare Vulnerability Disclosure
  slug: assetfare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: assetfare
tags:
- AI Agents
- Asset Transfer
- Bridge
- Cross-Chain
- Non-Custodial
- Cryptocurrency
- Solana
- Base
- OpenAPI
- MCP
- Agent Skills
website: https://assetfare.dev/
---
