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
  href: https://raw.githubusercontent.com/api-evangelist/arthexbiotech/refs/heads/main/hosts/arthexbiotech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arthexbiotech-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arthexbiotech/refs/heads/main/vendors/arthexbiotech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arthexbiotech-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arthexbiotech/refs/heads/main/security/arthexbiotech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arthexbiotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arthexbiotech.com
- group: other
  title: ''
  type: Image
  url: https://cdn.prod.website-files.com/6194be010f431cc064171cc5/644d9efb2a4a5308db2e0b82_Arthex-Logo-Rev.png
- group: docs
  title: ''
  type: Documentation
  url: https://www.arthexbiotech.com/about-arthex
- group: operate
  title: ''
  type: Contact
  url: https://www.arthexbiotech.com/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arthexbiotech.com/privacy-cookie-policy
coverage:
  checked: 2026-09-26
  detail: The site provides only marketing pages and no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.arthexbiotech.com/about-arthex
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arthex Biotech is a biotechnology company focused on developing antisense RNA therapeutics for unmet medical needs, notably an anti‑miR program targeting Myotonic Dystrophy. The company emphasizes innovative RNA medicine delivery, with a pipeline of microRNA‑based treatments and a commitment to advancing clinical trials and patient support. Based in Valencia, Spain, Arthex Biotech engages with partners and investors to bring next‑generation RNA therapies to market.
image: https://cdn.prod.website-files.com/6194be010f431cc064171cc5/6451ac051216fb21665431e0_Arthex-OG-Card.jpg
layout: provider
modified: '2026-09-26'
name: Arthexbiotech
nav: Providers
network: true
overview: 'Arthexbiotech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, RNA Therapeutics, Myotonic Dystrophy, Valencia, and Healthcare.


  Arthexbiotech''s developer surface includes documentation and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arthexbiotech Domain Security
  slug: arthexbiotech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arthexbiotech
tags:
- Biotechnology
- RNA Therapeutics
- Myotonic Dystrophy
- Valencia
- Healthcare
website: https://www.arthexbiotech.com
---
