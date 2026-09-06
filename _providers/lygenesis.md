---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
- group: company
  title: ''
  type: Website
  url: https://www.lygenesis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lygenesis.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.lygenesis.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.lygenesis.com/media/insights/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lygenesis/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LyGenesis_Inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lygenesis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lygenesis-llms.txt
coverage:
  checked: '2026-08-25'
  detail: 'LyGenesis is a clinical-stage cell therapy company whose product is a lymph-node organogenesis therapy in a Phase 2a trial, not software: its www.lygenesis.com Nuxt site 404s on every spec and /.well-known/ path, api./developer./docs.lygenesis.com do not resolve, and there is no GitHub org, npm or PyPI package.'
  evidence:
  - status: 404
    url: https://www.lygenesis.com/openapi.json
  - status: 404
    url: https://www.lygenesis.com/.well-known/agent-card.json
  - status: 404
    url: https://www.lygenesis.com/llms.txt
  - status: 200
    url: https://api.github.com/search/repositories?q=lygenesis
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'LyGenesis is a Pittsburgh-based clinical-stage cell therapy company developing allogeneic regenerative therapies that use a patient''s own lymph nodes as bioreactors to grow functioning ectopic organs. Its lead program transplants donor hepatocytes into upper-abdominal lymph nodes via endoscopic ultrasound to treat end-stage liver disease and is in a Phase 2a clinical trial; preclinical proof-of-concept programs target thymus (aging), kidney (end-stage renal disease) and pancreas (Type 1 diabetes). LyGenesis is a laboratory and clinical-research organization, not a software vendor: it publishes no developer portal, no API documentation and no machine-readable API contract, and this profile records that absence rather than any API surface.'
layout: provider
modified: '2026-08-25'
name: LyGenesis
nav: Providers
network: true
overview: 'LyGenesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Regenerative Medicine, and Life Sciences.


  LyGenesis'' developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lygenesis/refs/heads/main/screenshots/lygenesis-2026-09-02T150338.png
security:
- kind: domain-security
  name: Lygenesis Domain Security
  slug: lygenesis-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lygenesis
tags:
- Company
- Biotechnology
- Cell Therapy
- Regenerative Medicine
- Life Sciences
- Healthcare
- Clinical Trials
- Organ Transplantation
website: https://www.lygenesis.com/
---
