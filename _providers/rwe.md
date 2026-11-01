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
  href: https://artifacts.apis.io/rwe/hosts/rwe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rwe-hosts.yml
- group: other
  href: https://artifacts.apis.io/rwe/vendors/rwe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rwe-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rwe.com/en/products-and-services/supplier-portal/general-conditions/terms-of-delivery-and-service/
- group: company
  title: ''
  type: Newsroom
  url: https://www.rwe.com/en/press/contact/
- group: other
  title: ''
  type: Leadership
  url: https://www.rwe.com/der-konzern/rwest/management/
- group: auth
  href: https://artifacts.apis.io/rwe/security/rwe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rwe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rwe.com/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found at standard locations on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.rwe.com/openapi.json
  - status: 404
    url: https://www.rwe.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: RWE Mobility, part of the RWE Group, provides energy solutions and services across Europe, focusing on renewable energy, electricity generation, and innovative mobility offerings. The company leverages digital platforms to deliver data and APIs for energy management, sustainability reporting, and customer services, supporting a transition to a sustainable energy future.
image: https://www.rwe.com/-/media/RWE/Logos/RWE_Logo_Social_Image_8.jpg
layout: provider
modified: '2026-10-28'
name: RWE Mobility
nav: Providers
network: true
overview: RWE Mobility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Mobility, Renewable, Sustainability, and Europe.
random_paper: 22
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rwe Domain Security
  slug: rwe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rwe
tags:
- Energy
- Mobility
- Renewable
- Sustainability
- Europe
- Company
website: https://rwe.com/
---
