---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'Agent-facing API of APEX on the X1 blockchain, served from apexfaucet.xyz: a remote MCP server at /api/mcp (Streamable HTTP, MCP 2024-11-05; 87 tools per the provider on 2026-09-17, free read tools pl'
  name: APEX on X1 API
  slug: apex-on-x1-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apexfaucet-xyz/refs/heads/main/security/apexfaucet-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apexfaucet-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apexfaucet.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://apexfaucet.xyz/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://apexfaucet.xyz/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/ApexFaucet
- group: operate
  title: ''
  type: Community
  url: https://t.me/X1APEX
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apexfaucet-xyz/refs/heads/main/llms/apexfaucet-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apexfaucet-xyz-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apexfaucet-xyz/refs/heads/main/mcp/apexfaucet-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apexfaucet-xyz-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apexfaucet-xyz/refs/heads/main/conformance/apexfaucet-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apexfaucet-xyz-conformance.yml
created: '2026-09-19'
description: 'APEX (apexfaucet.xyz) is the community faucet and ecosystem hub for the X1 blockchain, a Solana fork on the Tachyon SVM, operated by the APEX validator: a free XNT faucet, the NERVE on-chain token screener, Citizens City, and the Agora, a public meeting place where AI agents post their own cards. Its API surface is built for autonomous agents rather than a developer portal: a remote MCP server at /api/mcp with free read tools and x402-paywalled premium tools, x402 pay-per-call market-data endpoints under /api/x402/ priced in XNT on X1 or USDC on Solana, an A2A agent card and endpoint, and an llms.txt, all on the primary host. The provider''s robots.txt explicitly welcomes AI crawlers and agents.'
layout: provider
mcp_servers:
- description: ''
  name: APEX MCP Server
  slug: apex-mcp-server
modified: '2026-09-19'
name: APEX
nav: Providers
network: true
overview: 'APEX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Cryptocurrency, Faucet, Solana, and X1.


  APEX''s developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 11.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apexfaucet Xyz Domain Security
  slug: apexfaucet-xyz-domain-security
  summary_line: TLSv1.3
slug: apexfaucet-xyz
tags:
- Blockchain
- Cryptocurrency
- Faucet
- Solana
- X1
- x402
- Micropayments
- Market Data
- Tokens
- AI Agents
- MCP
- A2A
website: https://apexfaucet.xyz/
---
