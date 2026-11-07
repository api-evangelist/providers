---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/judoscale/authentication/judoscale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/judoscale-authentication.yml
- group: agent
  href: https://artifacts.apis.io/judoscale/llms/judoscale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/judoscale-llms.txt
- group: other
  href: https://artifacts.apis.io/judoscale/hosts/judoscale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/judoscale-hosts.yml
- group: other
  href: https://artifacts.apis.io/judoscale/vendors/judoscale-vendors.yml
  title: ''
  type: Vendors
  url: vendors/judoscale-vendors.yml
- group: build
  href: https://artifacts.apis.io/judoscale/packages/judoscale-packages.yml
  title: ''
  type: SDKs
  url: packages/judoscale-packages.yml
- group: build
  href: https://artifacts.apis.io/judoscale/packages/judoscale-packages.yml
  title: ''
  type: Packages
  url: packages/judoscale-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://judoscale.com/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://judoscale.com/docs/privacy
- group: start
  title: ''
  type: Login
  url: https://judoscale.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://judoscale.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://judoscale.com/docs/heroku-getting-started
- group: auth
  href: https://artifacts.apis.io/judoscale/security/judoscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/judoscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://judoscale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://judoscale.com/docs
- group: company
  title: ''
  type: Blog
  url: https://judoscale.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://judoscale.com/pricing
coverage:
  checked: '2026-10-26'
  detail: Documentation is provided as HTML pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://judoscale.com/docs/heroku-getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Judoscale provides an autoscaling platform that integrates with cloud hosting services such as Heroku, Render, Railway, Fly.io, Scalingo, Northflank, and AWS. It automatically adjusts the number of web and worker dynos or containers based on request queue length and job queue metrics, offering configurable step sizes, schedules, and per‑process scaling ranges. The service aims to improve performance and reduce costs by scaling only when needed, with support for multiple programming languages and frameworks.
image: https://judoscale.com/icon.png
layout: provider
modified: '2026-10-26'
name: Judoscale
nav: Providers
network: true
overview: 'Judoscale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Auto-Scaling, Cloud, DevOps, and Heroku.


  Judoscale''s developer surface includes authentication, changelog, getting-started guide, documentation, engineering blog, pricing, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/judoscale/judoscale-2026-11-03T134238.png
security:
- kind: authentication
  name: Judoscale Authentication
  slug: judoscale-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Judoscale Domain Security
  slug: judoscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: judoscale
tags:
- Company
- Auto-Scaling
- Cloud
- DevOps
- Heroku
- Amazon Web Services
website: https://judoscale.com/
---
