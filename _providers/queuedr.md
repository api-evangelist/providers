---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://queuedr.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.phreesia.com/see-more-patients/appointments/ — a different registrable domain (queuedr.com -> phreesia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/phreesia/
- group: company
  title: ''
  type: Website
  url: https://queuedr.com
- group: start
  title: ''
  type: Login
  url: https://app.queuedr.com/users/sign_in
- group: other
  title: ''
  type: Acquirer
  url: https://www.phreesia.com/queuedr/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/queuedr-domain-security.yml
created: '2026-07-17'
description: QueueDr is a healthcare scheduling automation product that automatically fills unexpected appointment cancellations, rebooks no-shows, and balances provider schedules to reduce lost revenue for medical practices and health systems. Originally a 500 Global-backed startup, QueueDr was acquired by Phreesia and is now offered as the Phreesia Appointment Accelerator within Phreesia's patient intake and engagement platform. The queuedr.com domain now redirects to Phreesia; existing customers continue to sign in at the app.queuedr.com dashboard. No independent public developer portal, API documentation, SDKs, or machine-readable API surface is published for QueueDr as a standalone product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/queuedr.png
layout: provider
modified: '2026-07-20'
name: QueueDr
nav: Providers
network: true
overview: QueueDr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Appointment Scheduling, and Patient Engagement.
random_paper: 7
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/queuedr/refs/heads/main/screenshots/queuedr-2026-09-02T152648.png
security:
- kind: domain-security
  name: Queuedr Domain Security
  slug: queuedr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: queuedr
tags:
- Company
- Healthcare
- Health IT
- Appointment Scheduling
- Patient Engagement
- Medical Practice
- Acquired
website: https://queuedr.com
---
