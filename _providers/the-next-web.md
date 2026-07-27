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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The Next Web provides an RSS 2.0 feed updated hourly with the latest technology news, analysis, and articles published on thenextweb.com. The feed covers topics including artificial intelligence, star
  name: TNW RSS Feed
  slug: the-next-web-rss-feed
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-next-web-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thenextweb.com/
- group: other
  title: ''
  type: RSS
  url: https://thenextweb.com/feed/
- group: company
  title: ''
  type: News
  url: https://thenextweb.com/latest
- group: company
  title: ''
  type: Newsletter
  url: https://thenextweb.com/newsletters
- group: other
  title: ''
  type: Events
  url: https://thenextweb.com/events
- group: other
  title: ''
  type: Events
  url: https://thenextweb.com/conference
- group: company
  title: ''
  type: About
  url: https://thenextweb.com/about
- group: other
  title: ''
  type: Advertising
  url: https://thenextweb.com/advertise
- group: other
  title: ''
  type: Marketplace
  url: https://deals.thenextweb.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thenextweb.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thenextweb.com/terms-of-service
- group: operate
  title: ''
  type: Contact
  url: https://thenextweb.com/contact
- group: other
  title: ''
  type: X
  url: https://x.com/thenextweb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-next-web
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/thenextweb/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thenextweb
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/the-next-web-article-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/the-next-web-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/the-next-web-vocabulary.yml
created: '2026-03-24'
description: The Next Web is a leading online media organization covering technology news, business, and culture. Founded in 2006, TNW reports on startups, innovation, artificial intelligence, digital culture, and the future of work. The primary programmatic access to TNW content is through its RSS 2.0 feed, which is updated hourly with the latest articles across all topic areas. Category-specific feeds are also available for Deep Tech, Plugged (consumer tech), and Sustainability. TNW also organizes the annual TNW Conference and operates a technology events business.
finops:
- name: The Next Web Finops
  service_category: API
  slug: the-next-web-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-next-web.png
json_schemas:
- name: TNW RSS Article
  property_count: 8
  slug: the-next-web-article
json_structures:
- name: The Next Web Article Structure
  property_count: 0
  slug: the-next-web-article-structure
jsonld:
- class_count: 12
  name: The Next Web Context
  property_count: 4
  slug: the-next-web-context
layout: provider
modified: '2026-05-03'
name: The Next Web
nav: Providers
network: true
overview: 'The Next Web publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Technology News, Innovation, Media, Events, and Startups.


  The The Next Web catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Next Web''s developer surface includes product news, GitHub presence, and 18 more developer resources.'
plans:
- name: The Next Web Plans Pricing
  plan_count: 3
  slug: the-next-web-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: The Next Web Rate Limits
  slug: the-next-web-rate-limits
rules:
- name: The Next Web API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-next-web-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 40.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-next-web/refs/heads/main/screenshots/the-next-web-2026-06-20T195230.png
security:
- kind: domain-security
  name: The Next Web Domain Security
  slug: the-next-web-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-next-web
tags:
- Technology News
- Innovation
- Media
- Events
- Startups
- Artificial Intelligence
website: https://thenextweb.com/
---
