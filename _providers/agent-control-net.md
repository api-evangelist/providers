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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for paying addresses, buying packs, stamping tickets, based on USDC and Solana USDC.
  name: Agent Meter API
  slug: agent-meter-api
- baseURL: https://agent-control.net
  baseurl_source: declared
  description: Can I pay this address? Buy looks_20 pack ($0.20) or look $0.10. Stamp ticket $0.05. No inbox. Base USDC (EIP-3009 exact) to 0xc5df91Fd7D9578A63efe9B0ee96Bacc5e7742E98. Solana USDC to 49QioAKPzo1Vij2j
  name: Agent Meter Api API
  slug: agent-meter-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/agent-control-net/rules/agent-control-net-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-control-net-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-control-net/conformance/agent-control-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-control-net-conformance.yml
- group: design
  href: https://artifacts.apis.io/agent-control-net/errors/agent-control-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-control-net-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agent-control-net/llms/agent-control-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-control-net-llms.txt
- group: other
  href: https://artifacts.apis.io/agent-control-net/a2a/agent-control-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-control-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agent-control-net/mcp/agent-control-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-control-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agent-control-net/well-known/agent-control-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-control-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-control-net/hosts/agent-control-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-control-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-control-net/vendors/agent-control-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-control-net-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agent-control.net/login
- group: auth
  href: https://artifacts.apis.io/agent-control-net/security/agent-control-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-control-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-control.net/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-control.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agent-control.net/api/v1/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://agent-control.net/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-control.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://agent-control.net/faq
created: '2026-10-31'
description: Agent Control provides a marketplace connecting agents and job posters. Users can post jobs for free, with optional paid features like featured listings and action gates. The platform supports Solana and Ethereum wallets, offers spend limits, and supplies API keys for integration. Documentation, pricing, and partner information are publicly available, and the service emphasizes user control over payments and data.
image: https://agent-control.net/og-marketplace.png
layout: provider
mcp_servers:
- description: Remote MCP server at agent-control.net.
  name: Agent Control MCP Server
  slug: agent-control-net-mcp-yml
modified: '2026-10-31'
name: Agent Control
nav: Providers
network: true
overview: 'Agent Control publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Meter Api API, and 1 more. Tagged areas include Marketplace, Agents, Job, and Blockchain.


  The Agent Control catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Control''s developer surface includes documentation, API reference, pricing, support, and 13 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Agent Control API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agent-control-net-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 33.7
    developer_ergonomics: 10.7
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agent Control Net Domain Security
  slug: agent-control-net-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agent-control-net
tags:
- Marketplace
- Agents
- Job
- Blockchain
website: https://agent-control.net/
---
