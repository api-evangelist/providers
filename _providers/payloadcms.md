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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-09-25'
api_count: 8
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
- description: Payload is a TypeScript-first headless CMS and application framework that automatically generates REST, GraphQL, and Local APIs from collection schemas, with built-in authentication, access control, a
  name: Payload
  slug: payload
- baseURL: https://payloadcms.com/api
  baseurl_source: declared
  description: The Authentication API from Payload — 8 operation(s) for authentication.
  name: Payload Authentication API
  slug: payload-authentication-api
- baseURL: https://payloadcms.com/api
  baseurl_source: declared
  description: The Collections API from Payload — 3 operation(s) for collections.
  name: Payload Collections API
  slug: payload-collections-api
- baseURL: https://payloadcms.com/api
  baseurl_source: declared
  description: The Globals API from Payload — 1 operation(s) for globals.
  name: Payload Globals API
  slug: payload-globals-api
- baseURL: https://payloadcms.com/api
  baseurl_source: declared
  description: The Preferences API from Payload — 1 operation(s) for preferences.
  name: Payload Preferences API
  slug: payload-preferences-api
artifact_total: 14
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/payloadcms/refs/heads/main/security/payloadcms-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/payloadcms/refs/heads/main/plans/payloadcms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payloadcms-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/payloadcms/refs/heads/main/rate-limits/payloadcms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/payloadcms-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/payloadcms/refs/heads/main/finops/payloadcms-finops.yml
  title: ''
  type: FinOps
  url: finops/payloadcms-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://payloadcms.com/docs
- group: company
  title: ''
  type: Blog
  url: https://payloadcms.com/posts
created: '2026-06-13'
description: Open-source headless CMS and fullstack Next.js framework providing automatic REST and GraphQL APIs for managing collections, globals, media, users, and custom fields in self-hosted or cloud deployments.
finops:
- name: Payloadcms Finops
  service_category: ''
  slug: payloadcms-finops
graphqls:
- description: Payload is a TypeScript-first headless CMS and application framework that automatically generates REST, GraphQL, and Local APIs from collection schemas, with built-in authentication, access control, a
  name: Payload GraphQL API
  slug: payload-graphql
- description: 'Payload CMS ships a fully featured GraphQL API generated automatically from your collection and global configurations. Every collection defined in your Payload config produces a set of strongly-typed '
  name: Payload CMS GraphQL API
  slug: payloadcms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payloadcms.png
layout: provider
modified: '2026-06-13'
name: Payload CMS
nav: Providers
network: true
overview: 'Payload CMS publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Payload Authentication API, Payload Collections API, Payload Globals API, and 5 more. Tagged areas include Headless CMS, Content Management, REST API, GraphQL, and Next.js.


  Payload CMS''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Payloadcms Plans Pricing
  plan_count: 4
  slug: payloadcms-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Payloadcms Rate Limits
  slug: payloadcms-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.6
    catalog_earned_first_party: 0.0
    catalog_gap: 50.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 46.8
    contract_governance: 0.0
    contract_quality: 46.4
    developer_ergonomics: 23.8
    discoverability: 71.4
    operational_transparency: 33.7
  previous_composite: 33.9
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
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
- Application Framework
- CMS
- Content
- Headless
website: https://payloadcms.com
---
