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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SEO APIs provides a suite of free, publicly accessible APIs for bot detection, HTTP status validation, CLS measurement, and disavow file checks.
  name: SEO APIs
  slug: seo-apis
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/seoapi-com/hosts/seoapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seoapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/seoapi-com/vendors/seoapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seoapi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/seoapi-com/security/seoapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seoapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seoapi.com/
coverage:
  checked: '2026-10-29'
  detail: The site lists only external API links and provides no developer documentation or machine-readable contract for its own API.
  evidence:
  - status: 200
    url: https://seoapi.com/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: SEO API provides a suite of free, publicly accessible APIs that let developers identify search engine bot traffic, validate HTTP status codes, measure cumulative layout shift, and validate disavow files. Each endpoint returns IP address ranges for major bots such as Googlebot, Bingbot, YandexBot, Applebot, Baiduspider, DuckDuckBot, and others, as well as tools for testing HTTP responses and web performance metrics. The service is aimed at SEO professionals, webmasters, and developers who need reliable bot detection and web diagnostics without authentication.
image: https://seoapi.com/favicon.ico
layout: provider
modified: '2026-10-29'
name: seoapi-com
nav: Providers
network: true
overview: seoapi-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Bots, Data, and Company.
random_paper: 21
scopes:
- name: Seoapi Com Scopes
  scope_count: 0
  slug: seoapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seoapi-com/seoapi-com-2026-11-03T143038.png
security:
- kind: authentication
  name: Seoapi Com Authentication
  slug: seoapi-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Seoapi Com Domain Security
  slug: seoapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: seoapi-com
tags:
- SEO
- Bots
- Data
- Company
website: https://seoapi.com/
---
