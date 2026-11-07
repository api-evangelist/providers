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
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/findbroadbanddeals-com/conformance/findbroadbanddeals-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findbroadbanddeals-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/findbroadbanddeals-com/llms/findbroadbanddeals-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findbroadbanddeals-com-llms.txt
- group: other
  href: https://artifacts.apis.io/findbroadbanddeals-com/hosts/findbroadbanddeals-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findbroadbanddeals-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/findbroadbanddeals-com/vendors/findbroadbanddeals-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findbroadbanddeals-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findbroadbanddeals.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findbroadbanddeals.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.findbroadbanddeals.com/pricing-regulation
- group: company
  title: ''
  type: Newsroom
  url: https://www.findbroadbanddeals.com/news
- group: start
  title: ''
  type: Login
  url: https://www.findbroadbanddeals.com/sign-in
- group: other
  title: ''
  type: Leadership
  url: https://www.findbroadbanddeals.com/team
- group: docs
  title: ''
  type: Documentation
  url: https://www.findbroadbanddeals.com/guides
- group: auth
  href: https://artifacts.apis.io/findbroadbanddeals-com/security/findbroadbanddeals-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findbroadbanddeals-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findbroadbanddeals.com/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript with no machine‑readable OpenAPI or other contract available.
  evidence:
  - status: 200
    url: https://www.findbroadbanddeals.com/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Find Broadband Deals helps UK households compare broadband offers from major providers, highlighting savings and contract details. The service aggregates plans, prices, speeds, and terms, enabling users to input their address and view personalized recommendations, ensuring they avoid overpaying for internet services.
image: https://www.findbroadbanddeals.com/opengraph-image-18u3ps.png?cfd9873910bc9d9f
layout: provider
modified: '2026-10-30'
name: findbroadbanddeals-com
nav: Providers
network: true
overview: 'findbroadbanddeals-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Broadband, United Kingdom, Comparison, and Consumer.


  findbroadbanddeals-com''s developer surface includes pricing, documentation, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
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
  previous_composite: 19.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/findbroadbanddeals-com/findbroadbanddeals-com-2026-11-03T132032.png
security:
- kind: domain-security
  name: Findbroadbanddeals Com Domain Security
  slug: findbroadbanddeals-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: findbroadbanddeals-com
tags:
- Company
- Broadband
- United Kingdom
- Comparison
- Consumer
website: https://findbroadbanddeals.com/
---
