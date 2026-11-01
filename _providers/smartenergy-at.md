---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/smartenergy-at/hosts/smartenergy-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartenergy-at-hosts.yml
- group: auth
  href: https://artifacts.apis.io/smartenergy-at/security/smartenergy-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartenergy-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smartenergy.at/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smartenergy.at/
- group: docs
  title: ''
  type: Documentation
  url: https://smartenergy.at/api-schnittstellen
- group: docs
  title: ''
  type: APIReference
  url: https://smartenergy.at/api-schnittstellen
- group: start
  title: ''
  type: GettingStarted
  url: https://smartenergy.at/api-schnittstellen
- group: operate
  title: ''
  type: Support
  url: https://smartenergy.at/kontakt
- group: commercial
  title: ''
  type: Pricing
  url: https://smartenergy.at/stromtarife
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation page lists API endpoints but offers no machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://smartenergy.at/api-schnittstellen
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: smartENERGY is an Austrian energy company offering renewable electricity and smart‑grid services. It provides public APIs for electricity price data (smartCONTROL), time‑based pricing (smartTIMES) and live energy metrics (energyLIVE). The APIs enable developers to integrate real‑time pricing, consumption forecasts and community energy management into applications, supporting sustainability and smart‑meter integration.
layout: provider
modified: '2026-10-28'
name: smartENERGY
nav: Providers
network: true
overview: 'smartENERGY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Renewable, SmartGrid, API, and Austria.


  smartENERGY''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 4 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smartenergy At Domain Security
  slug: smartenergy-at-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smartenergy-at
tags:
- Energy
- Renewable
- SmartGrid
- API
- Austria
website: https://smartenergy.at/
---
