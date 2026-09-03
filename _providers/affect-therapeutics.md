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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.affect.com/
- group: company
  title: ''
  type: Blog
  url: https://www.affect.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.affecttherapeutics.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.affect.com/members/onboarding
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affect.com/insurance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affect.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affect.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affect-therapeutics
- group: auth
  title: ''
  type: Compliance
  url: https://www.affect.com/data-handling/
- group: design
  title: ''
  type: Conformance
  url: conformance/affect-therapeutics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/affect-therapeutics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affect-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Affect ships only an end-user patient app (iOS/Android) — its one API host, api.affect.com, is a private Django backend on Aptible whose root serves an HTML "Login Required" page with meta robots=noindex, and every contract path there (/openapi.json, /swagger.json, /graphql, /docs, /.well-known/*) returns a real 404 confirmed against a control path; there is no developer portal, no partner API, and the company's five public GitHub repos are all forks of third-party projects.
  evidence:
  - status: 200
    url: https://api.affect.com/
  - status: 404
    url: https://api.affect.com/openapi.json
  - status: 404
    url: https://api.affect.com/graphql
  - status: 404
    url: https://www.affect.com/developers
  - status: 404
    url: https://www.affect.com/.well-known/security.txt
  - status: 200
    url: https://www.affect.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Affect Therapeutics (operating as "Affect") is a US digital health company founded in 2020 that delivers app-based outpatient and intensive outpatient treatment for substance use and mental health disorders. Care is delivered entirely through a mobile application on iOS and Android and combines contingency management, cognitive behavioral therapy, medication-assisted treatment, psychiatry, peer support and care coordination. The program treats alcohol, opioid, methamphetamine, cocaine, cannabis and prescription stimulant use disorders alongside anxiety, depression, OCD, PTSD, bipolar disorder and postpartum depression, and is offered to Medicaid and commercial insurance members across multiple US states. Affect is CARF-accredited and operates as a HIPAA-covered telehealth provider. It publishes no public developer program, API documentation, or machine-readable specification; its software is delivered exclusively as an end-user patient application.
image: https://www.affect.com/wp-content/uploads/2024/05/cropped-Affect-logomark-400-px.png
layout: provider
modified: '2026-08-06'
name: Affect Therapeutics
nav: Providers
network: true
overview: 'Affect Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Telehealth, and Mental Health.


  Affect Therapeutics'' developer surface includes engineering blog, support, signup flow, pricing, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.3
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
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/affect-therapeutics/refs/heads/main/screenshots/affect-therapeutics-2026-08-07T161025.png
security:
- kind: domain-security
  name: Affect Therapeutics Domain Security
  slug: affect-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: affect-therapeutics
tags:
- Company
- Healthcare
- Digital Health
- Telehealth
- Mental Health
- Behavioral Health
- Substance Use Disorder
- Addiction Treatment
- Medicaid
website: https://www.affect.com/
---
