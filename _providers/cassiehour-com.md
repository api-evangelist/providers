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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Cassie Hour services as described in the Agent API markdown documentation.
  name: Cassie Hour API
  slug: cassie-hour-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/cassiehour-com/llms/cassiehour-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cassiehour-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cassiehour-com/a2a/cassiehour-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cassiehour-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cassiehour-com/mcp/cassiehour-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cassiehour-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cassiehour-com/well-known/cassiehour-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cassiehour-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cassiehour-com/hosts/cassiehour-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cassiehour-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cassiehour-com/vendors/cassiehour-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cassiehour-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cassiehour.com/press/
- group: auth
  href: https://artifacts.apis.io/cassiehour-com/security/cassiehour-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cassiehour-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cassiehour.com/
created: '2026-11-04'
description: 'cassiehour-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://cassiehour.com/cassiehour-site-assets/cassie-hour-book-hero-direct.png
layout: provider
mcp_servers:
- description: Remote MCP server at cassiehour.com.
  name: Cassie Hour MCP Server
  slug: cassiehour-com-mcp-yml
modified: '2026-11-04'
name: Cassie Hour
nav: Providers
network: true
overview: Cassie Hour is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Literature, Mystery, Music, and AI Experiment.
random_paper: 2
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.2
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cassiehour Com Domain Security
  slug: cassiehour-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: cassiehour-com
tags:
- Literature
- Mystery
- Music
- AI Experiment
website: https://cassiehour.com/
---
