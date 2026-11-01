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
api_count: 1
apis:
- description: Provides access to various online geoscience data tools and portals.
  name: Geoscience Australia Data Online Tools
  slug: geoscience-australia-data-online-tools
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/geoscience-australia/well-known/geoscience-australia-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/geoscience-australia-portal-security.txt
- group: auth
  href: https://artifacts.apis.io/geoscience-australia/well-known/geoscience-australia-earthquakes-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/geoscience-australia-earthquakes-security.txt
- group: auth
  href: https://artifacts.apis.io/geoscience-australia/well-known/geoscience-australia-communication-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/geoscience-australia-communication-security.txt
- group: agent
  href: https://artifacts.apis.io/geoscience-australia/well-known/geoscience-australia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/geoscience-australia-well-known.yml
- group: other
  href: https://artifacts.apis.io/geoscience-australia/hosts/geoscience-australia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geoscience-australia-hosts.yml
- group: other
  href: https://artifacts.apis.io/geoscience-australia/vendors/geoscience-australia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/geoscience-australia-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ga.gov.au/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ga.gov.au/news
- group: auth
  href: https://artifacts.apis.io/geoscience-australia/security/geoscience-australia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoscience-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ga.gov.au/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documentation pages.
  evidence:
  - status: 200
    url: https://www.ga.gov.au/data-pubs/online-tools
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Geoscience Australia is the national agency delivering geoscientific knowledge and data to support decision‑making, research, and public understanding. It provides authoritative information on Australia’s geology, natural resources, hazards, and environmental processes, offering open data, maps, and tools for scientists, industry, and the community.
image: https://www.ga.gov.au/about/hivo-ga-Yi2cTKBdCjkhH7ubL-cropped_about_web.jpg
layout: provider
modified: '2026-10-29'
name: Geoscience Australia
nav: Providers
network: true
overview: Geoscience Australia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geoscience, Australia, Government, Data, and Research.
random_paper: 16
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Geoscience Australia Domain Security
  slug: geoscience-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geoscience-australia
tags:
- Geoscience
- Australia
- Government
- Data
- Research
- Environment
website: http://www.ga.gov.au/
---
