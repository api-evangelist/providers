---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: One REST API to publish, comment, message, and read analytics on Instagram, Facebook, TikTok, YouTube, X, and Bluesky.
  name: Adeli API
  slug: adeli-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/tryadeli-com/plans/tryadeli-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tryadeli-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/tryadeli-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tryadeli-com/conventions/tryadeli-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tryadeli-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/tryadeli-com/conventions/tryadeli-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tryadeli-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tryadeli-com/authentication/tryadeli-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tryadeli-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tryadeli-com/errors/tryadeli-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tryadeli-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tryadeli-com/conformance/tryadeli-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tryadeli-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tryadeli-com/llms/tryadeli-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tryadeli-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tryadeli-com/hosts/tryadeli-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tryadeli-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tryadeli-com/vendors/tryadeli-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tryadeli-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tryadeli-com/security/tryadeli-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryadeli-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryadeli.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tryadeli.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tryadeli.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tryadeli.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.tryadeli.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryadeli.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tryadeli.com/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.tryadeli.com/openapi.json
  - status: null
    url: https://beta.tryadeli.com/openapi.json
  - status: 401
    url: https://app.tryadeli.com/mcp
  - status: 401
    url: https://beta.tryadeli.com/mcp
  - status: 200
    url: https://tryadeli.com
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Adeli provides a unified social media and advertising API that enables developers to publish, schedule, and analyze posts across major platforms such as Instagram, TikTok, YouTube, Facebook, X, and Bluesky. It offers multi‑network publishing, built‑in scheduling, and comprehensive analytics, with a free tier for small‑scale use and paid plans for larger volumes.
image: https://www.tryadeli.com/opengraph-image-12o0cb?8ab8a75afbf65db9
layout: provider
modified: '2026-10-28'
name: Adeli
nav: Providers
network: true
overview: 'Adeli is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Advertising, Marketing, and Automation.


  Adeli''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Tryadeli Com Plans Pricing
  plan_count: 3
  slug: tryadeli-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Tryadeli Com Rate Limits
  slug: tryadeli-com-rate-limits
scopes:
- name: Tryadeli Com Scopes
  scope_count: 0
  slug: tryadeli-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.8
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.5
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tryadeli-com/tryadeli-com-2026-11-03T145125.png
security:
- kind: authentication
  name: Tryadeli Com Authentication
  slug: tryadeli-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tryadeli Com Domain Security
  slug: tryadeli-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tryadeli-com
tags:
- Social Media
- Advertising
- Marketing
- Automation
website: https://tryadeli.com
---
