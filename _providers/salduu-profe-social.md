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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
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
random_paper: 8
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salduu-profe-social/refs/heads/main/screenshots/salduu-profe-social-2026-09-02T154317.png
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
