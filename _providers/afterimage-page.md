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
    agent_card: near-conformant
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
  score: 6.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Shared copies of public web pages for AI agents.
  name: AfterImage API
  slug: afterimage-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/afterimage-page/conformance/afterimage-page-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afterimage-page-conformance.yml
- group: agent
  href: https://artifacts.apis.io/afterimage-page/llms/afterimage-page-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afterimage-page-llms.txt
- group: other
  href: https://artifacts.apis.io/afterimage-page/a2a/afterimage-page-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afterimage-page-a2a.yml
- group: build
  href: https://artifacts.apis.io/afterimage-page/mcp/afterimage-page-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/afterimage-page-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/afterimage-page/mcp/afterimage-page-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/afterimage-page-mcp.yml
- group: agent
  href: https://artifacts.apis.io/afterimage-page/well-known/afterimage-page-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afterimage-page-well-known.yml
- group: other
  href: https://artifacts.apis.io/afterimage-page/hosts/afterimage-page-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afterimage-page-hosts.yml
- group: other
  href: https://artifacts.apis.io/afterimage-page/vendors/afterimage-page-vendors.yml
  title: ''
  type: Vendors
  url: vendors/afterimage-page-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://afterimage.page/docs
- group: auth
  href: https://artifacts.apis.io/afterimage-page/security/afterimage-page-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afterimage-page-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afterimage.page/
created: '2026-10-31'
description: AfterImage provides a platform for fresh copies of page models, offering APIs for model catalogs, provider pricing, protocol specifications, changelogs, deprecations, rate limits, and current package versions. Users can search, retrieve, and pay per use with microtransactions, integrating with AI services. The service includes documentation, OpenAPI specs, and an MCP server for managing access and billing.
layout: provider
mcp_servers:
- description: Remote MCP server at afterimage.page.
  name: AfterImage MCP Server
  slug: afterimage-page-mcp-yml
modified: '2026-10-31'
name: AfterImage
nav: Providers
network: true
overview: 'AfterImage is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data, and Platform.


  AfterImage''s developer surface includes API reference and 10 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 7.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afterimage Page Domain Security
  slug: afterimage-page-domain-security
  summary_line: TLSv1.3
slug: afterimage-page
tags:
- Company
- Artificial Intelligence
- Data
- Platform
website: https://afterimage.page/
---
