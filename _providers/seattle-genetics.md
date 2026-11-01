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
  href: https://artifacts.apis.io/seattle-genetics/hosts/seattle-genetics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seattle-genetics-hosts.yml
- group: other
  href: https://artifacts.apis.io/seattle-genetics/vendors/seattle-genetics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seattle-genetics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pfizer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pfizer.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.pfizer.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.pfizer.com/about/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seagen.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Seagen
- group: auth
  href: https://artifacts.apis.io/seattle-genetics/security/seattle-genetics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seattle-genetics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seagen.com
created: '2026-10-26'
description: Seagen (formerly Seattle Genetics) is a biotechnology company focused on developing and commercializing antibody-drug conjugate (ADC) therapies for the treatment of cancer. Founded in 1998 and headquartered in Bothell, Washington, Seagen leverages its proprietary technology platform to create targeted therapies that deliver cytotoxic agents directly to tumor cells while sparing healthy tissue. The company’s portfolio includes FDA‑approved products such as Tivdak, Padcev, and Enhertu, and it maintains a robust pipeline of investigational ADCs across multiple oncology indications. Seagen is publicly traded on NASDAQ under the ticker SGEN and is committed to advancing precision oncology through innovative research and strategic collaborations.
layout: provider
modified: '2026-10-26'
name: Seattle Genetics
nav: Providers
network: true
overview: 'Seattle Genetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Oncology, ADC, CancerTherapy, and Seattle.


  Seattle Genetics'' developer surface includes documentation and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: Seattle Genetics Domain Security
  slug: seattle-genetics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: seattle-genetics
tags:
- Biotechnology
- Oncology
- ADC
- CancerTherapy
- Seattle
- Seagen
website: https://www.seagen.com
---
