---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Astronomy Api Agentic Access
  operation_count: 7
  slug: astronomy-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: The Astronomy API provides access to astronomical data including celestial body positions, moon phases, planet positions, star charts, astronomical events, and deep space object search for any locatio
  name: Astronomy API
  slug: astronomy-api
- baseURL: https://api.astronomyapi.com/api/v2
  baseurl_source: declared
  description: Celestial body information and positions
  name: Astronomy API Bodies API
  slug: astronomy-api-bodies-api
- baseURL: https://api.astronomyapi.com/api/v2
  baseurl_source: declared
  description: Astronomical events for a given location and date range
  name: Astronomy API Events API
  slug: astronomy-api-events-api
- baseURL: https://api.astronomyapi.com/api/v2
  baseurl_source: declared
  description: Search for stars and deep space objects
  name: Astronomy API Search API
  slug: astronomy-api-search-api
- baseURL: https://api.astronomyapi.com/api/v2
  baseurl_source: declared
  description: Generated imagery (moon phase and star charts)
  name: Astronomy API Studio API
  slug: astronomy-api-studio-api
- baseURL: https://api.astronomyapi.com/api/v3
  baseurl_source: declared
  description: Version 3 of the Astronomy API, published by the provider as a reference draft with a complete OpenAPI 3.1 definition before it ships — "so that the design can be read and argued with". A breaking red
  name: Astronomy API v3
  slug: astronomy-api-v3
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Astronomy Bodies API
  slug: open-astronomy-api-bodies-api
- collection_type: open
  name: Astronomy Bodies Events API
  slug: open-astronomy-api-events-api
- collection_type: open
  name: Astronomy Bodies Search API
  slug: open-astronomy-api-search-api
- collection_type: open
  name: Astronomy Bodies Studio API
  slug: open-astronomy-api-studio-api
- collection_type: open
  name: Astronomy API
  slug: open-astronomy-api
common:
- group: company
  title: ''
  type: Website
  url: https://astronomyapi.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/astronomy-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astronomy-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/astronomy-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AstronomyAPI
- group: start
  title: Astronomy API Website
  type: Portal
  url: https://astronomyapi.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://docs.astronomyapi.com/
- group: start
  title: Sign Up
  type: Signup
  url: https://astronomyapi.com/auth/signup
- group: agent
  title: llms.txt (documentation host)
  type: LlmsText
  url: https://docs.astronomyapi.com/llms.txt
- group: operate
  title: Changelog
  type: ChangeLog
  url: https://docs.astronomyapi.com/changelog
- group: commercial
  title: Terms of Service
  type: TermsOfService
  url: https://astronomyapi.com/terms-of-service
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://astronomyapi.com/privacy-policy
- group: operate
  title: Support (GitHub issues, per the provider's Getting Started page)
  type: Support
  url: https://github.com/AstronomyAPI/Samples/issues
- group: design
  title: ''
  type: Conventions
  url: conventions/astronomy-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/astronomy-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astronomy-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astronomy-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/astronomy-api-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/astronomy-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/astronomy-api-packages.yml
- group: design
  title: ''
  type: Components
  url: components/astronomy-api-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/astronomy-api-rate-limits.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/astronomy-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/astronomy-api-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2024-03-30'
description: AstronomyAPI is a web API for retrieving astronomical information including data about celestial bodies, moon phases, planet positions, star charts, and astronomical events for a given location and time. The API provides developers with access to celestial body positions, astronomical event data, star chart generation, moon phase imagery, and deep space object search capabilities for any geographic location and date/time combination.
features:
- description: Retrieve real-time and historical positions of celestial bodies including planets, moons, and other astronomical objects for any geographic location and date/time.
  name: Celestial Body Positions
- description: Access data on celestial events such as eclipses, conjunctions, and other notable astronomical occurrences for a given body and date range.
  name: Astronomical Events
- description: Generate customizable star charts as images for any sky position, date, and observer location for use in applications and publications.
  name: Star Chart Generation
- description: Generate moon phase images showing the illumination and appearance of the moon for any given date and location.
  name: Moon Phase Imagery
- description: Search for stars and deep space objects by name or catalog designation to retrieve positional and descriptive data.
  name: Deep Space Object Search
finops:
- name: Astronomy Api Finops
  service_category: API
  slug: astronomy-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astronomy-api.png
integrations:
- description: Mobile applications integrate the Astronomy API to provide real-time sky data and star chart overlays for stargazing experiences.
  name: Mobile Astronomy Apps
- description: Planetarium and sky simulation software integrates celestial body position data from the Astronomy API for accurate sky rendering.
  name: Planetarium Software
layout: provider
modified: '2026-09-04'
name: Astronomy API
nav: Providers
network: true
overview: 'Astronomy API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bodies API, Events API, Search API, and 2 more. Tagged areas include Astronomy, Celestial Data, Space, Moon Phases, and Star Charts.


  Astronomy API''s developer surface includes authentication, developer portal, documentation, signup flow, changelog, support, and 19 more developer resources.'
plans:
- name: Astronomy Api Plans Pricing
  plan_count: 0
  slug: astronomy-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Astronomy Api Rate Limits
  slug: astronomy-api-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astronomy-api/refs/heads/main/screenshots/astronomy-api-2026-06-20T172510.png
security:
- kind: authentication
  name: Astronomy Api Authentication
  slug: astronomy-api-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Astronomy Api Domain Security
  slug: astronomy-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: astronomy-api
tags:
- Astronomy
- Celestial Data
- Space
- Moon Phases
- Star Charts
use_cases:
- description: Developers build educational astronomy applications that display real-time planet positions, star charts, and moon phases for learners and enthusiasts.
  name: Astronomy Education Apps
- description: Amateur astronomers use the API to plan observing sessions by retrieving celestial body positions and upcoming astronomical events for their location.
  name: Observation Planning Tools
- description: Astrology apps integrate the Astronomy API for accurate planetary position data to power birth chart calculations and transit predictions.
  name: Astrology and Horoscope Applications
website: https://astronomyapi.com/
---
