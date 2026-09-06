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
  url: security/amparo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amparo.com.vc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amparo.com.vc/privacidade
- group: operate
  title: ''
  type: Support
  url: https://amparo.com.vc/contato
created: '2026-07-17'
description: Amparo is a Brazilian fintech that supports bereaved families in the days after a funeral. Its Central de Cadastros uses automated document reading and data extraction to register a family once and share that data across partner systems, while a WhatsApp assistant delivers personalized financial guidance covering INSS pension advances, life-insurance payouts, credit, repatriation reimbursements, and debt and inventory organization. Amparo exposes integration APIs so its Central de Cadastros can connect with funeral-home and insurer client systems. Backed by QED Investors.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amparo.png
layout: provider
modified: '2026-07-17'
name: Amparo
nav: Providers
network: true
overview: 'Amparo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Brazil, Financial-Services, and Insurance.


  Amparo''s developer surface includes support and 3 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amparo/refs/heads/main/screenshots/amparo-2026-07-25T200126.png
security:
- kind: domain-security
  name: Amparo Domain Security
  slug: amparo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amparo
tags:
- Company
- Fintech
- Brazil
- Financial-Services
- Insurance
- Lending
- Bereavement
- Document Processing
website: https://www.amparo.com.vc
---
