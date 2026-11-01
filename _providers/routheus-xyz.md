---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Routheus Xyz Agentic Access
  operation_count: 3
  slug: routheus-xyz-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://routheus.xyz
  baseurl_source: declared
  description: The Router API from routheus-xyz — 1 operation(s) for router.
  name: routheus-xyz Router API
  slug: routheus-xyz-router-api
- baseURL: https://routheus.xyz
  baseurl_source: declared
  description: The Tokens API from routheus-xyz — 2 operation(s) for tokens.
  name: routheus-xyz Tokens API
  slug: routheus-xyz-tokens-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/routheus-xyz/agentic-access/routheus-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/routheus-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/routheus-xyz/rules/routheus-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/routheus-xyz-rules.yml
- group: agent
  href: https://artifacts.apis.io/routheus-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/routheus-xyz/errors/routheus-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/routheus-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/routheus-xyz/conformance/routheus-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routheus-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/routheus-xyz/llms/routheus-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routheus-xyz-llms.txt
- group: build
  href: https://artifacts.apis.io/routheus-xyz/mcp/routheus-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/routheus-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/routheus-xyz/mcp/routheus-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/routheus-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/routheus-xyz/well-known/routheus-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/routheus-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/routheus-xyz/hosts/routheus-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/routheus-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/routheus-xyz/vendors/routheus-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/routheus-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/routheus-xyz/security/routheus-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routheus-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://routheus.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://routheus.xyz/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://routheus.xyz/openapi.json
- group: operate
  title: ''
  type: StatusPage
  url: https://routheus.xyz/health
created: '2026-10-31'
description: 'Live DEX token prices and best‑route swap quotes across 13 EVM chains (Base, Ethereum, Arbitrum, BSC, Optimism, Polygon and more). Sub‑millisecond answers from our own real‑time pool‑state engine, not a proxy. Executable swap calldata (Permit2), simulation‑verified quotes, chained‑state arb quoting, token metadata, token search, DEX pools. For AI agents: pay per call in USDC on Base, Polygon, Arbitrum, Avalanche or Solana via x402 — no API keys, no subscription. From $0.001 per call; failed answers are free.'
image: https://routheus.xyz/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at routheus.xyz.
  name: routheus-xyz MCP Server
  slug: routheus-xyz-mcp-yml
modified: '2026-10-31'
name: routheus-xyz
nav: Providers
network: true
overview: 'routheus-xyz publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Router API and Tokens API. Tagged areas include Company, DeFi, Crypto, DEX, and Multichain.


  The routheus-xyz catalog on APIs.io includes 1 Spectral governance ruleset.


  routheus-xyz''s developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: routheus-xyz API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: routheus-xyz-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 65.5
    contract_quality: 42.9
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Routheus Xyz Domain Security
  slug: routheus-xyz-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: routheus-xyz
tags:
- Company
- DeFi
- Crypto
- DEX
- Multichain
- Swap
website: https://routheus.xyz/
---
