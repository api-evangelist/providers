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
  href: https://artifacts.apis.io/geoscape/hosts/geoscape-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geoscape-hosts.yml
- group: other
  href: https://artifacts.apis.io/geoscape/vendors/geoscape-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geoscape-vendors.yml
- group: build
  href: https://artifacts.apis.io/geoscape/packages/geoscape-packages.yml
  title: ''
  type: SDKs
  url: packages/geoscape-packages.yml
- group: build
  href: https://artifacts.apis.io/geoscape/packages/geoscape-packages.yml
  title: ''
  type: Packages
  url: packages/geoscape-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geoscape.com.au/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://geoscape.com.au/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geoscape.com.au/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.geoscape.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geoscape
- group: auth
  href: https://artifacts.apis.io/geoscape/security/geoscape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoscape-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geoscape.com.au/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api-docs.geoscape.com.au/mcp
  - status: 403
    url: https://docs.geoscape.com.au/mcp
  - status: 200
    url: https://geoscape.com.au/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Geoscape provides location intelligence data for Australia, offering products such as national address verification, building data, land parcels, surface cover, roads, and administrative boundaries. Their services help governments, financial services, insurance, utilities, and real estate sectors make informed decisions based on accurate geographic information. The company emphasizes high-quality, consistent data to support planning, risk assessment, and compliance across various industries.
layout: provider
modified: '2026-10-26'
name: Geoscape
nav: Providers
network: true
overview: 'Geoscape is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location-Intelligence, Data-Analytics, Australia, and GIS.


  Geoscape''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    mcp: unknown
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
  name: Geoscape Domain Security
  slug: geoscape-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geoscape
tags:
- Company
- Location-Intelligence
- Data-Analytics
- Australia
- GIS
website: https://geoscape.com.au/
---
