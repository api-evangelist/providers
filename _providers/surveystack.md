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
- description: SurveyStack provides tools for building surveys, collecting responses, and managing communities.
  name: SurveyStack API
  slug: surveystack-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/surveystack/hosts/surveystack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/surveystack-hosts.yml
- group: other
  href: https://artifacts.apis.io/surveystack/vendors/surveystack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/surveystack-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.surveystack.io/
- group: auth
  href: https://artifacts.apis.io/surveystack/security/surveystack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/surveystack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.surveystack.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.surveystack.io/#pricing
- group: company
  title: ''
  type: Blog
  url: https://www.surveystack.io/news/
coverage:
  checked: '2026-10-28'
  detail: Docs are public HTML tutorials but no machine‑readable API specification is published.
  evidence:
  - status: 200
    url: https://docs.surveystack.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SurveyStack provides flexible tools for building surveys, collecting data, managing communities, processing data, and visualizing results. Their platform enables users to create intuitive surveys, integrate custom filters, and pull data via an API for dashboards and analytics, supporting the full journey from data collection to insight.
layout: provider
modified: '2026-10-28'
name: SurveyStack
nav: Providers
network: true
overview: 'SurveyStack is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SurveyStack, Data Collection, Analytics, and Community.


  SurveyStack''s developer surface includes documentation, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Surveystack Plans Pricing
  plan_count: 0
  slug: surveystack-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Surveystack Rate Limits
  slug: surveystack-rate-limits
scopes:
- name: Surveystack Scopes
  scope_count: 0
  slug: surveystack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/surveystack/surveystack-2026-11-03T144121.png
security:
- kind: authentication
  name: Surveystack Authentication
  slug: surveystack-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Surveystack Domain Security
  slug: surveystack-domain-security
  summary_line: DMARC
slug: surveystack
tags:
- SurveyStack
- Data Collection
- Analytics
- Community
website: https://www.surveystack.io/
---
