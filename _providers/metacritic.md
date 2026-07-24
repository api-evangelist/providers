---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The official Metacritic API, delivered through Fabric Origin (formerly IVA / Gracenote), provides structured access to Metascores, user scores, and individual critic reviews for movies and TV shows. R
  name: Metacritic API (Fabric Origin)
  slug: metacritic-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metacritic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.metacritic.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.origin.fabricdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.origin.fabricdata.com/origin/apis-all/metacritic-api-docs/metacritic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metacritic.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metacritic.com/about/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://metacritichelp.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Contact
  url: https://www.fabricdata.com/contact
created: '2026-06-13'
description: Metacritic is a review aggregator that collects critic and user scores for games, movies, TV shows, and music, computing a weighted Metascore for each title. The Metacritic API (provided via Fabric Origin / IVA / Gracenote) gives programmatic access to Metascores, user scores, individual critic reviews, publication details, and entertainment rankings for movies and television. Unofficial community-built wrappers also expose game, movie, and TV data from Metacritic's public backend.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metacritic.png
layout: provider
modified: '2026-06-13'
name: Metacritic
nav: Providers
network: true
overview: 'Metacritic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Entertainment, Reviews, Metascore, Games, and Movies.


  Metacritic''s developer surface includes developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 41
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metacritic/refs/heads/main/screenshots/metacritic-2026-06-20T185245.png
security:
- kind: domain-security
  name: Metacritic Domain Security
  slug: metacritic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metacritic
tags:
- Entertainment
- Reviews
- Metascore
- Games
- Movies
- Television
- Music
- Review Aggregator
- Critic Scores
- User Scores
website: https://www.metacritic.com/
---
