---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: FreeToken.link provides an API for discovering free-access LLM models and related metadata. Documentation is available at the guides page, but no machine‑readable contract (OpenAPI, GraphQL, AsyncAPI,
  name: FreeToken API
  slug: freetoken-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/freetoken-link/plans/freetoken-link-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/freetoken-link-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/freetoken-link/hosts/freetoken-link-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freetoken-link-hosts.yml
- group: other
  href: https://artifacts.apis.io/freetoken-link/vendors/freetoken-link-vendors.yml
  title: ''
  type: Vendors
  url: vendors/freetoken-link-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://freetoken.link/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://freetoken.link/status
- group: auth
  title: ''
  type: Security
  url: https://freetoken.link/security
- group: start
  title: ''
  type: Sandbox
  url: https://freetoken.link/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freetoken.link/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://freetoken.link/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://freetoken.link/changelog
- group: auth
  href: https://artifacts.apis.io/freetoken-link/security/freetoken-link-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freetoken-link-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freetoken.link/
- group: docs
  title: ''
  type: Documentation
  url: https://freetoken.link/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://freetoken.link/get-key
- group: company
  title: ''
  type: Blog
  url: https://freetoken.link/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://freetoken.link/pricing
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://freetoken.link/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: FreeToken.link provides a platform for discovering and testing free-access Large Language Model (LLM) APIs. It aggregates model information, key testing guides, and tool setup instructions across multiple providers such as NVIDIA, Google Gemini, Groq, and SiliconFlow. Users can compare models, obtain API keys, and run browser‑direct requests to evaluate free‑tier limits and compliance. The site also offers documentation, pricing details, and a community‑driven watchlist for monitoring changes in model availability and access policies.
image: https://freetoken.link/og-card.png
layout: provider
modified: '2026-10-30'
name: freetoken-link
nav: Providers
network: true
overview: 'freetoken-link is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Free, Platform, and Discovery.


  freetoken-link''s developer surface includes sandbox, changelog, documentation, getting-started guide, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Freetoken Link Plans Pricing
  plan_count: 9
  slug: freetoken-link-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 58.0
    operational_transparency: 21.1
  previous_composite: 29.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/freetoken-link/freetoken-link-2026-11-03T132334.png
security:
- kind: domain-security
  name: Freetoken Link Domain Security
  slug: freetoken-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freetoken-link
tags:
- Artificial Intelligence
- LLM
- Free
- Platform
- Discovery
website: https://freetoken.link/
---
