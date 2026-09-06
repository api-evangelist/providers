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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://welbehealth.com/
- group: company
  title: ''
  type: About
  url: https://welbehealth.com/about/
- group: company
  title: ''
  type: Blog
  url: https://welbehealth.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://welbehealth.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://welbehealth.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://welbehealth.com/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://welbehealth.com/privacy-policy/
- group: company
  title: ''
  type: Partners
  url: https://welbehealth.com/partners/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/welbehealth-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/welbehealth-llms.txt
coverage:
  checked: '2026-09-04'
  detail: WelbeHealth is a PACE care-delivery organization and provider-sponsored health plan, not a software vendor; its only public web surfaces are a WordPress marketing site, a Phenom-hosted careers SPA and a broker login, and welbehealth.com returns 404 on /developers, /api, /fhir, /openapi.json and every /.well-known/ path, with no api./developer./docs./fhir. subdomain resolving and no github.com/welbehealth organization.
  evidence:
  - status: 404
    url: https://welbehealth.com/developers
  - status: 404
    url: https://welbehealth.com/openapi.json
  - status: 404
    url: https://welbehealth.com/.well-known/api-catalog
  - status: 0
    url: https://api.welbehealth.com/
  - status: 404
    url: https://github.com/welbehealth
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: WelbeHealth is a California public benefit company and provider-sponsored health plan operating Programs of All-Inclusive Care for the Elderly (PACE). Founded in 2015 and headquartered in Menlo Park, California, it is both insurer and care provider for frail seniors who qualify for nursing-home level of care, coordinating and paying for all medical, behavioral, pharmacy, home care, rehabilitation, transportation and social services through interdisciplinary teams at PACE centers across California including Fresno, Long Beach, Los Angeles, Modesto, North Hollywood, Pasadena, Rosemead, Stockton and the Inland Empire, funded by capitated Medicare and Medi-Cal payments. In 2022 it became the first PACE organization to convert to public benefit company status. API Evangelist finds no public developer program, no API documentation and no machine-readable contract on any WelbeHealth-controlled host as of September 2026.
image: https://welbehealth.com/wp-content/uploads/2022/03/WelbeHealth_Logo.png
layout: provider
modified: '2026-09-04'
name: WelbeHealth
nav: Providers
network: true
overview: 'WelbeHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Healthcare, Health Plans, and Senior Care.


  WelbeHealth''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Welbehealth Domain Security
  slug: welbehealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: welbehealth
tags:
- Company
- Health Care
- Healthcare
- Health Plans
- Senior Care
- PACE
- Medicare
- Medicaid
- Managed Care
- Public Benefit Company
website: https://welbehealth.com/
---
