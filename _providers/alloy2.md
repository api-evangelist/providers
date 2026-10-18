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
  href: https://raw.githubusercontent.com/api-evangelist/alloy2/refs/heads/main/hosts/alloy2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alloy2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alloy2/refs/heads/main/vendors/alloy2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alloy2-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alloy2/refs/heads/main/security/alloy2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alloy2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/alloy2
created: '2026-09-24'
description: Alloy2 is a technology company focused on providing advanced data integration and API management solutions for enterprises. The company aims to simplify complex data workflows by offering a unified platform that connects disparate systems, automates processes, and delivers real-time insights. Alloy2’s platform includes API gateways, data transformation tools, monitoring dashboards, and security controls that help organizations accelerate digital transformation. While public information is limited, Alloy2 positions itself as a strategic partner for businesses seeking to improve operational efficiency through robust API services and integration capabilities. The company emphasizes scalability, low latency, and compliance with industry standards, targeting large enterprises and fintech firms.
layout: provider
modified: '2026-09-24'
name: Alloy2
nav: Providers
network: true
overview: Alloy2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Data, Platform, and Enterprise.
random_paper: 1
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
  delta: 1.9
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
  previous_composite: 1.2
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
  name: Alloy2 Domain Security
  slug: alloy2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alloy2
tags:
- Company
- Integration
- Data
- Platform
- Enterprise
website: https://equityzen.com/company/alloy2
---
