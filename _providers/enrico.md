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
api_count: 1
apis:
- description: Holiday data API providing public holiday information for multiple countries.
  name: Enrico Holiday Service API
  slug: enrico-holiday-service-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/enrico/hosts/enrico-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enrico-hosts.yml
- group: auth
  href: https://artifacts.apis.io/enrico/security/enrico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enrico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kayaposoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kayaposoft.com/enrico/
- group: docs
  title: ''
  type: APIReference
  url: https://kayaposoft.com/enrico/docs-v1.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://kayaposoft.com/enrico/json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jurajmajer
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://kayaposoft.com/enrico/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Enrico holiday service is a public holidays web service offered by Kayapo, a Slovak software company founded in 2010. The service provides holiday data for various countries via a simple API, supporting integration into calendars, scheduling tools, and applications. Kayapo specializes in software development across multiple languages and offers innovative IT solutions for commercial and non-commercial use.
layout: provider
modified: '2026-10-28'
name: Enrico holiday service
nav: Providers
network: true
overview: 'Enrico holiday service is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Holiday, API, Slovakia, and OpenSource.


  Enrico holiday service''s developer surface includes documentation, API reference, getting-started guide, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Enrico Domain Security
  slug: enrico-domain-security
  summary_line: TLSv1.3
slug: enrico
tags:
- Company
- Holiday
- API
- Slovakia
- OpenSource
website: https://kayaposoft.com/
---
