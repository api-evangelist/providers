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
  band: agent-aware
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/coinfuty-com/llms/coinfuty-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinfuty-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinfuty-com/mcp/coinfuty-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinfuty-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/coinfuty-com/well-known/coinfuty-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinfuty-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinfuty-com/hosts/coinfuty-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinfuty-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinfuty-com/vendors/coinfuty-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinfuty-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.coinfuty.com/coin/TRUST/overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinfuty.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinfuty
- group: auth
  href: https://artifacts.apis.io/coinfuty-com/security/coinfuty-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinfuty-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinfuty.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://api.coinfuty.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Coinfuty is an independent crypto derivatives analytics platform providing live futures market data including open interest, funding rates, long/short ratios, volume and liquidations across major exchanges. It offers real-time insights for traders and researchers, aggregating data from multiple sources to deliver comprehensive market analytics.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.coinfuty.com.
  name: Coinfuty MCP Server
  slug: coinfuty-com-mcp-yml
modified: '2026-11-04'
name: Coinfuty
nav: Providers
network: true
overview: Coinfuty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Crypto Futures, Market Data, Open Interest, Funding Rates, and Liquidations.
random_paper: 21
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinfuty Com Domain Security
  slug: coinfuty-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinfuty-com
tags:
- Crypto Futures
- Market Data
- Open Interest
- Funding Rates
- Liquidations
- Indicators
website: https://coinfuty.com/
---
