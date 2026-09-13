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
  scored_at: '2026-09-12'
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
  description: 'Distribution-side REST API of TIGER GDS. Version 2.0, OpenAPI 3.1.1, 24 operations across five capability groups: reference code lookups (languages, currencies, continents, countries, regions, cities,'
  name: AGL OTA API
  slug: agl-ota
- baseURL: https://agl-bridgeapi.tigergds.com
  baseurl_source: declared
  description: 'Supplier-integration bridge API between AGL and golf-club suppliers. Version 0.0.1, OpenAPI 3.1.1, 7 operations in two directions: Supplier to AGL (register a golf club, retrieve golf club information'
  name: AGL OPEN API
  slug: agl-open
- baseURL: https://outboundapi-trip-reserv.tigergds.com
  baseurl_source: declared
  description: AGL-operated outbound reservation bridge that accepts Trip.com-format reservation messages. OpenAPI 3.0.1, a single POST /api/v1 operation carrying a signed request header (accountId, serviceName enum
  name: AGL Trip.com Reservation Integration API
  slug: agl-tripcom-outbound
artifact_total: 9
asyncapis:
- description: ''
  name: Agl Webhooks
  slug: agl-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agl-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/agl-packages.yml
- group: agent
  title: ''
  type: X-WellKnownProbe
  url: well-known/agl-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/agl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agl-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/agl-ota-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/agl-open-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/agl-tripcom-outbound-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/agl-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agl-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agl-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agl-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agl-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agl-plans-pricing.yml
- group: operate
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
overview: 'AGL publishes 3 APIs on the [APIs.io](https://apis.io/) network: OTA API, OPEN API, and Trip.com Reservation Integration API. Tagged areas include Company, Golf, Travel, Booking, and Reservations.


  The AGL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AGL''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Agl Plans Pricing
  plan_count: 0
  slug: agl-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Agl Rate Limits
  slug: agl-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 37.5
    discoverability: 74.1
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-12'
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
