---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Agl Agentic Access
  operation_count: 31
  slug: agl-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 3
apis:
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: APIs where AGL sends reservation and cancellation requests to suppliers
  name: AGL AGL To Supplier API
  slug: agl-agltosupplier-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Codes API from AGL — 9 operation(s) for codes.
  name: AGL Codes API
  slug: agl-codes-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Golf Clubs API from AGL — 2 operation(s) for golf clubs.
  name: AGL Golf Clubs API
  slug: agl-golf-clubs-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Reservation API from AGL — 1 operation(s) for reservation.
  name: AGL Reservation API
  slug: agl-reservation-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Reservations API from AGL — 6 operation(s) for reservations.
  name: AGL Reservations API
  slug: agl-reservations-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Static Packages API from AGL — 2 operation(s) for static packages.
  name: AGL Static Packages API
  slug: agl-static-packages-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: APIs where suppliers send data to AGL (e.g., golf club registration, tee times, etc.)
  name: AGL Supplier To AGL API
  slug: agl-suppliertoagl-api
- baseURL: https://gw-ota.tigergds.com
  baseurl_source: declared
  description: The Tee Times API from AGL — 2 operation(s) for tee times.
  name: AGL Tee Times API
  slug: agl-tee-times-api
artifact_total: 14
asyncapis:
- description: ''
  name: Agl Webhooks
  slug: agl-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/agentic-access/agl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agl-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/security/agl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agl-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/authentication/agl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agl-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aglgw.com/en/
- group: company
  title: ''
  type: About
  url: https://www.aglgw.com/en/aboutagl
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.tigergds.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.tigergds.com/reference
- group: operate
  title: ''
  type: Support
  url: https://www.aglgw.com/en/partners
- group: company
  title: ''
  type: Blog
  url: https://www.aglgw.com/en/contents/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aglgw
- group: start
  title: ''
  type: SignUp
  url: https://www.tigergds.com/signup/step1
- group: start
  title: ''
  type: Login
  url: https://www.tigergds.com/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aglgw
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/packages/agl-packages.yml
  title: ''
  type: Packages
  url: packages/agl-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/well-known/agl-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/agl-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/mcp/agl-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agl-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/llms/agl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agl-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/overlays/agl-ota-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agl-ota-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/overlays/agl-open-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agl-open-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/overlays/agl-tripcom-outbound-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agl-tripcom-outbound-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/conformance/agl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agl-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/errors/agl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agl-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/lifecycle/agl-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agl-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/conventions/agl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agl-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/data-model/agl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agl-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/asyncapi/agl-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agl-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/plans/agl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agl-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agl/refs/heads/main/rate-limits/agl-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agl-rate-limits.yml
created: '2026-09-12'
description: 'AGL Inc. (에이지엘) is a Seoul-headquartered golf technology company, founded in 2019, that operates TIGER GDS — a global distribution system for golf. Its SaaS platform connects golf club tee-time inventory to travel and booking channels in real time, covering more than 1,000 contracted golf courses across 30+ countries, and is the system behind the HeyTeeTime/TIGERBOOKING consumer apps and the Reserve with Google golf integration. AGL publishes three machine-readable REST contracts on tigergds.com: the AGL OTA API (distribution — code lookups, golf club catalog, tee-time availability, static packages and the full reservation lifecycle), the AGL OPEN API (a bi-directional supplier bridge for golf-club and tee-time registration plus reservation callbacks) and a Trip.com outbound reservation integration. Offices in Seoul, Tokyo, Brea (CA) and Singapore.'
image: https://www.aglgw.com/image/ko/img_main.png
layout: provider
modified: '2026-09-12'
name: AGL
nav: Providers
network: true
overview: 'AGL publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AGL To Supplier API, Codes API, Golf Clubs API, and 5 more. Tagged areas include Company, Golf, Travel, Booking, and Reservations.


  The AGL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AGL''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Agl Plans Pricing
  plan_count: 0
  slug: agl-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agl Rate Limits
  slug: agl-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 60.3
    developer_ergonomics: 37.5
    discoverability: 74.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agl Authentication
  slug: agl-authentication
  summary_line: apiKey/http · 9 schemes
- kind: domain-security
  name: Agl Domain Security
  slug: agl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agl
tags:
- Company
- Golf
- Travel
- Booking
- Reservations
- Distribution
- Tee Times
- GDS
- Hospitality
- Sports
- Leisure
- South Korea
website: https://www.aglgw.com/en/
---
