---
access_model:
  confidence: high
  label: Free today, commercialization review required for production
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - '{''url'': ''https://developers.hyundai.com/web/v1/hyundai/faqs'', ''status'': 200, ''note'': ''provider states API use has been free to date and that charging is decided in consultation at commercialization review (probed 2026-09-13)''}'
  - '{''url'': ''https://developers.hyundai.com/api/v1/sampleTest/getSampleTestInfo'', ''status'': 200, ''note'': ''anonymous public sample-test tier issues a token and five fixture vehicles with no signup (probed 2026-09-13)''}'
  - '{''url'': ''https://www.hyundai.com/'', ''status'': 301, ''note'': ''declared corporate website redirects to https://www.hyundaiusa.com/us/en for US clients, but continues to serve /.well-known/security.txt and /llms.txt directly (probed 2026-09-13)''}'
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: 'Hyundai Developers exposes connected-car data from Bluelink-enrolled vehicles to third-party services over a REST API on prd.kr-ccapi.hyundai.com. Nineteen operations are published across five groups:'
  name: Hyundai Developers Connected Car API
  slug: hyundai-developer-api
artifact_total: 8
asyncapis:
- description: ''
  name: Hyundai Webhooks
  slug: hyundai-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hyundai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hyundai.com/web/v1/hyundai/data_api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hyundai.com/web/v1/hyundai/specification/account
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hyundai.com/web/v1/hyundai/guide_developers
- group: operate
  title: ''
  type: Support
  url: https://developers.hyundai.com/web/v1/hyundai/tech_support
- group: operate
  title: ''
  type: HelpCenter
  url: https://developers.hyundai.com/web/v1/hyundai/faqs
- group: start
  title: ''
  type: SignUp
  url: https://console.developers.hyundai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.hyundai.com/web/v1/hyundai/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.hyundai.com/overview/full-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/changelog/hyundai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hyundai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/lifecycle/hyundai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hyundai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/conformance/hyundai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hyundai-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/packages/hyundai-packages.yml
  title: ''
  type: Packages
  url: packages/hyundai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/llms/hyundai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hyundai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/well-known/hyundai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hyundai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/well-known/hyundai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hyundai-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/security/hyundai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/hyundai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/security/hyundai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyundai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/security/hyundai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hyundai-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/plans/hyundai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hyundai-plans-pricing.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyundai-motor-company
- group: company
  title: ''
  type: Website
  url: https://www.hyundai.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.hyundainews.com/
created: '2025-02-25'
description: Hyundai Motor Company is a South Korean multinational automotive manufacturer and, through Hyundai Developers, the operator of a connected-car data platform for third-party developers. The platform exposes the Hyundai integrated account over OAuth 2.0 and serves nineteen documented REST operations covering user profile, vehicle list, connected-service contract dates, odometer, distance-to-empty, EV battery and charging state, and seven warning-light indicators, sourced from vehicles enrolled in Bluelink. Access is governed by a two-stage consent model built around the Korean Personal Information Protection Act — a per-vehicle OAuth consent plus a separate third-party data-provision consent — and a manual commercialization review before any real customer vehicle data is released. The API reference, a public sample-test tier with fixture vehicles, and the developer guide are all readable without an account; data is limited to vehicles in South Korea.
finops:
- name: Hyundai Finops
  service_category: API
  slug: hyundai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyundai.png
layout: provider
modified: '2026-09-13'
name: Hyundai
nav: Providers
network: true
overview: 'Hyundai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Connected Vehicles, Mobility, and Vehicles.


  The Hyundai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hyundai''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Hyundai Plans Pricing
  plan_count: 0
  slug: hyundai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Hyundai Rate Limits
  slug: hyundai-rate-limits
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 57.1
    discoverability: 75.9
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 48.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/screenshots/hyundai-2026-06-20T183205.png
security:
- kind: authentication
  name: Hyundai Authentication
  slug: hyundai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Hyundai Domain Security
  slug: hyundai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hyundai Vulnerability Disclosure
  slug: hyundai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hyundai
tags:
- Automobiles
- Cars
- Connected Vehicles
- Mobility
- Vehicles
- Automotive
- Telematics
- Electric Vehicles
- Vehicle Data
- South Korea
website: https://www.hyundai.com/
---
