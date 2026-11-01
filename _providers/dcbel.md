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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dcbel/hosts/dcbel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dcbel-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dcbel.energy/press
- group: auth
  href: https://artifacts.apis.io/dcbel/security/dcbel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dcbel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dcbel.energy
- group: company
  title: ''
  type: Blog
  url: https://www.dcbel.energy/blog
- group: operate
  title: ''
  type: Support
  url: https://www.dcbel.energy/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dcbel.energy/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dcbel.energy/privacy-policy
- group: company
  title: ''
  type: AboutUs
  url: https://www.dcbel.energy/about-us
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.dcbel.energy/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dcbel builds private energy grids for homes, offering the Ara system that integrates solar, battery storage, and vehicle-to-home charging. The company aims to provide reliable, flexible, and clean energy solutions, reducing dependence on traditional grids and enabling homeowners to generate, store, and use power independently. Their platform includes hardware, software, and services to manage energy flow, supporting sustainability and resilience.
image: https://cms-portal-c7ffe5bqbnatcfc0.a01.azurefd.net/api/media/file/ara-front-image.png
layout: provider
modified: '2026-10-22'
name: Dcbel
nav: Providers
network: true
overview: 'Dcbel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Cleantech, Home Energy, Solar, and Battery.


  Dcbel''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.4
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dcbel Domain Security
  slug: dcbel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dcbel
tags:
- Energy
- Cleantech
- Home Energy
- Solar
- Battery
website: https://www.dcbel.energy
---
