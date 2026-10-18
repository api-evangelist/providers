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
  href: https://raw.githubusercontent.com/api-evangelist/alephlabs/refs/heads/main/hosts/alephlabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alephlabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alephlabs/refs/heads/main/vendors/alephlabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alephlabs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alephlabs/refs/heads/main/security/alephlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alephlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alephlabs.net
coverage:
  checked: '2026-10-05'
  detail: The site provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://alephlabs.net
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Aleph Labs is a software company focused on building intentional, high‑quality applications and developer tools. It offers a platform for creating, deploying, and managing modern software solutions, emphasizing security, scalability, and developer experience. The company showcases its products and APIs through a clean, modern website and provides documentation for developers to integrate its services.
layout: provider
modified: '2026-09-24'
name: Alephlabs
nav: Providers
network: true
overview: Alephlabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Developer Tools, and Platform.
random_paper: 16
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alephlabs Domain Security
  slug: alephlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alephlabs
tags:
- Company
- Software
- Developer Tools
- Platform
website: https://alephlabs.net
---
