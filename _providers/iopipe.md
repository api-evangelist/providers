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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/iopipe/plans/iopipe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iopipe-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/iopipe/hosts/iopipe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iopipe-hosts.yml
- group: other
  href: https://artifacts.apis.io/iopipe/vendors/iopipe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iopipe-vendors.yml
- group: build
  href: https://artifacts.apis.io/iopipe/packages/iopipe-packages.yml
  title: ''
  type: SDKs
  url: packages/iopipe-packages.yml
- group: build
  href: https://artifacts.apis.io/iopipe/packages/iopipe-packages.yml
  title: ''
  type: Packages
  url: packages/iopipe-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iopipe.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://www.iopipe.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iopipe.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iopipe.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iopipe/
- group: auth
  href: https://artifacts.apis.io/iopipe/security/iopipe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iopipe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iopipe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.iopipe.com/features/
- group: company
  title: ''
  type: Blog
  url: http://read.iopipe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.iopipe.com/en/collections/302941-iopipe-faq/
- group: start
  title: ''
  type: Login
  url: https://dashboard.iopipe.com/login/
created: '2026-10-22'
description: IOpipe provides real‑time observability for serverless applications on AWS Lambda. It offers detailed tracing, profiling, alerts, metrics, and logging to help developers monitor function performance, detect issues, and optimize costs. The platform integrates with existing CI/CD pipelines and supports custom dashboards, enabling teams to gain deep insights into their serverless workloads.
image: https://www.iopipe.com/static/img/iopipe_serverless_observability_og.png
layout: provider
modified: '2026-10-22'
name: IOpipe
nav: Providers
network: true
overview: 'IOpipe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Observability, Serverless, and Amazon Web Services.


  IOpipe''s developer surface includes pricing, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Iopipe Plans Pricing
  plan_count: 4
  slug: iopipe-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iopipe/iopipe-2026-11-03T134022.png
security:
- kind: domain-security
  name: Iopipe Domain Security
  slug: iopipe-domain-security
  summary_line: TLSv1.3 · HSTS
slug: iopipe
tags:
- Company
- Monitoring
- Observability
- Serverless
- Amazon Web Services
website: https://www.iopipe.com/
---
