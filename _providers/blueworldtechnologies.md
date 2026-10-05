---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blueworldtechnologies/refs/heads/main/well-known/blueworldtechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blueworldtechnologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blueworldtechnologies/refs/heads/main/hosts/blueworldtechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blueworldtechnologies-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.blue.world/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.blue.world/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blueworldtechnologies/refs/heads/main/security/blueworldtechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blueworldtechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blue.world
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blue.world/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blue.world/cookies-and-privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.blue.world/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/blueworldtechnologies
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Blue World Technologies develops and manufactures high‑temperature PEM methanol fuel cell components and systems for maritime, stationary and heavy‑duty transportation sectors. The company aims to provide green, efficient alternatives to combustion engines and diesel generators, focusing on renewable methanol solutions and advanced fuel cell platforms.
image: https://www.blue.world/wp-content/uploads/2021/03/product_image.jpg
layout: provider
modified: '2026-09-29'
name: Blueworldtechnologies
nav: Providers
network: true
overview: 'Blueworldtechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Fuel Cells, Maritime, and Renewables.


  Blueworldtechnologies'' developer surface includes support and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blueworldtechnologies Domain Security
  slug: blueworldtechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blueworldtechnologies
tags:
- Company
- Energy
- Fuel Cells
- Maritime
- Renewables
website: https://www.blue.world
---
