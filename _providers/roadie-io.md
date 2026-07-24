---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Roadie Io Agentic Access
  operation_count: 21
  slug: roadie-io-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 6
apis:
- description: Six agent-native Model Context Protocol (MCP) servers over the Roadie API - api-docs-query, backend-config, catalog-decorators, rich-catalog-entity, scaffolder-use, and tech-insights-facts - letting A
  name: Roadie MCP Servers
  slug: roadie-io-mcp-servers
- description: Read Backstage software catalog entities in your Roadie tenant.
  name: Roadie Catalog API
  slug: roadie-io-catalog-api
- description: Create, delete, and idempotently manage Roadie-owned catalog entities and entity sets.
  name: Roadie Entity Push API
  slug: roadie-io-entity-push-api
- description: Backstage software templates - discover, dry-run, execute, and track scaffolder tasks.
  name: Roadie Scaffolder API
  slug: roadie-io-scaffolder-api
- description: Facts, checks, and scorecards describing entity quality and compliance.
  name: Roadie Tech Insights API
  slug: roadie-io-tech-insights-api
- description: Technical documentation (docs-like-code) metadata and static content. Modeled from Backstage.
  name: Roadie TechDocs API
  slug: roadie-io-techdocs-api
artifact_total: 12
collections:
- collection_type: open
  name: Roadie API
  slug: open-roadie-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roadie-io-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roadie-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roadiehq
- group: company
  title: ''
  type: Website
  url: https://roadie.io
- group: docs
  title: ''
  type: Documentation
  url: https://roadie.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/roadie-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roadie-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/roadie-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://roadie.io/blog/
created: '2026-07-11'
description: Roadie is managed Backstage - a fully hosted internal developer portal (IDP) and software catalog delivered as SaaS, so teams get the Backstage software catalog, TechDocs, Scaffolder software templates, Tech Insights scorecards, and 75+ plugins without operating Backstage themselves. Roadie exposes a public REST API under https://api.roadie.so/api (Bearer-token authenticated with User or Service tokens) for reading catalog entities, pushing Roadie-managed entities and idempotent entity sets into the software catalog, running Scaffolder templates, and querying Tech Insights facts, checks, and scorecards. Roadie also ships six agent-native MCP servers over the same API base. Backstage itself is free and open source; Roadie is the commercial managed product, priced per contributing developer. Operated by Larder Software Limited.
finops:
- name: Roadie Io Finops
  service_category: Developer Tools and Platform Engineering
  slug: roadie-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roadie-io.png
layout: provider
modified: '2026-07-11'
name: Roadie
nav: Providers
network: true
overview: 'Roadie publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Entity Push API, Scaffolder API, and 2 more. Tagged areas include Software Catalog, Internal Developer Portal, Backstage, Developer Experience, and IDP.


  Roadie''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Roadie Io Plans Pricing
  plan_count: 3
  slug: roadie-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Roadie Io Rate Limits
  slug: roadie-io-rate-limits
score:
  band: thin
  composite: 38.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.8
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Roadie Io Authentication
  slug: roadie-io-authentication
  summary_line: http · 1 scheme
slug: roadie-io
tags:
- Software Catalog
- Internal Developer Portal
- Backstage
- Developer Experience
- IDP
- Developer Portal
- Managed Backstage
- Scaffolder
- TechDocs
- Service Catalog
- Platform Engineering
website: https://roadie.io
---
