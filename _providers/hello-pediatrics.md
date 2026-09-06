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
  url: security/hello-pediatrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellopediatrics.com/
- group: company
  title: ''
  type: About
  url: https://hellopediatrics.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://hellopediatrics.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hellopediatrics.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://hellopediatrics.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://book.hellopediatrics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hellopediatrics.com/terms-of-use-1418/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hellopediatrics.com/privacy-policy/
- group: company
  title: ''
  type: Partners
  url: https://hellopediatrics.com/partnerships/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hello-pediatrics-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Hello Pediatrics is a virtual pediatric medical practice, not a software vendor — its booking and video surface at book.hellopediatrics.com is a white-labeled third-party Mend deployment whose SPA answers HTTP 200 with the same 1,349-byte shell for every path including a nonsense control, and no api./developer./docs. subdomain resolves at all, so there is no Hello Pediatrics contract to publish.
  evidence:
  - status: 404
    url: https://hellopediatrics.com/openapi.json
  - status: 404
    url: https://hellopediatrics.com/.well-known/agent-card.json
  - status: 200
    url: https://book.hellopediatrics.com/this-path-should-404-xyz
  - status: 0
    url: https://api.hellopediatrics.com/
  - status: 200
    url: https://hellopediatrics.com/partnerships/
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Hello Pediatrics is a virtual pediatric medical practice that partners with primary care pediatric offices to cover their patients after hours. Board-certified pediatricians deliver telehealth visits — triage, video appointments and real-time messaging — on nights, weekends and holidays, and send a visit summary back to the child''s regular pediatrician so the medical home keeps the record. The practice works with 30+ partner pediatric practices, participates with major insurers (Cigna, UnitedHealthcare, Aetna, Anthem, CareFirst), and prices partner coverage at $16 per call with a monthly minimum. It is a clinical service organization, not a software vendor: patient scheduling and video are delivered on a white-labeled third-party telehealth platform (Mend) at book.hellopediatrics.com, and Hello Pediatrics publishes no developer program, public API, SDK or machine-readable API contract of any kind.'
image: https://hellopediatrics.com/wp-content/uploads/2024/11/Hello.png
layout: provider
modified: '2026-08-22'
name: Hello Pediatrics
nav: Providers
network: true
overview: 'Hello Pediatrics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Pediatrics, and Virtual Care.


  Hello Pediatrics'' developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hello-pediatrics/refs/heads/main/screenshots/hello-pediatrics-2026-09-02T145718.png
security:
- kind: domain-security
  name: Hello Pediatrics Domain Security
  slug: hello-pediatrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hello-pediatrics
tags:
- Company
- Healthcare
- Telehealth
- Pediatrics
- Virtual Care
- Digital Health
- Medical Practice
website: https://hellopediatrics.com/
---
