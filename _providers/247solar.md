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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/247solar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://247solar.com/
- group: company
  title: ''
  type: About
  url: https://247solar.com/about/
- group: company
  title: ''
  type: Blog
  url: https://247solar.com/solar-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://247solar.com/feed/
- group: operate
  title: ''
  type: ContactUs
  url: https://247solar.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://247solar.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://247solar.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://247solar.com/our-investors/
- group: company
  title: ''
  type: Careers
  url: https://247solar.com/solar-energy-careers/
coverage:
  checked: '2026-09-05'
  detail: 247Solar sells concentrated-solar-power plants, Heat2Power turbines and HeatStore thermal storage as capital equipment and power purchase agreements, so there is no software product to put an API on; the only machine-readable surface on 247solar.com is the stock WordPress core REST API at /wp-json, whose 404 routes are entirely CMS plugin namespaces (Divi, Yoast, Wordfence, Newfold, Contact Form 7) and not a 247Solar product.
  evidence:
  - status: 404
    url: https://247solar.com/openapi.json
  - status: 404
    url: https://247solar.com/.well-known/agent-card.json
  - status: 404
    url: https://247solar.com/llms.txt
  - status: 200
    url: https://247solar.com/wp-json
  - status: 404
    url: https://api.github.com/users/247solar
  - status: 200
    url: https://247solar.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 247Solar, Inc. is a zero-carbon energy technology company with MIT origins that designs and builds modular third-generation concentrated solar power (CSP) systems delivering round-the-clock clean electricity and industrial-grade heat. Its 247Solar Plant couples a high-temperature solar receiver (~970C) with the Heat2Power turbine and HeatStore thermal storage, holding energy in ceramic pellets or ordinary sand for 20+ hours without batteries or molten salts. The company targets mining, microgrids, off-grid and rural electrification, industrial heat, economic development zones, grid support, data centers and green hydrogen, and sells through power purchase agreements as well as equipment. Headquartered in Great Falls, Virginia, 247Solar is a hardware and project-development business; it publishes no public API, developer program or machine-readable specification.
image: https://247solar.com/wp-content/uploads/2021/10/logo.png
layout: provider
modified: '2026-09-05'
name: 247Solar
nav: Providers
network: true
overview: '247Solar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Concentrated Solar Power, and Renewable Energy.


  247Solar''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 247Solar Domain Security
  slug: 247solar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 247solar
tags:
- Company
- Energy
- Solar
- Concentrated Solar Power
- Renewable Energy
- Thermal Energy Storage
- Clean Technology
- Industrial Heat
- Microgrids
- Green Hydrogen
- Mining
- Climate Tech
website: https://247solar.com/
---
