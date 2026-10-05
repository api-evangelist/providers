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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-data-storage/refs/heads/main/hosts/atlas-data-storage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-data-storage-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-data-storage/refs/heads/main/vendors/atlas-data-storage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-data-storage-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-data-storage/refs/heads/main/security/atlas-data-storage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-data-storage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlasbase.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atlasbase.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlasbase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlasbase.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.atlasbase.com/contact
coverage:
  checked: 2026-09-26
  detail: OpenAPI spec not found at common endpoints on api.atlasbase.com
  evidence:
  - status: 0
    url: https://api.atlasbase.com/openapi.json
  - status: 0
    url: https://api.atlasbase.com/openapi.yaml
  - status: 0
    url: https://api.atlasbase.com/swagger.json
  - status: 0
    url: https://api.atlasbase.com/v1/openapi.json
  - status: 0
    url: https://api.atlasbase.com/api-docs
  - status: 0
    url: https://api.atlasbase.com/docs
  - status: 200
    url: https://www.atlasbase.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atlas Data Storage provides secure, scalable cloud storage solutions for enterprises, enabling efficient data management, backup, and disaster recovery. The company offers APIs for data ingestion, retrieval, and lifecycle management, supporting compliance and high availability across multiple regions. As a participant in the secondary market ecosystem, Atlas Data Storage connects investors and stakeholders with data-driven insights and services.
image: https://www.atlasbase.com/open-graph.jpg
layout: provider
modified: '2026-09-26'
name: Atlas Data Storage
nav: Providers
network: true
overview: 'Atlas Data Storage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Storage, Enterprise, and Data Management.


  Atlas Data Storage''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlas Data Storage Domain Security
  slug: atlas-data-storage-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atlas-data-storage
tags:
- Cloud
- Storage
- Enterprise
- Data Management
website: https://www.atlasbase.com/
---
