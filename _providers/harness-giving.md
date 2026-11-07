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
- description: Recurring Giving Suite for Nonprofits API providing endpoints for managing donor subscriptions, programs, and dashboards.
  name: Harness Giving API
  slug: harness-giving-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/harness-giving/llms/harness-giving-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harness-giving-llms.txt
- group: auth
  href: https://artifacts.apis.io/harness-giving/well-known/harness-giving-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/harness-giving-help-security.txt
- group: agent
  href: https://artifacts.apis.io/harness-giving/well-known/harness-giving-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/harness-giving-well-known.yml
- group: other
  href: https://artifacts.apis.io/harness-giving/hosts/harness-giving-hosts.yml
  title: ''
  type: Hosts
  url: hosts/harness-giving-hosts.yml
- group: other
  href: https://artifacts.apis.io/harness-giving/vendors/harness-giving-vendors.yml
  title: ''
  type: Vendors
  url: vendors/harness-giving-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goharness.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goharness.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://goharness.com/press
- group: company
  title: ''
  type: Blog
  url: https://goharness.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.goharness.com/en/articles/3753366-harness-your-3-onboarding-steps
- group: docs
  title: ''
  type: Documentation
  url: https://help.harnessgiving.com/
- group: auth
  href: https://artifacts.apis.io/harness-giving/security/harness-giving-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harness-giving-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://harnessgiving.com/
coverage:
  checked: '2026-10-27'
  detail: The nonprofit API documentation is served as HTML pages without any OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://goharness.com/nonprofits
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Harness provides a recurring giving platform for nonprofits, enabling frictionless monthly donor subscriptions, retention dashboards, and automated stewardship. Their suite helps organizations launch, grow, and retain donors with easy-to-use forms and subscription‑economy‑style experiences, aiming to increase sustainable funding for charitable causes.
image: https://cdn.prod.website-files.com/6a0dfa44d46f3e02b6960cba/6a0f59c1bdccfa459ac2d678_Favicon_Harness%20Blue.png
layout: provider
modified: '2026-10-27'
name: Harness (nonprofit giving app)
nav: Providers
network: true
overview: 'Harness (nonprofit giving app) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Giving, Recurring Payments, and Software-as-a-Service.


  Harness (nonprofit giving app)''s developer surface includes engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/harness-giving/harness-giving-2026-11-03T133209.png
security:
- kind: domain-security
  name: Harness Giving Domain Security
  slug: harness-giving-domain-security
  summary_line: TLSv1.3 · HSTS
slug: harness-giving
tags:
- Company
- Non-Profit
- Giving
- Recurring Payments
- Software-as-a-Service
website: https://harnessgiving.com/
---
