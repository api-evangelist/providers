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
api_count: 1
apis:
- description: API for Inside platform, documentation hosted at dashboard.inside.com
  name: Inside API
  slug: inside-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/inside/hosts/inside-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inside-hosts.yml
- group: other
  href: https://artifacts.apis.io/inside/vendors/inside-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inside-vendors.yml
- group: auth
  href: https://artifacts.apis.io/inside/security/inside-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inside-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inside.com/
coverage:
  checked: '2026-10-29'
  detail: Dashboard docs at https://dashboard.inside.com return HTML shells for OpenAPI endpoints, no machine-readable spec found.
  evidence:
  - status: 200
    url: https://dashboard.inside.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Inside is a technology company specializing in data integration and analytics platforms. Founded with backing from Sequoia Capital, Inside provides APIs that enable secure data ingestion, transformation, and real-time insights for enterprise applications. The platform supports a wide range of industries, offering robust documentation, developer tools, and scalable infrastructure to help businesses unlock the value of their data assets across cloud and on-premise environments.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/f5cac1a2-9bde-48e3-8f6f-c3e192e701c7/id-preview-a51d44ad--32b702ad-2f0a-4460-acd2-2c0b77d63759.lovable.app-1781215722361.png
layout: provider
modified: '2026-10-29'
name: Inside
nav: Providers
network: true
overview: Inside is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Analytics, and Enterprise.
random_paper: 12
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.3
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/inside/inside-2026-11-03T133826.png
security:
- kind: domain-security
  name: Inside Domain Security
  slug: inside-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inside
tags:
- Company
- Data Integration
- Analytics
- Enterprise
website: https://inside.com/
---
