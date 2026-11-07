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
- description: WebSynco provides a cloud‑based CMMS platform. Documentation is at the main site.
  name: WebSynco API
  slug: websynco-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/websynco/hosts/websynco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/websynco-hosts.yml
- group: auth
  href: https://artifacts.apis.io/websynco/security/websynco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/websynco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://websynco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://websynco.com/main-en.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://websynco.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://websynco.com/main-en.html
- group: operate
  title: ''
  type: Support
  url: https://websynco.com/
- group: company
  title: ''
  type: Blog
  url: https://websynco.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://websynco.com/
- group: start
  title: ''
  type: SignUp
  url: https://websynco.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://websynco.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://websynco.com/privacy
coverage:
  checked: '2026-10-19'
  detail: Main site returns HTML pages for spec URLs, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://websynco.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: EnerZam, a division of UctriX inc., delivers WebSynco, a modern, customizable, modular, cloud‑based Computerized Maintenance Management System (CMMS). Leveraging over 20 years of experience, the platform helps organizations improve asset performance through flexible, reliable, and secure software. WebSynco is ISO‑27001 certified, supports multiple languages, and offers mobile apps for iOS and Android, positioning it as a next‑generation solution for asset management and maintenance.
layout: provider
modified: '2026-10-19'
name: EnerZam
nav: Providers
network: true
overview: 'EnerZam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Asset Management, CMMS, Maintenance Software, and ISO 27001.


  EnerZam''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 21.7
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/websynco/websynco-2026-11-03T150100.png
security:
- kind: domain-security
  name: Websynco Domain Security
  slug: websynco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: websynco
tags:
- Company
- Asset Management
- CMMS
- Maintenance Software
- ISO 27001
website: https://websynco.com/
---
