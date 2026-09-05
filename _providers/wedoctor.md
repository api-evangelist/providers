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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://wedoctor.com
- group: operate
  title: ''
  type: Support
  url: https://wedoctor.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://wedoctor.com/intro/doctorhelp
- group: start
  title: ''
  type: SignUp
  url: https://wedoctor.com/register/mobile
- group: start
  title: ''
  type: Login
  url: https://wedoctor.com/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wedoctor.com/agreement/doctor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wedoctor.com/agreement/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wedoctor-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wedoctor-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wedoctor-llms.txt
coverage:
  checked: '2026-09-04'
  detail: 'WeDoctor ships only end-user software — the 微医 patient app, the 微医生 clinician app and the wedoctor.com internet-hospital portal — and operates no developer program of any kind: the readable apex host wedoctor.com returns a genuine HTTP 404 for every OpenAPI, GraphQL, llms.txt, agent-card and /.well-known discovery path, and no open.*/developer.*/api.* subdomain exists (the 200s on those names are a *.wedoctor.com wildcard answering a Tencent EdgeOne bot challenge, proven by a negative-control hostname returning the identical body).'
  evidence:
  - status: 404
    url: https://wedoctor.com/openapi.json
  - status: 404
    url: https://wedoctor.com/.well-known/agent-card.json
  - status: 404
    url: https://wedoctor.com/llms.txt
  - status: 404
    url: https://wedoctor.com/graphql
  - status: 404
    url: https://api.guahao.com/openapi.json
  - status: 200
    url: https://wedoctor.com/contact
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: WeDoctor (微医, formerly Guahao.com / 挂号网) is a Hangzhou-based Chinese digital health platform founded in 2010 by Liao Jieyuan. It began as an online hospital-appointment registration network and grew into a full-stack "Internet + Healthcare" operator spanning online consultation and internet hospitals (it launched China's first, the Wuzhen Internet Hospital, in 2015), e-prescription and pharmacy fulfilment, screening and diagnostics, chronic-disease management, medical insurance settlement, and the WeDoctor Cloud platform sold to hospitals and regional health authorities. The company reports connections to thousands of Chinese hospitals and hundreds of thousands of registered physicians. Its public surface is consumer- and clinician-facing (web portal plus the 微医 patient app and 微医生 doctor app); as of this profile it operates no public developer program, publishes no machine-readable API contract, and exposes no documented partner API — hospital and insurer integrations are handled
  through private commercial agreements rather than a self-serve developer portal.
layout: provider
modified: '2026-09-04'
name: WeDoctor
nav: Providers
network: true
overview: 'WeDoctor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Telemedicine, and Internet Hospital.


  WeDoctor''s developer surface includes support, signup flow, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Wedoctor Domain Security
  slug: wedoctor-domain-security
  summary_line: TLSv1.2 · DMARC
slug: wedoctor
tags:
- Company
- Healthcare
- Digital Health
- Telemedicine
- Internet Hospital
- Appointment Booking
- Electronic Prescription
- Health Insurance
- China
website: https://wedoctor.com
---
