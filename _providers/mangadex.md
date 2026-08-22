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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Manga Database and Community
  name: MangaDex
  slug: mangadex
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mangadex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.mangadex.org/docs.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Manga Database and Community
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mangadex.png
layout: provider
modified: '2026-05-28'
name: MangaDex
nav: Providers
network: true
overview: MangaDex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anime and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mangadex/refs/heads/main/screenshots/mangadex-2026-06-20T184915.png
security:
- kind: domain-security
  name: Mangadex Domain Security
  slug: mangadex-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mangadex
tags:
- Anime
- Public APIs
website: https://api.mangadex.org/docs.html
---
