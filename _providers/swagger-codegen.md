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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Swagger Codegen Agentic Access
  operation_count: 10
  slug: swagger-codegen-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 3
apis:
- description: The Swagger Codegen command-line interface for generating code artifacts locally. Available as a JAR file and Docker image. Supports the same generators as the online API with additional template cust
  name: Swagger Codegen CLI
  slug: swagger-codegen-cli
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: Code generation endpoints for clients, servers, and documentation
  name: Swagger Codegen Generation API
  slug: swagger-codegen-generation-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: Discover available generator languages and types
  name: Swagger Codegen Languages API
  slug: swagger-codegen-languages-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: Retrieve per-language configuration options
  name: Swagger Codegen Options API
  slug: swagger-codegen-options-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: Template rendering and intermediate model generation
  name: Swagger Codegen Utilities API
  slug: swagger-codegen-utilities-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: The clients API from Swagger Codegen — 9 operation(s) for clients.
  name: Swagger Codegen Clients API
  slug: swagger-codegen-clients-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: The documentation API from Swagger Codegen — 2 operation(s) for documentation.
  name: Swagger Codegen Documentation API
  slug: swagger-codegen-documentation-api
- baseURL: https://generator3.swagger.io/api
  baseurl_source: declared
  description: The servers API from Swagger Codegen — 4 operation(s) for servers.
  name: Swagger Codegen Servers API
  slug: swagger-codegen-servers-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swagger Generator Generation API
  slug: open-swagger-codegen-generation-api
- collection_type: open
  name: Swagger Generator Generation Languages API
  slug: open-swagger-codegen-languages-api
- collection_type: open
  name: Swagger Generator Generation Options API
  slug: open-swagger-codegen-options-api
- collection_type: open
  name: Swagger Generator Generation Utilities API
  slug: open-swagger-codegen-utilities-api
- collection_type: open
  name: Swagger Generator API
  slug: open-swagger-generator
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/swagger-api/swagger-codegen/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/swagger-api/swagger-codegen/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-08-06'
name: Swagger Codegen
nav: Providers
network: true
overview: 'Swagger Codegen publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Generation API, Languages API, Options API, and 4 more. Tagged areas include Client Libraries, Code Generation, Open-Source, OpenAPI, and SDK.


  The Swagger Codegen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Swagger Codegen''s developer surface includes developer portal, documentation, release notes, CLI, authentication, changelog, sandbox, and 34 more developer resources.'
plans:
- name: Swagger Codegen Plans Pricing
  plan_count: 3
  slug: swagger-codegen-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Swagger Codegen Rate Limits
  slug: swagger-codegen-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Swagger Codegen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swagger-codegen-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Swagger Codegen API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: swagger-codegen-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 31.8
    contract_quality: 52.5
    developer_ergonomics: 80.4
    discoverability: 64.8
    governance: 31.8
    operational_transparency: 44.7
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- OpenAPI
- SDK
website: https://swagger.io/
---
