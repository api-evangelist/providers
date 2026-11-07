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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Profitpather provides AI‑powered analytics for Shopify stores, accessible via a developer portal.
  name: Profitpather API
  slug: profitpather-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/profitpather-com/plans/profitpather-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/profitpather-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/profitpather-com/security/profitpather-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/profitpather-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/profitpather-com/llms/profitpather-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/profitpather-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/profitpather-com/well-known/profitpather-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/profitpather-com-security.txt
- group: agent
  href: https://artifacts.apis.io/profitpather-com/well-known/profitpather-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/profitpather-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/profitpather-com/hosts/profitpather-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/profitpather-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/profitpather-com/vendors/profitpather-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/profitpather-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/profitpather-com/security/profitpather-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/profitpather-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/profitpather-com/security/profitpather-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/profitpather-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profitpather.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://profitpather.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://profitpather.com/login
coverage:
  checked: '2026-10-29'
  detail: Docs pages are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://profitpather.com/login
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Profitpather provides AI‑powered analytics for Shopify stores, turning e‑commerce data into real‑time insights that can be queried by large language models like Claude and Codex. By installing a simple pixel, merchants gain unsampled, privacy‑first event tracking, customizable dashboards, and the ability to ask natural‑language questions about sales, traffic, and customer behavior. The platform offers a free tier with basic tools and a paid Pro plan with full history, unlimited tool access, and integration across multiple AI assistants.
image: https://profitpather.com/icon.png
layout: provider
modified: '2026-10-29'
name: profitpather-com
nav: Providers
network: true
overview: 'profitpather-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Shopify, and E-Commerce.


  profitpather-com''s developer surface includes pricing, signup flow, and 10 more developer resources.'
plans:
- name: Profitpather Com Plans Pricing
  plan_count: 2
  slug: profitpather-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/profitpather-com/profitpather-com-2026-11-03T141530.png
security:
- kind: domain-security
  name: Profitpather Com Domain Security
  slug: profitpather-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Profitpather Com Vulnerability Disclosure
  slug: profitpather-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: profitpather-com
tags:
- Company
- Artificial Intelligence
- Analytics
- Shopify
- E-Commerce
website: https://profitpather.com/
---
