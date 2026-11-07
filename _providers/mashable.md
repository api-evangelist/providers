---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mashable Agentic Access
  operation_count: 2
  slug: mashable-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://newsapi.org/v2
  baseurl_source: declared
  description: Search across all indexed articles.
  name: Mashable Articles API
  slug: mashable-articles-api
- baseURL: https://newsapi.org/v2
  baseurl_source: declared
  description: Top headline retrieval.
  name: Mashable Headlines API
  slug: mashable-headlines-api
artifact_total: 12
collections:
- collection_type: open
  name: Mashable via News Articles API
  slug: open-mashable-articles-api
- collection_type: open
  name: Mashable via News Articles Headlines API
  slug: open-mashable-headlines-api
- collection_type: open
  name: Mashable via News API
  slug: open-mashable
common:
- group: commercial
  href: https://artifacts.apis.io/mashable/plans/mashable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mashable-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mashable/rate-limits/mashable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mashable-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mashable/finops/mashable-finops.yml
  title: ''
  type: FinOps
  url: finops/mashable-finops.yml
- group: agent
  href: https://artifacts.apis.io/mashable/agentic-access/mashable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mashable-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mashable/security/mashable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mashable-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mashable/authentication/mashable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mashable-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mashable.com/
- group: company
  title: ''
  type: About
  url: https://mashable.com/about
- group: other
  title: ''
  type: Advertising
  url: https://mashable.com/advertise
- group: company
  title: ''
  type: Newsletter
  url: https://mashable.com/newsletter
- group: docs
  title: ''
  type: Documentation
  url: https://newsapi.org/s/mashable-api
- group: other
  title: ''
  type: RSS
  url: http://feeds.mashable.com/mashable
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mashable.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mashable.com/terms
- group: other
  title: ''
  type: X
  url: https://twitter.com/mashable
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/mashable/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/mashable/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/mashable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mashable
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mashable
created: '2026-03-24'
description: Mashable is a digital media and entertainment company covering tech, culture, and digital trends. Founded in 2005, Mashable has grown into a global, multi-platform media and entertainment company. Mashable does not publish a first-party REST API, but its headlines and articles are accessible via the third-party News API REST service.
finops:
- has_sources: false
  method: generated
  name: Mashable Finops
  primary_unit: request
  service_category: API
  slug: mashable-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mashable.png
layout: provider
modified: '2026-05-19'
name: Mashable
nav: Providers
network: true
overview: 'Mashable publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Articles API and Headlines API. Tagged areas include Articles, Digital Culture, Headlines, Media, and News.


  The Mashable catalog on APIs.io includes 1 Spectral governance ruleset.


  Mashable''s developer surface includes authentication, documentation, YouTube channel, GitHub presence, and 16 more developer resources.'
plans:
- name: Mashable Plans Pricing
  plan_count: 3
  slug: mashable-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Mashable Rate Limits
  slug: mashable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Mashable API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: mashable-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 47.8
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mashable/mashable-2026-06-20T185014.png
security:
- kind: authentication
  name: Mashable Authentication
  slug: mashable-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mashable Domain Security
  slug: mashable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mashable
tags:
- Articles
- Digital Culture
- Headlines
- Media
- News
- Technology News
website: https://mashable.com/
---
