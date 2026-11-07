---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public MCP endpoint providing tools to search buildings, architects, routes, and corpus statistics.
  name: Art Deco Belgium MCP API
  slug: art-deco-belgium-mcp-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/art-deco-belgique-be/llms/art-deco-belgique-be-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/art-deco-belgique-be-llms.txt
- group: agent
  href: https://artifacts.apis.io/art-deco-belgique-be/mcp/art-deco-belgique-be-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/art-deco-belgique-be-mcp.yml
- group: other
  href: https://artifacts.apis.io/art-deco-belgique-be/hosts/art-deco-belgique-be-hosts.yml
  title: ''
  type: Hosts
  url: hosts/art-deco-belgique-be-hosts.yml
- group: other
  href: https://artifacts.apis.io/art-deco-belgique-be/vendors/art-deco-belgique-be-vendors.yml
  title: ''
  type: Vendors
  url: vendors/art-deco-belgique-be-vendors.yml
- group: auth
  href: https://artifacts.apis.io/art-deco-belgique-be/security/art-deco-belgique-be-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/art-deco-belgique-be-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://art-deco-belgique.be/
created: '2026-11-01'
description: Art Déco Belgique is a heritage exploration platform that aggregates Art Deco buildings across the three Belgian regions and the Hauts‑de‑France, offering an interactive map, editorial itineraries and an AI‑powered route generator. The inventory draws from official sources such as urban.brussels, Onroerend Erfgoed and the Walloon heritage inventory, and provides data in JSON, CSV, GeoJSON and llms.txt under a CC BY 4.0 licence. Users can query the public MCP server at https://art-deco-belgique.be/api/mcp to search buildings, architects and routes.
examples:
- key_count: 3
  name: Mcp Tools
  slug: mcp-tools
image: https://commons.wikimedia.org/wiki/Special:FilePath/Belgique%20-%20Bruxelles%20-%20Maison%20Hendrickx%20-%2002.jpg?width=1200
layout: provider
mcp_servers:
- description: Remote MCP server at art-deco-belgique.be.
  name: Art Déco Belgique MCP Server
  slug: art-deco-belgique-be-mcp-yml
modified: '2026-11-02'
name: Art Déco Belgique
nav: Providers
network: true
overview: Art Déco Belgique is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Art Deco, Heritage, Belgium, Architecture, and Open Data.
random_paper: 22
scopes:
- name: Art Deco Belgique Be Scopes
  scope_count: 0
  slug: art-deco-belgique-be-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.9
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
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 6.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Art Deco Belgique Be Authentication
  slug: art-deco-belgique-be-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Art Deco Belgique Be Domain Security
  slug: art-deco-belgique-be-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: art-deco-belgique-be
tags:
- Art Deco
- Heritage
- Belgium
- Architecture
- Open Data
website: https://art-deco-belgique.be/
---
