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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Capability area (endpointsModeled - no documented public REST endpoint). Generates idiomatic client-library SDKs from an OpenAPI Specification or Postman Collection in TypeScript/JavaScript, Python, J
  name: Konfig SDK Generation
  slug: konfig-sdk-generation
- description: Capability area (endpointsModeled). Tests and publishes generated SDKs to package registries (npm, PyPI, Maven Central/Sonatype, and others) via konfig test and konfig publish, and automatically repub
  name: Konfig SDK Publishing and Updates
  slug: konfig-sdk-publishing
- description: Capability area (endpointsModeled). Generates branded, interactive API reference documentation and markdown pages from the same OpenAPI spec, embedding language-specific SDK snippets that stay in sync
  name: Konfig Documentation Portal
  slug: konfig-documentation-portal
- description: Capability area (endpointsModeled). Builds interactive, runnable demos and markdown-based tutorials on top of the generated SDKs so API consumers can onboard and try live calls from the developer port
  name: Konfig Demos and Tutorials
  slug: konfig-demos-tutorials
- description: Capability area (endpointsModeled). A configurable linter that inspects an OpenAPI Specification for errors and quality issues before SDK and docs generation, so client libraries are produced from a c
  name: Konfig OpenAPI Linting
  slug: konfig-linting
artifact_total: 8
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/konfig-dev
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/konfig-sdks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/konfig
- group: company
  title: ''
  type: Website
  url: https://konfigthis.com
- group: docs
  title: ''
  type: Documentation
  url: https://konfigthis.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/konfig-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/konfig-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/konfig-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://konfigthis.com/blog
created: '2026-07-11'
description: Konfig is an SDK and API documentation generator that turns an OpenAPI Specification or Postman Collection into production-ready client libraries, interactive reference docs, demos, and tutorials. It generates and publishes idiomatic SDKs across TypeScript/JavaScript, Python, Java, C#, PHP, Ruby, Go, Swift, Kotlin, Objective-C, and Dart, republishing them automatically whenever the spec changes, and adds spec linting and generated SDK tests to keep client libraries in sync across the API lifecycle. Konfig is driven from a CLI (konfig-cli) and a konfig.yaml config that calls Konfig's hosted generation backend - it is a developer-tooling platform, not a hosted public REST API of its own. Konfig was sunset in December 2024 and its full codebase was open-sourced (MIT) at github.com/konfig-dev/konfig; the marketing site, docs, and 491 generated SDK repositories at github.com/konfig-sdks remain online.
finops:
- name: Konfig Api Finops
  service_category: Developer Tools and SDK Generation
  slug: konfig-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/konfig-api.png
layout: provider
modified: '2026-07-11'
name: Konfig
nav: Providers
network: true
overview: 'Konfig publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include SDK Generation, Client Library, API Documentation, Developer Tools, and API Lifecycle.


  Konfig''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Konfig Api Plans Pricing
  plan_count: 3
  slug: konfig-api-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Konfig Api Rate Limits
  slug: konfig-api-rate-limits
score:
  band: emerging
  composite: 21.3
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/konfig-api/refs/heads/main/screenshots/konfig-api-2026-07-25T224153.png
slug: konfig-api
tags:
- SDK Generation
- Client Library
- API Documentation
- Developer Tools
- API Lifecycle
- OpenAPI
- Code Generation
website: https://konfigthis.com
---
