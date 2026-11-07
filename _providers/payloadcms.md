---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 4
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
- baseURL: https://{your-domain}/api
  baseurl_source: declared
  description: The Authentication API from Payload CMS — 8 operation(s) for authentication.
  name: Payload CMS Authentication API
  slug: payloadcms-authentication-api
- baseURL: https://{your-domain}/api
  baseurl_source: declared
  description: The Collections API from Payload CMS — 3 operation(s) for collections.
  name: Payload CMS Collections API
  slug: payloadcms-collections-api
- baseURL: https://{your-domain}/api
  baseurl_source: declared
  description: The Globals API from Payload CMS — 1 operation(s) for globals.
  name: Payload CMS Globals API
  slug: payloadcms-globals-api
- baseURL: https://{your-domain}/api
  baseurl_source: declared
  description: The Preferences API from Payload CMS — 1 operation(s) for preferences.
  name: Payload CMS Preferences API
  slug: payloadcms-preferences-api
artifact_total: 15
common:
- group: auth
  href: https://artifacts.apis.io/payloadcms/security/payloadcms-domain-security.yml
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
  href: https://artifacts.apis.io/payloadcms/plans/payloadcms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payloadcms-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/payloadcms/rate-limits/payloadcms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/payloadcms-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/payloadcms/finops/payloadcms-finops.yml
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
- has_sources: false
  method: generated
  name: Payloadcms Finops
  primary_unit: ''
  service_category: ''
  slug: payloadcms-finops
  template: true
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
overview: 'Payload CMS publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Collections API, Globals API, and 5 more. Tagged areas include Headless CMS, Content Management, REST API, GraphQL, and Next.js.


  The Payload CMS catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Payload CMS API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: payloadcms-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 46.4
    developer_ergonomics: 23.8
    discoverability: 71.4
    operational_transparency: 13.2
  previous_composite: 31.5
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
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/payloadcms/payloadcms-2026-06-20T191501.png
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
