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
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Atoma Run (no public documentation or contract available).
  name: Atoma Run API
  slug: atoma-run-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/atoma-run/mcp/atoma-run-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atoma-run-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atoma-run/well-known/atoma-run-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atoma-run-well-known.yml
- group: other
  href: https://artifacts.apis.io/atoma-run/hosts/atoma-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atoma-run-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atoma-run/security/atoma-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atoma-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atoma.run/
- group: operate
  title: ''
  type: Support
  url: https://atoma.run/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atoma.run/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atoma.run/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atoma-run
coverage:
  checked: '2026-11-02'
  detail: API endpoints require authentication (401 responses for GraphQL and MCP endpoints).
  evidence:
  - status: 401
    url: https://atoma.run/api/graphql
  - status: 401
    url: https://atoma.run/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Atoma provides an AI‑driven platform that lets users request a drawing, sound, report, data study, proof, or software and have coordinated AI agents generate the finished work. The service checks results against the original request and offers step‑by‑step inspection. Atoma runs as a hosted service and can also be self‑hosted, with an MCP server for integration. It is under active development and includes support resources, privacy policy, and terms of service.
image: https://atoma.run/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at atoma.run.
  name: Atoma MCP Server
  slug: atoma-run-mcp-yml
modified: '2026-11-02'
name: Atoma
nav: Providers
network: true
overview: 'Atoma is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Workflows, Coordination, and Platform.


  Atoma''s developer surface includes support and 8 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 12.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atoma Run Domain Security
  slug: atoma-run-domain-security
  summary_line: TLSv1.3
slug: atoma-run
tags:
- Artificial Intelligence
- Automation
- Workflows
- Coordination
- Platform
website: https://atoma.run/
---
