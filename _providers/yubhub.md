---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/yubhub/plans/yubhub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yubhub-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/yubhub/authentication/yubhub-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yubhub-authentication.yml
- group: agent
  href: https://artifacts.apis.io/yubhub/llms/yubhub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yubhub-llms.txt
- group: agent
  href: https://artifacts.apis.io/yubhub/well-known/yubhub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yubhub-well-known.yml
- group: other
  href: https://artifacts.apis.io/yubhub/hosts/yubhub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yubhub-hosts.yml
- group: other
  href: https://artifacts.apis.io/yubhub/vendors/yubhub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yubhub-vendors.yml
- group: build
  href: https://artifacts.apis.io/yubhub/packages/yubhub-packages.yml
  title: ''
  type: SDKs
  url: packages/yubhub-packages.yml
- group: build
  href: https://artifacts.apis.io/yubhub/packages/yubhub-packages.yml
  title: ''
  type: Packages
  url: packages/yubhub-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://yubhub.co/jobs/graduate/security/
- group: start
  title: ''
  type: Login
  url: https://yubhub.co/sign-in/
- group: other
  title: ''
  type: Leadership
  url: https://yubhub.co/jobs/skill/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.yubhub.co.…
- group: auth
  href: https://artifacts.apis.io/yubhub/security/yubhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yubhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yubhub.co
- group: docs
  title: ''
  type: Documentation
  url: https://yubhub.co/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://yubhub.co/developers/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://yubhub.co/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yubhub.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yubhub.co/privacy/
coverage:
  checked: '2026-10-27'
  detail: API reference pages return 404 for OpenAPI spec URLs and no machine‑readable contract is available.
  evidence:
  - status: 404
    url: https://api.yubhub.co/openapi.json
  - status: 404
    url: https://api.yubhub.co/swagger.json
  - status: 404
    url: https://yubhub.co/developers/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: YubHub is a UK‑based job feed platform operated by Houtini Ltd. It aggregates live job listings from employer career pages, enriches them with salary, location and skill data, and provides access via a public REST API (open endpoints) and a paid MCP API for advanced feeds. The service supports XML and JSON formats and offers developer tools for integration into hiring pipelines and AI assistants.
image: https://yubhub.co/images/yubhub-solution.png
layout: provider
modified: '2026-10-27'
name: YubHub
nav: Providers
network: true
overview: 'YubHub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include JobFeed, Recruiting, United Kingdom, and Data Enrichment.


  YubHub''s developer surface includes authentication, documentation, API reference, pricing, and 15 more developer resources.'
plans:
- name: Yubhub Plans Pricing
  plan_count: 4
  slug: yubhub-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 47.3
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.1
  provenance:
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
screenshot: https://apis.io/screenshots/yubhub/yubhub-2026-11-03T150400.png
security:
- kind: authentication
  name: Yubhub Authentication
  slug: yubhub-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Yubhub Domain Security
  slug: yubhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yubhub
tags:
- JobFeed
- Recruiting
- United Kingdom
- Data Enrichment
website: https://yubhub.co
---
