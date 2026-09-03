---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Live Shopify-hosted storefront MCP endpoint for the Yeeps store, exposing catalog search, cart management, product details, and shop policy/FAQ tools over JSON-RPC (streamable HTTP). Probed live 2026-
  name: Yeeps Storefront MCP
  slug: yeeps-storefront-mcp
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trass-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trass.games
- group: company
  title: ''
  type: Website
  url: https://yeeps.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trass-games
- group: operate
  title: ''
  type: Support
  url: https://yeeps.com/pages/support
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/yeeps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yeeps.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yeeps.com/policies/privacy-policy
- group: other
  title: ''
  type: Licensing
  url: https://yeeps.com/pages/trass-games-licensing
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trass-games-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trass-games-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trass-games-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trass-games-conformance.yml
created: '2026-07-17'
description: Trass Games is an a16z-backed independent VR game studio best known for Yeeps - Hide and Seek, a free-to-play social hide-and-seek and building game on Meta Quest, and Gods of Gravity, an arcade space RTS. The studio ships a Yeeps companion app for iOS and Android, sells plush, maker-kit, and apparel merchandise through Shopify storefronts at yeeps.com and godsofgravityvr.com, and runs a community licensing program for creators. Trass Games publishes no first-party developer API, but its storefronts expose agent-ready commerce surfaces including llms.txt, agents.md, a Universal Commerce Protocol (UCP) merchant profile, and a live storefront MCP endpoint.
image: https://yeeps.com/cdn/shop/files/yeeps-head-full-color.png
layout: provider
mcp_servers:
- description: Trass Games publishes no first-party MCP server, but both of its Shopify storefronts expose the live Shopify-hosted storefront MCP endpoint. The tool list below was captured verbatim from a tools/list
  name: Trass Games MCP Server
  slug: trass-games-mcp-server
modified: '2026-07-21'
name: Trass Games
nav: Providers
network: true
overview: 'Trass Games publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Virtual Reality, VR Games, Meta Quest, and Social Games.


  Trass Games'' developer surface includes support and 12 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 15.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trass-games/refs/heads/main/screenshots/trass-games-2026-09-02T164145.png
security:
- kind: domain-security
  name: Trass Games Domain Security
  slug: trass-games-domain-security
  summary_line: TLSv1.3 · HSTS
slug: trass-games
tags:
- Gaming
- Virtual Reality
- VR Games
- Meta Quest
- Social Games
- E-Commerce
- Entertainment
website: https://trass.games
---
