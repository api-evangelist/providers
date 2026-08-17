---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Transistor Agentic Access
  operation_count: 23
  slug: transistor-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 6
apis:
- description: The authenticated user account.
  name: Transistor Account API
  slug: transistor-account-api
- description: Download analytics for shows and episodes.
  name: Transistor Analytics API
  slug: transistor-analytics-api
- description: Podcast episodes, drafts, uploads, and publishing.
  name: Transistor Episodes API
  slug: transistor-episodes-api
- description: Podcasts (shows) in your Transistor account.
  name: Transistor Shows API
  slug: transistor-shows-api
- description: Private (subscriber-only) podcast subscribers.
  name: Transistor Subscribers API
  slug: transistor-subscribers-api
- description: Event webhook subscriptions.
  name: Transistor Webhooks API
  slug: transistor-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Transistor Account API
  slug: open-transistor-account-api
- collection_type: open
  name: Transistor Account Analytics API
  slug: open-transistor-analytics-api
- collection_type: open
  name: Transistor Account Episodes API
  slug: open-transistor-episodes-api
- collection_type: open
  name: Transistor Account Shows API
  slug: open-transistor-shows-api
- collection_type: open
  name: Transistor Account Subscribers API
  slug: open-transistor-subscribers-api
- collection_type: open
  name: Transistor Account Webhooks API
  slug: open-transistor-webhooks-api
- collection_type: open
  name: Transistor API
  slug: open-transistor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/transistor-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/transistor-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transistor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transistor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transistor-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transistorfm
- group: company
  title: ''
  type: Website
  url: https://transistor.fm
- group: docs
  title: ''
  type: Documentation
  url: https://developers.transistor.fm/
- group: commercial
  title: ''
  type: Plans
  url: plans/transistor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transistor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/transistor-finops.yml
created: '2026-07-05'
description: Transistor is a podcast hosting and analytics platform that lets teams host unlimited shows, distribute episodes to Apple Podcasts, Spotify, and YouTube, run private (subscriber-only) podcasts, and measure downloads with advanced analytics. Transistor exposes a documented public REST API at https://api.transistor.fm/v1 that follows the JSON:API specification, is authenticated with an x-api-key header, and covers shows, episodes, analytics, private podcast subscribers, and event webhooks.
finops:
- name: Transistor Finops
  service_category: Media and Podcast Hosting
  slug: transistor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transistor.png
layout: provider
modified: '2026-07-05'
name: Transistor
nav: Providers
network: true
overview: 'Transistor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Episodes API, and 3 more. Tagged areas include Podcasting, Podcast Hosting, Analytics, Media, and Audio.


  Transistor''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Transistor Plans Pricing
  plan_count: 4
  slug: transistor-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Transistor Rate Limits
  slug: transistor-rate-limits
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Transistor Authentication
  slug: transistor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Transistor Domain Security
  slug: transistor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transistor Vulnerability Disclosure
  slug: transistor-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Transistor Trust Center
  slug: transistor-trust-center
  summary_line: SOC 2, ISO 27001
slug: transistor
tags:
- Podcasting
- Podcast Hosting
- Analytics
- Media
- Audio
- JSON:API
website: https://transistor.fm
---
