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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ablacare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mayhealth.com/
- group: operate
  title: ''
  type: Support
  url: https://mayhealth.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mayhealth.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mayhealth.com/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/may-health/
coverage:
  checked: '2026-09-06'
  detail: 'AblaCare rebranded to May Health and sells a physician-delivered radiofrequency ablation device, not software: ablacare.com 301s to mayhealth.com, a WordPress marketing site whose entire nav is company/patients/healthcare-professionals/press/careers with no developer, docs or API path, and whose only machine-readable surface is the stock WordPress core /wp-json CMS endpoint rather than any product API.'
  evidence:
  - status: 301
    url: https://ablacare.com/
  - status: 404
    url: https://mayhealth.com/openapi.json
  - status: 404
    url: https://mayhealth.com/llms.txt
  - status: 404
    url: https://mayhealth.com/.well-known/api-catalog
  - status: 404
    url: https://mayhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/mayhealth
  - status: 404
    url: https://registry.npmjs.org/mayhealth
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: AblaCare rebranded as May Health in September 2022 and now operates at mayhealth.com; ablacare.com 301-redirects there. It is a clinical-stage medical device company headquartered in Paris, France, founded in 2017 out of Sofinnova Partners' MD Start medtech acceleration program. The company develops Ovarian Rebalancing, a one-time minimally invasive in-office procedure using ultrasound-guided radiofrequency ablation of ovarian tissue to restore spontaneous ovulation in women with infertility related to polycystic ovary syndrome (PCOS). It raised a EUR 10M Series A in 2019, a USD 25M Series B co-led by Bpifrance and Trill Impact Ventures in 2024, and is running the randomized REBALANCE pivotal study intended to support an FDA submission. It publishes no developer program, API or SDK.
image: https://mayhealth.com/wp-content/uploads/2023/07/cropped-favicon-512-192x192.png
layout: provider
modified: '2026-09-06'
name: Ablacare
nav: Providers
network: true
overview: 'Ablacare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health Care, Medical Devices, Femtech, Fertility, and Womens Health.


  Ablacare''s developer surface includes support and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 4.8
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
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ablacare Domain Security
  slug: ablacare-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ablacare
tags:
- Health Care
- Medical Devices
- Femtech
- Fertility
- Womens Health
- Clinical Trials
- Medtech
- France
- Company
website: https://mayhealth.com/
---
