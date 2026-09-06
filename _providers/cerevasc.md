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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerevasc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerevasc.com/
- group: company
  title: ''
  type: About
  url: https://cerevasc.com/eshunt-system-cerevasc/
- group: operate
  title: ''
  type: Contact
  url: https://cerevasc.com/contact-cerevasc/
- group: company
  title: ''
  type: Blog
  url: https://cerevasc.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://cerevasc.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cerevasc.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/cerevasc_stock/
coverage:
  checked: '2026-08-09'
  detail: CereVasc is a clinical-stage neurovascular implant maker whose product is the physical eShunt device; its WordPress site has no /developers, /api or /docs path, no api./developer./docs. subdomain resolves in DNS, and every discovery probe (/openapi.json, /llms.txt, /.well-known/agent-card.json) returned 404.
  evidence:
  - status: 404
    url: https://cerevasc.com/openapi.json
  - status: 404
    url: https://cerevasc.com/developers
  - status: 404
    url: https://cerevasc.com/llms.txt
  - status: 404
    url: https://cerevasc.com/.well-known/agent-card.json
  - status: 404
    url: https://cerevasc.com/.well-known/security.txt
  - status: 200
    url: https://cerevasc.com/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: CereVasc, Inc. is a clinical-stage medical device company developing novel, minimally invasive treatments for patients with neurological diseases. Its lead product, the eShunt System, uses percutaneous transvenous-transdural access to the central nervous system to treat communicating hydrocephalus — including normal pressure hydrocephalus (NPH) — as a less invasive alternative to conventional neurosurgical shunt placement. The eShunt System is an investigational device limited by United States federal law to investigational use, and is being evaluated in the STRIDE pivotal study (NCT06498960). CereVasc raised a $70M Series B in 2024 and has received FDA Breakthrough Device Designation. The company builds implantable hardware and publishes no public API, developer program, or machine-readable specification.
image: https://cerevasc.com/wp-content/uploads/2023/10/CereVasc-logo-%C2%AEweb-main.svg
layout: provider
modified: '2026-08-09'
name: CereVasc
nav: Providers
network: true
overview: 'CereVasc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neurology, and Hydrocephalus.


  CereVasc''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerevasc/refs/heads/main/screenshots/cerevasc-2026-09-02T145029.png
security:
- kind: domain-security
  name: Cerevasc Domain Security
  slug: cerevasc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cerevasc
tags:
- Company
- Medical Devices
- Healthcare
- Neurology
- Hydrocephalus
- Medical Technology
- Clinical Stage
website: https://cerevasc.com/
---
