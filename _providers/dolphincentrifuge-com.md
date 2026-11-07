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
    agent_skills: unknown
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine Control Protocol (MCP) server for Dolphin Centrifuge API access.
  name: Dolphin Centrifuge MCP
  slug: dolphin-centrifuge-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dolphincentrifuge-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dolphincentrifuge-com/llms/dolphincentrifuge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dolphincentrifuge-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dolphincentrifuge-com/mcp/dolphincentrifuge-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dolphincentrifuge-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dolphincentrifuge-com/hosts/dolphincentrifuge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dolphincentrifuge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dolphincentrifuge-com/vendors/dolphincentrifuge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dolphincentrifuge-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dolphincentrifuge-com/security/dolphincentrifuge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dolphincentrifuge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dolphincentrifuge.com/
created: '2026-11-05'
description: Dolphin Centrifuge is the independent specialist in Alfa Laval centrifuges, offering remanufactured machines, turnkey systems, parts, and service. Based in Warren, Michigan, the company leverages over 40 years of Alfa Laval experience to provide solutions for oil, fuel, wastewater, and industrial applications worldwide.
image: https://dolphincentrifuge.com/images/homepage/alfa-laval-industrial-centrifuge-dolphin-centrifuge-1.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at dolphincentrifuge.com.
  name: Dolphin Centrifuge MCP Server
  slug: dolphincentrifuge-com-mcp-yml
modified: '2026-11-05'
name: Dolphin Centrifuge
nav: Providers
network: true
overview: Dolphin Centrifuge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Centrifuge, Alfa-Laval, Remanufacturing, Industrial, and Michigan.
random_paper: 22
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dolphincentrifuge Com Domain Security
  slug: dolphincentrifuge-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dolphincentrifuge-com
tags:
- Centrifuge
- Alfa-Laval
- Remanufacturing
- Industrial
- Michigan
website: https://dolphincentrifuge.com/
---
