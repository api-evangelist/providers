---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Buzzsprout Agentic Access
  operation_count: 5
  slug: buzzsprout-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 2
apis:
- description: The episodes belonging to a Buzzsprout podcast.
  name: Buzzsprout Episodes API
  slug: buzzsprout-episodes-api
- description: The podcasts on a Buzzsprout account.
  name: Buzzsprout Podcasts API
  slug: buzzsprout-podcasts-api
artifact_total: 9
collections:
- collection_type: open
  name: Buzzsprout API
  slug: open-buzzsprout
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buzzsprout-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buzzsprout-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buzzsprout-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buzzsprout
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buzzsprout
- group: company
  title: ''
  type: Website
  url: https://www.buzzsprout.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/buzzsprout/buzzsprout-api
- group: commercial
  title: ''
  type: Plans
  url: plans/buzzsprout-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buzzsprout-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buzzsprout-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.buzzsprout.com/blog
created: '2026-07-05'
description: Buzzsprout is a podcast hosting platform that handles hosting, distribution, promotion, and analytics for podcasters - uploading and optimizing audio, publishing an RSS feed, listing shows in directories like Apple Podcasts and Spotify, and reporting on plays. Buzzsprout also exposes a documented public REST API (base https://www.buzzsprout.com/api) so third parties can programmatically read and manage the podcasts and episodes on an account. The API is RESTful, JSON-serialized, SSL-only, and authenticated with a per-account token.
finops:
- name: Buzzsprout Finops
  service_category: Media and Podcast Hosting
  slug: buzzsprout-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buzzsprout.png
layout: provider
modified: '2026-07-05'
name: Buzzsprout
nav: Providers
network: true
overview: 'Buzzsprout publishes 2 APIs on the [APIs.io](https://apis.io/) network: Episodes API and Podcasts API. Tagged areas include Podcasting, Podcast Hosting, Audio, Media, and Episodes.


  Buzzsprout''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Buzzsprout Plans Pricing
  plan_count: 5
  slug: buzzsprout-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Buzzsprout Rate Limits
  slug: buzzsprout-rate-limits
score:
  band: thin
  composite: 37.6
  delta: -1.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buzzsprout/refs/heads/main/screenshots/buzzsprout-2026-07-25T204129.png
security:
- kind: authentication
  name: Buzzsprout Authentication
  slug: buzzsprout-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buzzsprout Domain Security
  slug: buzzsprout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buzzsprout
tags:
- Podcasting
- Podcast Hosting
- Audio
- Media
- Episodes
- RSS
website: https://www.buzzsprout.com
---
