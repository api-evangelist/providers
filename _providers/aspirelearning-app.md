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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ASPIRE app is a unique way to develop, digitalize and add dynamics to individual students or classrooms.
  name: Aspire Learning API
  slug: aspire-learning-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/aspirelearning-app/security/aspirelearning-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aspirelearning-app-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/aspirelearning-app/hosts/aspirelearning-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspirelearning-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aspirelearning-app/vendors/aspirelearning-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aspirelearning-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aspirelearning-app/security/aspirelearning-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aspirelearning-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aspirelearning-app/security/aspirelearning-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspirelearning-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aspirelearning.app/
- group: start
  title: ''
  type: Login
  url: https://aspirelearning.app/sign-in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aspirelearning.app/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aspirelearning.app/terms-and-conditions
- group: commercial
  title: ''
  type: Pricing
  url: https://aspirelearning.app/pricing
- group: operate
  title: ''
  type: Support
  url: https://aspirelearning.app/support
- group: company
  title: ''
  type: Blog
  url: https://aspirelearning.app/blog
coverage:
  checked: '2026-11-02'
  detail: Developer docs at https://api.aspirelearning.app/docs redirect to a sign‑in page, requiring authentication to view the API reference.
  evidence:
  - status: 307
    url: https://api.aspirelearning.app/docs
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Aspire Learning is a SaaS platform that provides personalized, affordable digital learning experiences for students and classrooms. Leveraging technology, community, and traditional education, Aspire aims to increase social mobility through education by offering systematic, customizable courses and tools for both individual learners and institutions.
image: https://aspirelearning.app/images/home-og-image.png
layout: provider
modified: '2026-11-01'
name: Aspire Learning
nav: Providers
network: true
overview: 'Aspire Learning is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Learning, Software-as-a-Service, Platform, and Students.


  Aspire Learning''s developer surface includes pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 10
scopes:
- name: Aspirelearning App Scopes
  scope_count: 0
  slug: aspirelearning-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 19.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aspirelearning App Authentication
  slug: aspirelearning-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aspirelearning App Domain Security
  slug: aspirelearning-app-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aspirelearning App Vulnerability Disclosure
  slug: aspirelearning-app-vulnerability-disclosure
  summary_line: no policy recorded
slug: aspirelearning-app
tags:
- Education
- Learning
- Software-as-a-Service
- Platform
- Students
website: https://aspirelearning.app/
---
