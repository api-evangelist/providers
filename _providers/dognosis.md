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
  url: security/dognosis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dognosis-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dognosis.tech
created: '2026-07-17'
description: Dognosis is a Bengaluru, India deeptech company building olfaction AI that pairs trained detection dogs with machine learning to find disease from a single breath sample. Its product, BreathEasy, is a non-invasive breath test that produces a VOC-based cancer risk score for clinicians; a Phase 2 study published in the Journal of Clinical Oncology reported over 90% accuracy across seven cancer types, including at early and treatable stages. Dognosis is a portfolio company of Prosus Ventures. No public developer API is published today; this API Evangelist profile tracks the company's digital, discovery, and security surface (an llms.txt is served; no /.well-known discovery documents are published).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dognosis.png
layout: provider
modified: '2026-07-18'
name: Dognosis
nav: Providers
network: true
overview: Dognosis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Cancer Detection.
random_paper: 9
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dognosis/refs/heads/main/screenshots/dognosis-2026-07-25T212234.png
security:
- kind: domain-security
  name: Dognosis Domain Security
  slug: dognosis-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dognosis
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Cancer Detection
- Breath Analysis
- Olfaction AI
- Deep Tech
website: https://dognosis.tech
---
