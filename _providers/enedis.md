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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Enedis provides electricity distribution services; public API documentation is not publicly available, and developer pages return 404.
  name: Enedis API
  slug: enedis-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/enedis/refs/heads/main/vendors/enedis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enedis-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://connect-racco.enedis.fr/prac-internet/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/enedis/refs/heads/main/security/enedis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enedis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enedis.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.enedis.fr/espace-prestataires
- group: operate
  title: ''
  type: Support
  url: https://www.enedis.fr/aide-contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enedis.fr/mentions-legales-et-conditions-generales-dutilisation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enedis.fr/donnees-personnelles
coverage:
  checked: 2026-09-22
  detail: Developer portal page https://www.enedis.fr/developpeurs returns 404, no machine‑readable API docs found.
  evidence:
  - status: 404
    url: https://www.enedis.fr/developpeurs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Enedis is the French public electricity distribution network operator, managing the grid for millions of customers across France. It modernizes, maintains, and services the electricity distribution infrastructure, providing metering, outage management, and customer support. As a public service entity, Enedis plays a key role in France’s energy transition and grid reliability.
image: https://www.enedis.fr/sites/default/files/images/2022-10/_DSC2923.jpg
layout: provider
modified: '2026-09-22'
name: Enedis
nav: Providers
network: true
overview: 'Enedis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Utility, and France.


  Enedis'' developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 15.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Enedis Domain Security
  slug: enedis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enedis
tags:
- Company
- Energy
- Electricity
- Utility
- France
- Public Service
website: https://www.enedis.fr/
---
