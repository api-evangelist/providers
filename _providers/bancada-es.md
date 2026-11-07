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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Integration of Claude/AI with Odoo via Bancada's MCP service.
  name: Bancada Odoo MCP
  slug: bancada-odoo-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bancada-es/mcp/bancada-es-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bancada-es-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bancada-es/well-known/bancada-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bancada-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/bancada-es/hosts/bancada-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bancada-es-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bancada-es/security/bancada-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancada-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bancada.es/
- group: operate
  title: ''
  type: Support
  url: https://bancada.es/#contacto
- group: start
  title: ''
  type: GettingStarted
  url: https://bancada.es/#como
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint https://mcp-odoo.bancada.es/mcp returns 401 auth-required, indicating API is gated.
  evidence:
  - status: 401
    url: https://mcp-odoo.bancada.es/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: 'Design and manufacture of custom products: devices, applications and AI that connect to your business. We turn ideas from sketch to functional hardware and software, delivering IoT hardware, firmware, web and mobile apps, and MCP servers. Our team works together in the same workshop, ensuring rapid decision‑making and seamless integration of embedded software and hardware. Based in Barcelona, we serve industrial IoT, prototyping, and bespoke product development.'
image: https://bancada.es/assets/3d/portada.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp-odoo.bancada.es requiring OAuth.
  name: Bancada MCP Server
  slug: bancada-es-mcp-yml
modified: '2026-11-02'
name: Bancada
nav: Providers
network: true
overview: 'Bancada is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Hardware, Software, and Engineering.


  Bancada''s developer surface includes support, getting-started guide, and 5 more developer resources.'
plans:
- name: Bancada Es Plans Pricing
  plan_count: 0
  slug: bancada-es-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Bancada Es Rate Limits
  slug: bancada-es-rate-limits
scopes:
- name: Bancada Es Scopes
  scope_count: 0
  slug: bancada-es-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 10.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bancada Es Authentication
  slug: bancada-es-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bancada Es Domain Security
  slug: bancada-es-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bancada-es
tags:
- Company
- IoT
- Hardware
- Software
- Engineering
website: https://bancada.es/
---
