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
  url: security/doctorly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doctorly.de
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doctorly.de/datenschutzerklarung
- group: operate
  title: ''
  type: Support
  url: https://doctorly.de/kontakt
- group: company
  title: ''
  type: About
  url: https://doctorly.de/ueber-uns
created: '2026-07-17'
description: Doctorly (doctorly GmbH, Berlin) builds a modern cloud-based practice management system (Praxisverwaltungssystem / PVS) for medical practices in Germany, positioned as a replacement for legacy systems such as Medistar, Turbomed and ALBIS. The platform covers KV quarterly billing, e-prescription (eRezept), electronic sick leave (eAU), real-time collaborative patient records, GDT device integration and cross-platform access on Windows, macOS, Linux and Android, and it is KBV-, gematik- and GDPR-compliant. Doctorly is a Seedcamp portfolio company. As of this profile the company exposes no public developer portal, API documentation, OpenAPI/FHIR specification, SDKs or GitHub organization; this entry is maintained as a company/provider record in the API Evangelist network.
image: https://cdn.prod.website-files.com/6166cdb1ddf5d92cb385f8e7/644667969b7bb127d37e1854_Open_Graph_Image_compressed.png
layout: provider
modified: '2026-07-18'
name: Doctorly
nav: Providers
network: true
overview: 'Doctorly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Practice Management, and Medical Software.


  Doctorly''s developer surface includes support and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.1
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
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctorly/refs/heads/main/screenshots/doctorly-2026-07-25T212239.png
security:
- kind: domain-security
  name: Doctorly Domain Security
  slug: doctorly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doctorly
tags:
- Company
- Healthcare
- Health IT
- Practice Management
- Medical Software
- Software-as-a-Service
- Germany
- Digital Health
website: https://doctorly.de
---
