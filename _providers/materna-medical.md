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
- group: company
  title: ''
  type: Website
  url: https://www.maternamedical.com/
- group: company
  title: ''
  type: About
  url: https://www.maternamedical.com/about/
- group: other
  title: ''
  type: Product
  url: https://www.hellomilli.com/vaginal-dilator/
- group: other
  title: ''
  type: Store
  url: https://www.hellomilli.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hellomilli.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.maternamedical.com/media/
- group: operate
  title: ''
  type: Support
  url: https://www.hellomilli.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.maternamedical.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.hellomilli.com/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellomilli.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellomilli.com/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/materna-medical/
- group: other
  title: ''
  type: Research
  url: https://www.maternamedical.com/data-bibliography/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/materna-medical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/materna-medical-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Materna Medical sells regulated physical devices — the FDA-cleared Milli vaginal dilator and the investigational Ellora labor device — through a WordPress marketing site and a WooCommerce storefront; every OpenAPI, GraphQL, MCP and agent-card path on www.maternamedical.com and www.hellomilli.com returns 404, api./developer./docs./app./mcp. subdomains are NXDOMAIN, there is no GitHub organization, and getmilli.com is a parked domain whose blanket 200s are a JS redirect shell to /lander.
  evidence:
  - status: 404
    url: https://www.maternamedical.com/openapi.json
  - status: 404
    url: https://www.maternamedical.com/llms.txt
  - status: 404
    url: https://www.maternamedical.com/.well-known/agent-card.json
  - status: 404
    url: https://www.hellomilli.com/openapi.json
  - status: 404
    url: https://www.hellomilli.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/materna-medical
  - status: 200
    url: https://getmilli.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Materna Medical is a Mountain View, California women''s health medical device company building an OBGYN platform around pelvic floor health. Its first product, Milli, is an expanding vaginal dilator that widens one millimeter at a time with optional vibration, sold direct-to-consumer and through OBGYN and pelvic floor physical therapy practices for vaginismus, dyspareunia, postpartum recovery and menopause-related painful sex; it launched as a wellness trainer in 2019 and received FDA over-the-counter clearance in 2023. Its second product, Ellora, is an investigational device used during labor to reduce pelvic floor muscle injury in vaginal delivery, studied in the randomized EASE trial across US hospitals and assigned a new ICD-10-PCS technology code effective April 2026. Materna Medical sells regulated physical devices and clinical evidence, not software: it operates a WordPress marketing site (maternamedical.com) and a WooCommerce consumer storefront (hellomilli.com), publishes
  no developer program, no public API, no SDK and no machine-readable API contract, and runs no api., developer., docs. or app. subdomain.'
image: https://www.maternamedical.com/wp-content/uploads/2024/10/materna-medical-logo-full-color.svg
layout: provider
modified: '2026-08-25'
name: Materna Medical
nav: Providers
network: true
overview: 'Materna Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Women''s Health, and Pelvic Health.


  Materna Medical''s developer surface includes engineering blog, product news, support, FAQ, and 11 more developer resources.'
random_paper: 17
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
screenshot: https://raw.githubusercontent.com/api-evangelist/materna-medical/refs/heads/main/screenshots/materna-medical-2026-09-02T150437.png
security:
- kind: domain-security
  name: Materna Medical Domain Security
  slug: materna-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: materna-medical
tags:
- Company
- Healthcare
- Medical Devices
- Women's Health
- Pelvic Health
- OBGYN
- Maternal Health
- Consumer Health
- Clinical Trials
- Medical Technology
website: https://www.maternamedical.com/
---
