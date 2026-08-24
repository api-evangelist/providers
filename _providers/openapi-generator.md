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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The clients API from OpenAPI Generator — 3 operation(s) for clients.
  name: OpenAPI Generator Clients API
  slug: openapi-generator-clients-api
- description: The servers API from OpenAPI Generator — 3 operation(s) for servers.
  name: OpenAPI Generator Servers API
  slug: openapi-generator-servers-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenAPI Generator Online Clients API
  slug: open-openapi-generator-clients-api
- collection_type: open
  name: OpenAPI Generator Online Servers API
  slug: open-openapi-generator-servers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/openapi-generator-online-overlay.yaml
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
- description: 'OpenAPI Generator publishes NO official hosted or remote MCP server. Searched on 2026-08-06: no /.well-known/* MCP or OAuth discovery document on either openapi-generator.tech or api.openapi-generator'
  name: OpenAPI Generator MCP Server
  slug: openapi-generator-mcp-server
modified: '2026-08-06'
name: OpenAPI Generator
nav: Providers
network: true
overview: 'OpenAPI Generator publishes 2 APIs on the [APIs.io](https://apis.io/) network: Clients API and Servers API. Tagged areas include Code Generation, Documentation, Open-Source, OpenAPI, and SDK.


  OpenAPI Generator''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Openapi Generator Plans Pricing
  plan_count: 2
  slug: openapi-generator-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Openapi Generator Rate Limits
  slug: openapi-generator-rate-limits
score:
  band: developing
  composite: 40.7
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 45.5
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 40.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
- Open-Source
- OpenAPI
- SDK
- API Tooling
- Developer Tools
- Swagger
- Server Stubs
- Codegen
website: https://openapi-generator.tech
---
