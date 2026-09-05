---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.stillatechnologies.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.bio-rad.com/en-us/category/digital-pcr?ID=bcdf1371-fa15-9804-647b-4c13f34cd622 — a different registrable domain (stillatechnologies.com -> bio-rad.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/stilla-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stillatechnologies.com/
created: '2026-07-17'
description: Stilla Technologies is a life-sciences instrumentation company that develops digital PCR (dPCR) systems, consumables, and assays, best known for its Naica system for Crystal Digital PCR and the Nio product line. With operations in France and the United States, its technology serves oncology diagnostics, cell and gene therapy, and infectious-disease testing. Stilla was acquired by Bio-Rad Laboratories (announced February 2025, ~$225M plus up to $50M in milestones, closed 2025); its web properties now redirect to Bio-Rad. The company operates laboratory hardware and consumables rather than a public developer platform — no OpenAPI, developer portal, SDKs, CLI, or MCP surface was found during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stilla-technologies.png
layout: provider
modified: '2026-07-21'
name: Stilla Technologies
nav: Providers
network: true
overview: Stilla Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Life Sciences, Diagnostics, and Digital PCR.
random_paper: 4
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
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Stilla Technologies Domain Security
  slug: stilla-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stilla-technologies
tags:
- Company
- Healthcare
- Life Sciences
- Diagnostics
- Digital PCR
- Genomics
- Biotechnology
- Laboratory Instruments
website: https://www.stillatechnologies.com/
---
