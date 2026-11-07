---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Try Cold Call Coach for free. 30 minutes of free practice calls with AI prospects.
  name: Cold Call Coach API
  slug: cold-call-coach-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/coldcall-coach/plans/coldcall-coach-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coldcall-coach-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coldcall-coach/changelog/coldcall-coach-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coldcall-coach-changelog.yml
- group: agent
  href: https://artifacts.apis.io/coldcall-coach/llms/coldcall-coach-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coldcall-coach-llms.txt
- group: other
  href: https://artifacts.apis.io/coldcall-coach/hosts/coldcall-coach-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coldcall-coach-hosts.yml
- group: other
  href: https://artifacts.apis.io/coldcall-coach/vendors/coldcall-coach-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coldcall-coach-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coldcall.coach/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coldcall.coach/privacy
- group: start
  title: ''
  type: Login
  url: https://coldcall.coach/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://coldcall.coach/changelog
- group: company
  title: ''
  type: Blog
  url: https://coldcall.coach/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://coldcall.coach/use-cases/onboarding
- group: auth
  href: https://artifacts.apis.io/coldcall-coach/security/coldcall-coach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coldcall-coach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coldcall.coach/
- group: commercial
  title: ''
  type: Pricing
  url: https://coldcall.coach/pricing
- group: operate
  title: ''
  type: Contact
  url: https://coldcall.coach/contact
created: '2026-11-04'
description: Cold Call Coach provides AI-powered sales roleplay and coaching platform that helps salespeople build phone confidence through realistic practice calls, automatic grading, and measurable results. The service offers scalable training, custom scorecards, and tools to ramp new hires and protect pipelines.
image: https://coldcall.coach/images/og-image.png
layout: provider
modified: '2026-11-04'
name: Cold Call Coach
nav: Providers
network: true
overview: 'Cold Call Coach is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, Coaching, Roleplay, and Training.


  Cold Call Coach''s developer surface includes changelog, engineering blog, getting-started guide, pricing, and 11 more developer resources.'
plans:
- name: Coldcall Coach Plans Pricing
  plan_count: 1
  slug: coldcall-coach-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coldcall Coach Domain Security
  slug: coldcall-coach-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coldcall-coach
tags:
- Artificial Intelligence
- Sales
- Coaching
- Roleplay
- Training
- Company
website: https://coldcall.coach/
---
