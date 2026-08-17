---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API and supports search across podcast series, episod
  name: Podcast API (Taddy)
  slug: podcast-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podcast-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listen-notes
- group: company
  title: ''
  type: Website
  url: https://taddy.org
- group: docs
  title: ''
  type: Documentation
  url: https://taddy.org/developers/podcast-api
created: '2025-05-02'
description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API, the Podcast API supports search across podcast series, episode details, transcripts, top charts, popularity data, and webhook subscriptions.
finops:
- name: Podcast Api Finops
  service_category: API
  slug: podcast-api-finops
graphqls:
- description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API and supports search across podcast series, episod
  name: Podcast API GraphQL API
  slug: podcast-api-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podcast-api.png
layout: provider
modified: '2026-04-28'
name: Podcast API
nav: Providers
network: true
overview: 'Podcast API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasts, Podcasting, Episodes, Transcripts, and Search.


  Podcast API''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Podcast Api Plans Pricing
  plan_count: 3
  slug: podcast-api-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Podcast Api Rate Limits
  slug: podcast-api-rate-limits
score:
  band: minimal
  composite: 12.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podcast-api/refs/heads/main/screenshots/podcast-api-2026-06-20T191829.png
security:
- kind: domain-security
  name: Podcast Api Domain Security
  slug: podcast-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: podcast-api
tags:
- Podcasts
- Podcasting
- Episodes
- Transcripts
- Search
- GraphQL
- Webhooks
website: https://taddy.org
---
