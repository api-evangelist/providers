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
  url: security/rippl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ripplcare.com/
created: '2026-07-17'
description: 'Rippl (Rippl Care, now part of Harbor Health) is a value-based, technology-enabled dementia and senior behavioral-health care provider backed by General Catalyst. It delivers specialized dementia care including medication assessments, personalized care plans, counseling, community-resource connections, care-navigation check-ins, safety guidance, and caregiver support, partnering with health systems and payors to lower total cost of care and improve outcomes for older adults. Rippl operates as a clinical care-delivery organization rather than an API-first software vendor: it publishes no public developer API, SDK, or documentation surface, and its patient portal is provided through an athenahealth integration.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rippl.png
layout: provider
modified: '2026-07-21'
name: Rippl
nav: Providers
network: true
overview: Rippl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Dementia Care, Behavioral Health, and Value-Based Care.
random_paper: 5
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rippl/refs/heads/main/screenshots/rippl-2026-09-02T153844.png
security:
- kind: domain-security
  name: Rippl Domain Security
  slug: rippl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rippl
tags:
- Company
- Healthcare
- Dementia Care
- Behavioral Health
- Value-Based Care
- Senior Care
- Caregiver Support
- Telehealth
website: https://ripplcare.com/
---
