---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://fortyseveninc.com'', ''status'': 307, ''note'': ''declared website redirects to https://www.gilead.com/ — a different registrable domain (fortyseveninc.com -> gilead.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: https://apis.io/providers/gilead-sciences/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forty-seven-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://fortyseveninc.com
created: '2026-07-17'
description: Forty Seven, Inc. was an immuno-oncology biotechnology company founded in 2015 to commercialize CD47 immune-evasion research licensed from Stanford University (Irv Weissman and colleagues). Its lead program was magrolimab, a monoclonal antibody targeting CD47 — the "do not eat me" signal tumor cells use to evade macrophage-mediated killing — studied in myelodysplastic syndrome (MDS), acute myeloid leukemia (AML), and diffuse large B-cell lymphoma (DLBCL). Backed by GV, the company was acquired by Gilead Sciences in 2020 for roughly $4.9 billion; the fortyseveninc.com domain now redirects to gilead.com. As a clinical-stage therapeutics company it exposes no public developer API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forty-seven.png
layout: provider
modified: '2026-07-19'
name: Forty Seven *
nav: Providers
network: true
overview: Forty Seven * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Immuno-Oncology, and Oncology.
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
screenshot: https://raw.githubusercontent.com/api-evangelist/forty-seven/refs/heads/main/screenshots/forty-seven-2026-07-25T215017.png
security:
- kind: domain-security
  name: Forty Seven Domain Security
  slug: forty-seven-domain-security
  summary_line: TLSv1.3 · DMARC
slug: forty-seven
tags:
- Company
- Life Sciences
- Biotechnology
- Immuno-Oncology
- Oncology
- Pharmaceuticals
- Cancer
- Therapeutics
website: http://fortyseveninc.com
---
