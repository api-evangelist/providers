---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Acast Agentic Access
  operation_count: 8
  slug: acast-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: Register HTTP callback URLs to receive real-time notifications when events occur on your account - for example when a new episode is published. Webhooks are server-to-endpoint HTTP callbacks, not a bi
  name: Acast Webhooks
  slug: acast-webhooks-api
- description: Place or update ad markers on an episode for dynamic ad insertion.
  name: Acast Ad Markers API
  slug: acast-ad-markers-api
- description: Create, read, update, and delete episodes within a show.
  name: Acast Episodes API
  slug: acast-episodes-api
- description: Read podcast show metadata assigned to the API key's user.
  name: Acast Shows API
  slug: acast-shows-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acast-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acast-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acast
- group: company
  title: ''
  type: Website
  url: https://www.acast.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.acast.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/acast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acast-finops.yml
created: '2026-07-05'
description: Acast is a podcast hosting, distribution, and advertising marketplace that helps creators publish shows, distribute to every major listening platform, and monetize through dynamic ad insertion and sponsorships. Acast exposes a documented public Publishing API for programmatically managing shows and episodes - listing shows and episodes, fetching details, and creating, updating, and deleting episodes - plus placing ad markers and receiving webhook notifications for events like new episode publications. The API is documented openly at developers.acast.com, but access is gated - an X-API-Key credential is issued by Acast's customer success team to accounts on the Ace plan or in the Acast Creator Network.
finops:
- name: Acast Finops
  service_category: Media and Podcasting
  slug: acast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acast.png
layout: provider
modified: '2026-07-05'
name: Acast
nav: Providers
network: true
overview: 'Acast publishes 3 APIs on the [APIs.io](https://apis.io/) network: Ad Markers API, Episodes API, and Shows API. Tagged areas include Podcasting, Podcast Hosting, Publishing, Advertising, and Monetization.


  Acast''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Acast Plans Pricing
  plan_count: 4
  slug: acast-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Acast Rate Limits
  slug: acast-rate-limits
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acast/refs/heads/main/screenshots/acast-2026-07-25T181426.png
security:
- kind: authentication
  name: Acast Authentication
  slug: acast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Acast Domain Security
  slug: acast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acast Vulnerability Disclosure
  slug: acast-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: acast
tags:
- Podcasting
- Podcast Hosting
- Publishing
- Advertising
- Monetization
- Media
- Audio
website: https://www.acast.com
---
