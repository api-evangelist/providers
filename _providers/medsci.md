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
  url: security/medsci-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medsci.cn
- group: other
  title: ''
  type: Company
  url: https://www.medscihealthcare.com
created: '2026-07-17'
description: MedSci (梅斯医学 / MedSci Healthcare Holdings Limited, HKEX 2415) is a leading online professional physician platform in China, founded in 2012 and headquartered in Shanghai. It connects roughly 2.9 million registered physician users with pharmaceutical and medical device companies through big data and AI, offering physician platform solutions (medical knowledge, clinical study assistance), precision omni-channel marketing, real-world study (RWS) solutions, and the MedSci xAI medical AI agent. Surfaced as a portfolio company of Qiming Venture Partners and added to the API Evangelist network. No public third-party developer API program, OpenAPI/SDK, or developer portal was found; the primary web host is geo-restricted and unreachable for HTTP probing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medsci.png
layout: provider
modified: '2026-07-20'
name: MedSci
nav: Providers
network: true
overview: MedSci is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical, Physician Platform, and Artificial Intelligence.
random_paper: 20
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
screenshot: https://raw.githubusercontent.com/api-evangelist/medsci/refs/heads/main/screenshots/medsci-2026-08-07T172413.png
security:
- kind: domain-security
  name: Medsci Domain Security
  slug: medsci-domain-security
  summary_line: DMARC
slug: medsci
tags:
- Company
- Healthcare
- Medical
- Physician Platform
- Artificial Intelligence
- Real-World Evidence
- China
website: https://www.medsci.cn
---
