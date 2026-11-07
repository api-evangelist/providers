---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Tokamak Energy website at tokamakenergy.com: the route index of the site''s content management system, catalogued as one site surface rather than as separ'
  name: Tokamak Energy Website (WordPress REST)
  slug: tokamakenergy-com-website-wordpress-rest
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/tokamak-energy/plans/tokamak-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tokamak-energy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tokamak-energy/rate-limits/tokamak-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tokamak-energy-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://tokamakenergy.com/
- group: company
  title: ''
  type: About
  url: https://tokamakenergy.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://tokamakenergy.com/latest-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://tokamakenergy.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://tokamakenergy.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tokamakenergy.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokamak-energy
- group: company
  title: ''
  type: Careers
  url: https://tokamakenergy.com/careers-at-tokamak-energy-fusion-energy/
- group: other
  title: ''
  type: Technology
  url: https://tokamakenergy.com/our-fusion-energy-and-hts-technology/
- group: learn
  title: ''
  type: Videos
  url: https://tokamakenergy.com/videos/
- group: auth
  href: https://artifacts.apis.io/tokamak-energy/authentication/tokamak-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tokamak-energy-authentication.yml
- group: design
  href: https://artifacts.apis.io/tokamak-energy/conventions/tokamak-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tokamak-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/tokamak-energy/errors/tokamak-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tokamak-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tokamak-energy/conformance/tokamak-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tokamak-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/tokamak-energy/lifecycle/tokamak-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tokamak-energy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tokamak-energy/data-model/tokamak-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tokamak-energy-data-model.yml
- group: build
  href: https://artifacts.apis.io/tokamak-energy/packages/tokamak-energy-packages.yml
  title: ''
  type: Packages
  url: packages/tokamak-energy-packages.yml
- group: agent
  href: https://artifacts.apis.io/tokamak-energy/llms/tokamak-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tokamak-energy-llms.txt
- group: auth
  href: https://artifacts.apis.io/tokamak-energy/security/tokamak-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tokamak-energy-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/tokamak-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: 'Tokamak Energy is a private fusion energy company founded in 2009 as a spinout from the UK Atomic Energy Authority, headquartered at 173 Brook Drive, Milton Park, Oxfordshire OX14 4SD, with subsidiaries in the United States and Japan and more than 300 employees. It runs a two-track strategy: advancing commercial fusion energy through compact spherical tokamaks, and developing high temperature superconducting (HTS) magnet technology as a business in its own right. Its flagship device ST40 is the world''s highest field spherical tokamak and is undergoing a USD 52 million upgrade co-funded with the US Department of Energy and the UK Department for Energy Security and Net Zero. Demo4 became the first HTS fusion magnet system to achieve fusion-relevant magnetic fields in 2025, and the company was selected as Magnet Systems Partner for the UK''s STEP programme under a GBP 70 million contract running to 2029. The group is organised into three integrated businesses — TE Magnetics (HTS
  technology, established 2024), Ridgway Machines (manufacturing, acquired 2025) and Fusion. Tokamak Energy is a fusion and superconducting hardware company rather than a software vendor: it publishes no commercial or developer-facing product API, no developer portal, no SDKs and no OpenAPI of its own. The only machine-readable interface it exposes publicly is the WordPress REST content API behind its corporate website at tokamakenergy.com, which is anonymously readable, read-only for unauthenticated callers, and is captured here for discovery purposes. Its public engineering output is instead released as open-source plasma physics code — GSFit, RTGSFit and FORGE — through the tokamak-energy GitHub organisation.'
image: https://tokamakenergy.com/wp-content/uploads/2025/03/TE_symbol_orange.svg
layout: provider
modified: '2026-08-30'
name: Tokamak Energy
nav: Providers
network: true
overview: 'Tokamak Energy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fusion Energy, Energy, Superconductors, and HTS Magnets.


  Tokamak Energy''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Tokamak Energy Plans Pricing
  plan_count: 0
  slug: tokamak-energy-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Tokamak Energy Rate Limits
  slug: tokamak-energy-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 15.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tokamak-energy/tokamak-energy-2026-09-02T163845.png
security:
- kind: authentication
  name: Tokamak Energy Authentication
  slug: tokamak-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tokamak Energy Domain Security
  slug: tokamak-energy-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: tokamak-energy-discover-the-surface
  slug: tokamak-energy-discover-the-surface
- name: tokamak-energy-harvest-media
  slug: tokamak-energy-harvest-media
- name: tokamak-energy-track-fusion-news
  slug: tokamak-energy-track-fusion-news
slug: tokamak-energy
tags:
- Company
- Fusion Energy
- Energy
- Superconductors
- HTS Magnets
- Advanced Manufacturing
- Deep Tech
- Plasma Physics
- Scientific Computing
- Research and Development
- United Kingdom
website: https://tokamakenergy.com/
---
