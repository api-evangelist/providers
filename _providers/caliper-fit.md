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
    agent_card: flavored
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
  score: 4.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Geometry and CAD file metadata extraction API.
  name: Caliper API
  slug: caliper-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/caliper-fit/conformance/caliper-fit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caliper-fit-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caliper-fit/llms/caliper-fit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caliper-fit-llms.txt
- group: other
  href: https://artifacts.apis.io/caliper-fit/a2a/caliper-fit-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/caliper-fit-a2a.yml
- group: agent
  href: https://artifacts.apis.io/caliper-fit/mcp/caliper-fit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caliper-fit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/caliper-fit/well-known/caliper-fit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caliper-fit-well-known.yml
- group: other
  href: https://artifacts.apis.io/caliper-fit/hosts/caliper-fit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caliper-fit-hosts.yml
- group: auth
  href: https://artifacts.apis.io/caliper-fit/security/caliper-fit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caliper-fit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caliper.fit/
- group: docs
  title: ''
  type: APIReference
  url: https://caliper.fit/mcp/manifest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caliper.fit/privacy
created: '2026-10-30'
description: Caliper provides a Geometry and CAD file metadata extraction API. It accepts 3D geometry files via URL or base64 and returns structured statistics such as bounding boxes, triangle counts, manifold analysis, point cloud statistics, and more. Files under 150KB are processed for free, while larger files are billed at $0.02 per MB with optional card surcharge. The service operates as an MCP server with no signup required, supporting formats like STL, OBJ, PLY, PCD, LAS/LAZ, and glTF/GLB, with upcoming support for STEP and IGES.
layout: provider
mcp_servers:
- description: Remote MCP server at caliper.fit.
  name: caliper-fit MCP Server
  slug: caliper-fit-mcp-yml
modified: '2026-10-30'
name: caliper-fit
nav: Providers
network: true
overview: 'caliper-fit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geometry, CAD, Metadata, and MCP.


  caliper-fit''s developer surface includes API reference and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 10.2
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/caliper-fit/caliper-fit-2026-11-03T123022.png
security:
- kind: domain-security
  name: Caliper Fit Domain Security
  slug: caliper-fit-domain-security
  summary_line: TLSv1.3
slug: caliper-fit
tags:
- Company
- Geometry
- CAD
- Metadata
- MCP
website: https://caliper.fit/
---
