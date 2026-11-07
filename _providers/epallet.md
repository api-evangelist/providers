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
- description: ePallet provides an online wholesale marketplace API (details not publicly documented).
  name: ePallet API
  slug: epallet-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/epallet/hosts/epallet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/epallet-hosts.yml
- group: other
  href: https://artifacts.apis.io/epallet/vendors/epallet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/epallet-vendors.yml
- group: auth
  href: https://artifacts.apis.io/epallet/security/epallet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/epallet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epallet.com/
- group: operate
  title: ''
  type: Support
  url: https://epallet.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://epallet.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://epallet.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://epallet.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epallet.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://epallet.com/?epallet_signup=true
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Epallet
coverage:
  checked: '2026-10-29'
  detail: The provider's website does not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://epallet.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ePallet is an online wholesale marketplace that enables bulk purchasing of a wide variety of products. The platform offers a curated selection of brands and categories, providing real‑time pricing, secure checkout, and hassle‑free delivery coordination. Shoppers can explore brands, business categories, and mixed pallets, while the site emphasizes safe and secure checkout, customer service, and guarantees. ePallet’s mission is to make bulk buying easy and efficient for both consumers and businesses.
image: https://22338452.fs1.hubspotusercontent-na1.net/hubfs/22338452/logos_storefront/main_logo_5.png
layout: provider
modified: '2026-10-29'
name: ePallet
nav: Providers
network: true
overview: 'ePallet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Wholesale, Marketplace, bulk-buying, and Logistics.


  ePallet''s developer surface includes support, engineering blog, pricing, signup flow, and 7 more developer resources.'
plans:
- name: Epallet Plans Pricing
  plan_count: 0
  slug: epallet-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Epallet Rate Limits
  slug: epallet-rate-limits
scopes:
- name: Epallet Scopes
  scope_count: 0
  slug: epallet-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/epallet/epallet-2026-11-03T131557.png
security:
- kind: authentication
  name: Epallet Authentication
  slug: epallet-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Epallet Domain Security
  slug: epallet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: epallet
tags:
- E-Commerce
- Wholesale
- Marketplace
- bulk-buying
- Logistics
- B2B
- Retail
website: https://epallet.com/
---
