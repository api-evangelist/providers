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
- description: Wialon provides a RESTful API for fleet management, telemetry and asset tracking as documented in the developer portal.
  name: Wialon API
  slug: wialon-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/wialon/llms/wialon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wialon-llms.txt
- group: other
  href: https://artifacts.apis.io/wialon/hosts/wialon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wialon-hosts.yml
- group: build
  href: https://artifacts.apis.io/wialon/packages/wialon-packages.yml
  title: ''
  type: SDKs
  url: packages/wialon-packages.yml
- group: build
  href: https://artifacts.apis.io/wialon/packages/wialon-packages.yml
  title: ''
  type: Packages
  url: packages/wialon-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://wialon.com/en/security
- group: auth
  href: https://artifacts.apis.io/wialon/security/wialon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wialon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wialon.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.wialon.com/en/api
- group: docs
  title: ''
  type: APIReference
  url: https://help.wialon.com/en/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wialon.com/en/soft-developers
- group: commercial
  title: ''
  type: Pricing
  url: https://wialon.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.wialon.com/
- group: company
  title: ''
  type: Blog
  url: https://wialon.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://help.wialon.com/
coverage:
  checked: '2026-10-14'
  detail: API documentation page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://help.wialon.com/en/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Wialon provides a comprehensive fleet management and digitalization platform, offering GPS tracking, asset monitoring, and telematics integration for vehicles, equipment, and personnel. Their services include a robust API and SDKs for developers to build custom solutions, a marketplace of integrations, and tools for analytics, routing, and compliance. The company serves logistics, transportation, agriculture, and public sector customers worldwide.
layout: provider
modified: '2026-10-13'
name: Wialon
nav: Providers
network: true
overview: 'Wialon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Telematics, and GPS Tracking.


  Wialon''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, support, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 5.3
  previous_composite: 18.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wialon/wialon-2026-11-03T150156.png
security:
- kind: domain-security
  name: Wialon Domain Security
  slug: wialon-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: wialon
tags:
- Company
- Fleet Management
- Telematics
- GPS Tracking
website: https://wialon.com
---
