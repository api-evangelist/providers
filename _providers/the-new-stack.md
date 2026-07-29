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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: RSS feed providing the latest articles and news from The New Stack covering cloud native, DevOps, AI, and open source technologies. Feed follows RSS 2.0 with Dublin Core and WordPress content extensio
  name: The New Stack RSS Feed
  slug: rss
- description: RSS feed for The New Stack podcast, featuring discussions with developers, engineers, and operations professionals building at-scale architectures. Hosted on Simplecast.
  name: The New Stack Podcast Feed
  slug: podcast-rss
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-new-stack-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thenewstack
- group: company
  title: ''
  type: Website
  url: https://thenewstack.io/
- group: company
  title: ''
  type: About
  url: https://thenewstack.io/about-and-contact-info/
- group: other
  title: ''
  type: RSS
  url: https://thenewstack.io/rss-feeds/
- group: other
  title: ''
  type: RSS
  url: https://thenewstack.io/feed/
- group: company
  title: ''
  type: Newsletter
  url: https://thenewstack.io/newsletter/
- group: other
  title: ''
  type: Podcast
  url: https://thenewstack.io/podcasts/
- group: other
  title: ''
  type: Podcast
  url: https://thenewstack.simplecast.com/
- group: other
  title: ''
  type: Podcast
  url: https://open.spotify.com/show/2nj1mpDb9jxHxi9vjZvDdk
- group: other
  title: ''
  type: Contribute
  url: https://thenewstack.io/contributions/
- group: other
  title: ''
  type: Sponsorship
  url: https://thenewstack.io/sponsorship/
- group: other
  title: ''
  type: Events
  url: https://thenewstack.io/events/
- group: learn
  title: ''
  type: Webinars
  url: https://thenewstack.io/webinars/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thenewstack.io/privacy-policy/
- group: other
  title: ''
  type: X
  url: https://x.com/thenewstack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-new-stack
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/thenewstack/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/thenewstack
created: '2024-01-01'
description: The New Stack is a tech media platform covering cloud native, DevOps, AI, and open source technologies, providing news, analysis, podcasts, webinars, and ebooks for developers, software engineers, and operations professionals. Public data access is available via RSS feeds for articles and podcasts.
examples:
- key_count: 3
  name: The New Stack Rss Feed Example
  slug: the-new-stack-rss-feed-example
finops:
- name: The New Stack Finops
  service_category: API
  slug: the-new-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-new-stack.png
json_schemas:
- name: The New Stack RSS Article Item
  property_count: 8
  slug: the-new-stack-article
json_structures:
- name: The New Stack Rss Feed Structure
  property_count: 0
  slug: the-new-stack-rss-feed-structure
jsonld:
- class_count: 1
  name: The New Stack Context
  property_count: 17
  slug: the-new-stack-context
layout: provider
modified: '2026-05-03'
name: The New Stack
nav: Providers
network: true
overview: 'The New Stack publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, DevOps, Media, and Technology News.


  The The New Stack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The New Stack''s developer surface includes YouTube channel and 18 more developer resources.'
plans:
- name: The New Stack Plans Pricing
  plan_count: 3
  slug: the-new-stack-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: The New Stack Rate Limits
  slug: the-new-stack-rate-limits
rules:
- name: The New Stack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: the-new-stack-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.9
  delta: -4.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 35.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-new-stack/refs/heads/main/screenshots/the-new-stack-2026-06-20T195228.png
security:
- kind: domain-security
  name: The New Stack Domain Security
  slug: the-new-stack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: the-new-stack
tags:
- Cloud Native
- DevOps
- Media
- Technology News
website: https://thenewstack.io/
---
