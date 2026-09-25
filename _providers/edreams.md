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
api_count: 0
artifact_total: 1
common:
- group: docs
  title: ''
  type: Documentation
  url: https://help.edreams.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/edreams/refs/heads/main/llms/edreams-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edreams-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/edreams/refs/heads/main/hosts/edreams-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edreams-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/edreams/refs/heads/main/vendors/edreams-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edreams-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edreams.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edreams.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.edreams.com/our-brand/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/edreams/refs/heads/main/security/edreams-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edreams-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.edreams.com/
- group: company
  title: ''
  type: Blog
  url: https://www.edreams.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.edreams.com
created: '2026-09-23'
description: eDreams ODIGEO is a leading online travel agency operating globally, offering a comprehensive platform for booking flights, hotels, vacation packages, and car rentals. The company provides a range of travel services through its website and mobile apps, serving millions of customers worldwide. It is part of the ODIGEO group, which includes other travel brands, and focuses on delivering competitive prices, a user-friendly experience, and extensive travel options across numerous destinations.
image: https://www.edreams.com/images/onefront/bluestone/ED/OpenGraph.png
layout: provider
modified: '2026-09-23'
name: eDreams ODIGEO
nav: Providers
network: true
overview: 'eDreams ODIGEO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Booking, Flights, Hotels, and Car Rentals.


  eDreams ODIGEO''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Edreams Domain Security
  slug: edreams-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edreams
tags:
- Travel
- Booking
- Flights
- Hotels
- Car Rentals
- Europe
website: https://www.edreams.com/
---
