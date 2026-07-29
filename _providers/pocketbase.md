---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 5
apis:
- description: CRUD operations for collection records including list, view, create, update, delete, and batch operations. Supports filtering, sorting, pagination, relation expansion, field selection, and multipart f
  name: PocketBase Records API
  slug: records-api
- description: Authentication endpoints supporting password-based login, OAuth2 providers, one-time passwords, token refresh, email verification, password reset, email change confirmation, and superuser impersonatio
  name: PocketBase Authentication API
  slug: authentication-api
- description: Server-Sent Events (SSE) based real-time subscriptions for create, update, and delete record events across individual records or entire collections. Connections auto-disconnect after 5 minutes of inac
  name: PocketBase Realtime API
  slug: realtime-api
- description: File download, thumbnail generation, and protected file token generation. File uploads are handled through the Records API using multipart form data. Supports on-the-fly image resizing and forced down
  name: PocketBase Files API
  slug: files-api
- description: Superuser-only endpoints for listing and updating application settings, testing S3 storage connectivity, sending test emails, generating Apple OAuth2 client secrets, and configuring rate-limiting rule
  name: PocketBase Settings API
  slug: settings-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pocketbase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pocketbase.io
- group: docs
  title: ''
  type: Documentation
  url: https://pocketbase.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pocketbase
- group: company
  title: ''
  type: Blog
  url: https://github.com/pocketbase/pocketbase/releases
- group: commercial
  title: ''
  type: Pricing
  url: https://pocketbase.io/faq/
- group: other
  title: ''
  type: X
  url: https://x.com/pocketbase
- group: commercial
  title: ''
  type: Plans
  url: plans/pocketbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pocketbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pocketbase-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/pocketbase-context.jsonld
created: '2026-06-12'
description: PocketBase is an open-source backend-as-a-service delivered as a single executable, providing a REST API for managing collections, records, authentication, file uploads, real-time subscriptions via Server-Sent Events, and admin management through a built-in dashboard. It embeds SQLite for persistent storage and supports OAuth2, OTP, and password-based authentication out of the box. Developers can extend PocketBase with custom business logic using Go or JavaScript hooks and event handlers. Official SDKs for JavaScript and Dart make client integration straightforward across web, mobile, and desktop platforms.
finops:
- name: Pocketbase Finops
  service_category: ''
  slug: pocketbase-finops
graphqls:
- description: PocketBase is a REST-only backend-as-a-service. It does not provide a native GraphQL API. All data operations are performed through a REST-ish HTTP API served at `{your-instance}/api/`, with endpoints
  name: PocketBase GraphQL API
  slug: pocketbase-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pocketbase.png
jsonld:
- class_count: 10
  name: Pocketbase Context
  property_count: 11
  slug: pocketbase-context
layout: provider
modified: '2026-06-12'
name: PocketBase
nav: Providers
network: true
overview: 'PocketBase publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Backend-as-a-Service, Open Source, SQLite, Realtime, and Authentication.


  The PocketBase catalog on APIs.io includes 1 JSON-LD context.


  PocketBase''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Pocketbase Plans Pricing
  plan_count: 1
  slug: pocketbase-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Pocketbase Rate Limits
  slug: pocketbase-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 6.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.6
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/pocketbase/refs/heads/main/screenshots/pocketbase-2026-06-20T191826.png
security:
- kind: domain-security
  name: Pocketbase Domain Security
  slug: pocketbase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pocketbase
tags:
- Backend-as-a-Service
- Open Source
- SQLite
- Realtime
- Authentication
- File Storage
- REST API
- Self-Hosted
- Go
website: https://pocketbase.io
---
