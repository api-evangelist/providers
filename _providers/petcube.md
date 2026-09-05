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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petcube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://petcube.com/
created: '2026-07-17'
description: Petcube is a pet-technology company (a Y Combinator alum) that makes interactive Wi-Fi pet cameras and a companion mobile app for remote pet care. Its consumer hardware line includes the Petcube Cam, Bites treat-dispensing camera, and Play laser camera, offering HD video, night vision, two-way audio, motion and sound alerts, and app-controlled treat tossing and play. Petcube also sells the Care subscription (cloud video history, extended alerts) and Online Vet / Emergency Fund telehealth services. As of this enrichment pass Petcube exposes no public developer API, developer portal, or documented integration surface — the primary interface is the consumer iOS/Android app tied to its private cloud backend. This profile is maintained in the API Evangelist network as a company record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petcube.png
layout: provider
modified: '2026-07-20'
name: Petcube
nav: Providers
network: true
overview: Petcube is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Tech, Internet of Things, Consumer Hardware, and Camera.
random_paper: 9
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
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/petcube/refs/heads/main/screenshots/petcube-2026-09-02T151116.png
security:
- kind: domain-security
  name: Petcube Domain Security
  slug: petcube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petcube
tags:
- Company
- Pet Tech
- Internet of Things
- Consumer Hardware
- Camera
- Pet Care
- Telehealth
- Y Combinator
website: https://petcube.com/
---
