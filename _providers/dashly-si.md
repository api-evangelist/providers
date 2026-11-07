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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dashly.si/
- group: commercial
  href: https://artifacts.apis.io/dashly-si/plans/dashly-si-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dashly-si-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dashly-si/llms/dashly-si-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dashly-si-llms.txt
- group: agent
  href: https://artifacts.apis.io/dashly-si/well-known/dashly-si-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dashly-si-well-known.yml
- group: other
  href: https://artifacts.apis.io/dashly-si/hosts/dashly-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dashly-si-hosts.yml
- group: other
  href: https://artifacts.apis.io/dashly-si/vendors/dashly-si-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dashly-si-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://dashly.si/support
- group: start
  title: ''
  type: Login
  url: https://dashly.si/app/sign-in
- group: auth
  href: https://artifacts.apis.io/dashly-si/security/dashly-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dashly-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dashly.si/
- group: start
  title: ''
  type: GettingStarted
  url: https://dashly.si/install
- group: company
  title: ''
  type: Blog
  url: https://dashly.si/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dashly.si/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashly.si/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashly.si/privacy
coverage:
  checked: '2026-11-05'
  detail: Provider docs are served as JavaScript‑rendered pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://dashly.si/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Dashly is a lifestyle dashboard that lets users track habits, health metrics, finances, and tasks through AI assistants like ChatGPT and Claude. The platform offers free trials, subscription plans, and a visual tile‑based interface for personal goal‑setting and data review.
image: https://dashly.si/og/home.png
layout: provider
modified: '2026-11-04'
name: Dashly
nav: Providers
network: true
overview: 'Dashly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include habit-tracker, Lifestyle, Artificial Intelligence, Dashboards, and Subscription.


  Dashly''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Dashly Si Plans Pricing
  plan_count: 2
  slug: dashly-si-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dashly Si Domain Security
  slug: dashly-si-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dashly-si
tags:
- habit-tracker
- Lifestyle
- Artificial Intelligence
- Dashboards
- Subscription
- Company
website: https://dashly.si/
---
