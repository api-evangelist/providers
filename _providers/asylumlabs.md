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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asylumlabs/refs/heads/main/hosts/asylumlabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asylumlabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asylumlabs/refs/heads/main/vendors/asylumlabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asylumlabs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asylumlabs/refs/heads/main/security/asylumlabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asylumlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/asylumlabs
created: '2026-09-26'
description: Asylumlabs is a nascent technology company focused on developing advanced AI-driven laboratory automation solutions. The firm aims to streamline scientific workflows by integrating robotics, machine learning, and cloud-based data management, targeting biotech and pharmaceutical research labs. While still early in its market presence, Asylumlabs positions itself as an innovator in the emerging field of autonomous lab instrumentation, seeking partnerships and pilot programs with research institutions.
layout: provider
modified: '2026-09-26'
name: Asylumlabs
nav: Providers
network: true
overview: Asylumlabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Laboratory Automation, Biotechnology, and Robotics.
random_paper: 7
score:
  band: minimal
  composite: 2.9
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
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asylumlabs Domain Security
  slug: asylumlabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asylumlabs
tags:
- Company
- Artificial Intelligence
- Laboratory Automation
- Biotechnology
- Robotics
website: https://equityzen.com/company/asylumlabs
---
