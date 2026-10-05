---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.3
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blueshockrace/refs/heads/main/mcp/blueshockrace-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blueshockrace-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blueshockrace/refs/heads/main/well-known/blueshockrace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blueshockrace-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blueshockrace/refs/heads/main/hosts/blueshockrace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueshockrace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blueshockrace/refs/heads/main/vendors/blueshockrace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blueshockrace-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blueshockrace/refs/heads/main/security/blueshockrace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueshockrace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/blueshockrace
coverage:
  checked: '2026-09-29'
  detail: Blueshockrace sells electric go‑karts and provides no developer API.
  evidence:
  - status: 200
    url: https://www.blueshockrace.com
  reason: not-a-software-company
  state: none
created: '2026-09-29'
description: Blueshockrace is a stub entry in the API Evangelist catalog, originating from a secondary-market harvest. The company appears to be a placeholder with no publicly available website or detailed information. This entry awaits further discovery of its official domain, documentation, and API specifications as the profiling process continues.
layout: provider
mcp_servers:
- description: Remote MCP server at blueshockrace.com.
  name: Blueshockrace MCP Server
  slug: blueshockrace-mcp-yml
modified: '2026-09-29'
name: Blueshockrace
nav: Providers
network: true
overview: Blueshockrace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Racing, Sports, and Data.
random_paper: 7
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blueshockrace Domain Security
  slug: blueshockrace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blueshockrace
tags:
- Company
- Technology
- Racing
- Sports
- Data
website: https://equityzen.com/company/blueshockrace
---
