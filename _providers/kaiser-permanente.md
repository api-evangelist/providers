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
api_count: 1
apis:
- description: Kaiser Permanente provides a patient access FHIR API supporting the CMS Interoperability and Patient Access Final Rule. Authenticated members and their authorized third-party applications can retrieve
  name: Kaiser Permanente Patient Access FHIR API
  slug: kaiser-permanente-fhir
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaiser-permanente-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kaiserpermanente
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kaiser-permanente
- group: company
  title: ''
  type: Website
  url: https://www.kaiserpermanente.org/
- group: start
  title: ''
  type: Portal
  url: https://kp.org/fhir
- group: company
  title: ''
  type: Blog
  url: https://about.kaiserpermanente.org/news
created: '2026-05-05'
description: One of the largest nonprofit health plans in the United States integrating health insurance with healthcare delivery. Serves over 12 million members through its network of hospitals, medical offices, and health plan services. Publishes a patient access FHIR API at kp.org/fhir in compliance with the CMS Interoperability and Patient Access Final Rule.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaiser-permanente.png
layout: provider
modified: '2026-05-16'
name: Kaiser Permanente
nav: Providers
network: true
overview: 'Kaiser Permanente publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Insurance, Health Insurance, Hospitals, and FHIR.


  Kaiser Permanente''s developer surface includes developer portal, engineering blog, and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaiser-permanente/refs/heads/main/screenshots/kaiser-permanente-2026-06-20T183902.png
security:
- kind: domain-security
  name: Kaiser Permanente Domain Security
  slug: kaiser-permanente-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kaiser-permanente
tags:
- Healthcare
- Insurance
- Health Insurance
- Hospitals
- FHIR
- Interoperability
website: https://www.kaiserpermanente.org/
---
