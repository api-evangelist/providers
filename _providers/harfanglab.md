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
  href: https://artifacts.apis.io/harfanglab/hosts/harfanglab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/harfanglab-hosts.yml
- group: other
  href: https://artifacts.apis.io/harfanglab/vendors/harfanglab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/harfanglab-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HarfangLab
- group: auth
  href: https://artifacts.apis.io/harfanglab/security/harfanglab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harfanglab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://harfanglab.io/
created: '2026-10-29'
description: HarfangLab is a European cybersecurity company providing an open API‑ready platform for endpoint detection and response (EDR), endpoint protection (EPP), attack surface management, and AI‑driven threat investigation. The solution offers on‑premise, cloud, and hybrid deployments, emphasizing strategic autonomy, transparency, and compliance with regulations such as GDPR and NIS2. HarfangLab serves enterprises across multiple industries, delivering a lightweight agent, AI engines, and extensive integration capabilities.
layout: provider
modified: '2026-10-29'
name: HarfangLab
nav: Providers
network: true
overview: HarfangLab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, EDR, EPP, and Attack Surface Management.
random_paper: 22
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Harfanglab Domain Security
  slug: harfanglab-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: harfanglab
tags:
- Company
- Cybersecurity
- EDR
- EPP
- Attack Surface Management
- AI
website: https://harfanglab.io/
---
