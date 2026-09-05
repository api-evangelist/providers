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
  url: security/rizm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rizm.de
- group: start
  title: ''
  type: Login
  url: https://app.rizm.de
created: '2026-07-17'
description: RIZM is a holistic energy optimization platform for industrial enterprises, operated by Kerith GmbH of Münster, Germany. It integrates data from production, energy procurement, and infrastructure into a digital twin, then optimizes energy system design and day-to-day operational decisions — from long-term infrastructure investment and power purchase agreements to short-term asset dispatch and production scheduling — helping manufacturers cut energy costs and emissions at the same time. Named customers include BMW Group, Bosch, Mercedes-Benz, Volkswagen, and BSH. The product is delivered as a login-gated web application (app.rizm.de) with authenticated documentation; no public developer API, OpenAPI, or SDK surface is published at this time. Backed by Point Nine, this profile was surfaced from the venture portfolio graph.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rizm.png
layout: provider
modified: '2026-07-21'
name: Rizm
nav: Providers
network: true
overview: Rizm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Optimization, Industrial, and Manufacturing.
random_paper: 9
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
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rizm/refs/heads/main/screenshots/rizm-2026-09-02T153946.png
security:
- kind: domain-security
  name: Rizm Domain Security
  slug: rizm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rizm
tags:
- Company
- Energy
- Energy Optimization
- Industrial
- Manufacturing
- Sustainability
- Digital Twin
- Sector Coupling
- Germany
website: https://www.rizm.de
---
