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
api_count: 3
apis:
- description: Netflix Zuul is an L7 application gateway built on Netty that provides dynamic routing, load balancing, authentication, monitoring, and resiliency for edge services. Zuul 3.x is the current release, s
  name: Netflix Zuul Gateway
  slug: netflix-zuul-gateway
- description: The Zuul Filters API provides the core extension point for building custom logic into the Zuul gateway pipeline. Developers implement inbound, endpoint, and outbound filters using synchronous or async
  name: Netflix Zuul Filters API
  slug: netflix-zuul-filters-api
- description: Zuul Push Messaging enables server-to-client push communications over WebSockets and Server Sent Events (SSE). It provides a PushConnectionRegistry for managing connected clients and supports distribu
  name: Netflix Zuul Push Messaging
  slug: netflix-zuul-push-messaging
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/Netflix/zuul
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netflix
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Netflix/zuul
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Netflix/zuul/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Netflix/zuul/wiki/Getting-Started-3.0
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Netflix/zuul/releases
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/Netflix/zuul/issues
- group: company
  title: ''
  type: Blog
  url: https://netflixtechblog.com/open-sourcing-zuul-2-82ea476cb2b3
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/netflix-zuul
created: '2026-03-16'
description: Netflix Zuul is an open-source L7 application gateway that provides dynamic routing, monitoring, resiliency, and security for edge services. Originally developed by Netflix, Zuul 2 uses Netty for non-blocking I/O and is commonly used as an API gateway and edge service.
finops:
- name: Netflix Zuul Finops
  service_category: API
  slug: netflix-zuul-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netflix-zuul.png
layout: provider
modified: '2026-04-28'
name: Netflix Zuul
nav: Providers
network: true
overview: 'Netflix Zuul publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Gateway, Edge Service, Netflix, and Open Source.


  Netflix Zuul''s developer surface includes documentation, getting-started guide, changelog, engineering blog, Stack Overflow tag, and 4 more developer resources.'
plans:
- name: Netflix Zuul Plans Pricing
  plan_count: 3
  slug: netflix-zuul-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Netflix Zuul Rate Limits
  slug: netflix-zuul-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netflix-zuul/refs/heads/main/screenshots/netflix-zuul-2026-06-20T190156.png
slug: netflix-zuul
tags:
- API Gateway
- Edge Service
- Netflix
- Open Source
---
