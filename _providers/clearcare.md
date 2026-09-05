---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.clearcareonline.com'', ''status'': 301, ''note'': ''declared website redirects to https://wellsky.com/personal-care-software/ — a different registrable domain (clearcareonline.com -> wellsky.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/clearcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearcareonline.com
- group: company
  title: ''
  type: Website
  url: https://wellsky.com/personal-care-software/
created: '2026-07-17'
description: 'ClearCare (originally ClearCare Online) is a web-based home care agency management platform founded in 2011 and headquartered in San Francisco. It provides non-medical home care agencies with back-office and point-of-care tooling: caregiver scheduling, telephony-based clock-in/clock-out and electronic visit verification (EVV), billing and payroll, client and caregiver management, care planning, a family room portal, and business analytics. ClearCare was backed by Battery Ventures and Cendana Capital and was acquired by WellSky (formerly Mediware) in 2019; the product is now marketed as WellSky Personal Care, and the clearcareonline.com domain redirects to WellSky. This profile was surfaced as a Battery Ventures portfolio company and enriched as a historical company record — ClearCare no longer operates a standalone public developer or API program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearcare.png
layout: provider
modified: '2026-07-18'
name: ClearCare
nav: Providers
network: true
overview: ClearCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Care, Home Health, Healthcare, and Agency Management.
random_paper: 6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/clearcare/refs/heads/main/screenshots/clearcare-2026-07-25T205539.png
security:
- kind: domain-security
  name: Clearcare Domain Security
  slug: clearcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearcare
tags:
- Company
- Home Care
- Home Health
- Healthcare
- Agency Management
- Caregiving
- Electronic Visit Verification
- Software-as-a-Service
- Scheduling
website: https://www.clearcareonline.com
---
