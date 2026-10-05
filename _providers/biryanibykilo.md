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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biryanibykilo/refs/heads/main/security/biryanibykilo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/biryanibykilo-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biryanibykilo/refs/heads/main/hosts/biryanibykilo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biryanibykilo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biryanibykilo/refs/heads/main/vendors/biryanibykilo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biryanibykilo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biryanibykilo.com/terms-and-conditions
- group: company
  title: ''
  type: Newsroom
  url: https://biryanibykilo.com/media
- group: company
  title: ''
  type: Blog
  url: https://biryanibykilo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/biryanibykilo
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biryanibykilo/refs/heads/main/security/biryanibykilo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/biryanibykilo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biryanibykilo/refs/heads/main/security/biryanibykilo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biryanibykilo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biryanibykilo.com
coverage:
  checked: '2026-09-28'
  detail: Biryanibykilo provides a consumer food ordering website with no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://biryanibykilo.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Biryanibykilo is an Indian online food ordering platform specializing in biryani and related dishes. It offers customers the ability to browse menus, place orders for delivery or pickup, and track order status through its website and mobile apps. The service focuses on a wide variety of regional biryani styles, catering to diverse taste preferences across India.
image: https://biryanibykilo.com/favicon.png
layout: provider
modified: '2026-09-28'
name: Biryanibykilo
nav: Providers
network: true
overview: 'Biryanibykilo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Delivery, Biryani, and India.


  Biryanibykilo''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.6
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biryanibykilo Domain Security
  slug: biryanibykilo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Biryanibykilo Vulnerability Disclosure
  slug: biryanibykilo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: biryanibykilo
tags:
- Company
- Food
- Delivery
- Biryani
- India
website: https://biryanibykilo.com
---
