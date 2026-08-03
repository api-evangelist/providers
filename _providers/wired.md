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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Wired provides standard RSS feeds for its main content stream and individual topic categories including Business, Science, Security, Politics, Gear, Ideas, Culture, and AI. These feeds allow developer
  name: Wired RSS Feed
  slug: rss-feed
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wired-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wired.com/
- group: company
  title: ''
  type: About
  url: https://www.wired.com/about/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/rss
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/category/business/latest/rss
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/category/science/latest/rss
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/category/security/latest/rss
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/category/gear/latest/rss
- group: other
  title: ''
  type: RSSFeed
  url: https://www.wired.com/feed/tag/ai/latest/rss
- group: other
  title: ''
  type: Subscription
  url: https://subscribe.wired.com/
- group: company
  title: ''
  type: Newsletter
  url: https://www.wired.com/newsletter/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.condenast.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.condenast.com/user-agreement
- group: other
  title: ''
  type: Advertising
  url: https://www.wired.com/about/advertising-info/
- group: company
  title: ''
  type: Careers
  url: https://www.condenast.com/careers/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/wired
- group: other
  title: ''
  type: X
  url: https://x.com/wired
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wired
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/wired/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@wired
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/json-ld/wired-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/vocabulary/wired-vocabulary.yml
created: '2026-03-24'
description: Wired (wired.com) is an American technology and culture magazine published by Condé Nast, covering how emerging technologies affect culture, the economy, and politics. Founded in 1993, Wired provides RSS feeds for programmatic content consumption across categories including Business, Science, Security, Politics, Gear, Ideas, Culture, and AI. The magazine also maintains a YouTube channel, newsletters, and social media presence.
examples:
- key_count: 10
  name: Wired Article Example
  slug: wired-article-example
finops:
- name: Wired Finops
  service_category: API
  slug: wired-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wired.png
json_schemas:
- name: Wired Article
  property_count: 10
  slug: wired-article
json_structures:
- name: Wired Article Structure
  property_count: 0
  slug: wired-article-structure
jsonld:
- class_count: 18
  name: Wired Context
  property_count: 1
  slug: wired-context
layout: provider
modified: '2026-05-03'
name: Wired
nav: Providers
network: true
overview: 'Wired publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Content, Innovation, Media, News, and RSS.


  The Wired catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wired''s developer surface includes YouTube channel and 21 more developer resources.'
plans:
- name: Wired Plans Pricing
  plan_count: 3
  slug: wired-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Wired Rate Limits
  slug: wired-rate-limits
rules:
- name: Wired API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wired-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 34.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wired/refs/heads/main/screenshots/wired-2026-06-20T201521.png
security:
- kind: domain-security
  name: Wired Domain Security
  slug: wired-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wired
tags:
- Content
- Innovation
- Media
- News
- RSS
- Science
- Technology News
website: https://www.wired.com/
---
