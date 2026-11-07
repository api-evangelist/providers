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
- description: API for device status, control, and integration with third‑party services.
  name: VeSync API
  slug: vesync-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/vesync/hosts/vesync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vesync-hosts.yml
- group: other
  href: https://artifacts.apis.io/vesync/vendors/vesync-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vesync-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vesync.com/legal/terms-of-use-jp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vesync.com/legal/privacy?protocol_id=1
- group: company
  title: ''
  type: Newsroom
  url: https://www.vesync.com/news/press
- group: other
  title: ''
  type: Leadership
  url: https://www.vesync.com/career-list/category/Leadership
- group: auth
  href: https://artifacts.apis.io/vesync/security/vesync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vesync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vesync.com/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host (api.vesync.com) despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.vesync.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: VeSync provides smart home devices and a cloud‑based platform that lets users control appliances such as air purifiers, humidifiers, robot vacuums, and lighting through mobile apps and voice assistants. The company offers an API for device status, control, and integration with third‑party services, supporting OAuth‑like authentication and real‑time updates. VeSync’s ecosystem focuses on energy‑efficient, Wi‑Fi‑enabled products aimed at improving indoor air quality and convenience for consumers.
image: http://static1.squarespace.com/static/5f7e35a4361a901ec00de453/t/602da53eaeb40c6f3fbe4f1a/1613604164770/vesync-logo-header.png?format=1500w
layout: provider
modified: '2026-10-26'
name: VeSync
nav: Providers
network: true
overview: VeSync is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, IoT, Consumer Electronics, and Cloud Platform.
random_paper: 16
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vesync/vesync-2026-11-03T145750.png
security:
- kind: domain-security
  name: Vesync Domain Security
  slug: vesync-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vesync
tags:
- Company
- Smart Home
- IoT
- Consumer Electronics
- Cloud Platform
website: https://www.vesync.com/
---
