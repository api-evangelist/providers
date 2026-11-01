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
  href: https://artifacts.apis.io/zenqry/hosts/zenqry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenqry-hosts.yml
- group: other
  href: https://artifacts.apis.io/zenqry/vendors/zenqry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenqry-vendors.yml
- group: auth
  href: https://artifacts.apis.io/zenqry/security/zenqry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenqry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenqry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zenqry.com/manual.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenqry.com/plans.html
- group: operate
  title: ''
  type: Support
  url: https://bjoernkw.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bjoernkw.com/privacy-policy/
coverage:
  checked: '2026-10-22'
  detail: Provider documentation is HTML without any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://www.zenqry.com/manual.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: ZenQuery, offered by Björn Wilmsmann IT Services, provides an enterprise backend-as-a-service platform that instantly creates RESTful APIs over existing SQL databases. It enables users to query relational data stores and receive results in JSON, XML, or CSV without writing code. Targeted at enterprises seeking to unlock siloed data, ZenQuery supports major RDBMSs including Oracle, SQL Server, PostgreSQL, MySQL, and IBM DB2, and emphasizes on‑premise deployment for data security.
layout: provider
modified: '2026-10-21'
name: Björn Wilmsmann IT Services
nav: Providers
network: true
overview: 'Björn Wilmsmann IT Services is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, BaaS, Enterprise, Data Integration, and REST API.


  Björn Wilmsmann IT Services'' developer surface includes documentation, pricing, support, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Zenqry Domain Security
  slug: zenqry-domain-security
  summary_line: TLSv1.3
slug: zenqry
tags:
- Backend
- BaaS
- Enterprise
- Data Integration
- REST API
website: https://www.zenqry.com/
---
