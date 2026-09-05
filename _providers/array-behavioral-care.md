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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/array-behavioral-care-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arraybc.com/
- group: company
  title: ''
  type: About
  url: https://arraybc.com/about/
- group: company
  title: ''
  type: Press
  url: https://arraybc.com/press/
- group: company
  title: ''
  type: Blog
  url: https://arraybc.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://arraybc.com/questions-about-care/
- group: operate
  title: ''
  type: ContactSales
  url: https://arraybc.com/start-an-inquiry/
- group: start
  title: ''
  type: Login
  url: https://mychart.arraybc.com/Array/Authentication/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arraybc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arraybc.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://arraybc.com/online-safety-and-security/
- group: design
  title: ''
  type: Conformance
  url: conformance/array-behavioral-care-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/array-behavioral-care-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/array-behavioral-care-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Array is a virtual psychiatry practice whose only software surfaces are an Epic MyChart patient portal and a partner referral portal — there is no developer site, no api./developer. subdomain resolves, and its Epic-based EHR exposes no public FHIR endpoint (the R4 CapabilityStatement path 404s and Array is absent from Epic's 479-entry public endpoint directory).
  evidence:
  - status: 404
    url: https://arraybc.com/developers
  - status: 404
    url: https://arraybc.com/openapi.json
  - status: 404
    url: https://mychart.arraybc.com/Array/api/FHIR/R4/metadata
  - status: 200
    url: https://open.epic.com/Endpoints/R4
  - status: 200
    url: https://arraybc.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Array Behavioral Care is a virtual psychiatry and therapy practice headquartered in Mount Laurel, New Jersey, delivering telebehavioral health across the continuum of care — from the emergency department to the outpatient clinic to the home. Founded in 1999 (formerly InSight + Regroup, rebranded to Array Behavioral Care in January 2021), the company operates three product families — Array OnDemand Care (acute / emergency department consults), Array Community Care (outpatient clinics and physician groups) and Array AtHome (direct-to-patient virtual psychiatry and therapy) — unified since April 2025 under Array CareConnect. Its clinical technology is an Epic-based interoperable EHR with an Epic MyChart patient portal at mychart.arraybc.com. Array is accredited by The Joint Commission and earned HITRUST e1 certification for its integrated clinical systems in December 2024. It publishes no public developer program, API, SDK or machine-readable specification; integration with partner
  health systems runs through Epic interoperability and a referral portal rather than a self-service API.
image: https://arraybc.com/wp-content/uploads/2024/06/logo.png
layout: provider
modified: '2026-08-06'
name: Array Behavioral Care
nav: Providers
network: true
overview: 'Array Behavioral Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Mental Health, and Telehealth.


  Array Behavioral Care''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/array-behavioral-care/refs/heads/main/screenshots/array-behavioral-care-2026-08-07T161731.png
security:
- kind: domain-security
  name: Array Behavioral Care Domain Security
  slug: array-behavioral-care-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Array Behavioral Care Trust Center
  slug: array-behavioral-care-trust-center
  summary_line: HITRUST e1, The Joint Commission accreditation, HIPAA compliance
slug: array-behavioral-care
tags:
- Company
- Healthcare
- Behavioral Health
- Mental Health
- Telehealth
- Telepsychiatry
- Digital Health
- Electronic Health Records
- Patient Engagement
- HIPAA
website: https://arraybc.com/
---
