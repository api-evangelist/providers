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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.2
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Builder Io Agentic Access
  operation_count: 2
  slug: builder-io-agentic-access
  summary_line: 2 operations
api_count: 6
apis:
- baseURL: https://cdn.builder.io/api/v3/content
  baseurl_source: declared
  description: 'REST API for retrieving published content from Builder.io models. Supports filtering via MongoDB-style queries, targeting by user attributes, locale, and URL path. Returns paginated JSON results with '
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Builder.io Content API
  slug: open-builder-io-content-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/agentic-access/builder-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/builder-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/security/builder-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/builder-io-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/authentication/builder-io-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/plans/builder-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/builder-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/rate-limits/builder-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/builder-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/finops/builder-io-finops.yml
  title: ''
  type: FinOps
  url: finops/builder-io-finops.yml
- group: company
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/blogs/blogs.json
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/json-ld/builder-io-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/builder-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/builder-io/refs/heads/main/vocabulary/builder-io-vocabulary.yml
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
overview: 'Builder.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Content API, and 5 more. Tagged areas include Headless CMS, Visual Development, Content Delivery, A/B Testing, and GraphQL.


  The Builder.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Builder.io''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Builder Io Plans Pricing
  plan_count: 4
  slug: builder-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Builder Io Rate Limits
  slug: builder-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Builder.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: builder-io-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 80.4
    catalog_earned_first_party: 0.0
    catalog_gap: 34.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 46.8
    contract_governance: 23.5
    contract_quality: 61.6
    developer_ergonomics: 23.8
    discoverability: 73.3
    operational_transparency: 46.8
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
