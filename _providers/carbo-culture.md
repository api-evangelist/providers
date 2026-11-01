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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Carbo Culture services
  name: Carbo Culture API
  slug: carbo-culture-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/carbo-culture/hosts/carbo-culture-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbo-culture-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbo-culture/vendors/carbo-culture-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbo-culture-vendors.yml
- group: auth
  href: https://artifacts.apis.io/carbo-culture/security/carbo-culture-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbo-culture-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carboculture.com
- group: start
  title: ''
  type: GettingStarted
  url: https://carboculture.com/about
- group: company
  title: ''
  type: Blog
  url: https://medium.com/carboculture
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carboculture.com/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carboculture.com/legal
coverage:
  checked: '2026-10-24'
  detail: Main website returns JavaScript-rendered pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://carboculture.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Carbo Culture is a climate‑tech project developer building patented Carbolysis™ reactors that convert waste biomass into stable biochar, locking carbon away for centuries while generating renewable energy. The company aims to remove 1 billion tonnes of CO₂, offering biochar, carbon credits, and clean energy solutions. Founded in 2018, backed by True‑Ventures, it operates from Helsinki, Finland, and collaborates with industry partners to scale its carbon removal platform.
image: https://i0.wp.com/wp.carboculture.com/wp-content/uploads/2023/03/SEO-Image.jpg?fit=1200%2C675&ssl=1
layout: provider
modified: '2026-10-24'
name: Carbo Culture
nav: Providers
network: true
overview: 'Carbo Culture is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ClimateTech, CarbonRemoval, Biochar, and RenewableEnergy.


  Carbo Culture''s developer surface includes getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbo Culture Domain Security
  slug: carbo-culture-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbo-culture
tags:
- Company
- ClimateTech
- CarbonRemoval
- Biochar
- RenewableEnergy
website: https://carboculture.com
---
