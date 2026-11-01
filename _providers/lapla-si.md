---
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
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: Primary API host for Lapla SI, no public OpenAPI spec available.
  name: Lapla SI Primary API
  slug: lapla-si-primary-api
- description: MCP endpoint for claimback functionality.
  name: Lapla SI Claimback MCP
  slug: lapla-si-claimback-mcp
- description: MCP endpoint for world functionality.
  name: Lapla SI World MCP
  slug: lapla-si-world-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/lapla-si/changelog/lapla-si-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lapla-si-changelog.yml
- group: agent
  href: https://artifacts.apis.io/lapla-si/llms/lapla-si-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lapla-si-llms.txt
- group: agent
  href: https://artifacts.apis.io/lapla-si/mcp/lapla-si-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lapla-si-mcp.yml
- group: other
  href: https://artifacts.apis.io/lapla-si/hosts/lapla-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lapla-si-hosts.yml
- group: other
  href: https://artifacts.apis.io/lapla-si/vendors/lapla-si-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lapla-si-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Keith-CY/sayit/releases/latest
- group: auth
  href: https://artifacts.apis.io/lapla-si/security/lapla-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lapla-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lapla.si/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lapla.si/
coverage:
  checked: '2026-10-30'
  detail: All attempted OpenAPI spec URLs on the provider's API hosts returned 404.
  evidence:
  - status: 404
    url: https://api.lapla.si/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Lapla SI builds small, well‑calibrated artificial intelligence models that run on hardware people already own. Their flagship projects include Gua, a computer‑use model for macOS, the Melix AI workspace for creative tasks, and SayIt, a native macOS dictation tool. By focusing on efficient, on‑device AI, Lapla SI enables developers and users to integrate intelligent features without relying on cloud services.
image: https://lapla.si/brand/lapla-si-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at claimback.lapla.si.
  name: lapla-si MCP Server
  slug: lapla-si-mcp-yml
modified: '2026-10-30'
name: lapla-si
nav: Providers
network: true
overview: 'lapla-si is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, macOS, Productivity, Workspace, and Dictation.


  lapla-si''s developer surface includes changelog and 8 more developer resources.'
random_paper: 19
scopes:
- name: Lapla Si Scopes
  scope_count: 0
  slug: lapla-si-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 70.0
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lapla Si Authentication
  slug: lapla-si-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lapla Si Domain Security
  slug: lapla-si-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lapla-si
tags:
- AI
- macOS
- Productivity
- Workspace
- Dictation
website: https://lapla.si/
---
