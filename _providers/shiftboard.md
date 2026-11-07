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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/shiftboard/llms/shiftboard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiftboard-llms.txt
- group: operate
  href: https://artifacts.apis.io/shiftboard/changelog/shiftboard-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shiftboard-changelog.yml
- group: agent
  href: https://artifacts.apis.io/shiftboard/well-known/shiftboard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shiftboard-well-known.yml
- group: other
  href: https://artifacts.apis.io/shiftboard/hosts/shiftboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shiftboard-hosts.yml
- group: other
  href: https://artifacts.apis.io/shiftboard/vendors/shiftboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shiftboard-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ukg.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.ukg.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ukg.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ukg.com/products/ukg-ready/plans
- group: company
  title: ''
  type: Newsroom
  url: https://www.ukg.com/company/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.ukg.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ukg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ukg
- group: auth
  href: https://artifacts.apis.io/shiftboard/security/shiftboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiftboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ukg.com/information-shiftboard-customers
coverage:
  checked: '2026-10-13'
  detail: No public API documentation or OpenAPI spec found on discovered hosts.
  evidence:
  - status: 404
    url: https://apply.ukg.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Shiftboard provides workforce management and scheduling solutions, now part of UKG. Their customers are listed on the UKG site, indicating integration into a broader human capital management platform. Shiftboard’s technology helps organizations manage employee shifts, compliance, and labor costs, leveraging AI-driven scheduling and analytics.
layout: provider
modified: '2026-10-13'
name: Shiftboard
nav: Providers
network: true
overview: 'Shiftboard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce, Scheduling, Human Resources, and UKG.


  Shiftboard''s developer surface includes changelog, support, pricing, engineering blog, documentation, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 52.7
    operational_transparency: 18.4
  previous_composite: 17.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shiftboard/shiftboard-2026-11-03T143118.png
security:
- kind: domain-security
  name: Shiftboard Domain Security
  slug: shiftboard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shiftboard
tags:
- Company
- Workforce
- Scheduling
- Human Resources
- UKG
website: https://www.ukg.com/information-shiftboard-customers
---
