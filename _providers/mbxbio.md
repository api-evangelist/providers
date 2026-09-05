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
  url: security/mbxbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mbxbio.com
created: '2026-07-17'
description: MBX Biosciences is a clinical-stage biopharmaceutical company developing novel precision peptide therapies for people living with endocrine and metabolic disorders. Its proprietary Precision Endocrine Peptide (PEP) platform engineers long-acting peptide prodrugs, and its pipeline includes canvuparatide (MBX 2109) for chronic hypoparathyroidism, MBX 4291 for obesity, and MBX 5765 for post-bariatric hypoglycemia. The company is publicly traded on Nasdaq under the ticker MBX. As a clinical-stage biotech it publishes no public API, developer portal, SDKs, or technical documentation surface; this profile is maintained for network completeness.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mbxbio.png
layout: provider
modified: '2026-07-20'
name: MBX Biosciences
nav: Providers
network: true
overview: MBX Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biopharmaceutical, Healthcare, and Life Sciences.
random_paper: 11
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
screenshot: https://raw.githubusercontent.com/api-evangelist/mbxbio/refs/heads/main/screenshots/mbxbio-2026-08-07T172209.png
security:
- kind: domain-security
  name: Mbxbio Domain Security
  slug: mbxbio-domain-security
  summary_line: TLSv1.3
slug: mbxbio
tags:
- Company
- Biotechnology
- Biopharmaceutical
- Healthcare
- Life Sciences
- Endocrine
- Metabolic
- Peptide Therapeutics
- Clinical Stage
- No API Surface
website: https://mbxbio.com
---
