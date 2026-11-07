---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 1
apis:
- description: Donelane provides an async standup service accessible via email. The API documentation is presented as HTML pages without a machine‑readable contract.
  name: Donelane API
  slug: donelane-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/donelane-app/plans/donelane-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/donelane-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/donelane-app/changelog/donelane-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/donelane-app-changelog.yml
- group: agent
  href: https://artifacts.apis.io/donelane-app/well-known/donelane-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donelane-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/donelane-app/hosts/donelane-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donelane-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/donelane-app/vendors/donelane-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donelane-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://donelane.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://donelane.app/privacy
- group: start
  title: ''
  type: Login
  url: https://donelane.app/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://donelane.app/changelog
- group: auth
  href: https://artifacts.apis.io/donelane-app/security/donelane-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donelane-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donelane.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://donelane.app/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://donelane.app/about
coverage:
  checked: '2026-11-06'
  detail: The provider's documentation is HTML pages rendered by JavaScript with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://donelane.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Donelane is an async standup tool that lets your team answer daily standup questions via email. It aims to simplify remote team coordination by delivering prompts and collecting responses without requiring a dedicated UI. The service is built to be lightweight, privacy‑focused, and integrates with email workflows, making it easy to adopt for distributed teams seeking efficient status updates without the overhead of traditional standup meetings.
image: https://donelane.app/assets/images/og-image-7hcNxkM.png
layout: provider
modified: '2026-11-05'
name: Donelane
nav: Providers
network: true
overview: 'Donelane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Async, Standup, Email, Remote Work, and Productivity.


  Donelane''s developer surface includes changelog, pricing, getting-started guide, and 10 more developer resources.'
plans:
- name: Donelane App Plans Pricing
  plan_count: 2
  slug: donelane-app-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donelane App Domain Security
  slug: donelane-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: donelane-app
tags:
- Async
- Standup
- Email
- Remote Work
- Productivity
website: https://donelane.app/
---
