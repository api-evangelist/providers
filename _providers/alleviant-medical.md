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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alleviant-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alleviantmedical.com
- group: other
  title: ''
  type: Product
  url: https://alleviantmedical.com/hf-shunt-therapy
- group: other
  title: ''
  type: HealthcareProfessionals
  url: https://alleviantmedical.com/healthcare-professionals
- group: start
  title: ''
  type: ClinicalTrials
  url: https://alleviantmedical.com/allay-hf
- group: company
  title: ''
  type: Blog
  url: https://alleviantmedical.com/press-resources
- group: operate
  title: ''
  type: PressReleases
  url: https://alleviantmedical.com/press-resources
- group: other
  title: ''
  type: Locations
  url: https://alleviantmedical.com/find-a-center
- group: other
  title: ''
  type: Patents
  url: https://alleviantmedical.com/patents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alleviantmedical.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alleviantmedical.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alleviant-medical/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/alleviant
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/alleviantmedical
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alleviant-medical_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alleviant-medical-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Alleviant Medical is a clinical-stage cardiac device company whose product is an investigational transcatheter shunt procedure, not software, so there is nothing to expose as an API; alleviantmedical.com is a 25-page clinician and patient-education site with no /developers or /api path and no api./docs./developer. subdomain resolving in DNS at all.
  evidence:
  - status: 404
    url: https://alleviantmedical.com/developers
  - status: 404
    url: https://alleviantmedical.com/openapi.json
  - status: 404
    url: https://alleviantmedical.com/llms.txt
  - status: 404
    url: https://alleviantmedical.com/.well-known/agent-card.json
  - status: 404
    url: https://alleviantmedical.com/.well-known/security.txt
  - status: 0
    url: https://api.alleviantmedical.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Alleviant Medical, Inc. is a clinical-stage medical device company headquartered in Austin, Texas, founded in 2017 to develop minimally invasive, transcatheter therapies for heart failure. The Alleviant System is an investigational, no-implant approach that creates a small interatrial passageway to relieve elevated left atrial pressure without leaving a permanent device behind; it holds U.S. FDA Breakthrough Device designation for both preserved and reduced ejection fraction heart failure and is under study in the FDA-approved ALLAY-HF and ALLAY-HFrEF pivotal trials. The company has raised roughly $164M across a $75M round led by S3 Ventures and RiverVest Venture Partners and a $90M round led by Gilde Healthcare with Omega Funds, Vensana Capital, Longview Ventures, Gilmartin Capital and the TMC Venture Fund. Alleviant is a device and clinical-trial business, not a software business: it publishes no developer portal, no public API, no SDK and no machine-readable specification,
  and its public web surface is limited to clinician, patient-education, investor and press material.'
image: https://alleviantmedical.com/logo.svg
layout: provider
modified: '2026-08-06'
name: Alleviant Medical
nav: Providers
network: true
overview: 'Alleviant Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  Alleviant Medical''s developer surface includes engineering blog and 15 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alleviant-medical/refs/heads/main/screenshots/alleviant-medical-2026-08-07T161223.png
security:
- kind: domain-security
  name: Alleviant Medical Domain Security
  slug: alleviant-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alleviant-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Interventional Cardiology
- Clinical Trials
- Medical Technology
- Life Sciences
- Austin
- Texas
website: https://alleviantmedical.com
---
