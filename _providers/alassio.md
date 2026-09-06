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
  url: security/alassio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alassio.fr/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.alassio.fr/mentions-legales
created: '2026-07-17'
description: Alassio is a French financial-technology company building a next-generation payroll software platform (logiciel de paie nouvelle generation) for businesses. Alassio positions itself as offering the functional depth expected of a specialist payroll and HR tool, with added transparency and control for finance and people teams. The company is backed by venture-capital firm Partech and operates from France, serving the French and European payroll, compensation, and human-resources market. As of this profile the company publishes only a marketing landing page and a legal notice; no public API, developer documentation, SDK, or integration surface has been located. This profile is maintained in the API Evangelist network as a portfolio-lead stub awaiting a public developer surface to enrich.
image: https://www.alassio.fr/og-image.png
layout: provider
modified: '2026-07-17'
name: Alassio
nav: Providers
network: true
overview: Alassio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Payroll, Human Resources, and HR Tech.
random_paper: 13
score:
  band: minimal
  composite: 5.0
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alassio/refs/heads/main/screenshots/alassio-2026-07-25T195535.png
security:
- kind: domain-security
  name: Alassio Domain Security
  slug: alassio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alassio
tags:
- Company
- Financial-Services
- Payroll
- Human Resources
- HR Tech
- Payroll Software
- Software-as-a-Service
- France
- Fintech
- Compensation
website: https://www.alassio.fr/
---
