---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-09-19'
api_count: 1
apis:
- baseURL: https://edelweiss-hotel.com.ua
  baseurl_source: declared
  description: Official open REST API (JSON + XML) for Edelweiss Hotel Polyana with OpenAPI 3.1.0 contract, hotel info, room tariffs, real-time quotes, Google Hotels XML feed, and LLM knowledge manifests. No authent
  name: Edelweiss Hotel Polyana API
  slug: edelweiss-hotel-polyana-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://edelweiss-hotel.com.ua/
- group: docs
  title: ''
  type: Documentation
  url: https://edelweiss-hotel.com.ua/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://edelweiss-hotel.com.ua/prices/
- group: operate
  title: ''
  type: Support
  url: https://edelweiss-hotel.com.ua/contacts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edelweiss-hotel.com.ua/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edelweiss-hotel.com.ua/privacy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/authentication/edelweiss-hotel-polyana-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edelweiss-hotel-polyana-api-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/well-known/edelweiss-hotel-polyana-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edelweiss-hotel-polyana-api-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/mcp/edelweiss-hotel-polyana-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edelweiss-hotel-polyana-api-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/conformance/edelweiss-hotel-polyana-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edelweiss-hotel-polyana-api-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/conventions/edelweiss-hotel-polyana-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edelweiss-hotel-polyana-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/data-model/edelweiss-hotel-polyana-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edelweiss-hotel-polyana-api-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edelweiss-hotel-polyana-api-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/plans/edelweiss-hotel-polyana-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edelweiss-hotel-polyana-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/rate-limits/edelweiss-hotel-polyana-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edelweiss-hotel-polyana-api-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/edelweiss-hotel-polyana-api/refs/heads/main/security/edelweiss-hotel-polyana-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edelweiss-hotel-polyana-api-domain-security.yml
created: '2026-09-18'
description: Public open REST API and structured data feeds for Edelweiss Hotel Polyana, a 3-star boutique eco-hotel in Polyana, Zakarpattia, Ukraine. Provides real-time room tariffs, hotel info, a Google Hotels XML pricing feed, quote calculation, and LLM knowledge bases. Open access, no authentication.
layout: provider
mcp_servers:
- description: 'Candidate MCP tool list derived from the hotel''s open REST API. No MCP server is published by the provider; these tools would map 1:1 onto the existing unauthenticated GET operations if a server were '
  name: Edelweiss Hotel Polyana API MCP Server
  slug: edelweiss-hotel-polyana-api-mcp-server
modified: '2026-09-18'
name: Edelweiss Hotel Polyana API
nav: Providers
network: true
overview: 'Edelweiss Hotel Polyana API publishes 1 API on the [APIs.io](https://apis.io/) network: Edelweiss Hotel Polyana API. Tagged areas include Hotels, Hospitality, Travel, Tourism, and Ukraine.


  Edelweiss Hotel Polyana API''s developer surface includes documentation, pricing, support, authentication, and 13 more developer resources.'
plans:
- name: Edelweiss Hotel Polyana Api Plans Pricing
  plan_count: 0
  slug: edelweiss-hotel-polyana-api-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Edelweiss Hotel Polyana Api Rate Limits
  slug: edelweiss-hotel-polyana-api-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 23.2
    discoverability: 72.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ukraine
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 34.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Edelweiss Hotel Polyana Api Authentication
  slug: edelweiss-hotel-polyana-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Edelweiss Hotel Polyana Api Domain Security
  slug: edelweiss-hotel-polyana-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: edelweiss-hotel-polyana-api
tags:
- Hotels
- Hospitality
- Travel
- Tourism
- Ukraine
- Carpathians
- Mineral Water
- Balneology
- Booking
- Room Rates
- google-hotels
website: https://edelweiss-hotel.com.ua/
---
