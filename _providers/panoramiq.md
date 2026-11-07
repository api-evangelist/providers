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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/panoramiq/hosts/panoramiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/panoramiq-hosts.yml
- group: auth
  href: https://artifacts.apis.io/panoramiq/security/panoramiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/panoramiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://panoramiq.com/
created: '2026-10-26'
description: Panoramiq Insights provides analytics and insights tools for Instagram and social media platforms, helping businesses track engagement, audience demographics, and performance metrics. The company offers a dashboard and API to integrate social data into marketing workflows, aiming to simplify data-driven decisions for brands and agencies.
layout: provider
modified: '2026-10-26'
name: Panoramiq Insights
nav: Providers
network: true
overview: Panoramiq Insights is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
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
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/panoramiq/panoramiq-2026-11-03T140915.png
security:
- kind: domain-security
  name: Panoramiq Domain Security
  slug: panoramiq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: panoramiq
tags:
- Company
website: https://panoramiq.com/
---
