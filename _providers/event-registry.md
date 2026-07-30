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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Event Registry Agentic Access
  operation_count: 12
  slug: event-registry-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 5
apis:
- description: Search and retrieve individual news articles from 150,000+ global sources.
  name: Event Registry Articles API
  slug: event-registry-articles-api
- description: Search and retrieve clustered news events (deduplicated story groups).
  name: Event Registry Events API
  slug: event-registry-events-api
- description: Resolve entity names to URIs for use in search filters.
  name: Event Registry Suggest API
  slug: event-registry-suggest-api
- description: Retrieve content matching user-defined topic page configurations.
  name: Event Registry Topic Pages API
  slug: event-registry-topic-pages-api
- description: Monitor API token quota and usage.
  name: Event Registry Usage API
  slug: event-registry-usage-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/event-registry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/event-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/event-registry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://eventregistry.org
- group: docs
  title: ''
  type: Documentation
  url: https://newsapi.ai/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/EventRegistry
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/event-registry/
- group: company
  title: ''
  type: Blog
  url: https://newsapi.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://newsapi.ai/plans
- group: other
  title: ''
  type: X
  url: https://x.com/event_registry
- group: commercial
  title: ''
  type: Plans
  url: plans/event-registry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/event-registry-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/event-registry-finops.yml
created: 2026-06-13
description: Event Registry (NewsAPI.ai) is the world's leading news intelligence platform providing a REST API for accessing global news articles, trending topics, event detection, named entities, sentiment analysis, and media monitoring across 150,000+ sources in 60+ languages, with historical archive access dating back to 2014.
examples:
- key_count: 4
  name: Search Articles
  slug: search-articles
- key_count: 4
  name: Search Events
  slug: search-events
- key_count: 5
  name: Suggest Concepts
  slug: suggest-concepts
finops:
- name: Event Registry Finops
  service_category: ''
  slug: event-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/event-registry.png
json_schemas:
- name: Article
  property_count: 19
  slug: article
- name: Event
  property_count: 14
  slug: event
jsonld:
- class_count: 40
  name: context Context
  property_count: 1
  slug: context
layout: provider
modified: 2026-06-13
name: Event Registry
nav: Providers
network: true
overview: 'Event Registry publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Events API, Suggest API, and 2 more. Tagged areas include News, Media Monitoring, News Intelligence, Event Detection, and Named Entity Recognition.


  The Event Registry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Event Registry''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Event Registry Plans Pricing
  plan_count: 5
  slug: event-registry-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Event Registry Rate Limits
  slug: event-registry-rate-limits
rules:
- name: Event Registry API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: event-registry-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 51.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/event-registry/refs/heads/main/screenshots/event-registry-2026-06-20T180857.png
security:
- kind: authentication
  name: Event Registry Authentication
  slug: event-registry-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Event Registry Domain Security
  slug: event-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: event-registry
tags:
- News
- Media Monitoring
- News Intelligence
- Event Detection
- Named Entity Recognition
- Sentiment Analysis
- Media Analytics
- News API
website: https://eventregistry.org
---
