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
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/coveralls/well-known/coveralls-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coveralls-status-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coveralls.io/terms
- group: commercial
  href: https://artifacts.apis.io/coveralls/plans/coveralls-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coveralls-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.coveralls.io/
- group: agent
  href: https://artifacts.apis.io/coveralls/well-known/coveralls-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coveralls-well-known.yml
- group: other
  href: https://artifacts.apis.io/coveralls/hosts/coveralls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coveralls-hosts.yml
- group: other
  href: https://artifacts.apis.io/coveralls/vendors/coveralls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coveralls-vendors.yml
- group: build
  href: https://artifacts.apis.io/coveralls/packages/coveralls-packages.yml
  title: ''
  type: SDKs
  url: packages/coveralls-packages.yml
- group: build
  href: https://artifacts.apis.io/coveralls/packages/coveralls-packages.yml
  title: ''
  type: Packages
  url: packages/coveralls-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coveralls.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trust-center
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coveralls.io/index
- group: auth
  href: https://artifacts.apis.io/coveralls/security/coveralls-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coveralls-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coveralls/security/coveralls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coveralls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coveralls.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coveralls.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://coveralls.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coveralls.io/sign-up?plan_id=price_0MLtUJdAZILtb4AQbItx0P9h
- group: company
  title: ''
  type: Blog
  url: https://coveralls.io/announcements
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/coveralls/workspace/coveralls-api
coverage:
  checked: '2026-10-27'
  detail: Coveralls provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://coveralls.io
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Coveralls provides a hosted service that tracks test coverage for software projects. It integrates with many CI systems and version control platforms, offering detailed coverage reports, badges, and insights for both open‑source and private repositories. Users can view coverage trends, set coverage thresholds, and receive notifications. The platform supports multiple programming languages and offers enterprise features such as on‑premises deployment and advanced analytics.
image: https://coveralls.io/social.png
layout: provider
modified: '2026-10-26'
name: Coveralls
nav: Providers
network: true
overview: 'Coveralls is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code Coverage, CI Integration, Open Source, and Software-as-a-Service.


  Coveralls'' developer surface includes getting-started guide, documentation, pricing, signup flow, engineering blog, and 15 more developer resources.'
plans:
- name: Coveralls Plans Pricing
  plan_count: 8
  slug: coveralls-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 23.7
  previous_composite: 32.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coveralls/coveralls-2026-11-03T125445.png
security:
- kind: domain-security
  name: Coveralls Domain Security
  slug: coveralls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coveralls Trust Center
  slug: coveralls-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: coveralls
tags:
- Company
- Code Coverage
- CI Integration
- Open Source
- Software-as-a-Service
website: https://coveralls.io/
---
