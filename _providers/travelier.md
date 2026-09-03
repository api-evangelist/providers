---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Travelier Connect is the group's partner distribution API — marketed on travelier.com/partners as "the largest ground & sea transportation GDS", aggregating 12,000+ intercity transport operators acros
  name: Travelier Connect
  slug: travelier-connect
- description: SeatOS is Travelier's SaaS transportation management system for ground and sea operators (built for APAC operators, sibling to Sisorg in Latin America). Its marketing site publishes a single documente
  name: SeatOS API
  slug: seatos-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.travelier.com/
- group: operate
  title: ''
  type: Support
  url: https://www.travelier.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Travelier
- group: commercial
  title: ''
  type: Plans
  url: plans/travelier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/travelier-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/travelier-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/travelier-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/travelier-llms.txt
coverage:
  checked: '2026-08-30'
  detail: 'Travelier markets two APIs — Travelier Connect ("the largest ground & sea transportation GDS") and the SeatOS operator API — but publishes neither a developer portal nor a reference: both partner pages terminate in a "Let''s Talk" / "Request API docs" contact form, docs.seatos.com and api.seatos.com serve the SeatOS login SPA, and api.travelier.com answers every path with HTTP 403 {"message":"Missing Authentication Token"}.'
  evidence:
  - status: 200
    url: https://www.travelier.com/partners/
  - status: 200
    url: https://www.seatos.com/
  - status: 200
    url: https://docs.seatos.com/
  - status: 403
    url: https://api.travelier.com/
  - status: 403
    url: https://api.12go.asia/openapi.json
  - status: 404
    url: https://www.travelier.com/.well-known/agent-card.json
  - status: 404
    url: https://www.bookaway.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-08-30'
description: 'Travelier (founded 2016, formerly Bookaway Group, headquartered in Tel Aviv, Israel) is a travel technology group digitizing ground and sea transportation — the segment of travel that is still largely sold offline. The group operates seven consumer and operator brands: Bookaway, 12Go, Plataforma10, DeOnibus, Traveling.com, Sisorg and SeatOS, together reaching more than 120 countries and roughly 14 million monthly visitors. Its commercial developer surface is Travelier Connect, a single partner API that the company markets as the largest ground and sea transportation GDS — 12,000+ operators across 122 countries and around 500,000 routes for buses, ferries, trains and shuttles — alongside the SeatOS transportation management system, which exposes the same inventory to OTAs, GDSs, resellers and agent networks through one API connection. Both are partner integrations: as of this profile no public developer portal, API reference or machine-readable contract is published, and access
  runs through a sales contact form.'
image: https://www.travelier.com/wp-content/uploads/2024/01/T_Icon_square.png
layout: provider
modified: '2026-08-30'
name: Travelier
nav: Providers
network: true
overview: 'Travelier publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Transportation, Ground Transportation, and Ferries.


  Travelier''s developer surface includes support and 8 more developer resources.'
plans:
- name: Travelier Plans Pricing
  plan_count: 0
  slug: travelier-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Travelier Rate Limits
  slug: travelier-rate-limits
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.2
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/travelier/refs/heads/main/screenshots/travelier-2026-09-02T164142.png
security:
- kind: domain-security
  name: Travelier Domain Security
  slug: travelier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: travelier
tags:
- Company
- Travel
- Transportation
- Ground Transportation
- Ferries
- Bus
- Trains
- Booking
- Marketplace
- Distribution
website: https://www.travelier.com/
---
