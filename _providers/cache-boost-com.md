---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.cache-boost.com/v1
  baseurl_source: declared
  description: The Auth API from CacheBoost — 1 operation(s) for auth.
  name: CacheBoost Auth API
  slug: cache-boost-com-auth-api
- baseURL: https://api.cache-boost.com/v1
  baseurl_source: declared
  description: The Boosts API from CacheBoost — 3 operation(s) for boosts.
  name: CacheBoost Boosts API
  slug: cache-boost-com-boosts-api
- baseURL: https://api.cache-boost.com/v1
  baseurl_source: declared
  description: The Runs API from CacheBoost — 2 operation(s) for runs.
  name: CacheBoost Runs API
  slug: cache-boost-com-runs-api
- baseURL: https://api.cache-boost.com/v1
  baseurl_source: declared
  description: The Sitemaps API from CacheBoost — 2 operation(s) for sitemaps.
  name: CacheBoost Sitemaps API
  slug: cache-boost-com-sitemaps-api
- baseURL: https://api.cache-boost.com/v1
  baseurl_source: declared
  description: The Sites API from CacheBoost — 5 operation(s) for sites.
  name: CacheBoost Sites API
  slug: cache-boost-com-sites-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/cache-boost-com/plans/cache-boost-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cache-boost-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cache-boost-com/data-model/cache-boost-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cache-boost-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cache-boost-com/authentication/cache-boost-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cache-boost-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cache-boost-com/errors/cache-boost-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cache-boost-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cache-boost-com/llms/cache-boost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cache-boost-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cache-boost-com/well-known/cache-boost-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cache-boost-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cache-boost-com/hosts/cache-boost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cache-boost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cache-boost-com/vendors/cache-boost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cache-boost-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cache-boost-com/security/cache-boost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cache-boost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cache-boost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cache-boost.com/support/guides/allow-traffic
- group: docs
  title: ''
  type: APIReference
  url: https://www.cache-boost.com/support/api-reference/overview
- group: company
  title: ''
  type: Blog
  url: https://www.cache-boost.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cache-boost.com/support/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.cache-boost.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cache-boost.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cache-boost.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cache-boost.com/register
- group: start
  title: ''
  type: Login
  url: https://app.cache-boost.com/login
created: '2026-11-03'
description: CacheBoost provides automatic cache warming for websites, improving performance, SEO, and user experience. It supports WordPress, Magento, PrestaShop, and other platforms, offering configurable request rates and integration via webhooks for CI/CD pipelines. The service works with any CDN or caching layer, ensuring visitors receive fast page loads from a warm cache.
image: https://www.cache-boost.com/img/og.png
layout: provider
modified: '2026-11-03'
name: CacheBoost
nav: Providers
network: true
overview: 'CacheBoost publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Boosts API, Runs API, and 2 more. Tagged areas include Cache, Performance, SEO, WordPress, and CDN.


  CacheBoost''s developer surface includes authentication, documentation, API reference, engineering blog, getting-started guide, support, pricing, and 12 more developer resources.'
plans:
- name: Cache Boost Com Plans Pricing
  plan_count: 4
  slug: cache-boost-com-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 50.4
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cache Boost Com Authentication
  slug: cache-boost-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cache Boost Com Domain Security
  slug: cache-boost-com-domain-security
  summary_line: TLSv1.3
slug: cache-boost-com
tags:
- Cache
- Performance
- SEO
- WordPress
- CDN
website: https://cache-boost.com/
---
