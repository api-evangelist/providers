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
    agentic_access: derived
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hacker News Agentic Access
  operation_count: 10
  slug: hacker-news-agentic-access
  summary_line: 10 operations
api_count: 4
apis:
- description: Stories, comments, jobs, Ask HNs, polls, and pollopts.
  name: Hacker News Items API
  slug: hacker-news-items-api
- description: Top, new, best, ask, show, and job story lists.
  name: Hacker News Lists API
  slug: hacker-news-lists-api
- description: Max item ID and recent updates.
  name: Hacker News Live API
  slug: hacker-news-live-api
- description: User profiles.
  name: Hacker News Users API
  slug: hacker-news-users-api
artifact_total: 10
collections:
- collection_type: open
  name: Hacker News API
  slug: open-hacker-news
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hacker-news-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hacker-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://news.ycombinator.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/HackerNews/API
- group: docs
  title: ''
  type: Guidelines
  url: https://news.ycombinator.com/newsguidelines.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://news.ycombinator.com/legal
- group: auth
  title: ''
  type: Security
  url: https://news.ycombinator.com/security.html
- group: start
  title: ''
  type: Portal
  url: https://news.ycombinator.com/lists
- group: other
  title: ''
  type: RSS
  url: https://news.ycombinator.com/rss
- group: operate
  title: ''
  type: Forums
  url: https://news.ycombinator.com/ask
- group: other
  title: ''
  type: Showcase
  url: https://news.ycombinator.com/show
- group: company
  title: ''
  type: About
  url: https://www.ycombinator.com/
created: '2026-03-24'
description: Hacker News is Y Combinator's technology news aggregation and discussion platform. It exposes a public, read-only Firebase-backed API that gives developers real-time access to stories, comments, jobs, polls, and user profiles across the full HN dataset.
finops:
- name: Hacker News Finops
  service_category: API
  slug: hacker-news-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hacker-news.png
layout: provider
modified: '2026-05-19'
name: Hacker News
nav: Providers
network: true
overview: 'Hacker News publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Items API, Lists API, Live API, and 1 more. Tagged areas include Developer Community, Technology News, and Y Combinator.


  Hacker News'' developer surface includes documentation, developer portal, and 10 more developer resources.'
plans:
- name: Hacker News Plans Pricing
  plan_count: 3
  slug: hacker-news-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Hacker News Rate Limits
  slug: hacker-news-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -1.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.8
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hacker-news/refs/heads/main/screenshots/hacker-news-2026-06-20T182448.png
security:
- kind: domain-security
  name: Hacker News Domain Security
  slug: hacker-news-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hacker-news
tags:
- Developer Community
- Technology News
- Y Combinator
website: https://news.ycombinator.com/
---
