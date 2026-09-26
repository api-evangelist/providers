---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: REST place-search and geocoding API (search, reverse geocode, nearby, bbox, countries). API-key authenticated via X-API-Key header or api_key query param. Includes an unauthenticated machine agent-onb
  name: Geoloods API
  slug: geoloods-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://geoloods.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://geoloods.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://geoloods.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://geoloods.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://geoloods.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://geoloods.io/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geoloods.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geoloods.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.softwareloods.nl/798067685
- group: operate
  title: ''
  type: Support
  url: mailto:support@geoloods.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/security/geoloods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoloods-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/authentication/geoloods-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geoloods-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/conformance/geoloods-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geoloods-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/lifecycle/geoloods-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geoloods-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/rate-limits/geoloods-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geoloods-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/plans/geoloods-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geoloods-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/geoloods/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-20'
description: A place-search and geocoding API that resolves named places (cities, towns, villages, parks, landmarks) to coordinates and rich location metadata over JSON/HTTPS. Covers 6.5M+ named places across 195 countries with coordinates, timezone, population, and country metadata. Agent-aware with machine signup and llms.txt index.
layout: provider
mcp_servers:
- description: ''
  name: Geoloods MCP Server
  slug: geoloods-mcp-server
modified: '2026-09-20'
name: Geoloods
nav: Providers
network: true
overview: 'Geoloods publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding, Place Search, Location, Coordinates, and Mapping.


  Geoloods'' developer surface includes documentation, API reference, pricing, signup flow, support, authentication, and 11 more developer resources.'
plans:
- name: Geoloods Plans Pricing
  plan_count: 4
  slug: geoloods-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Geoloods Rate Limits
  slug: geoloods-rate-limits
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 44.6
    discoverability: 69.6
    operational_transparency: 15.8
  previous_composite: 47.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Geoloods Authentication
  slug: geoloods-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Geoloods Domain Security
  slug: geoloods-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: geoloods
tags:
- Geocoding
- Place Search
- Location
- Coordinates
- Mapping
- Geospatial
- Agents
- OpenAPI
- llms-txt
website: https://geoloods.io
---
