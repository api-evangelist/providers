---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Odessia provides a platform API (details gated behind authentication).
  name: Odessia API
  slug: odessia-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/odessia/well-known/odessia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/odessia-well-known.yml
- group: other
  href: https://artifacts.apis.io/odessia/hosts/odessia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/odessia-hosts.yml
- group: other
  href: https://artifacts.apis.io/odessia/vendors/odessia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/odessia-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.odessia.com/
- group: auth
  href: https://artifacts.apis.io/odessia/security/odessia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odessia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://odessia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://odessia.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://odessia.com/terms
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract found; only opaque GraphQL and MCP endpoints require authentication.
  evidence:
  - status: 401
    url: https://api.odessia.com/api/graphql
  - status: 401
    url: https://api.odessia.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Odessia is an AI-powered travel concierge that plans and books trips, accommodations, and experiences for users. It offers personalized itineraries, integrates loyalty programs, and provides real-time assistance via messaging. The platform aims to simplify travel planning with AI-driven recommendations and seamless booking, targeting modern travelers seeking convenience and tailored experiences.
image: https://odessia.com/public/og/odessia-preview.png
layout: provider
modified: '2026-10-29'
name: Odessia
nav: Providers
network: true
overview: Odessia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, AI, Concierge, and Booking.
random_paper: 0
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Odessia Domain Security
  slug: odessia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: odessia
tags:
- Company
- Travel
- AI
- Concierge
- Booking
website: https://odessia.com/
---
