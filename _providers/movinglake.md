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
  href: https://artifacts.apis.io/movinglake/hosts/movinglake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/movinglake-hosts.yml
- group: other
  href: https://artifacts.apis.io/movinglake/vendors/movinglake-vendors.yml
  title: ''
  type: Vendors
  url: vendors/movinglake-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: http://movinglake.com/terms-and-conditions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MovingLake
- group: auth
  href: https://artifacts.apis.io/movinglake/security/movinglake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/movinglake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://movinglake.com/
coverage:
  checked: '2026-10-21'
  detail: MovingLake provides no public developer documentation or API specification.
  evidence:
  - status: 200
    url: https://movinglake.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: MovingLake provides real-time API integration solutions for enterprises, connecting ERP, CRM, PMS, and RMS systems to databases, data warehouses, and message queues. Their platform enables seamless data sync across SaaS applications, supporting e-commerce, hospitality, telecommunications, and property management use cases. With a focus on low-latency, scalable connectors, MovingLake helps businesses automate data flows and build unified data pipelines for analytics and operational efficiency.
image: http://movinglake.com/img/logo_256x256.png
layout: provider
modified: '2026-10-21'
name: MovingLake
nav: Providers
network: true
overview: MovingLake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Integration, Real-Time Data, ETL, Enterprise, and E-Commerce.
random_paper: 13
score:
  band: minimal
  composite: 5.8
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
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Movinglake Domain Security
  slug: movinglake-domain-security
  summary_line: TLSv1.3 · DMARC
slug: movinglake
tags:
- API Integration
- Real-Time Data
- ETL
- Enterprise
- E-Commerce
- Hospitality
- Telecommunications
- Data Sync
website: https://movinglake.com/
---
