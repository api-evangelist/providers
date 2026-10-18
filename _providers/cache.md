---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Cache provides tax-efficient solutions for diversifying concentrated stock positions via its platform.
  name: Cache API
  slug: cache-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cache/refs/heads/main/plans/cache-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cache-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cache/refs/heads/main/hosts/cache-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cache-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cache/refs/heads/main/vendors/cache-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cache-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usecache.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://usecache.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usecache.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://usecache.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cache/refs/heads/main/security/cache-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cache-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usecache.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://usecache.com/api/mcp
  - status: 200
    url: https://usecache.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Cache provides tax-efficient solutions for diversifying concentrated stock positions, offering exchange funds, long‑short strategies, and collar‑advance financing. It serves individual investors and advisors, delivering tools to manage large stock holdings, reduce tax drag, and access institutional‑grade strategies through a modern digital platform.
image: https://cdn.prod.website-files.com/655a158485a10c0b88c01948/66e42cae7964fbcf06ecb20d_cache-og-image.png
layout: provider
modified: '2026-10-06'
name: Cache
nav: Providers
network: true
overview: 'Cache is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Investment, Tax-Optimization, Wealth Management, and Platform.


  Cache''s developer surface includes support and 8 more developer resources.'
plans:
- name: Cache Plans Pricing
  plan_count: 8
  slug: cache-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cache Domain Security
  slug: cache-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cache
tags:
- Finance
- Investment
- Tax-Optimization
- Wealth Management
- Platform
website: https://usecache.com
---
