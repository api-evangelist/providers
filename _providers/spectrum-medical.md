---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spectrum-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spectrummedical.com/
- group: operate
  title: ''
  type: Support
  url: https://www.spectrummedical.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.spectrummedical.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spectrummedical.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spectrummedical.com/terms-conditions
- group: design
  title: ''
  type: Conformance
  url: conformance/spectrum-medical-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/spectrum-medical-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/spectrum-medical-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spectrum-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spectrum-medical-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spectrum-medical-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Spectrum Medical ships perfusion hardware and the on-premise Quantum Informatics / VIPER EMR stack, and its only integration path is HL7 v2 messaging through a Mirth Connect engine installed on the hospital's own Windows/SQL server (QI.yourdomain.com) — there is no public API, no developer portal, no SDK and no GitHub organization, and api./developer./docs.spectrummedical.com do not resolve.
  evidence:
  - status: 404
    url: https://www.spectrummedical.com/openapi.json
  - status: 404
    url: https://www.spectrummedical.com/.well-known/api-catalog
  - status: 0
    url: https://api.spectrummedical.com/
  - status: 404
    url: https://api.github.com/orgs/spectrummedical
  - status: 200
    url: https://www.spectrummedical.com/en-us/quantum-informatics-24-us/vision
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: 'Spectrum Medical is a privately held medical technology company, co-founded by Steve Turner and Mark Drain, with corporate headquarters in Cheltenham, England, a U.S. headquarters in Fort Mill, South Carolina, and a European headquarters in Mirandola, Italy. It entered the global medical device market in 2005 with its non-invasive System M diagnostic technology and today builds two connected product families: Quantum Perfusion Technologies (workstations, centrifugal and roller pumps, oxygenators, heater-coolers, sensor modules and single-use sterile technologies for cardiopulmonary bypass, ECMO and other extracorporeal therapies) and Quantum Informatics (the VIPER clinical interfacing EMR, the VISION server and Perfusion Information Management System). Its software surface is a customer-deployed, on-premise stack: the VISION server passes case data to the hospital EHR over HL7 v2 interfaces through a bundled Mirth Connect interface engine, and third-party device connectivity
  is delivered through optional device-driver software rather than a public web API. Spectrum Medical is ISO/IEC 27001:2013 certified and its VIPER Clinical Information Solution 3.0 earned ONC-HIT 2014 Edition Modular Certification via the Drummond Group. Systems are in use in over 60 countries.'
image: https://www.spectrummedical.com/images/spectrum-medical-logo.svg
layout: provider
modified: '2026-08-28'
name: Spectrum Medical
nav: Providers
network: true
overview: 'Spectrum Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Health IT, and Electronic Medical Records.


  Spectrum Medical''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Spectrum Medical Plans Pricing
  plan_count: 0
  slug: spectrum-medical-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Spectrum Medical Rate Limits
  slug: spectrum-medical-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spectrum-medical/refs/heads/main/screenshots/spectrum-medical-2026-09-02T160353.png
security:
- kind: domain-security
  name: Spectrum Medical Domain Security
  slug: spectrum-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spectrum-medical
tags:
- Company
- Medical Devices
- Healthcare
- Health IT
- Electronic Medical Records
- Perfusion
- Extracorporeal Life Support
- Clinical Information Systems
- Medical Device Connectivity
- HL7
website: https://www.spectrummedical.com/
---
