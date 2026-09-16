---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: Read-only REST API to list, filter and fetch coworking spaces; no API key required for reads, production doubles as sandbox. OpenAPI 3.1 spec declared at coworkingview.com/openapi.json.
  name: CoworkingView REST API
  slug: coworkingview-rest-api
- description: 'Hosted MCP server (Streamable HTTP) exposing 10 read-only tools for searching, comparing and fetching coworking spaces, market rates, locations, operators and guides. Independently health-verified on '
  name: CoworkingView MCP Server
  slug: coworkingview-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://coworkingview.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/security/coworkingview-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coworkingview-api-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/well-known/coworkingview-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coworkingview-api-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/conformance/coworkingview-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coworkingview-api-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/components/coworkingview-api-components.yml
  title: ''
  type: Components
  url: components/coworkingview-api-components.yml
created: '2026-09-15'
description: An independent search and comparison platform for coworking spaces and flexible workspace across Europe and the Middle East, exposing a read-only REST API and a hosted MCP server with operator-published prices, amenities and location data. Holds no availability and books nothing; free with no commission and no API key required for reads.
image: https://coworkingview.com/og-image.png
layout: provider
mcp_servers:
- description: Official hosted, remote MCP server (Streamable HTTP) for CoworkingView, exposing 10 read-only tools for discovering, searching, comparing and profiling coworking spaces, operators, places and market r
  name: CoworkingView MCP Server
  slug: coworkingview-mcp-server
modified: '2026-09-15'
name: CoworkingView API
nav: Providers
network: true
overview: 'CoworkingView API publishes 1 API on the [APIs.io](https://apis.io/) network: CoworkingView REST API. Tagged areas include Co-Working, Flexible Workspace, Real-Estate, Location Services, and Search.'
plans:
- name: Coworkingview Api Plans Pricing
  plan_count: 0
  slug: coworkingview-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Coworkingview Api Rate Limits
  slug: coworkingview-api-rate-limits
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 42.3
    discoverability: 75.9
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Coworkingview Api Authentication
  slug: coworkingview-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Coworkingview Api Domain Security
  slug: coworkingview-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coworkingview-api
tags:
- Co-Working
- Flexible Workspace
- Real-Estate
- Location Services
- Search
- Comparison
- MCP
- agent-native
- Business
website: https://coworkingview.com
---
