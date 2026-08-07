---
access_model:
  confidence: high
  label: Free / Open Source
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - https://openapi-generator.tech/docs/installation
  - https://api.openapi-generator.tech/api/gen/clients
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The hosted OpenAPI Generator Online API — a seven-operation REST service that lists the available client generators and server frameworks, returns each generator's configuration options, generates a c
  name: OpenAPI Generator Online
  slug: openapi-generator
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openapi-generator-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/openapi-generator-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/openapi-generator-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openapi-generator-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openapi-generator-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openapi-generator-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openapi-generator-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openapi-generator-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openapi-generator-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openapi-generator-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openapi-generator-finops.yml
- group: company
  title: ''
  type: Website
  url: https://openapi-generator.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi-generator.tech
- group: docs
  title: ''
  type: Documentation
  url: https://openapi-generator.tech/docs/installation
- group: docs
  title: ''
  type: APIReference
  url: https://api.openapi-generator.tech/
- group: start
  title: ''
  type: GettingStarted
  url: https://openapi-generator.tech/docs/usage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenAPITools
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OpenAPITools/openapi-generator
- group: operate
  title: ''
  type: Support
  url: https://github.com/OpenAPITools/openapi-generator/issues
- group: operate
  title: ''
  type: Roadmap
  url: https://openapi-generator.tech/docs/roadmap
- group: company
  title: ''
  type: Blog
  url: https://openapi-generator.tech/blog
- group: operate
  title: ''
  type: FAQ
  url: https://openapi-generator.tech/docs/faq
- group: other
  title: ''
  type: Generators
  url: https://openapi-generator.tech/docs/generators
- group: build
  title: ''
  type: Plugins
  url: https://openapi-generator.tech/docs/plugins
- group: other
  title: ''
  type: Team
  url: https://openapi-generator.tech/team
- group: commercial
  title: ''
  type: License
  url: https://github.com/OpenAPITools/openapi-generator/blob/master/LICENSE
created: '2026-03-16'
description: OpenAPI Generator is a community-governed, Apache-2.0 open-source project that generates client libraries (SDKs), server stubs, API documentation and configuration automatically from an OpenAPI Specification (v2 and v3). Forked from Swagger Codegen in 2018 by more than 40 of that project's top contributors and template creators, it is one of the most widely deployed implementations of the OpenAPI Specification in existence. The product is a CLI plus Maven, Gradle and sbt plugins, a Docker image and an embeddable JVM library, distributed through npm, PyPI, Maven Central, Homebrew, Scoop and Docker Hub. A hosted Online Generator REST API at api.openapi-generator.tech offers the same generation over HTTP, anonymously and without a key, across 84 client generators and 65 server frameworks.
finops:
- name: Openapi Generator Finops
  service_category: API
  slug: openapi-generator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openapi-generator.png
layout: provider
mcp_servers:
- description: ''
  name: openapi-generator-mcp.yml
  slug: openapi-generator-mcpyml
modified: '2026-08-06'
name: OpenAPI Generator
nav: Providers
network: true
overview: 'OpenAPI Generator publishes 1 API on the [APIs.io](https://apis.io/) network: Online. Tagged areas include Code Generation, Documentation, Open Source, OpenAPI, and SDK.


  OpenAPI Generator''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 20 more developer resources.'
plans:
- name: Openapi Generator Plans Pricing
  plan_count: 2
  slug: openapi-generator-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Openapi Generator Rate Limits
  slug: openapi-generator-rate-limits
score:
  band: developing
  composite: 42.9
  delta: 22.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 44.2
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 20.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/openapi-generator/refs/heads/main/screenshots/openapi-generator-2026-06-20T190908.png
security:
- kind: authentication
  name: Openapi Generator Authentication
  slug: openapi-generator-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Openapi Generator Domain Security
  slug: openapi-generator-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openapi-generator
tags:
- Code Generation
- Documentation
- Open Source
- OpenAPI
- SDK
- API Tooling
- Developer Tools
- Swagger
- Server Stubs
- Codegen
website: https://openapi-generator.tech
---
