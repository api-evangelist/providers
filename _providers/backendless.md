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
- acting_count: 16
  human_in_the_loop: 1
  name: Backendless Agentic Access
  operation_count: 26
  slug: backendless-agentic-access
  summary_line: 26 operations · 16 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Server-side key/value cache.
  name: Backendless Cache API
  slug: backendless-cache-api
- description: Invocation of custom serverless API services.
  name: Backendless CloudCode API
  slug: backendless-cloudcode-api
- description: Thread-safe atomic counters.
  name: Backendless Counters API
  slug: backendless-counters-api
- description: CRUD and search over schema-backed database tables.
  name: Backendless Data API
  slug: backendless-data-api
- description: File and directory storage operations.
  name: Backendless Files API
  slug: backendless-files-api
- description: Geolocation point management and proximity search.
  name: Backendless Geo API
  slug: backendless-geo-api
- description: Publish-subscribe messaging, push notifications, and email.
  name: Backendless Messaging API
  slug: backendless-messaging-api
- description: User registration, authentication, and session management.
  name: Backendless Users API
  slug: backendless-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Backendless REST API
  slug: open-backendless
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/backendless-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backendless-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backendless-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Backendless
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/backendless
- group: company
  title: ''
  type: Website
  url: https://backendless.com
- group: docs
  title: ''
  type: Documentation
  url: https://backendless.com/docs/rest/
- group: commercial
  title: ''
  type: Plans
  url: plans/backendless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/backendless-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/backendless-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://backendless.com/feed/
created: '2026-06-20'
description: Backendless is a visual app development and backend-as-a-service (BaaS) platform that exposes a full set of REST APIs for data persistence, user management, file storage, publish-subscribe messaging, push notifications, geolocation, caching, and atomic counters, plus serverless Cloud Code (custom API services and timers). Requests are authenticated with an application id and REST API key carried in the URL path and a user-token header for authenticated sessions.
finops:
- name: Backendless Finops
  service_category: Developer Tools and Platforms
  slug: backendless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backendless.png
layout: provider
modified: '2026-06-20'
name: Backendless
nav: Providers
network: true
overview: 'Backendless publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Cache API, CloudCode API, Counters API, and 5 more. Tagged areas include BaaS, Backend as a Service, Visual Development, Low Code, and Database.


  Backendless'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Backendless Plans Pricing
  plan_count: 4
  slug: backendless-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 6
  name: Backendless Rate Limits
  slug: backendless-rate-limits
score:
  band: thin
  composite: 40.5
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backendless/refs/heads/main/screenshots/backendless-2026-06-20T172920.png
security:
- kind: authentication
  name: Backendless Authentication
  slug: backendless-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Backendless Domain Security
  slug: backendless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backendless
tags:
- BaaS
- Backend as a Service
- Visual Development
- Low Code
- Database
- Realtime
website: https://backendless.com
---
