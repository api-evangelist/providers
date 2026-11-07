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
  score: 4.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/albumora-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/albumora-de/mcp/albumora-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/albumora-de-mcp.yml
- group: other
  href: https://artifacts.apis.io/albumora-de/hosts/albumora-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/albumora-de-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://albumora.de/app/login
- group: auth
  href: https://artifacts.apis.io/albumora-de/security/albumora-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/albumora-de-domain-security.yml
coverage:
  checked: '2026-11-01'
  detail: Attempted to fetch OpenAPI spec at known locations but none were reachable.
  evidence:
  - status: 0
    url: https://albumora.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'albumora-de is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://albumora.de/opengraph-image?fb36b5fe1107c47f
layout: provider
mcp_servers:
- description: Remote MCP server at albumora.de.
  name: albumora-de MCP Server
  slug: albumora-de-mcp-yml
modified: '2026-11-01'
name: albumora-de
nav: Providers
network: true
overview: albumora-de is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 17
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 31.7
    operational_transparency: 0.0
  previous_composite: 5.7
  provenance:
    mcp: derived
    skills: unknown
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
  name: Albumora De Domain Security
  slug: albumora-de-domain-security
  summary_line: DMARC
slug: albumora-de
tags:
- Company
---
