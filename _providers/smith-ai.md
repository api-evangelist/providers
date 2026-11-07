---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Smith.ai Outbound Call Request API lets you programmatically create outbound call requests via POST to https://app.smith.ai/api/vr/v1/outbound/.
  name: Outbound Call Request API
  slug: outbound-call-request-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/smith-ai/plans/smith-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smith-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smith-ai/changelog/smith-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/smith-ai-changelog.yml
- group: agent
  href: https://artifacts.apis.io/smith-ai/llms/smith-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smith-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/smith-ai/hosts/smith-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smith-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/smith-ai/vendors/smith-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smith-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://smith.ai/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.smith.ai/changelog/spring-2025-ai-receptionist-recap-new-features-integrations-smarter-ai
- group: auth
  href: https://artifacts.apis.io/smith-ai/security/smith-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smith-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smith.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.smith.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.smith.ai/category/ydtshfm8im-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.smith.ai/article/ikzvnbatop-how-to-set-up-outbound-calling
- group: operate
  title: ''
  type: Support
  url: https://docs.smith.ai/
- group: company
  title: ''
  type: Blog
  url: https://smith.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://smith.ai/pricing/ai-receptionist
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smith.ai/receptionists/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smith.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.smith.ai/va/get-started/signup
coverage:
  checked: '2026-10-29'
  detail: API requires an active Smith.ai plan and API key, restricting access to paying customers.
  evidence:
  - status: 200
    url: https://docs.smith.ai/article/7p93p6osc0-using-the-outbound-call-request-api
  reason: sales-gate
  state: gated
created: '2026-10-28'
description: Smith.ai offers AI agents and 500+ live North American receptionists to answer calls, qualify leads, book appointments, and update your CRM — 24/7, for law firms, home services, healthcare, and other small businesses. Handles 400,000+ calls per month across 5,000+ clients since 2015. Setup in minutes.
image: https://cdn.prod.website-files.com/5b15ca3d02dd414c89ecc3ed/69cc13455478ed77ea0f70a3_Social%20share%20-%201200x630.png
layout: provider
modified: '2026-10-28'
name: Smith.ai
nav: Providers
network: true
overview: 'Smith.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Receptionist, Call Answering, and Scheduling.


  Smith.ai''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Smith Ai Plans Pricing
  plan_count: 7
  slug: smith-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Smith Ai Rate Limits
  slug: smith-ai-rate-limits
scopes:
- name: Smith Ai Scopes
  scope_count: 0
  slug: smith-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 74.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/smith-ai/smith-ai-2026-11-03T143349.png
security:
- kind: authentication
  name: Smith Ai Authentication
  slug: smith-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Smith Ai Domain Security
  slug: smith-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smith-ai
tags:
- Company
- Artificial Intelligence
- Receptionist
- Call Answering
- Scheduling
- Small Business
website: https://smith.ai/
---
