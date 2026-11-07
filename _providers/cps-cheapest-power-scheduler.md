---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Advisory scheduler intelligence for AI training and batch workloads, providing endpoints to register sites, submit jobs, and retrieve cheapest power scheduling decisions.
  name: CPS API
  slug: cps-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cps-cheapest-power-scheduler/hosts/cps-cheapest-power-scheduler-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cps-cheapest-power-scheduler-hosts.yml
- group: other
  href: https://artifacts.apis.io/cps-cheapest-power-scheduler/vendors/cps-cheapest-power-scheduler-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cps-cheapest-power-scheduler-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cps-cheapest-power-scheduler/security/cps-cheapest-power-scheduler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cps-cheapest-power-scheduler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cps.sedra-0b3.workers.dev
- group: docs
  title: ''
  type: Documentation
  url: https://cps.sedra-0b3.workers.dev/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cps.sedra-0b3.workers.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cps.sedra-0b3.workers.dev/privacy
created: '2026-10-14'
description: CPS (Cheapest-Power Scheduler) provides a cloud-based platform that enables users to schedule and optimize power usage for compute workloads. By integrating with major cloud providers, CPS offers cost-effective power allocation, real-time monitoring, and automated scaling to reduce electricity expenses while maintaining performance. The service includes a dashboard, API access, and billing options for pilot and production use.
layout: provider
modified: '2026-10-14'
name: CPS (Cheapest-Power Scheduler)
nav: Providers
network: true
overview: 'CPS (Cheapest-Power Scheduler) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Cloud, Scheduling, and Optimization.


  CPS (Cheapest-Power Scheduler)''s developer surface includes documentation and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 12.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cps-cheapest-power-scheduler/cps-cheapest-power-scheduler-2026-11-03T125516.png
security:
- kind: domain-security
  name: Cps Cheapest Power Scheduler Domain Security
  slug: cps-cheapest-power-scheduler-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cps-cheapest-power-scheduler
tags:
- Company
- Energy
- Cloud
- Scheduling
- Optimization
website: https://cps.sedra-0b3.workers.dev
---
