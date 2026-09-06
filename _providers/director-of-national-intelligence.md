---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.dni.gov/'', ''status'': 301, ''note'': ''declared website redirects to https://www.odni.gov/ — a different registrable domain (dni.gov -> odni.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/director-of-national-intelligence-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/odni
- group: company
  title: ''
  type: Website
  url: https://www.dni.gov/
created: '2024-07-11'
description: The Office of the Director of National Intelligence leads intelligence integration and forges an intelligence community that delivers the most insightful intelligence possible. The ODNI serves as the head of the intelligence community, overseeing and coordinating the foreign and domestic activities of the US intelligence community.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/director-of-national-intelligence.png
layout: provider
modified: '2026-04-28'
name: Director of National Intelligence
nav: Providers
network: true
overview: Director of National Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government and Intelligence.
random_paper: 11
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/director-of-national-intelligence/refs/heads/main/screenshots/director-of-national-intelligence-2026-06-20T180032.png
security:
- kind: domain-security
  name: Director Of National Intelligence Domain Security
  slug: director-of-national-intelligence-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: director-of-national-intelligence
tags:
- Federal-Government
- Intelligence
website: https://www.dni.gov/
---
