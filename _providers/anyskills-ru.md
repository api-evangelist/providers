---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AnySkills platform provides online school services, courses, student management, video hosting, and integration features.
  name: AnySkills API
  slug: anyskills-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/anyskills-ru/llms/anyskills-ru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anyskills-ru-llms.txt
- group: other
  href: https://artifacts.apis.io/anyskills-ru/hosts/anyskills-ru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyskills-ru-hosts.yml
- group: auth
  href: https://artifacts.apis.io/anyskills-ru/security/anyskills-ru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyskills-ru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anyskills.ru/
- group: start
  title: ''
  type: SignUp
  url: https://lk.anyskills.ru/signup/
- group: start
  title: ''
  type: Login
  url: https://lk.anyskills.ru/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://anyskills.ru/#pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lk.anyskills.ru/
coverage:
  checked: '2026-11-01'
  detail: AnySkills provides education services and does not expose a public API.
  evidence:
  - status: 200
    url: https://anyskills.ru/
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: AnySkills is a convenient platform for online schools, offering courses, students, video hosting with download protection, Telegram bots, and a unified dashboard. Schools can create courses, manage learners, set start dates, assign curators, and integrate payment processing without fees. The service provides a free tier with unlimited students and various paid plans with additional storage, video bandwidth, and CRM capabilities.
image: https://anyskills.ru/assets/og.png
layout: provider
modified: '2026-11-01'
name: AnySkills
nav: Providers
network: true
overview: 'AnySkills is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, E-Learning, Platform, Course Management, and Russian.


  AnySkills'' developer surface includes signup flow, pricing, and 6 more developer resources.'
plans:
- name: Anyskills Ru Plans Pricing
  plan_count: 0
  slug: anyskills-ru-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Anyskills Ru Rate Limits
  slug: anyskills-ru-rate-limits
scopes:
- name: Anyskills Ru Scopes
  scope_count: 0
  slug: anyskills-ru-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anyskills Ru Authentication
  slug: anyskills-ru-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anyskills Ru Domain Security
  slug: anyskills-ru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anyskills-ru
tags:
- Education
- E-Learning
- Platform
- Course Management
- Russian
website: https://anyskills.ru/
---
