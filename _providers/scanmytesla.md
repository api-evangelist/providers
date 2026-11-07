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
- description: Provides access to vehicle diagnostics and OTA updates as described on the developer docs.
  name: Scan My Tesla API
  slug: scan-my-tesla-api
artifact_total: 2
common:
- group: build
  href: https://artifacts.apis.io/scanmytesla/packages/scanmytesla-packages.yml
  title: ''
  type: SDKs
  url: packages/scanmytesla-packages.yml
- group: build
  href: https://artifacts.apis.io/scanmytesla/packages/scanmytesla-packages.yml
  title: ''
  type: Packages
  url: packages/scanmytesla-packages.yml
- group: operate
  href: https://artifacts.apis.io/scanmytesla/changelog/scanmytesla-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scanmytesla-changelog.yml
- group: other
  href: https://artifacts.apis.io/scanmytesla/hosts/scanmytesla-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scanmytesla-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scanmytesla.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.scanmytesla.com/changelog
- group: auth
  href: https://artifacts.apis.io/scanmytesla/security/scanmytesla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scanmytesla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scanmytesla.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and cannot be parsed for machine‑readable specs.
  evidence:
  - status: 200
    url: https://www.scanmytesla.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Scan My Tesla provides a platform for owners of Tesla vehicles to remotely access diagnostic data, perform over‑the‑air updates, and retrieve detailed vehicle health reports. The service aggregates telemetry, offers alerts for maintenance, and integrates with third‑party tools for fleet management and analytics, enabling owners and service providers to monitor battery health, range, and performance in real time.
image: https://lh7-us.googleusercontent.com/sitesv-images-rt/AMxu72u4fxN13ZFPQntQd0mCSbfU5c52uUmzxPujWngA9_iVs-2tKgrWI2opdrfBRkUnWDrB6UJ45GbDUKB3j2t88_woxAkWE7aANAtK4Y5raui1gTJEwImCeF9TAXawLkYn7ujXOGZdxYf-t6KA-zFmPx1UgmFvbA=w16383
layout: provider
modified: '2026-10-28'
name: Scan My Tesla
nav: Providers
network: true
overview: 'Scan My Tesla is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Telemetry, Diagnostics, and Fleet Management.


  Scan My Tesla''s developer surface includes changelog and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scanmytesla/scanmytesla-2026-11-03T142757.png
security:
- kind: domain-security
  name: Scanmytesla Domain Security
  slug: scanmytesla-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: scanmytesla
tags:
- Company
- Automotive
- Telemetry
- Diagnostics
- Fleet Management
- Tesla
website: https://scanmytesla.com/
---
