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
- description: OPeNDAP provides an API for scientific data access as described in their developer documentation.
  name: OPeNDAP API
  slug: opendap-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/opendap/changelog/opendap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opendap-changelog.yml
- group: other
  href: https://artifacts.apis.io/opendap/hosts/opendap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opendap-hosts.yml
- group: other
  href: https://artifacts.apis.io/opendap/vendors/opendap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opendap-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.opendap.org/community/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.opendap.org/about/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OPENDAP/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.opendap.org/software/releases/
- group: company
  title: ''
  type: Blog
  url: https://www.opendap.org/blog/
- group: auth
  href: https://artifacts.apis.io/opendap/security/opendap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendap.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.opendap.org/documentation/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.opendap.org/developers/
- group: operate
  title: ''
  type: Support
  url: https://www.opendap.org/support/
coverage:
  checked: '2026-10-30'
  detail: Documentation is publicly accessible but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.opendap.org/documentation/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OPeNDAP provides open-source software for distributed scientific data access, enabling researchers and data providers to share and retrieve large datasets efficiently. Their Hyrax Data Server implements the DAP protocols, offering robust, scalable solutions for data discovery, access, and management across diverse scientific domains.
image: https://www.opendap.org/wp-content/uploads/2024/01/Group-1000001644.jpg
layout: provider
modified: '2026-10-28'
name: OPeNDAP
nav: Providers
network: true
overview: 'OPeNDAP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-Source, Scientific Data, Distributed Systems, and Data Access.


  OPeNDAP''s developer surface includes changelog, engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 60.7
    operational_transparency: 21.1
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
  name: Opendap Domain Security
  slug: opendap-domain-security
  summary_line: TLSv1.3
slug: opendap
tags:
- Company
- Open-Source
- Scientific Data
- Distributed Systems
- Data Access
website: https://www.opendap.org
---
