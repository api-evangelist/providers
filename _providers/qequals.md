---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: Google autocomplete suggestions and live Google search results, as an API. Built so an agent can start without an account.
  name: qequals API
  slug: qequals-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/qequals/plans/qequals-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qequals-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/qequals/llms/qequals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qequals-llms.txt
- group: other
  href: https://artifacts.apis.io/qequals/hosts/qequals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qequals-hosts.yml
- group: other
  href: https://artifacts.apis.io/qequals/vendors/qequals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qequals-vendors.yml
- group: auth
  href: https://artifacts.apis.io/qequals/security/qequals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qequals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qequals.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.qequals.com/catalog
- group: company
  title: ''
  type: Blog
  url: https://www.qequals.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qequals.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.qequals.com/account
coverage:
  checked: '2026-10-30'
  detail: The provider’s documentation (llms.txt) describes the API but does not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://www.qequals.com/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Qequals provides an agent‑first API delivering Google autocomplete suggestions and live search result data. It powers applications with real‑time search insights, offering a public catalog that demonstrates the available endpoints and data structures. The service focuses on SEO and search‑engine data, enabling developers to integrate up‑to‑date query trends and SERP information into their products.
image: https://www.qequals.com/featured-images/site-og.jpg
layout: provider
modified: '2026-10-30'
name: Qequals
nav: Providers
network: true
overview: 'Qequals is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Autocomplete, SEO, Data, and Company.


  Qequals'' developer surface includes documentation, engineering blog, getting-started guide, and 7 more developer resources.'
plans:
- name: Qequals Plans Pricing
  plan_count: 2
  slug: qequals-plans-pricing
random_paper: 20
scopes:
- name: Qequals Scopes
  scope_count: 0
  slug: qequals-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qequals/qequals-2026-11-03T141741.png
security:
- kind: authentication
  name: Qequals Authentication
  slug: qequals-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qequals Domain Security
  slug: qequals-domain-security
  summary_line: TLSv1.3
slug: qequals
tags:
- Search
- Autocomplete
- SEO
- Data
- Company
website: https://www.qequals.com/
---
