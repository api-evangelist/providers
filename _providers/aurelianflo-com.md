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
- description: Pay-per-call OFAC wallet screening and compliance endpoints.
  name: AurelianFlo API
  slug: aurelianflo-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/aurelianflo-com/vocabulary/aurelianflo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aurelianflo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aurelianflo-com/conformance/aurelianflo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aurelianflo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aurelianflo-com/llms/aurelianflo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurelianflo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/aurelianflo-com/mcp/aurelianflo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aurelianflo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aurelianflo-com/mcp/aurelianflo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aurelianflo-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aurelianflo-com/well-known/aurelianflo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurelianflo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aurelianflo-com/hosts/aurelianflo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurelianflo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurelianflo-com/vendors/aurelianflo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurelianflo-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://aurelianflo.com/docs
- group: auth
  href: https://artifacts.apis.io/aurelianflo-com/security/aurelianflo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurelianflo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aurelianflo.com/
created: '2026-11-02'
description: AurelianFlo provides Pay-per-call OFAC wallet screening, batch crypto sanctions checks, EDD memos, and audit-ready document output. Built for humans, AI agents, OpenAPI, MCP, and x402, it offers compliance APIs for financial services and crypto platforms.
image: https://aurelianflo.com/aurelianflo-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at aurelianflo.com.
  name: AurelianFlo MCP Server
  slug: aurelianflo-com-mcp-yml
modified: '2026-11-02'
name: AurelianFlo
nav: Providers
network: true
overview: 'AurelianFlo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Finance, Cryptocurrency, and Screening.


  AurelianFlo''s developer surface includes documentation and 10 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aurelianflo Com Domain Security
  slug: aurelianflo-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aurelianflo-com
tags:
- Company
- Compliance
- Finance
- Cryptocurrency
- Screening
website: https://aurelianflo.com/
---
