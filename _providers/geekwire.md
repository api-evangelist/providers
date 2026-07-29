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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: GeekWire provides RSS feeds for its main news stream and individual topic categories including Microsoft, Space, Science, Real Estate, Games, Google, Mobile, GeekLife, Podcasts, and Apple. These Atom/
  name: GeekWire RSS Feed
  slug: rss-feed
- description: GeekWire is built on WordPress and exposes the standard WordPress REST API, providing JSON endpoints for accessing posts, categories, tags, authors, and other content types. The API is available at th
  name: GeekWire WordPress REST API
  slug: wordpress-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geekwire-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geekwire
- group: company
  title: ''
  type: Website
  url: https://www.geekwire.com/
- group: company
  title: ''
  type: About
  url: https://www.geekwire.com/about-geekwire/
- group: operate
  title: ''
  type: Contact
  url: https://www.geekwire.com/contact-us/
- group: other
  title: ''
  type: RSSFeeds
  url: https://www.geekwire.com/rss-feeds/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.geekwire.com/feed/
- group: company
  title: ''
  type: Newsletter
  url: https://www.geekwire.com/newsletter/
- group: other
  title: ''
  type: JobBoard
  url: https://www.geekwire.com/jobs/
- group: other
  title: ''
  type: Advertising
  url: https://www.geekwire.com/advertise/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geekwire.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geekwire.com/termsofuse/
- group: other
  title: ''
  type: Podcast
  url: https://podcasts.apple.com/us/podcast/geekwire/id427374434
- group: other
  title: ''
  type: Podcast
  url: https://open.spotify.com/show/2PPEGel5l0v3XxlD8fVxAh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geekwire
- group: other
  title: ''
  type: X
  url: https://x.com/geekwire
created: '2026-03-24'
description: GeekWire is a leading technology news site covering startups, innovation, and the Pacific Northwest tech scene. Founded in Seattle, GeekWire delivers breaking news, analysis, and commentary on technology, business, and entrepreneurship, with a particular focus on companies like Amazon, Microsoft, and the broader Seattle and Pacific Northwest startup ecosystem. GeekWire also operates GeekWork, a technology job board, and produces popular podcasts and weekly radio programming.
finops:
- name: Geekwire Finops
  service_category: API
  slug: geekwire-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geekwire.png
layout: provider
modified: '2026-04-28'
name: GeekWire
nav: Providers
network: true
overview: 'GeekWire publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Media, Startups, and Technology News.'
plans:
- name: Geekwire Plans Pricing
  plan_count: 3
  slug: geekwire-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Geekwire Rate Limits
  slug: geekwire-rate-limits
score:
  band: thin
  composite: 30.9
  delta: -3.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geekwire/refs/heads/main/screenshots/geekwire-2026-06-20T181712.png
security:
- kind: domain-security
  name: Geekwire Domain Security
  slug: geekwire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: geekwire
tags:
- Media
- Startups
- Technology News
website: https://www.geekwire.com/
---
