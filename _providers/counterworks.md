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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/counterworks/refs/heads/main/hosts/counterworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/counterworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/counterworks/refs/heads/main/vendors/counterworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/counterworks-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/counterworks/refs/heads/main/security/counterworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/counterworks-domain-security.yml
created: '2026-10-11'
description: Counterworks is a technology company focused on providing advanced data integration and workflow automation solutions for enterprises. The firm offers a suite of APIs that enable developers to programmatically access its platform for tasks such as data ingestion, transformation, and real‑time event handling. While detailed public documentation is limited, Counterworks positions itself as a B2B SaaS provider aiming to streamline complex data pipelines and improve operational efficiency across various industry verticals.
layout: provider
modified: '2026-10-11'
name: Counterworks
nav: Providers
network: true
overview: Counterworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Automation, Software-as-a-Service, and Enterprise.
random_paper: 14
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Counterworks Domain Security
  slug: counterworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: counterworks
tags:
- Company
- Data Integration
- Automation
- Software-as-a-Service
- Enterprise
---
