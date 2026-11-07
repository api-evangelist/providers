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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Fundraising Report Card providing nonprofit analytics and reporting tools.
  name: Fundraising Report Card API
  slug: fundraising-report-card-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/fundraising-report-card/conformance/fundraising-report-card-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fundraising-report-card-conformance.yml
- group: other
  href: https://artifacts.apis.io/fundraising-report-card/hosts/fundraising-report-card-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fundraising-report-card-hosts.yml
- group: other
  href: https://artifacts.apis.io/fundraising-report-card/vendors/fundraising-report-card-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fundraising-report-card-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://fundraisingreportcard.com/help/
- group: auth
  title: ''
  type: Security
  url: https://fundraisingreportcard.com/security/
- group: start
  title: ''
  type: Login
  url: https://app.fundraisingreportcard.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://fundraisingreportcard.com/resources/getting-started/
- group: auth
  href: https://artifacts.apis.io/fundraising-report-card/security/fundraising-report-card-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fundraising-report-card-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fundraisingreportcard.com/
- group: company
  title: ''
  type: Blog
  url: https://fundraisingreportcard.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fundraisingreportcard.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fundraisingreportcard.com/privacy/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found despite public docs.
  evidence:
  - status: 404
    url: https://fundraisingreportcard.com/openapi.json
  - status: 404
    url: https://api.fundraisingreportcard.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Fundraising Report Card provides nonprofit analytics and reporting tools that deliver metrics such as donation growth, donor retention, donor lifetime value, and churn. The platform offers one‑click dashboards for fundraising performance, helping organizations track and improve their fundraising efforts with clear, actionable insights.
layout: provider
modified: '2026-10-27'
name: Fundraising Report Card
nav: Providers
network: true
overview: 'Fundraising Report Card is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Analytics, Fundraising, and Metrics.


  Fundraising Report Card''s developer surface includes support, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fundraising-report-card/fundraising-report-card-2026-11-03T132358.png
security:
- kind: domain-security
  name: Fundraising Report Card Domain Security
  slug: fundraising-report-card-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fundraising-report-card
tags:
- Company
- Non-Profit
- Analytics
- Fundraising
- Metrics
website: https://fundraisingreportcard.com/
---
