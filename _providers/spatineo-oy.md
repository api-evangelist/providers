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
  href: https://artifacts.apis.io/spatineo-oy/hosts/spatineo-oy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spatineo-oy-hosts.yml
- group: other
  href: https://artifacts.apis.io/spatineo-oy/vendors/spatineo-oy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spatineo-oy-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spatineo.com/privacy-policy?hsLang=en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spatineo
- group: auth
  href: https://artifacts.apis.io/spatineo-oy/security/spatineo-oy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spatineo-oy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spatineo.com
- group: company
  title: ''
  type: Blog
  url: https://spatineo.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://spatineo.com/contact
- group: company
  title: ''
  type: About
  url: https://spatineo.com/about
- group: other
  title: ''
  type: Services
  url: https://spatineo.com/services
- group: docs
  title: ''
  type: References
  url: https://spatineo.com/references
coverage:
  checked: '2026-10-26'
  detail: Spatineo provides GIS consulting services but does not publish a developer program or public API specifications.
  evidence:
  - status: 200
    url: https://spatineo.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Spatineo Oy provides expert consultancy, services, and software products focused on spatial web services and data infrastructure. Founded in 2011 and headquartered in Helsinki, Finland, the company has over 15 years of GIS expertise, serving governments, enterprises, and research institutions. It contributes to ISO standards and is an active OGC member, helping organizations create value from geospatial data.
layout: provider
modified: '2026-10-26'
name: Spatineo Oy
nav: Providers
network: true
overview: 'Spatineo Oy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, Geospatial, DataInfrastructure, and Consulting.


  Spatineo Oy''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Spatineo Oy Domain Security
  slug: spatineo-oy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spatineo-oy
tags:
- Company
- GIS
- Geospatial
- DataInfrastructure
- Consulting
website: https://spatineo.com
---
