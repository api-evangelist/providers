---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
- description: Provides the full product catalogue as JSON, including pricing, deliverables, and store info.
  name: Catalog API
  slug: catalog-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/agentfulfyl-com/llms/agentfulfyl-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentfulfyl-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentfulfyl-com/mcp/agentfulfyl-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentfulfyl-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentfulfyl-com/hosts/agentfulfyl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentfulfyl-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentfulfyl-com/vendors/agentfulfyl-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentfulfyl-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Capataina
- group: auth
  href: https://artifacts.apis.io/agentfulfyl-com/security/agentfulfyl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentfulfyl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentfulfyl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentfulfyl.com/catalog.json
- group: docs
  title: ''
  type: APIReference
  url: https://agentfulfyl.com/catalog.json
created: '2026-10-31'
description: AgentFulfyl is a storefront where customers are AI agents, offering a curated catalogue of productised research services that agents can discover, parse, and order. Each deliverable ships both human‑readable reports and machine‑checkable evidence ledgers. The platform operates on a business‑to‑agent commerce model, charging only when the service works, with no accounts or ads, and provides refunds if claims are unsupported.
image: https://agentfulfyl.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agentfulfyl.com.
  name: AgentFulfyl MCP Server
  slug: agentfulfyl-com-mcp-yml
modified: '2026-10-31'
name: AgentFulfyl
nav: Providers
network: true
overview: 'AgentFulfyl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Research, Services, and Commerce.


  AgentFulfyl''s developer surface includes documentation, API reference, and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 9.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentfulfyl Com Domain Security
  slug: agentfulfyl-com-domain-security
  summary_line: TLSv1.3
slug: agentfulfyl-com
tags:
- Artificial Intelligence
- Marketplace
- Research
- Services
- Commerce
website: https://agentfulfyl.com/
---
