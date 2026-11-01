---
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/otprun-com/plans/otprun-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/otprun-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/otprun-com/conventions/otprun-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/otprun-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/otprun-com/conventions/otprun-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/otprun-com-conventions.yml
- group: agent
  href: https://artifacts.apis.io/otprun-com/llms/otprun-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/otprun-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/otprun-com/well-known/otprun-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/otprun-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/otprun-com/hosts/otprun-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/otprun-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/otprun-com/vendors/otprun-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/otprun-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://otprun.com/status
- group: start
  title: ''
  type: Login
  url: https://otprun.com/app/login
- group: auth
  href: https://artifacts.apis.io/otprun-com/security/otprun-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/otprun-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otprun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://otprun.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://otprun.com/whatsapp-api
- group: start
  title: ''
  type: GettingStarted
  url: https://otprun.com/whatsapp-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://otprun.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://otprun.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://otprun.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://otprun.com/openapi.json
  - status: 401
    url: https://otprun.com/mcp
  - status: 200
    url: https://otprun.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: OTP Run provides a WhatsApp API service that lets businesses and developers send unlimited messages from their own phone number using AI assistants. The platform offers features like automated reminders, sign‑in codes, and AI‑driven conversations, all managed via a web dashboard without per‑message fees. It integrates with popular AI models such as ChatGPT and Claude, and includes pricing tiers, documentation, and a developer portal for easy integration.
image: https://otprun.com/og/home-en.jpg
layout: provider
modified: '2026-10-30'
name: otprun-com
nav: Providers
network: true
overview: 'otprun-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, WhatsApp, AI, and SaaS.


  otprun-com''s developer surface includes documentation, API reference, getting-started guide, pricing, and 13 more developer resources.'
plans:
- name: Otprun Com Plans Pricing
  plan_count: 4
  slug: otprun-com-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Otprun Com Domain Security
  slug: otprun-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: otprun-com
tags:
- Company
- Messaging
- WhatsApp
- AI
- SaaS
website: https://otprun.com/
---
