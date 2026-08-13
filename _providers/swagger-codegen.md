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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Swagger Codegen Agentic Access
  operation_count: 10
  slug: swagger-codegen-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 5
apis:
- description: The Swagger Codegen command-line interface for generating code artifacts locally. Available as a JAR file and Docker image. Supports the same generators as the online API with additional template cust
  name: Swagger Codegen CLI
  slug: swagger-codegen-cli
- description: Code generation endpoints for clients, servers, and documentation
  name: Swagger Codegen Generation API
  slug: swagger-codegen-generation-api
- description: Discover available generator languages and types
  name: Swagger Codegen Languages API
  slug: swagger-codegen-languages-api
- description: Retrieve per-language configuration options
  name: Swagger Codegen Options API
  slug: swagger-codegen-options-api
- description: Template rendering and intermediate model generation
  name: Swagger Codegen Utilities API
  slug: swagger-codegen-utilities-api
artifact_total: 22
collections:
- collection_type: open
  name: Swagger Generator API
  slug: open-swagger-generator
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swagger-codegen-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swagger-codegen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swagger-codegen-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://swagger.io/tools/swagger-codegen/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/swagger-api/swagger-codegen/wiki
- group: company
  title: ''
  type: Website
  url: https://swagger.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swagger-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/swagger-api/swagger-codegen
- group: operate
  title: ''
  type: Issues
  url: https://github.com/swagger-api/swagger-codegen/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/swagger-api/swagger-codegen/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/swagger-api/swagger-codegen/blob/master/LICENSE
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
- group: build
  title: ''
  type: Maven Plugin
  url: https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-maven-plugin
- group: build
  title: ''
  type: Gradle Plugin
  url: https://plugins.gradle.org/plugin/org.hidetake.swagger.generator
- group: build
  title: ''
  type: Packages
  url: packages/swagger-codegen-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swagger-codegen-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/swagger-codegen-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swagger-codegen-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swagger-codegen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swagger-codegen-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swagger-codegen-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/swagger-codegen-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smartbear.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swagger-codegen-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swagger-codegen-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swagger-codegen-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.smartbear.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/swagger-codegen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swagger-codegen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://smartbear.com/security/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swagger-codegen-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swagger-codegen-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://generator3.swagger.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/swagger-api/swagger-codegen#getting-started
- group: operate
  title: ''
  type: Support
  url: https://swagger.io/support/
- group: company
  title: ''
  type: Blog
  url: https://swagger.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smartbear.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smartbear.com/privacy/
created: '2026-03-16'
description: Swagger Codegen is an open-source template-driven code generation tool that automatically generates client libraries, server stubs, and API documentation from OpenAPI Specification definitions. It supports 40+ client languages and 20+ server frameworks. Available as a CLI, Docker image, Maven/Gradle plugin, and online REST API at generator3.swagger.io.
examples:
- key_count: 3
  name: Swagger Codegen Generate Python Client Example
  slug: swagger-codegen-generate-python-client-example
- key_count: 3
  name: Swagger Codegen List Languages Example
  slug: swagger-codegen-list-languages-example
finops:
- name: Swagger Codegen Finops
  service_category: API
  slug: swagger-codegen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swagger-codegen.png
json_schemas:
- name: Swagger Codegen Generation Request
  property_count: 6
  slug: swagger-codegen-generation-request
json_structures:
- name: Swagger Codegen Structure
  property_count: 0
  slug: swagger-codegen-structure
jsonld:
- class_count: 0
  name: Swagger Codegen Context
  property_count: 27
  slug: swagger-codegen-context
layout: provider
mcp_servers:
- description: ''
  name: swagger-codegen-mcp.yml
  slug: swagger-codegen-mcpyml
modified: '2026-08-06'
name: Swagger Codegen
nav: Providers
network: true
overview: 'Swagger Codegen publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Generation API, Languages API, Options API, and 1 more. Tagged areas include Client Libraries, Code Generation, Open Source, OpenAPI, and SDK.


  The Swagger Codegen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Swagger Codegen''s developer surface includes developer portal, documentation, release notes, CLI, authentication, changelog, sandbox, and 32 more developer resources.'
plans:
- name: Swagger Codegen Plans Pricing
  plan_count: 3
  slug: swagger-codegen-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 5
  name: Swagger Codegen Rate Limits
  slug: swagger-codegen-rate-limits
rules:
- name: Swagger Codegen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swagger-codegen-jsonschema-spectral-rules
- name: Swagger Codegen API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: swagger-codegen-rules
score:
  band: strong
  composite: 65.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.0
    developer_ergonomics: 75.5
    discoverability: 72.2
    governance: 79.2
    operational_transparency: 63.2
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swagger-codegen/refs/heads/main/screenshots/swagger-codegen-2026-06-20T194753.png
security:
- kind: authentication
  name: Swagger Codegen Authentication
  slug: swagger-codegen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Swagger Codegen Domain Security
  slug: swagger-codegen-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Swagger Codegen Vulnerability Disclosure
  slug: swagger-codegen-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Swagger Codegen Trust Center
  slug: swagger-codegen-trust-center
  summary_line: SOC 2, ISO/IEC 27001, GDPR, CCPA, NIST CSF
slug: swagger-codegen
tags:
- Client Libraries
- Code Generation
- Open Source
- OpenAPI
- SDK
website: https://swagger.io/
---
