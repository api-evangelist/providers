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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Auto-generated GraphQL API served at /api/graphql that provides full CRUD operations for every list in the schema. Includes single-item queries, list queries with filtering and pagination, count queri
  name: KeystoneJS GraphQL API
  slug: keystonejs-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keystonejs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keystonejs.com
- group: docs
  title: ''
  type: Documentation
  url: https://keystonejs.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/keystonejs
- group: company
  title: ''
  type: Blog
  url: https://keystonejs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thinkmill.com.au/services/keystone
- group: other
  title: ''
  type: X
  url: https://x.com/keystonejs
- group: commercial
  title: ''
  type: Plans
  url: plans/keystonejs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keystonejs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keystonejs-finops.yml
created: '2026-06-13'
description: KeystoneJS is an open-source headless CMS and GraphQL API platform for Node.js. It auto-generates a powerful GraphQL API and a beautiful management UI from schema definitions, enabling developers to manage content and user data without boilerplate. Built on TypeScript with Prisma for database migrations, it supports PostgreSQL, MySQL, and SQLite and includes access control, session management, hooks, and rich document editing out of the box.
finops:
- name: Keystonejs Finops
  service_category: ''
  slug: keystonejs-finops
graphqls:
- description: KeystoneJS auto-generates a fully typed GraphQL API from its schema definition — every list defined in `keystone.ts` produces a standard set of queries and mutations without any manual resolver writin
  name: KeystoneJS GraphQL API
  slug: keystonejs-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keystonejs.png
layout: provider
modified: '2026-06-13'
name: KeystoneJS
nav: Providers
network: true
overview: 'KeystoneJS publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Headless CMS, GraphQL, Node.js, Content Management, and Open Source.


  KeystoneJS''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Keystonejs Plans Pricing
  plan_count: 4
  slug: keystonejs-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Keystonejs Rate Limits
  slug: keystonejs-rate-limits
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keystonejs/refs/heads/main/screenshots/keystonejs-2026-06-20T184013.png
security:
- kind: domain-security
  name: Keystonejs Domain Security
  slug: keystonejs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keystonejs
tags:
- Headless CMS
- GraphQL
- Node.js
- Content Management
- Open Source
- TypeScript
- Prisma
website: https://keystonejs.com
---
