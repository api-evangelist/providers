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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scalar Api Agentic Access
  operation_count: 4
  slug: scalar-api-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Open-source (MIT) renderer that turns an OpenAPI/Swagger or AsyncAPI document into an interactive API reference with a built-in request-testing panel and multi-language code samples. Embeds from a sin
  name: Scalar API Reference
  slug: scalar-api-reference
- description: Fully open-source, offline-first API client built on the OpenAPI standard - a Postman/Insomnia alternative for sending REST, GraphQL, and WebSocket requests, organizing collections and environments, r
  name: Scalar API Client
  slug: scalar-api-client
- description: 'Hosted developer-portal product that combines Markdown/MDX guides with generated API references, custom domains and subdomains, themes, versions, and two-way Git Sync from GitHub. Content is deployed '
  name: Scalar Docs Platform
  slug: scalar-docs-platform
- description: Open-source command-line tool (@scalar/cli) for validating and linting OpenAPI documents (Spectral rules), previewing references, and publishing/listing/ updating/deleting documents in the Scalar Regi
  name: Scalar CLI
  slug: scalar-cli
- description: Hosted SDK generation that produces type-safe client libraries from an OpenAPI document for TypeScript, Python, Go, Java, PHP, C#, and Ruby, kept in sync with the registry. Paid add-on on the hosted p
  name: Scalar SDK Generation
  slug: scalar-sdk-generation
- description: AI layer that lets developers chat with an API inside the docs and exposes hosted MCP (Model Context Protocol) servers generated from an OpenAPI document so agents can call the API. Metered in Agent S
  name: Scalar Agent and MCP
  slug: scalar-agent-mcp
- description: Publish / list / update / delete documents - performed via the Scalar CLI (modeled).
  name: Scalar Registry Management API
  slug: scalar-api-registry-management-api
- description: Public retrieval of published OpenAPI documents (confirmed public surface).
  name: Scalar Registry Read API
  slug: scalar-api-registry-read-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scalar Registry (Public Read Surface) - Modeled Registry Management API
  slug: open-scalar-api-registry-management-api
- collection_type: open
  name: Scalar Registry (Public Read Surface) - Modeled Registry Management Registry Read API
  slug: open-scalar-api-registry-read-api
- collection_type: open
  name: Scalar Registry (Public Read Surface) - Modeled
  slug: open-scalar-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/scalar/scalar/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/scalar/scalar/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/scalar/scalar/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/scalar/scalar/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/scalar/scalar/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/scalar/scalar/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalar-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalar-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scalar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scalar-com
- group: company
  title: ''
  type: Website
  url: https://scalar.com
- group: docs
  title: ''
  type: Documentation
  url: https://guides.scalar.com
- group: commercial
  title: ''
  type: Plans
  url: plans/scalar-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scalar-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scalar-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://scalar.com/blog
created: '2026-07-11'
description: Scalar is an open-source (MIT) API platform built on the OpenAPI standard. Its core is a self-hostable API Reference renderer that turns an OpenAPI or AsyncAPI document into a beautiful, interactive reference with a built-in API testing tool, plus a fully open-source, offline-first API Client (a Postman alternative available as a desktop app and in the browser). On top of the open-source components Scalar runs a hosted SaaS platform (dashboard.scalar.com) providing an API Registry that stores and versions OpenAPI documents behind a public read CDN (registry.scalar.com), a Docs product for developer portals with Git Sync and Markdown/MDX, SDK generation for TypeScript, Python, Go, Java, PHP, C#, and Ruby, hosted MCP servers, and an AI Agent for chatting with APIs. Scalar is the default API documentation UI for many frameworks (FastAPI, Hono, Elysia, NestJS, Laravel, and others). Publishing to the hosted registry is done through the Scalar CLI; the registry read surface and the
  Galaxy example API are public over HTTPS.
finops:
- name: Scalar Api Finops
  service_category: Developer Tools and API Documentation
  slug: scalar-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalar-api.png
layout: provider
modified: '2026-07-11'
name: Scalar
nav: Providers
network: true
overview: 'Scalar publishes 2 APIs on the [APIs.io](https://apis.io/) network: Registry Management API and Registry Read API. Tagged areas include API Documentation, API Client, Open-Source, Developer Tools, and API Reference.


  Scalar''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Scalar Api Plans Pricing
  plan_count: 5
  slug: scalar-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Scalar Api Rate Limits
  slug: scalar-api-rate-limits
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 60.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Scalar Api Authentication
  slug: scalar-api-authentication
  summary_line: apiKey · 1 scheme
slug: scalar-api
tags:
- API Documentation
- API Client
- Open-Source
- Developer Tools
- API Reference
- OpenAPI
website: https://scalar.com
---
