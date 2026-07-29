---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 0
  human_in_the_loop: 0
  name: Builder Io Agentic Access
  operation_count: 2
  slug: builder-io-agentic-access
  summary_line: 2 operations
api_count: 6
apis:
- description: 'REST API for retrieving published content from Builder.io models. Supports filtering via MongoDB-style queries, targeting by user attributes, locale, and URL path. Returns paginated JSON results with '
  name: Builder.io Content API
  slug: content-api
- description: GraphQL API for querying Builder.io content models with type-safe schemas. Supports GET and POST requests, model-level queries with pagination, and targeting via user attributes. The interactive Graph
  name: Builder.io GraphQL Content API
  slug: graphql-api
- description: Private GraphQL API for back-end servers and trusted integrations. Enables space management, user access control, SSO configuration (SAML/OIDC), webhook setup, model and folder management, and asset r
  name: Builder.io Admin GraphQL API
  slug: admin-api
- description: API for programmatically creating, updating, and deleting content entries in Builder.io. Intended for server-side automation and content migration workflows that need to manage Builder models at scale
  name: Builder.io Write API
  slug: write-api
- description: API for programmatically uploading files such as images and videos to Builder.io. Supports automation of asset ingestion pipelines and bulk media management workflows.
  name: Builder.io Upload API
  slug: upload-api
- description: API for accessing and downloading optimized versions of images uploaded to Builder.io. Supports on-the-fly image transformation and CDN-optimized delivery for web performance use cases.
  name: Builder.io Image API
  slug: image-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/builder-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/builder-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/builder-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.builder.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.builder.io/c/docs/api-intro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BuilderIO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/builder-io
- group: other
  title: ''
  type: X
  url: https://twitter.com/builderio
- group: company
  title: ''
  type: Blog
  url: https://www.builder.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.builder.io/m/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.builder.io
- group: commercial
  title: ''
  type: Plans
  url: plans/builder-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/builder-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/builder-io-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/builder-io-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/builder-io-vocabulary.yml
created: '2026-06-12'
description: Builder.io is a visual development platform and headless CMS that enables teams to build, test, and optimize digital experiences without requiring constant developer involvement. The platform combines an AI-powered visual editor with a suite of APIs including REST Content, GraphQL, Write, Upload, Image, Assets, and Admin APIs for managing and delivering content at scale. Builder.io supports A/B testing, personalization, and targeting, making it suitable for marketing and product teams working across web and mobile channels. It integrates natively with React, Vue, Svelte, Qwik, Angular, and other frameworks through official SDKs, and connects to Git-based workflows via GitHub, GitLab, and Bitbucket.
examples:
- key_count: 3
  name: Builder Io Get Content Example
  slug: builder-io-get-content-example
finops:
- name: Builder Io Finops
  service_category: Developer Tools / Headless CMS
  slug: builder-io-finops
graphqls:
- description: 'Builder.io exposes a public GraphQL Content API that enables type-safe queries against your Builder.io space''s content models. The API is schema-driven: every content model defined in your Builder spa'
  name: Builder.io GraphQL API
  slug: builder-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/builder-io.png
json_schemas:
- name: BuilderContentEntry
  property_count: 14
  slug: builder-io-content-entry
jsonld:
- class_count: 3
  name: Builder Io Context
  property_count: 24
  slug: builder-io-context
layout: provider
modified: '2026-06-12'
name: Builder.io
nav: Providers
network: true
overview: 'Builder.io publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Headless CMS, Visual Development, Content Delivery, A/B Testing, and GraphQL.


  The Builder.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Builder.io''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Builder Io Plans Pricing
  plan_count: 4
  slug: builder-io-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Builder Io Rate Limits
  slug: builder-io-rate-limits
rules:
- name: Builder.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: builder-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/screenshots/builder-io-2026-06-20T173746.png
security:
- kind: authentication
  name: Builder Io Authentication
  slug: builder-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Builder Io Domain Security
  slug: builder-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: builder-io
tags:
- Headless CMS
- Visual Development
- Content Delivery
- A/B Testing
- GraphQL
- REST
- Personalization
- Page Building
website: https://www.builder.io
---
