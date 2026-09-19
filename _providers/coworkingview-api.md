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
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: 'Hosted MCP server (Streamable HTTP) exposing 10 read-only tools for searching, comparing and fetching coworking spaces, market rates, locations, operators and guides. Independently health-verified on '
  name: CoworkingView MCP Server
  slug: coworkingview-mcp-server
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The config API from CoworkingView API — 1 operation(s) for config.
  name: CoworkingView API Config API
  slug: coworkingview-api-config-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The facets API from CoworkingView API — 1 operation(s) for facets.
  name: CoworkingView API Facets API
  slug: coworkingview-api-facets-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The geo API from CoworkingView API — 1 operation(s) for geo.
  name: CoworkingView API Geo API
  slug: coworkingview-api-geo-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The health API from CoworkingView API — 1 operation(s) for health.
  name: CoworkingView API Health API
  slug: coworkingview-api-health-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The leads API from CoworkingView API — 2 operation(s) for leads.
  name: CoworkingView API Leads API
  slug: coworkingview-api-leads-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The market API from CoworkingView API — 1 operation(s) for market.
  name: CoworkingView API Market API
  slug: coworkingview-api-market-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The operators API from CoworkingView API — 1 operation(s) for operators.
  name: CoworkingView API Operators API
  slug: coworkingview-api-operators-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The places API from CoworkingView API — 1 operation(s) for places.
  name: CoworkingView API Places API
  slug: coworkingview-api-places-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The properties API from CoworkingView API — 3 operation(s) for properties.
  name: CoworkingView API Properties API
  slug: coworkingview-api-properties-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The rankings API from CoworkingView API — 1 operation(s) for rankings.
  name: CoworkingView API Rankings API
  slug: coworkingview-api-rankings-api
- baseURL: https://api.coworkingview.com
  baseurl_source: declared
  description: The search API from CoworkingView API — 1 operation(s) for search.
  name: CoworkingView API Search API
  slug: coworkingview-api-search-api
artifact_total: 17
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/overlays/coworkingview-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coworkingview-api-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coworkingview-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
overview: CoworkingView API publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Config API, Facets API, Geo API, and 8 more. Tagged areas include Co-Working, Flexible Workspace, Real-Estate, Location Services, and Search.
plans:
- name: Coworkingview Api Plans Pricing
  plan_count: 0
  slug: coworkingview-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Coworkingview Api Rate Limits
  slug: coworkingview-api-rate-limits
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 42.3
    discoverability: 75.9
    operational_transparency: 7.9
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
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
