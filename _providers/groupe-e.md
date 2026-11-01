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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/groupe-e/hosts/groupe-e-hosts.yml
  title: ''
  type: Hosts
  url: hosts/groupe-e-hosts.yml
- group: other
  href: https://artifacts.apis.io/groupe-e/vendors/groupe-e-vendors.yml
  title: ''
  type: Vendors
  url: vendors/groupe-e-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.groupe-e.ch/fr/univers-groupe-e/media/communique-presse/nouveau-site-web
- group: company
  title: ''
  type: Blog
  url: https://www.groupe-e.ch/fr/blog
- group: auth
  href: https://artifacts.apis.io/groupe-e/security/groupe-e-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/groupe-e-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://groupe-e.ch/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://groupe-e.ch/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Groupe E is a Swiss energy solutions provider offering electricity, solar, heating, and mobility services to private, corporate, real‑estate and public customers. The company focuses on renewable energy, smart‑metering, collective self‑consumption and electric‑vehicle charging infrastructure. It operates across Switzerland and promotes sustainable energy transition through digital services and customer‑centric platforms.
layout: provider
modified: '2026-10-28'
name: Groupe E
nav: Providers
network: true
overview: 'Groupe E is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable, Switzerland, and Utilities.


  Groupe E''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    mcp: derived
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
  name: Groupe E Domain Security
  slug: groupe-e-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groupe-e
tags:
- Company
- Energy
- Renewable
- Switzerland
- Utilities
website: https://groupe-e.ch/
---
