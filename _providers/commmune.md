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
  href: https://raw.githubusercontent.com/api-evangelist/commmune/refs/heads/main/hosts/commmune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commmune-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commmune/refs/heads/main/vendors/commmune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commmune-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commmune/refs/heads/main/security/commmune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commmune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/commmune
coverage:
  checked: '2026-10-09'
  detail: The provider's website https://www.commune.us returns HTML with no discoverable machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.commune.us
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Commmune (styled as Commune) provides a cloud‑based community marketing platform that enables brands to build and nurture customer advocacy through AI‑driven personalization, gamified rewards, and analytics dashboards. The SaaS solution helps reduce churn, lower acquisition costs, and increase lifetime value by turning loyal customers into brand advocates. Founded in 2018 and based in Tokyo, Japan, Commune serves enterprises across retail, healthcare, and government sectors.
layout: provider
modified: '2026-10-09'
name: Commmune
nav: Providers
network: true
overview: Commmune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Commmune Domain Security
  slug: commmune-domain-security
  summary_line: TLSv1.3 · DMARC
slug: commmune
tags:
- Company
website: https://equityzen.com/company/commmune
---
