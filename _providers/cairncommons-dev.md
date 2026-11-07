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
    agent_card: conformant
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Cairn Commons, providing endpoints for shared memory of software failures and technical claims.
  name: Cairn Commons API
  slug: cairn-commons-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/cairncommons-dev/llms/cairncommons-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cairncommons-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/cairncommons-dev/a2a/cairncommons-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cairncommons-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cairncommons-dev/mcp/cairncommons-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cairncommons-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/cairncommons-dev/hosts/cairncommons-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cairncommons-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/cairncommons-dev/vendors/cairncommons-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cairncommons-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cairncommons.dev/privacy
- group: auth
  href: https://artifacts.apis.io/cairncommons-dev/security/cairncommons-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cairncommons-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cairncommons.dev/
coverage:
  checked: '2026-11-03'
  detail: Provider documentation at https://cairncommons.dev/api-docs is HTML only with no machine-readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://cairncommons.dev/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cairn Commons builds a shared, searchable memory of software failures and technical claims, each labelled by how it was checked, so agents can benefit from what has already been learned. It collects new technical problems and claims from public sources, reproduces what it safely can in a disposable environment, and publishes the versions, conditions, steps, results and open questions as public threads.
layout: provider
mcp_servers:
- description: Remote MCP server at cairncommons.dev.
  name: Cairn Commons MCP Server
  slug: cairncommons-dev-mcp-yml
modified: '2026-11-03'
name: Cairn Commons
nav: Providers
network: true
overview: Cairn Commons is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Knowledge Base, Evidence Layer, and Open Exploration.
random_paper: 21
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cairncommons Dev Domain Security
  slug: cairncommons-dev-domain-security
  summary_line: TLSv1.3
slug: cairncommons-dev
tags:
- AI Agents
- Knowledge Base
- Evidence Layer
- Open Exploration
website: https://cairncommons.dev/
---
