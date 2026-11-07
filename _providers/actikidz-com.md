---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dynamic_client_registration: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for scheduling, payment, and notification management for children activities.
  name: ActiKidz API
  slug: actikidz-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://actikidz.com/security
- group: agent
  href: https://artifacts.apis.io/actikidz-com/llms/actikidz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actikidz-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/actikidz-com/well-known/actikidz-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/actikidz-com-security.txt
- group: agent
  href: https://artifacts.apis.io/actikidz-com/well-known/actikidz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actikidz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/actikidz-com/hosts/actikidz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actikidz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/actikidz-com/vendors/actikidz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actikidz-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://actikidz.com/security
- group: other
  title: ''
  type: Leadership
  url: https://actikidz.com/category/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://actikidz.com/changelog
- group: auth
  href: https://artifacts.apis.io/actikidz-com/security/actikidz-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/actikidz-com-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://actikidz.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://actikidz.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://actikidz.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://actikidz.com/support
- group: company
  title: ''
  type: Blog
  url: https://actikidz.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://actikidz.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actikidz.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actikidz.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://actikidz.com/postman
- group: auth
  href: https://artifacts.apis.io/actikidz-com/security/actikidz-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/actikidz-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/actikidz-com/security/actikidz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actikidz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actikidz.com/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages return HTML shells with no machine-readable spec.
  evidence:
  - status: 200
    url: https://actikidz.com/openapi.json
  - status: 200
    url: https://actikidz.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: ActiKidz is a North American platform that lets parents search for children’s courses and activities across multiple cities. It also provides private teachers and educational institutions with scheduling, payment, and notification management tools. The service covers swimming, piano, coding, art, fitness and more, offering clear details on time, location, and price without requiring registration.
image: https://actikidz.com/assets/og-default.png
layout: provider
modified: '2026-10-31'
name: ActiKidz
nav: Providers
network: true
overview: 'ActiKidz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Platform, Children, Courses, and Activities.


  ActiKidz''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 58.0
    operational_transparency: 13.2
  previous_composite: 29.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actikidz Com Domain Security
  slug: actikidz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Actikidz Com Vulnerability Disclosure
  slug: actikidz-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Actikidz Com Trust Center
  slug: actikidz-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: actikidz-com
tags:
- Education
- Platform
- Children
- Courses
- Activities
website: https://actikidz.com/
---
