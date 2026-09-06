---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbor-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://harborhealth.com
- group: company
  title: ''
  type: Blog
  url: https://harborhealth.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harborhealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harborhealth.com/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://harborhealth.com/member-portal-login
created: '2026-07-17'
description: Harbor Health is a Central Texas healthcare company building a vertically integrated "pay-vider" model that combines primary care, specialty care, and health coaching clinics with its own commercial and individual health insurance plans, so the same organization both delivers and covers care. Founded in 2022 by Dr. Clay Johnston (founding dean of UT Dell Medical School), Tony Miller, and Eric Scott, the company operates clinics and Express Care walk-in locations across the Austin, Dallas, El Paso, and San Antonio metros, and is pursuing a value-based care model for the commercial market. It is backed by General Catalyst, 8VC, and Alta Partners. Harbor Health publishes no public developer API; this API Evangelist profile tracks its public web properties (member portal, plans, blog, privacy and terms) for discovery and monitoring.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbor-health.png
layout: provider
modified: '2026-07-19'
name: Harbor Health
nav: Providers
network: true
overview: 'Harbor Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Insurance, Primary Care, and Specialty Care.


  Harbor Health''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbor-health/refs/heads/main/screenshots/harbor-health-2026-07-25T220703.png
security:
- kind: domain-security
  name: Harbor Health Domain Security
  slug: harbor-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harbor-health
tags:
- Company
- Healthcare
- Health Insurance
- Primary Care
- Specialty Care
- Value-Based Care
- Payer-Provider
- Texas
website: https://harborhealth.com
---
