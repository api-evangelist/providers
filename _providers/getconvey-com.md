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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/getconvey-com/llms/getconvey-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getconvey-com-llms.txt
- group: other
  href: https://artifacts.apis.io/getconvey-com/hosts/getconvey-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getconvey-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getconvey-com/vendors/getconvey-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getconvey-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.project44.com/help-center/
- group: auth
  title: ''
  type: Security
  url: https://www.project44.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.project44.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.project44.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.project44.com/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.project44.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.getconvey.com/
- group: auth
  href: https://artifacts.apis.io/getconvey-com/security/getconvey-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getconvey-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getconvey.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://developer.getconvey.com/mcp
  - status: 403
    url: https://api.getconvey.com/mcp
  - status: 401
    url: https://app.getconvey.com/api/mcp
  - status: 200
    url: https://getconvey.com/
  reason: partner-login
  state: gated
created: '2026-10-24'
description: project44 provides a decision intelligence platform that connects shippers, logistics service providers and carriers to enable real‑time visibility, analytics and automated actions across the supply chain. Its solutions include carrier onboarding, transportation management, yard management, e‑commerce logistics and AI‑driven orchestration for tasks such as rating, booking and exception handling. The platform serves global enterprises in industries such as automotive, retail, manufacturing and food & beverage.
image: https://www.project44.com/wp-content/uploads/2024/05/Frame-8.png
layout: provider
modified: '2026-10-24'
name: Convey
nav: Providers
network: true
overview: 'Convey is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Decision Intelligence, Transportation Management, Visibility, and AI Orchestration.


  Convey''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.9
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
screenshot: https://apis.io/screenshots/getconvey-com/getconvey-com-2026-11-03T132708.png
security:
- kind: domain-security
  name: Getconvey Com Domain Security
  slug: getconvey-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: getconvey-com
tags:
- Supply Chain
- Decision Intelligence
- Transportation Management
- Visibility
- AI Orchestration
- Yard Management
- E-commerce Logistics
website: https://getconvey.com/
---
