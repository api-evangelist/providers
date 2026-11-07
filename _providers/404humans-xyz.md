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
- description: Public API for the 402 Wall billboard platform
  name: 402 Wall API
  slug: 402-wall-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/404humans-xyz/conformance/404humans-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/404humans-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/404humans-xyz/llms/404humans-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/404humans-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/404humans-xyz/mcp/404humans-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/404humans-xyz-mcp.yml
- group: other
  href: https://artifacts.apis.io/404humans-xyz/hosts/404humans-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/404humans-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/404humans-xyz/vendors/404humans-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/404humans-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/404humans-xyz/security/404humans-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/404humans-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://404humans.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://404humans.xyz/openapi.json
created: '2026-10-31'
description: 404humans.xyz operates a decentralized billboard platform called the 402 Wall, where each pixel block can be owned via blockchain payment. Users can view the wall, purchase unclaimed blocks by answering HTTP 402 challenges, and programmatically interact via a public API. The service runs on the Ethereum-compatible network eip155:8453, offering a novel way to embed reputation and digital art on the web. It provides endpoints for canvas retrieval, block acquisition, pixel painting, and agent registration, all documented in OpenAPI and MCP formats.
image: https://404humans.xyz/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at 404humans.xyz.
  name: 404humans.xyz MCP Server
  slug: 404humans-xyz-mcp-yml
modified: '2026-10-31'
name: 404humans.xyz
nav: Providers
network: true
overview: '404humans.xyz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include On-chain Advertising.


  404humans.xyz''s developer surface includes API reference and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 7.0
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
  name: 404Humans Xyz Domain Security
  slug: 404humans-xyz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 404humans-xyz
tags:
- On-chain Advertising
website: https://404humans.xyz/
---
