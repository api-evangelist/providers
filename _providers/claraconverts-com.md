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
- description: AI-powered virtual employee API for website visitor engagement, lead capture, appointment booking, and e‑commerce conversion.
  name: ClaraConverts API
  slug: claraconverts-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/claraconverts-com/plans/claraconverts-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claraconverts-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/claraconverts-com/llms/claraconverts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claraconverts-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claraconverts-com/well-known/claraconverts-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claraconverts-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claraconverts-com/hosts/claraconverts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claraconverts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claraconverts-com/vendors/claraconverts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claraconverts-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://claraconverts.com/login
- group: auth
  href: https://artifacts.apis.io/claraconverts-com/security/claraconverts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claraconverts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claraconverts.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://claraconverts.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claraconverts.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claraconverts.com/privacy
created: '2026-11-03'
description: ClaraConverts provides an AI-powered virtual employee that engages website visitors in real-time chat and voice, capturing leads, booking appointments, handling service requests, and driving e‑commerce conversions. It integrates with major CRMs, calendars, and shopping platforms, offering a one‑line install for WordPress, Webflow, Squarespace and more, with plans for agencies, multi‑site businesses, and enterprises.
image: https://claraconverts.com/static/og-default.png
layout: provider
modified: '2026-11-03'
name: ClaraConverts
nav: Providers
network: true
overview: 'ClaraConverts is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Chatbot, Lead Capture, Appointment Booking, Ecommerce Checkout, and CRM Integration.


  ClaraConverts'' developer surface includes pricing and 10 more developer resources.'
plans:
- name: Claraconverts Com Plans Pricing
  plan_count: 3
  slug: claraconverts-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claraconverts Com Domain Security
  slug: claraconverts-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: claraconverts-com
tags:
- AI Chatbot
- Lead Capture
- Appointment Booking
- Ecommerce Checkout
- CRM Integration
- Web agency tools
website: https://claraconverts.com/
---
