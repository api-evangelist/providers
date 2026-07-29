---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salduu-profe-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profe.social
created: '2026-07-17'
description: Salduu, operating as Profe Social at profe.social, is a 500 Global-backed social networking platform. The live host serves Mastodon's default robots.txt (Disallow /search, sitemap.xml.gz) and a Ruby on Rails error stack, indicating the platform runs on Mastodon / ActivityPub fediverse technology, so it exposes the standard Mastodon client REST API and ActivityPub federation endpoints under /api. Both the site and its API surface sit behind a Cloudflare managed challenge, so the instance's own instance metadata, OpenAPI, and developer pages could not be retrieved by a non-browser client during enrichment. This profile records what was directly observed via DNS/TLS/HTTP and well-known probes; the API contract itself remains to be captured once the challenge is cleared or the provider publishes a spec.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salduu-profe-social.png
layout: provider
modified: '2026-07-21'
name: Salduu (Profe Social)
nav: Providers
network: true
overview: Salduu (Profe Social) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Social Networking, Fediverse, and Mastodon.
random_paper: 56
score:
  band: minimal
  composite: 6.1
  delta: -0.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Salduu Profe Social Domain Security
  slug: salduu-profe-social-domain-security
  summary_line: TLSv1.3 · DMARC
slug: salduu-profe-social
tags:
- Company
- Social
- Social Networking
- Fediverse
- Mastodon
- ActivityPub
- Education
website: https://profe.social
---
