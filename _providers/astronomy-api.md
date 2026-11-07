---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Astronomy Api Agentic Access
  operation_count: 7
  slug: astronomy-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 2
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
artifact_total: 31
collections:
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
- group: commercial
  href: https://artifacts.apis.io/astronomy-api/plans/astronomy-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astronomy-api-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/astronomy-api/finops/astronomy-api-finops.yml
  title: ''
  type: FinOps
  url: finops/astronomy-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://astronomyapi.com/blog/
- group: other
  href: https://artifacts.apis.io/astronomy-api/overlays/astronomy-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/astronomy-api-v3-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://astronomyapi.com/
- group: agent
  href: https://artifacts.apis.io/astronomy-api/agentic-access/astronomy-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astronomy-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/astronomy-api/security/astronomy-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astronomy-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/astronomy-api/authentication/astronomy-api-authentication.yml
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
  href: https://artifacts.apis.io/astronomy-api/conventions/astronomy-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/astronomy-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/astronomy-api/errors/astronomy-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astronomy-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astronomy-api/lifecycle/astronomy-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/astronomy-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/astronomy-api/conformance/astronomy-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astronomy-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/astronomy-api/data-model/astronomy-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astronomy-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/astronomy-api/packages/astronomy-api-packages.yml
  title: ''
  type: Packages
  url: packages/astronomy-api-packages.yml
- group: build
  href: https://artifacts.apis.io/astronomy-api/packages/astronomy-api-packages.yml
  title: ''
  type: SDKs
  url: packages/astronomy-api-packages.yml
- group: design
  href: https://artifacts.apis.io/astronomy-api/components/astronomy-api-components.yml
  title: ''
  type: Components
  url: components/astronomy-api-components.yml
- group: operate
  href: https://artifacts.apis.io/astronomy-api/rate-limits/astronomy-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/astronomy-api-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/astronomy-api/mcp/astronomy-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/astronomy-api-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/astronomy-api/mcp/astronomy-api-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/astronomy-api-mcp.yml
- group: agent
  href: https://artifacts.apis.io/astronomy-api/skills/_index.yml
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
- has_sources: false
  method: generated
  name: Astronomy Api Finops
  primary_unit: request
  service_category: API
  slug: astronomy-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astronomy-api.png
integrations:
- description: Mobile applications integrate the Astronomy API to provide real-time sky data and star chart overlays for stargazing experiences.
  name: Mobile Astronomy Apps
- description: Planetarium and sky simulation software integrates celestial body position data from the Astronomy API for accurate sky rendering.
  name: Planetarium Software
layout: provider
modified: '2026-10-06'
name: Astronomy API
nav: Providers
network: true
overview: 'Astronomy API publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bodies API, Events API, Search API, and 2 more. Tagged areas include Astronomy, Celestial Data, Space, Moon Phases, and Star Charts.


  The Astronomy API catalog on APIs.io includes 1 Spectral governance ruleset.


  Astronomy API''s developer surface includes engineering blog, authentication, developer portal, documentation, signup flow, changelog, support, and 22 more developer resources.'
plans:
- name: Astronomy Api Plans Pricing
  plan_count: 0
  slug: astronomy-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Astronomy Api Rate Limits
  slug: astronomy-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Astronomy API API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 2
  slug: astronomy-api-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 47.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/astronomy-api/astronomy-api-2026-06-20T172510.png
security:
- kind: authentication
  name: Astronomy Api Authentication
  slug: astronomy-api-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Astronomy Api Domain Security
  slug: astronomy-api-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: astronomy-api-deep-sky-search
  slug: astronomy-api-deep-sky-search
- name: astronomy-api-moon-phase-image
  slug: astronomy-api-moon-phase-image
- name: astronomy-api-observation-planning
  slug: astronomy-api-observation-planning
- name: astronomy-api-star-chart-image
  slug: astronomy-api-star-chart-image
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
