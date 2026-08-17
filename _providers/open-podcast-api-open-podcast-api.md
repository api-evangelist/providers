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
api_count: 6
apis:
- description: Authenticate users against an Open Podcast compliant server, establishing the session used for subsequent subscription, action, and device endpoints.
  name: Open Podcast Authentication API
  slug: authentication-api
- description: Synchronize a user's podcast subscriptions across clients, including adding and removing feed URLs and retrieving the current subscription set per device.
  name: Open Podcast Subscriptions API
  slug: subscriptions-api
- description: Record and synchronize per-episode listening actions such as play, pause, download, delete, and flag, including timestamp and position metadata.
  name: Open Podcast Episode Actions API
  slug: episode-actions-api
- description: Register and manage the devices a user syncs from, allowing servers to track per-device subscription state and last-sync timestamps.
  name: Open Podcast Devices API
  slug: devices-api
- description: Synchronize a user's favorited episodes across clients so that liked or starred items remain consistent regardless of which app or device the user is on.
  name: Open Podcast Favorites API
  slug: favorites-api
- description: Synchronize the user's playback queue (up-next list) across clients, including ordering, additions, and removals of episodes.
  name: Open Podcast Queue API
  slug: queue-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-podcast-api-open-podcast-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openpodcastapi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openpodcastapi.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openpodcastapi
- group: operate
  title: ''
  type: Forums
  url: https://github.com/orgs/openpodcastapi/discussions
- group: other
  title: ''
  type: Matrix Chat
  url: https://matrix.to/#/#openpodcastapi:matrix.org
created: '2025-05-02'
description: The Open Podcast API is an initiative aiming to provide a feature-complete synchronization API specification for podcast (web) apps and user-focused servers. The specification covers synchronization of subscriptions, listening progress, favorites, queues, and device state across compliant clients and self-hosted servers, with the goal of giving listeners portable control of their podcast data.
finops:
- name: Open Podcast Api Open Podcast Api Finops
  service_category: API
  slug: open-podcast-api-open-podcast-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-podcast-api-open-podcast-api.png
layout: provider
modified: '2026-04-28'
name: Open Podcast API
nav: Providers
network: true
overview: 'Open Podcast API publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Episodes, Open Standards, Podcasts, and Subscriptions.


  Open Podcast API''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Open Podcast Api Open Podcast Api Plans Pricing
  plan_count: 3
  slug: open-podcast-api-open-podcast-api-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Open Podcast Api Open Podcast Api Rate Limits
  slug: open-podcast-api-open-podcast-api-rate-limits
score:
  band: emerging
  composite: 14.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-podcast-api-open-podcast-api/refs/heads/main/screenshots/open-podcast-api-open-podcast-api-2026-06-20T190848.png
security:
- kind: domain-security
  name: Open Podcast Api Open Podcast Api Domain Security
  slug: open-podcast-api-open-podcast-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: open-podcast-api-open-podcast-api
tags:
- Audio
- Episodes
- Open Standards
- Podcasts
- Subscriptions
- Sync
website: https://openpodcastapi.org/
---
