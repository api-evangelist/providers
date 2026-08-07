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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: Auto-generated RESTful API for managing collections, globals, media uploads, users, and preferences. Mounted at /api/{collection-slug} with full CRUD operations plus authentication endpoints.
  name: Payload CMS REST API
  slug: rest-api
- description: 'Fully featured GraphQL API exposed at /api/graphql with auto-generated types for all collections and globals. Includes a GraphQL Playground at /api/graphql-playground and supports complexity limiting '
  name: Payload CMS GraphQL API
  slug: graphql-api
- description: Server-side Node.js API for direct database interaction without HTTP overhead. Supports all collection and global operations including authentication, ideal for React Server Components and server-side
  name: Payload CMS Local API
  slug: local-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payloadcms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payloadcms.com
- group: docs
  title: ''
  type: Documentation
  url: https://payloadcms.com/docs/getting-started/what-is-payload
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/payloadcms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payload-cms
- group: company
  title: ''
  type: Blog
  url: https://payloadcms.com/posts/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://payloadcms.com/cloud
- group: other
  title: ''
  type: X
  url: https://x.com/payloadcms
- group: commercial
  title: ''
  type: Plans
  url: plans/payloadcms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payloadcms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payloadcms-finops.yml
created: '2026-06-13'
description: Open-source headless CMS and fullstack Next.js framework providing automatic REST and GraphQL APIs for managing collections, globals, media, users, and custom fields in self-hosted or cloud deployments.
finops:
- name: Payloadcms Finops
  service_category: ''
  slug: payloadcms-finops
graphqls:
- description: 'Payload CMS ships a fully featured GraphQL API generated automatically from your collection and global configurations. Every collection defined in your Payload config produces a set of strongly-typed '
  name: Payload CMS GraphQL API
  slug: payloadcms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payloadcms.png
layout: provider
modified: '2026-06-13'
name: Payload CMS
nav: Providers
network: true
overview: 'Payload CMS publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Headless CMS, Content Management, REST API, GraphQL, and Next.js.


  Payload CMS''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Payloadcms Plans Pricing
  plan_count: 4
  slug: payloadcms-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 4
  name: Payloadcms Rate Limits
  slug: payloadcms-rate-limits
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payloadcms/refs/heads/main/screenshots/payloadcms-2026-06-20T191501.png
security:
- kind: domain-security
  name: Payloadcms Domain Security
  slug: payloadcms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payloadcms
tags:
- Headless CMS
- Content Management
- REST API
- GraphQL
- Next.js
- Open Source
- Self-Hosted
- TypeScript
website: https://payloadcms.com
---
