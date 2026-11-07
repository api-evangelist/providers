---
access_model:
  confidence: low
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
- group: other
  href: https://artifacts.apis.io/subito/hosts/subito-hosts.yml
  title: ''
  type: Hosts
  url: hosts/subito-hosts.yml
- group: other
  href: https://artifacts.apis.io/subito/vendors/subito-vendors.yml
  title: ''
  type: Vendors
  url: vendors/subito-vendors.yml
- group: auth
  href: https://artifacts.apis.io/subito/security/subito-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subito-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://subito.it/
- group: operate
  title: ''
  type: Support
  url: https://assistenza.subito.it/hc/it/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://info.subito.it/policies/condizioni-generali.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.subito.it/policies/privacy.htm
- group: docs
  title: ''
  type: Documentation
  url: https://info.subito.it/
coverage:
  checked: '2026-10-29'
  detail: Documentation pages (e.g., https://www.subito.it/api-docs) return a service-unavailable HTML page, and no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://www.subito.it/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Subito.it, founded in Milan in 2007, is Italy’s leading online classifieds platform for buying and selling a wide range of items. With over 26 million monthly visitors and 13 million live ads across 38 categories, it offers a fast, secure, and user‑friendly marketplace for individuals and businesses alike.
image: https://assets.subito.it/static/logos/corporate.svg
layout: provider
modified: '2026-10-28'
name: Subito.it
nav: Providers
network: true
overview: 'Subito.it is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Classifieds, E-Commerce, Italy, and Recommerce.


  Subito.it''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 14
scopes:
- name: Subito Scopes
  scope_count: 0
  slug: subito-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/subito/subito-2026-11-03T143945.png
security:
- kind: authentication
  name: Subito Authentication
  slug: subito-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Subito Domain Security
  slug: subito-domain-security
  summary_line: TLSv1.3 · DMARC
slug: subito
tags:
- Marketplace
- Classifieds
- E-Commerce
- Italy
- Recommerce
website: https://subito.it/
---
