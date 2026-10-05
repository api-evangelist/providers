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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aravax/refs/heads/main/hosts/aravax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aravax-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aravax/refs/heads/main/vendors/aravax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aravax-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aravax.com.au/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.aravax.com.au/about-aravax/management/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aravax/refs/heads/main/security/aravax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aravax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aravax.com.au
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/aravax
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Aravax is a biotechnology company focused on developing next‑generation immunotherapies for food allergies. It aims to revolutionise treatment by using proprietary peptide platforms to retrain the immune system, offering safer and more convenient solutions. The company runs international clinical trials for its lead product PVX108 targeting peanut allergy, with sites in the United States and Australia. Aravax is headquartered in Melbourne, Australia, and also operates in the UK.
layout: provider
modified: '2026-09-25'
name: Aravax
nav: Providers
network: true
overview: Aravax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Immunotherapy, Food Allergy, Clinical Trials, and Australia.
random_paper: 5
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aravax Domain Security
  slug: aravax-domain-security
  summary_line: TLSv1.3
slug: aravax
tags:
- Biotechnology
- Immunotherapy
- Food Allergy
- Clinical Trials
- Australia
website: https://www.aravax.com.au
---
