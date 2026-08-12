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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Podbean Agentic Access
  operation_count: 16
  slug: podbean-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 6
apis:
- description: Download, engagement, and advertising reports.
  name: Podbean Analytics API
  slug: podbean-analytics-api
- description: OAuth 2.0 login dialog, token exchange, inspection, and multi-podcast tokens.
  name: Podbean Authentication API
  slug: podbean-authentication-api
- description: List, read, publish, update, and delete podcast episodes.
  name: Podbean Episode API
  slug: podbean-episode-api
- description: Authorize a media/image upload and list uploaded media files.
  name: Podbean File Upload API
  slug: podbean-file-upload-api
- description: Embeddable player markup and metadata for a podcast or episode URL.
  name: Podbean oEmbed API
  slug: podbean-oembed-api
- description: Read the authorized podcast profile and settings.
  name: Podbean Podcast API
  slug: podbean-podcast-api
artifact_total: 14
collections:
- collection_type: open
  name: Podbean API
  slug: open-podbean
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podbean-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podbean-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podbean-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podbean-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/podbean
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podbean
- group: company
  title: ''
  type: Website
  url: https://www.podbean.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.podbean.com/podbean-api-docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/podbean-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podbean-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podbean-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://developers.podbean.com/
- group: company
  title: ''
  type: Blog
  url: https://www.podbean.com/podcast-news
created: '2026-07-05'
description: Podbean is a podcast hosting, distribution, and monetization platform for creators, businesses, and networks. Its public REST API (base https://api.podbean.com/v1) uses OAuth 2.0 and lets third-party apps and integrations manage a user's podcast programmatically - read podcast profiles, list and publish/update/delete episodes, authorize media file uploads, embed players via oEmbed, and pull download, engagement, and advertising analytics reports. Apps can act on behalf of a single podcast (Client Credentials) or across many podcasts (Multiple Podcasts tokens) for agencies and networks.
finops:
- name: Podbean Finops
  service_category: Media and Content Hosting
  slug: podbean-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podbean.png
layout: provider
modified: '2026-07-05'
name: Podbean
nav: Providers
network: true
overview: 'Podbean publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Episode API, and 3 more. Tagged areas include Podcasting, Podcast Hosting, Media, Audio, and Episodes.


  Podbean''s developer surface includes authentication, documentation, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Podbean Plans Pricing
  plan_count: 5
  slug: podbean-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 4
  name: Podbean Rate Limits
  slug: podbean-rate-limits
scopes:
- name: Podbean Scopes
  scope_count: 3
  slug: podbean-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.0
  delta: -0.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 59.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Podbean Authentication
  slug: podbean-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Podbean Domain Security
  slug: podbean-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: podbean
tags:
- Podcasting
- Podcast Hosting
- Media
- Audio
- Episodes
- Analytics
- Monetization
website: https://www.podbean.com
---
