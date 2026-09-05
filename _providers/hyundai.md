---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.hyundai.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.hyundaiusa.com/us/en — a different registrable domain (hyundai.com -> hyundaiusa.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Hyundai's developer platform provides APIs for connected vehicle services including remote control, vehicle status, energy management, diagnostics, and other mobility features for partners and integra
  name: Hyundai Developer API
  slug: hyundai-developer-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyundai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyundai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyundai
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
  type: USWebsite
  url: https://www.hyundaiusa.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.hyundai.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.hyundainews.com/
created: '2025-02-25'
description: Hyundai Motor Company is a South Korean multinational automotive manufacturer specializing in designing and producing a wide range of vehicles including cars, SUVs, and commercial vehicles. Hyundai operates a developer portal exposing connected vehicle services, mobility solutions, and partner integration touchpoints.
finops:
- name: Hyundai Finops
  service_category: API
  slug: hyundai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyundai.png
layout: provider
modified: '2026-04-28'
name: Hyundai
nav: Providers
network: true
overview: 'Hyundai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Connected Vehicles, Mobility, and Vehicles.


  Hyundai''s developer surface includes developer portal and 7 more developer resources.'
plans:
- name: Hyundai Plans Pricing
  plan_count: 3
  slug: hyundai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Hyundai Rate Limits
  slug: hyundai-rate-limits
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/screenshots/hyundai-2026-06-20T183205.png
security:
- kind: domain-security
  name: Hyundai Domain Security
  slug: hyundai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hyundai Vulnerability Disclosure
  slug: hyundai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hyundai
tags:
- Automobiles
- Cars
- Connected Vehicles
- Mobility
- Vehicles
website: https://www.hyundai.com/
---
