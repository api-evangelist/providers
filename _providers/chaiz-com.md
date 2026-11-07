---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.chaiz.com
  baseurl_source: declared
  description: Partner API for searching, comparing and selling vehicle service contracts.
  name: Chaiz Partner API
  slug: chaiz-partner-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/chaiz-com/rate-limits/chaiz-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chaiz-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chaiz-com/plans/chaiz-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chaiz-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/chaiz-com/authentication/chaiz-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chaiz-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/chaiz-com/errors/chaiz-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chaiz-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chaiz-com/conformance/chaiz-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chaiz-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chaiz-com/llms/chaiz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chaiz-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/chaiz-com/well-known/chaiz-com-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chaiz-com-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/chaiz-com/well-known/chaiz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chaiz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chaiz-com/hosts/chaiz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chaiz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chaiz-com/vendors/chaiz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chaiz-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chaiz.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chaiz.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.chaiz.com/category/news
- group: auth
  href: https://artifacts.apis.io/chaiz-com/security/chaiz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chaiz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chaiz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev-docs.chaiz.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev-docs.chaiz.com/reference/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://dev-docs.chaiz.com/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.chaiz.com/blog
created: '2026-11-03'
description: Chaiz is an online marketplace that connects consumers with vehicle service contract providers, offering transparent, digital‑first extended warranty options. The platform enables users to compare plans, get instant quotes, and purchase coverage online without sales pressure. Chaiz emphasizes fair pricing, a wide selection of vetted providers, and a fully remote team spread across North America, Africa, and Europe. It serves both end‑customers and partners through a documented Partner API for integration.
image: https://cdn.prod.website-files.com/62f3a95300236f13d26a4e0e/64775dd984d340b032749fbd_opengraph-1.png
layout: provider
modified: '2026-11-03'
name: Chaiz
nav: Providers
network: true
overview: 'Chaiz is listed with 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Marketplace, Automotive, Extended Warranty, and Digital-First.


  Chaiz''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Chaiz Com Plans Pricing
  plan_count: 4
  slug: chaiz-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Chaiz Com Rate Limits
  slug: chaiz-com-rate-limits
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 37.6
    developer_ergonomics: 27.4
    discoverability: 58.0
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chaiz Com Authentication
  slug: chaiz-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chaiz Com Domain Security
  slug: chaiz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chaiz-com
tags:
- Marketplace
- Automotive
- Extended Warranty
- Digital-First
website: https://chaiz.com/
---
