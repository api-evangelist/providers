---
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
  url: security/4d-molecular-therapeutics-4dmt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4dmoleculartherapeutics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4dmoleculartherapeutics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4dmoleculartherapeutics.com/privacy-notice/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4d-molecular-therapeutics-4dmt-llms.txt
coverage:
  checked: '2026-09-05'
  detail: '4DMT is a clinical-stage gene therapy developer whose product is a drug, not software: its entire public site is 18 WordPress marketing pages (about, pipeline, technology, patients, careers, investors, contact) with no developer, docs, or API section anywhere in its sitemap, and the only machine-readable JSON on the domain is the CMS-default WordPress REST API at /wp-json, which is Automattic''s contract running under 4DMT''s name rather than an API 4DMT designed, documented, or offers to anyone.'
  evidence:
  - status: 404
    url: https://4dmoleculartherapeutics.com/openapi.json
  - status: 404
    url: https://4dmoleculartherapeutics.com/.well-known/agent-card.json
  - status: 200
    url: https://4dmoleculartherapeutics.com/page-sitemap.xml
  - status: 200
    url: https://4dmoleculartherapeutics.com/wp-json
  - status: 200
    url: https://4dmoleculartherapeutics.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '4D Molecular Therapeutics (4DMT) is a late-stage clinical biotechnology company headquartered in Emeryville, California, developing genetic medicines for large-market diseases. The company uses a proprietary directed-evolution platform it calls Therapeutic Vector Evolution to invent customized, proprietary adeno-associated virus (AAV) gene delivery vectors that carry therapeutic payloads to specific tissue types. Its pipeline targets retinal and pulmonary disease, led by 4D-150 for wet age-related macular degeneration and diabetic macular edema, and 4D-710 for cystic fibrosis lung disease. 4DMT is a therapeutics developer rather than a software vendor: it publishes no public API, developer portal, SDK, or machine-readable API contract of any kind.'
image: https://4dmoleculartherapeutics.com/wp-content/uploads/4dmt-fb-card-scaled.jpg
layout: provider
modified: '2026-09-05'
name: 4D Molecular Therapeutics (4DMT)
nav: Providers
network: true
overview: 4D Molecular Therapeutics (4DMT) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Genetic Medicine, and Life Sciences.
random_paper: 6
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4D Molecular Therapeutics 4Dmt Domain Security
  slug: 4d-molecular-therapeutics-4dmt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 4d-molecular-therapeutics-4dmt
tags:
- Company
- Biotechnology
- Gene Therapy
- Genetic Medicine
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Ophthalmology
website: https://4dmoleculartherapeutics.com/
---
