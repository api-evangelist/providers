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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Pandora GraphQL API provides access to Pandora's music catalog and listener data, enabling developers to build applications with playback controls, search, user collection management, feedback (th
  name: Pandora GraphQL API
  slug: pandora-graphql-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pandora-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.pandora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pandora.com/docs/key-concepts/apis/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.pandora.com/docs/key-concepts/authorization-oauth2/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pandora.com/docs/getting-started/accessing-developer-portal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.pandora.com/terms-and-conditions/
- group: company
  title: ''
  type: PartnerAccess
  url: https://developer.pandora.com/docs/overview/partner-access/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/pandora/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/pandora/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/pandora/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Pandora is an internet radio and music streaming service powered by the Music Genome Project, offering personalized radio stations and on-demand streaming with a catalog of over 30 million tracks including songs, comedy albums, podcasts, and more. The Pandora GraphQL API enables developers to build applications that access stations, tracks, artist information, user listening history, feedback, playlists, and personalized radio content across Free, Plus, and Premium subscription tiers.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Pandora ERC-404 is an experimental mixed ERC-20/ERC-721 token standard developed by Pandora Labs Org. It enables native liquidity and fractionalization of NFTs by combining both standards into a singl
  name: Pandora ERC-404 GraphQL
  slug: pandora-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pandora.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Pandora
nav: Providers
network: true
overview: 'Pandora publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Music, Streaming, Radio, Podcasts, and Music Genome Project.


  The Pandora catalog on APIs.io includes 1 JSON-LD context.


  Pandora''s developer surface includes developer portal, documentation, authentication, getting-started guide, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 145
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 39.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pandora/refs/heads/main/screenshots/pandora-2026-06-20T191335.png
security:
- kind: domain-security
  name: Pandora Domain Security
  slug: pandora-domain-security
  summary_line: TLSv1.2 · DMARC
slug: pandora
tags:
- Music
- Streaming
- Radio
- Podcasts
- Music Genome Project
- Personalization
website: https://developer.pandora.com/
---
