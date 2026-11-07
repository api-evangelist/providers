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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/shopify
- group: auth
  href: https://artifacts.apis.io/handshake-com/well-known/handshake-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/handshake-com-security.txt
- group: agent
  href: https://artifacts.apis.io/handshake-com/well-known/handshake-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/handshake-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/handshake-com/hosts/handshake-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/handshake-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/handshake-com/vendors/handshake-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/handshake-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/handshake-com/packages/handshake-com-packages.yml
  title: ''
  type: SDKs
  url: packages/handshake-com-packages.yml
- group: build
  href: https://artifacts.apis.io/handshake-com/packages/handshake-com-packages.yml
  title: ''
  type: Packages
  url: packages/handshake-com-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/handshake
- group: auth
  href: https://artifacts.apis.io/handshake-com/security/handshake-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/handshake-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/handshake-com/security/handshake-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/handshake-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.handshake.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.handshake.com
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Handshake is a domain name marketplace and wholesale supplier platform that connects brands with manufacturers and distributors. It provides tools for sourcing products, managing wholesale relationships, and facilitating bulk orders. The service aims to streamline the supply chain for retailers and brands by offering a searchable catalog of suppliers, pricing information, and integration options for e‑commerce platforms.
image: https://cdn.shopify.com/b/shopify-brochure2-assets/956ca2a804e23a6910b546ef50c9846c.jpg
layout: provider
modified: '2026-10-28'
name: handshake
nav: Providers
network: true
overview: handshake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Wholesale, Suppliers, and E-Commerce.
random_paper: 3
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.7
  provenance:
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
screenshot: https://apis.io/screenshots/handshake-com/handshake-com-2026-11-03T133140.png
security:
- kind: domain-security
  name: Handshake Com Domain Security
  slug: handshake-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Handshake Com Vulnerability Disclosure
  slug: handshake-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: handshake-com
tags:
- Company
- Marketplace
- Wholesale
- Suppliers
- E-Commerce
website: https://www.handshake.com
---
