---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: HTTP/JSON API for Advanced Navigation's Kinematica cloud GNSS/INS post-processing kinematic (PPK) service. Eleven documented calls let a customer application create a data set, upload primary and seco
  name: Kinematica API
  slug: advancednavigation-kinematica
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancednavigation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.advancednavigation.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.advancednavigation.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://www.advancednavigation.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.advancednavigation.com/accessories/gnss-ins-post-processing/kinematica/api-reference-manual/
- group: operate
  title: ''
  type: Support
  url: https://help.advancednavigation.com/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.advancednavigation.com/
- group: company
  title: ''
  type: Blog
  url: https://www.advancednavigation.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/advanced-navigation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.advancednavigation.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advancednavigation.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://hq.advancednavigation.com.au/kinematica/home.jsp
- group: start
  title: ''
  type: SignUp
  url: https://hq.advancednavigation.com.au/kinematica/home.jsp
- group: build
  title: ''
  type: Packages
  url: packages/advancednavigation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/advancednavigation-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advancednavigation-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advancednavigation-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advancednavigation-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advancednavigation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advancednavigation-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/advancednavigation-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advancednavigation-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/advancednavigation-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/advancednavigation-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advancednavigation-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancednavigation-llms.txt
created: '2026-09-09'
description: Advanced Navigation is an Australian navigation and robotics manufacturer (Sydney, NSW) building inertial navigation systems (INS), IMU/AHRS, GNSS compasses, acoustic/USBL subsea positioning and underwater robotics for air, land, sea and space — the Boreas FOG and Certus MEMS GNSS/INS families, Motus, GNSS Compass, Subsonus USBL, Subsonus Tag and the Hydrus micro-AUV, plus the Chimera laser velocity sensor and Air Data Unit aiding accessories. Its devices speak the proprietary binary Advanced Navigation Packet Protocol (ANPP), documented in per-product reference manuals and implemented by first-party C SDKs, a Python SDK on PyPI and ROS 1 / ROS 2 drivers. Its one public web API is the Kinematica API — an HTTP/JSON interface to the Kinematica cloud GNSS/INS post-processing (PPK) service, documented as a versioned PDF reference manual rather than a machine-readable specification.
image: https://www.advancednavigation.com/wp-content/uploads/2024/08/adnav_logo_420x91-colour.webp
layout: provider
modified: '2026-09-09'
name: Advanced Navigation
nav: Providers
network: true
overview: 'Advanced Navigation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Navigation, Inertial Navigation, GNSS, and Positioning.


  Advanced Navigation''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Advancednavigation Plans Pricing
  plan_count: 3
  slug: advancednavigation-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Advancednavigation Rate Limits
  slug: advancednavigation-rate-limits
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    operational_transparency: 47.4
  previous_composite: 41.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advancednavigation Authentication
  slug: advancednavigation-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Advancednavigation Domain Security
  slug: advancednavigation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: advancednavigation
tags:
- Company
- Navigation
- Inertial Navigation
- GNSS
- Positioning
- Robotics
- Defense
- Subsea
- Geospatial
- Post Processing
- Hardware
website: https://www.advancednavigation.com/
---
