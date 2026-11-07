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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Amazon-FBA calculator via MCP for ChatGPT & Claude
  name: Arbitragex MCP
  slug: arbitragex-mcp
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/arbitragex-de/security/arbitragex-de-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arbitragex-de-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/arbitragex-de/llms/arbitragex-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arbitragex-de-llms.txt
- group: build
  href: https://artifacts.apis.io/arbitragex-de/mcp/arbitragex-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arbitragex-de-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arbitragex-de/mcp/arbitragex-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arbitragex-de-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arbitragex-de/well-known/arbitragex-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arbitragex-de-security.txt
- group: agent
  href: https://artifacts.apis.io/arbitragex-de/well-known/arbitragex-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arbitragex-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/arbitragex-de/hosts/arbitragex-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbitragex-de-hosts.yml
- group: auth
  href: https://artifacts.apis.io/arbitragex-de/security/arbitragex-de-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbitragex-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arbitragex-de/security/arbitragex-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbitragex-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbitragex.de/
- group: start
  title: ''
  type: SignUp
  url: https://arbitragex.de/signup
created: '2026-11-01'
description: Arbitragex provides an Amazon seller dashboard that aggregates real Amazon SP-API data to deliver real-time profit, cash-flow, and inventory insights. Users can monitor SKU profitability after fees and PPC, automatically track FBA reimbursements, and run EU-auto-listing and prep. The platform offers live dashboards with metrics per marketplace, cash-flow forecasts, automated price and stock warnings, and integrates with Amazon’s official SP-API for secure data access. Pricing starts at €1.10 per day, with features such as CSV/XLSX import, multi-marketplace support, and optional prep-center shipping automation.
examples:
- key_count: 3
  name: Mcp Tools List
  slug: mcp-tools-list
image: https://arbitragex.de/static/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at arbitragex.de.
  name: Arbitragex MCP Server
  slug: arbitragex-de-mcp-yml
modified: '2026-11-01'
name: Arbitragex
nav: Providers
network: true
overview: 'Arbitragex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Amazon, Arbitrage, FBA, Profit, and Automation.


  Arbitragex''s developer surface includes signup flow and 10 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 9.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arbitragex De Domain Security
  slug: arbitragex-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arbitragex De Vulnerability Disclosure
  slug: arbitragex-de-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arbitragex-de
tags:
- Amazon
- Arbitrage
- FBA
- Profit
- Automation
- SP-API
website: https://arbitragex.de/
---
