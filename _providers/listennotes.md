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
- acting_count: 5
  human_in_the_loop: 0
  name: Listennotes Agentic Access
  operation_count: 26
  slug: listennotes-agentic-access
  summary_line: 26 operations · 5 acting
api_count: 5
apis:
- description: Endpoints to fetch podcasts, episodes, charts, and reference data.
  name: Listen Notes Directory API API
  slug: listennotes-directory-api-api
- description: Endpoints to get insights of podcasts, e.g., audience demographics.
  name: Listen Notes Insights API API
  slug: listennotes-insights-api-api
- description: Endpoints to fetch Listen Later playlists data.
  name: Listen Notes Playlist API API
  slug: listennotes-playlist-api-api
- description: Endpoints to improve the podcast database.
  name: Listen Notes Podcaster API API
  slug: listennotes-podcaster-api-api
- description: Endpoints to search podcasts and episodes.
  name: Listen Notes Search API API
  slug: listennotes-search-api-api
artifact_total: 12
collections:
- collection_type: open
  name: Listen API (Listen Notes)
  slug: open-listennotes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/listennotes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listennotes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listennotes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ListenNotes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listen-notes
- group: company
  title: ''
  type: Website
  url: https://www.listennotes.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.listennotes.com/api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/listennotes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/listennotes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/listennotes-finops.yml
created: '2026-07-03'
description: Listen Notes runs the largest podcast search engine and database, and exposes it as the Listen API - a simple, no-nonsense podcast search, directory, and insights REST API. It lets developers full-text search millions of podcasts and episodes by people, places, and topics; fetch podcast and episode metadata; browse best-podcasts charts, curated lists, and genres; retrieve podcast/episode recommendations; power typeahead autocomplete; and pull audience demographics and publisher-domain insights. The API is served at https://listen-api.listennotes.com/api/v2 and authenticated with an X-ListenAPI-Key header, with FREE, PRO, and ENTERPRISE plans billed on a request basis.
finops:
- name: Listennotes Finops
  service_category: Search and Media APIs
  slug: listennotes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listennotes.png
layout: provider
modified: '2026-07-03'
name: Listen Notes
nav: Providers
network: true
overview: 'Listen Notes publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Directory API API, Insights API API, Playlist API API, and 2 more. Tagged areas include Podcasts, Podcast Search, Podcast Directory, Search, and Audio.


  Listen Notes'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Listennotes Plans Pricing
  plan_count: 3
  slug: listennotes-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 8
  name: Listennotes Rate Limits
  slug: listennotes-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listennotes/refs/heads/main/screenshots/listennotes-2026-07-25T225323.png
security:
- kind: authentication
  name: Listennotes Authentication
  slug: listennotes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listennotes Domain Security
  slug: listennotes-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: listennotes
tags:
- Podcasts
- Podcast Search
- Podcast Directory
- Search
- Audio
- Media
- Podcast Insights
website: https://www.listennotes.com/api/
---
