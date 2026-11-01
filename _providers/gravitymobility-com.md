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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/gravitymobility-com/hosts/gravitymobility-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gravitymobility-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gravitytechnologies.com/terms-conditions
- group: company
  title: ''
  type: Blog
  url: https://gravitytechnologies.com/blog
- group: auth
  href: https://artifacts.apis.io/gravitymobility-com/security/gravitymobility-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gravitymobility-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gravitytechnologies.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://gravitymobility.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Gravity provides high‑power electric vehicle (EV) charging solutions, offering 500 kW chargers that can add up to 250 kWh in just five minutes. Based in the United States, Gravity’s technology enables rapid, reliable charging for fleets, public stations, and commercial installations, supporting the transition to zero‑emission transportation.
image: https://gravity-assets.b-cdn.net/_1200x630_crop_center-center_82_none/O-Utside-2.jpg?mtime=1745240669
layout: provider
modified: '2026-10-22'
name: Gravity
nav: Providers
network: true
overview: 'Gravity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EVCharging, Energy, Infrastructure, and Mobility.


  Gravity''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gravitymobility Com Domain Security
  slug: gravitymobility-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: gravitymobility-com
tags:
- Company
- EVCharging
- Energy
- Infrastructure
- Mobility
- Technology
website: https://gravitytechnologies.com
---
