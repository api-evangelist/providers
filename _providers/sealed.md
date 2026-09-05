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
  url: security/sealed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sealed.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sealed.com/in-the-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sealed.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sealedinc
- group: start
  title: ''
  type: Login
  url: https://app.sealed.com/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sealed
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sealed-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sealed-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: Sealed ships software (the Sealed Pro contractor platform) but only as an end-user web application — the full 308-URL sitemap for www.sealed.com contains no developer, API, docs or integration page, and the only API-shaped surface is the private authenticated backend behind app.sealed.com whose paths under /api/ answer {"detail":"Not Found"} with interactive docs disabled and no contract published.
  evidence:
  - status: 404
    url: https://www.sealed.com/developers
  - status: 404
    url: https://www.sealed.com/api-docs
  - status: 404
    url: https://www.sealed.com/openapi.json
  - status: 404
    url: https://www.sealed.com/llms.txt
  - status: 404
    url: https://app.sealed.com/api/docs
  - status: 404
    url: https://app.sealed.com/api/openapi.json
  - status: 404
    url: https://www.sealed.com/.well-known/agent-card.json
  - status: 200
    url: https://www.sealed.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Sealed is a New York-based climate technology company, founded in 2012, whose Sealed Pro platform helps home-improvement contractors sell and finance home weatherization and electrification projects — insulation, air sealing, heat pumps, smart thermostats and heat-pump water heaters. Sealed pairs energy data and analytics with a rebate and incentive engine that qualifies a project at the point of sale, guarantees a minimum rebate amount, files the utility and Inflation Reduction Act (HOMES / HEAR) paperwork on the contractor's behalf, and pays the contractor after installation while Sealed carries the incentive-collection risk. The company began as a direct-to-consumer home energy retrofit provider with the first residential energy-savings guarantee, and relaunched as Sealed Pro, a contractor-facing software platform, working with utilities and state energy offices on measured- and modeled-savings programs.
image: https://www.sealed.com/gcs/sealed-dev.appspot.com/web/sealed-logo.svg
layout: provider
modified: '2026-08-26'
name: Sealed
nav: Providers
network: true
overview: 'Sealed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Efficiency, Climate Tech, and Home Services.


  Sealed''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Sealed Plans Pricing
  plan_count: 0
  slug: sealed-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Sealed Rate Limits
  slug: sealed-rate-limits
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sealed/refs/heads/main/screenshots/sealed-2026-09-02T154630.png
security:
- kind: domain-security
  name: Sealed Domain Security
  slug: sealed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sealed
tags:
- Company
- Energy
- Energy Efficiency
- Climate Tech
- Home Services
- HVAC
- Electrification
- Rebates
- Incentives
- Contractors
- Utilities
- Weatherization
website: https://www.sealed.com/
---
