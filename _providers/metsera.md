---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://metsera.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.pfizer.com/ — a different registrable domain (metsera.com -> pfizer.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/metsera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metsera.com
created: '2026-07-17'
description: Metsera is a clinical-stage biopharmaceutical company developing injectable and oral therapies for obesity and metabolic diseases, backed by GV and the SoftBank Vision Fund. As of this enrichment pass its corporate domain (metsera.com) issues a 301 redirect to pfizer.com, consistent with Metsera's acquisition by Pfizer. As a life-sciences drug-development company it publishes no public API, developer portal, OpenAPI, SDKs, or other machine-readable developer surface; it is tracked in the API Evangelist network as a company/portfolio record rather than an API producer.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metsera.png
layout: provider
modified: '2026-07-20'
name: Metsera *
nav: Providers
network: true
overview: Metsera * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biopharmaceutical, Pharmaceuticals, and Obesity.
random_paper: 18
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
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
security:
- kind: domain-security
  name: Metsera Domain Security
  slug: metsera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metsera
tags:
- Company
- Life Sciences
- Biopharmaceutical
- Pharmaceuticals
- Obesity
- Metabolic Disease
- Drug Development
website: https://metsera.com
---
