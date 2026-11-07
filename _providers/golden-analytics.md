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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public HTTP surface of goldenanalytics.com as described in the OpenAPI spec.
  name: Golden Analytics API
  slug: golden-analytics-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/golden-analytics/plans/golden-analytics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/golden-analytics-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/golden-analytics/conformance/golden-analytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/golden-analytics-conformance.yml
- group: agent
  href: https://artifacts.apis.io/golden-analytics/llms/golden-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/golden-analytics-llms.txt
- group: auth
  href: https://artifacts.apis.io/golden-analytics/well-known/golden-analytics-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/golden-analytics-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/golden-analytics/well-known/golden-analytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/golden-analytics-well-known.yml
- group: other
  href: https://artifacts.apis.io/golden-analytics/hosts/golden-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/golden-analytics-hosts.yml
- group: other
  href: https://artifacts.apis.io/golden-analytics/vendors/golden-analytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/golden-analytics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goldenanalytics.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goldenanalytics.com/
- group: auth
  title: ''
  type: Security
  url: https://goldenanalytics.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goldenanalytics.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://goldenanalytics.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://goldenanalytics.com/newsroom
- group: start
  title: ''
  type: DeveloperPortal
  url: https://goldenanalytics.com/developers
- group: company
  title: ''
  type: Blog
  url: https://goldenanalytics.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goldenanalytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://goldenanalytics.com/product/whats-new
- group: auth
  href: https://artifacts.apis.io/golden-analytics/security/golden-analytics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/golden-analytics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/golden-analytics/security/golden-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/golden-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goldenanalytics.com
created: '2026-10-22'
description: Golden Analytics provides an AI‑native business intelligence platform that enables data teams to connect, discover, prepare, analyze, and share insights within a single workflow. The platform serves analysts, business users, and data leaders who need automated discovery, AI‑augmented analysis, and governed metrics across cloud data warehouses.
image: https://cdn.sanity.io/images/d8jzjb8o/production/7346456bb8f1e912f52e64b2f6794e4bacc0ffb0-1120x263.svg
layout: provider
modified: '2026-10-22'
name: Golden Analytics
nav: Providers
network: true
overview: 'Golden Analytics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, AI-native, Data Analytics, Data Teams, and Enterprise Analytics.


  Golden Analytics'' developer surface includes pricing, engineering blog, documentation, API reference, and 16 more developer resources.'
plans:
- name: Golden Analytics Plans Pricing
  plan_count: 2
  slug: golden-analytics-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 74.1
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/golden-analytics/golden-analytics-2026-11-03T132920.png
security:
- kind: domain-security
  name: Golden Analytics Domain Security
  slug: golden-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Golden Analytics Vulnerability Disclosure
  slug: golden-analytics-vulnerability-disclosure
  summary_line: no policy recorded
slug: golden-analytics
tags:
- Business Intelligence
- AI-native
- Data Analytics
- Data Teams
- Enterprise Analytics
website: https://goldenanalytics.com
---
