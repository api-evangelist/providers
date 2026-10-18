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
api_count: 1
apis:
- description: BuildOS developer API documentation
  name: BuildOS API
  slug: buildos-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/buildos/refs/heads/main/plans/buildos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildos-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buildos/refs/heads/main/hosts/buildos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildos-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thebuildos.net/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildos/refs/heads/main/security/buildos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thebuildos.net
coverage:
  checked: '2026-10-06'
  detail: Developer pages return HTML shells with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.thebuildos.net/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Buildos provides construction project management software that centralizes bills of quantities, cost plans, site progress, inventory, and workforce management in a single web and Android platform. It enables contractors and quantity surveyors to streamline project data, reduce duplicate work, and improve budgeting and reporting across the entire construction lifecycle.
image: https://www.thebuildos.net/og-image.png
layout: provider
modified: '2026-10-06'
name: Buildos
nav: Providers
network: true
overview: 'Buildos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Project Management, Software, Software-as-a-Service, and BuildOS.


  Buildos'' developer surface includes pricing and 4 more developer resources.'
plans:
- name: Buildos Plans Pricing
  plan_count: 16
  slug: buildos-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Buildos Domain Security
  slug: buildos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buildos
tags:
- Construction
- Project Management
- Software
- Software-as-a-Service
- BuildOS
website: https://www.thebuildos.net
---
