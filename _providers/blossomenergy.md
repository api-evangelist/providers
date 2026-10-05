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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.2
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/llms/blossomenergy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blossomenergy-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/mcp/blossomenergy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blossomenergy-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/mcp/blossomenergy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blossomenergy-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/hosts/blossomenergy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blossomenergy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/vendors/blossomenergy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blossomenergy-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blossomenergy/refs/heads/main/security/blossomenergy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blossomenergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blossom-energy.co.jp/en
coverage:
  checked: '2026-09-29'
  detail: The developer site is a Wix‑generated page that serves only JavaScript‑rendered HTML with no machine‑readable OpenAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://www.blossom-energy.co.jp/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blossomenergy is a private renewable energy startup listed on secondary‑market platforms such as EquityZen. Public information about the company is limited; attempts to locate an official website or detailed corporate branding have been unsuccessful. The company appears in investment listings but its own domain, documentation, or API endpoints are not publicly discoverable. This entry serves as a placeholder for future enrichment when more concrete data becomes available.
layout: provider
mcp_servers:
- description: Remote MCP server at www.blossom-energy.co.jp.
  name: Blossomenergy MCP Server
  slug: blossomenergy-mcp-yml
modified: '2026-09-29'
name: Blossomenergy
nav: Providers
network: true
overview: Blossomenergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewables, Startups, and Private.
random_paper: 9
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 7
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
    discoverability: 55.0
    operational_transparency: 0.0
  provenance:
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blossomenergy Domain Security
  slug: blossomenergy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: blossomenergy
tags:
- Company
- Energy
- Renewables
- Startups
- Private
- Marketplace
website: https://www.blossom-energy.co.jp/en
---
