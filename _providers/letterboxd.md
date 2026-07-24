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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'REST API providing access to Letterboxd film data, member profiles, watchlists, ratings, diary log entries, user-created lists, contributors, editorial stories, and cross-catalog search. The base URL '
  name: Letterboxd API
  slug: letterboxd-api
artifact_total: 5
common:
- group: auth
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
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/letterboxd.png
layout: provider
modified: '2026-06-13'
name: Letterboxd
nav: Providers
network: true
overview: 'Letterboxd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Film, Movies, Social, Reviews, and Watchlist.


  Letterboxd''s developer surface includes GitHub presence, engineering blog, FAQ, and 4 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 14
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 37.7
    developer_ergonomics: 2.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
---
