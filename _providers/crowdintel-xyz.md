---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CrowdIntel provides a REST data API and MCP server for Polymarket, exposing on-chain trade data, wallet profiles, and analytics.
  name: CrowdIntel API
  slug: crowdintel-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/crowdintel-xyz/llms/crowdintel-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdintel-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/crowdintel-xyz/mcp/crowdintel-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crowdintel-xyz-mcp.yml
- group: other
  href: https://artifacts.apis.io/crowdintel-xyz/hosts/crowdintel-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdintel-xyz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/crowdintel-xyz/security/crowdintel-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdintel-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdintel.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crowdintel
coverage:
  checked: '2026-10-30'
  detail: The provider's site redirects API reference URLs to a maintenance page with no machine‑readable API specification.
  evidence:
  - status: 301
    url: https://crowdintel.xyz/api
  - status: 307
    url: https://crowdintel.xyz/api-docs
  - status: 307
    url: https://crowdintel.xyz/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: CrowdIntel provides the AI layer for Polymarket, offering a massive on-chain data API and MCP server that indexes over 1.7 billion trades, profiles 3 million wallets, and delivers insider signals, whale alerts, funding cluster detection, and advanced analytics for bots, agents, and traders.
image: https://crowdintel.xyz/CrowdIntelLogo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.crowdintel.xyz.
  name: crowdintel-xyz MCP Server
  slug: crowdintel-xyz-mcp-yml
modified: '2026-10-30'
name: crowdintel-xyz
nav: Providers
network: true
overview: crowdintel-xyz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, MCP, and Polymarket.
random_paper: 3
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 5.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crowdintel-xyz/crowdintel-xyz-2026-11-03T125658.png
security:
- kind: domain-security
  name: Crowdintel Xyz Domain Security
  slug: crowdintel-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdintel-xyz
tags:
- Company
- Finance
- Data
- MCP
- Polymarket
- Cryptocurrency
website: https://crowdintel.xyz/
---
