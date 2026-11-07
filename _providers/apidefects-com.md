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
- description: MCP endpoint providing tool list for API Defects.
  name: API Defects MCP
  slug: api-defects-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/apidefects-com/llms/apidefects-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apidefects-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apidefects-com/mcp/apidefects-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apidefects-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/apidefects-com/hosts/apidefects-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apidefects-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apidefects-com/vendors/apidefects-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apidefects-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/apidefects-com/security/apidefects-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apidefects-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apidefects.com/
created: '2026-11-01'
description: API Defects is a project that tracks and reports defects in the public description of machine‑callable operations such as OpenAPI documents and MCP servers. It maintains a directory of known issues, including stale host references, mismatched specifications, missing authentication details, and other inconsistencies that can affect API reliability and developer experience. The service provides JSON endpoints summarizing these defects and offers tools for developers to check and improve their API documentation.
layout: provider
mcp_servers:
- description: Remote MCP server at apidefects.com.
  name: API Defects MCP Server
  slug: apidefects-com-mcp-yml
modified: '2026-11-01'
name: API Defects
nav: Providers
network: true
overview: API Defects is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Defects, Monitoring, Quality, Documentation, and OpenAPI.
random_paper: 20
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 4.8
  provenance:
    mcp: first-party
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
security:
- kind: domain-security
  name: Apidefects Com Domain Security
  slug: apidefects-com-domain-security
  summary_line: TLSv1.3
slug: apidefects-com
tags:
- Defects
- Monitoring
- Quality
- Documentation
- OpenAPI
website: https://apidefects.com/
---
