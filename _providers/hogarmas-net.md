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
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: https://hogarmas.net/terminos/
- group: agent
  href: https://artifacts.apis.io/hogarmas-net/llms/hogarmas-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hogarmas-net-llms.txt
- group: auth
  href: https://artifacts.apis.io/hogarmas-net/well-known/hogarmas-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hogarmas-net-security.txt
- group: agent
  href: https://artifacts.apis.io/hogarmas-net/well-known/hogarmas-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hogarmas-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/hogarmas-net/hosts/hogarmas-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hogarmas-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/hogarmas-net/vendors/hogarmas-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hogarmas-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hogarmas-net/security/hogarmas-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hogarmas-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hogarmas-net/security/hogarmas-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hogarmas-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hogarmas.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hogarmas.net/terminos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hogarmas.net/privacidad/
coverage:
  checked: '2026-10-29'
  detail: Hogar Mas is a wholesale marketplace without a public API or developer documentation.
  evidence:
  - status: 200
    url: https://hogarmas.net/
  - status: 0
    url: https://api.hogarmas.net/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Hogar Mas is a Chilean B2B wholesale marketplace that aggregates price lists from local suppliers across categories such as food, beverages, cleaning, personal care, and more. It enables businesses to compare unit prices, quantity tiers, and delivery conditions, sourcing data from over 70 public providers and presenting searchable catalogs for bulk purchasing.
image: https://hogarmas.net/logo.png
layout: provider
modified: '2026-10-29'
name: hogarmas-net
nav: Providers
network: true
overview: hogarmas-net is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wholesale, Chile, B2B, Marketplace, and Product.
plans:
- name: Hogarmas Net Plans Pricing
  plan_count: 0
  slug: hogarmas-net-plans-pricing
random_paper: 22
scopes:
- name: Hogarmas Net Scopes
  scope_count: 0
  slug: hogarmas-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - chile
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hogarmas-net/hogarmas-net-2026-11-03T133451.png
security:
- kind: authentication
  name: Hogarmas Net Authentication
  slug: hogarmas-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hogarmas Net Domain Security
  slug: hogarmas-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Hogarmas Net Vulnerability Disclosure
  slug: hogarmas-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hogarmas-net
tags:
- Wholesale
- Chile
- B2B
- Marketplace
- Product
website: https://hogarmas.net/
---
