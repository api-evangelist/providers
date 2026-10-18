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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer hub for Musement API providing documentation and resources.
  name: Musement API
  slug: musement-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/musement/refs/heads/main/llms/musement-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/musement-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/musement/refs/heads/main/mcp/musement-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/musement-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/musement/refs/heads/main/hosts/musement-hosts.yml
  title: ''
  type: Hosts
  url: hosts/musement-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/musement/refs/heads/main/vendors/musement-vendors.yml
  title: ''
  type: Vendors
  url: vendors/musement-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.musement.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/musement/refs/heads/main/security/musement-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/musement-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://musement.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://partner-api.musement.com/mcp
  - status: 401
    url: https://helpcenter.musement.com/mcp
  - status: 200
    url: https://musement.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Musement is a travel experiences platform that lets users discover, book, and manage tickets for attractions, museums, tours, and activities worldwide. It offers a curated selection of experiences with flexible cancellation policies, detailed information, and a user-friendly interface for planning trips.
image: https://b2c-frontend-images.prod.musement.com/home_bg.jpg?w=1200&h=630&q=95&fit=crop
layout: provider
mcp_servers:
- description: Remote MCP server at partner-api.musement.com.
  name: Musement MCP Server
  slug: musement-mcp-yml
modified: '2026-10-12'
name: Musement
nav: Providers
network: true
overview: 'Musement is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Attractions, Museums, Tours, and Experience.


  Musement''s developer surface includes documentation and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Musement Domain Security
  slug: musement-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: musement
tags:
- Travel
- Attractions
- Museums
- Tours
- Experience
website: https://musement.com/
---
