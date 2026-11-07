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
- description: API for Rain financial health platform
  name: Rain API
  slug: rain-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/rainapp-com/llms/rainapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rainapp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/rainapp-com/hosts/rainapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rainapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rainapp-com/vendors/rainapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rainapp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rainapp.com/terms/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rainapp.com/terms/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.rainapp.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.rainapp.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rainapp.com/
- group: auth
  href: https://artifacts.apis.io/rainapp-com/security/rainapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rainapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rainapp.com
coverage:
  checked: '2026-10-29'
  detail: API documentation endpoint requires Basic authentication, blocking unauthenticated access.
  evidence:
  - status: 401
    url: https://docs.rainapp.com/api
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Rain is the leading all‑in‑one financial health platform that helps employees stabilize, control, and grow their finances. It offers AI‑driven skills, on‑demand pay, and a financial health agent to improve employee wellbeing and productivity.
image: https://cdn.prod.website-files.com/68b996281d0ebc23a4132352/6995cb2b2451fe567f5a6b7d_ae10ac2845cb1ca3efed61ac4fdc4b84_og_image.png
layout: provider
modified: '2026-10-28'
name: Rain
nav: Providers
network: true
overview: 'Rain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Health, Employee Benefits, Fintech, and Artificial Intelligence.


  Rain''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rainapp-com/rainapp-com-2026-11-03T141907.png
security:
- kind: domain-security
  name: Rainapp Com Domain Security
  slug: rainapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rainapp-com
tags:
- Company
- Financial Health
- Employee Benefits
- Fintech
- Artificial Intelligence
website: https://rainapp.com
---
