---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: 'REST API providing access to Letterboxd film data, member profiles, watchlists, ratings, diary log entries, user-created lists, contributors, editorial stories, and cross-catalog search. The base URL '
  name: Letterboxd API
  slug: letterboxd-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/letterboxd/refs/heads/main/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/letterboxd/refs/heads/main/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/letterboxd/refs/heads/main/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: company
  title: ''
  type: Blog
  url: https://letterboxd.com/journal/
- group: company
  title: ''
  type: BlogRSS
  url: https://letterboxd.com/journal/rss/
- group: company
  title: ''
  type: Website
  url: https://letterboxd.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/letterboxd/refs/heads/main/security/letterboxd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/letterboxd-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Letterboxd
- group: company
  title: ''
  type: Blog
  url: https://news.letterboxd.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://letterboxd.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://letterboxd.com/legal/privacy-notice/
- group: operate
  title: ''
  type: FAQ
  url: https://letterboxd.com/about/faq/
- group: operate
  title: ''
  type: Contact
  url: https://letterboxd.com/about/
created: '2026-06-13'
description: Letterboxd is a social film diary platform providing a REST API for accessing film metadata, user reviews, watchlists, ratings, member activity, log entries, lists, and film festival coverage. The API is available by request only and uses OAuth2 for authentication, supporting both public data access via Client Credentials and member-authenticated operations via Authorization Code flow. Developers can query films, members, log entries, lists, contributors, and search across the full Letterboxd catalog.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/letterboxd.png
layout: provider
modified: '2026-10-06'
name: Letterboxd
nav: Providers
network: true
overview: 'Letterboxd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Film, Movies, Social, Reviews, and Watchlist.


  Letterboxd''s developer surface includes engineering blog, GitHub presence, FAQ, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 7
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 30.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/letterboxd/refs/heads/main/screenshots/letterboxd-2026-06-20T184431.png
security:
- kind: domain-security
  name: Letterboxd Domain Security
  slug: letterboxd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: letterboxd
tags:
- Film
- Movies
- Social
- Reviews
- Watchlist
- Ratings
- Diary
- Film Festival
- Entertainment
website: https://letterboxd.com
---
