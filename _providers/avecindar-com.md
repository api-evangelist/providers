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
- description: 'Datos observados y explicaciones claras para buscar alquiler en Uruguay: precios, garantías y costos de ingreso.'
  name: Avecindar API
  slug: avecindar-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/avecindar-com/mcp/avecindar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avecindar-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/avecindar-com/hosts/avecindar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avecindar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/avecindar-com/vendors/avecindar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avecindar-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://avecindar.com/es/sign-in
- group: auth
  href: https://artifacts.apis.io/avecindar-com/security/avecindar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avecindar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avecindar.com/
- group: operate
  title: ''
  type: Support
  url: https://avecindar.com/es/help
- group: docs
  title: ''
  type: Documentation
  url: https://avecindar.com/es/guides
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avecindar.com/es/privacy
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are served as a JavaScript SPA with minimal HTML, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://avecindar.com/es/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Avecindar is a Uruguay-based online rental marketplace that connects renters with landlords, offering clear pricing, detailed listings, and tools to schedule viewings. The platform supports multiple languages and provides a transparent, user-friendly experience for finding homes across Montevideo and other regions, emphasizing cost clarity and convenience for both tenants and property owners.
image: https://avecindar.com/og/default.png
layout: provider
mcp_servers:
- description: Remote MCP server at avecindar.com.
  name: Avecindar MCP Server
  slug: avecindar-com-mcp-yml
modified: '2026-11-02'
name: Avecindar
nav: Providers
network: true
overview: 'Avecindar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Rentals, Uruguay, Housing, and Marketplace.


  Avecindar''s developer surface includes support, documentation, and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 56.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - uruguay
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 12.5
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avecindar Com Domain Security
  slug: avecindar-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avecindar-com
tags:
- Real Estate
- Rentals
- Uruguay
- Housing
- Marketplace
website: https://avecindar.com/
---
