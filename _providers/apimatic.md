---
access_model:
  confidence: high
  label: Paid · 14-day free trial · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.apimatic.io/pricing
  - plans/apimatic-plans-pricing.yml
  - authentication/apimatic-authentication.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Apimatic Agentic Access
  operation_count: 25
  slug: apimatic-agentic-access
  summary_line: 25 operations · 11 acting
api_count: 5
apis:
- description: APIMatic API Transformer converts API definition files between more than 15 supported API specification formats including OpenAPI, RAML, API Blueprint, WSDL, WADL, and Postman Collections.
  name: APIMatic API Transformer API
  slug: apimatic-api-transformer-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: Generate an APIMatic developer portal from a build input, synchronously (POST /portal) or asynchronously (POST /portal/v2 with status polling and download) — 4 operations, read from the reference data
  name: APIMatic Portals API
  slug: apimatic-portals-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: Generate SDKs from an API definition uploaded as a file or given by URL, list, fetch, download and delete code generations, and run asynchronous SDK generation from a build input — 10 operations, read
  name: APIMatic SDK Generation API
  slug: apimatic-sdk-generation-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: Transform an API definition from one specification format to another, by file or by URL, then list, fetch, download and delete transformations — 7 operations, read from the reference data APIMatic ser
  name: APIMatic Transformation API
  slug: apimatic-transformation-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: Validate an API definition by file or by URL, in the original and V2 validation endpoints — 4 operations, read from the reference data APIMatic serves for its own Platform API portal.
  name: APIMatic Validation API
  slug: apimatic-validation-api
artifact_total: 42
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/agentic-access/apimatic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apimatic-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/rules/apimatic-rules.yml
  title: ''
  type: Spectral
  url: rules/apimatic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/json-ld/apimatic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apimatic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/vocabulary/apimatic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apimatic-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/data-model/apimatic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apimatic-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/llms/apimatic-www-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apimatic-www-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/hosts/apimatic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apimatic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/vendors/apimatic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apimatic-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/security/apimatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apimatic-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/authentication/apimatic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apimatic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.apimatic.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apimatic.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apimatic.io/getting-started/importing-api-spec/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apimatic.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.apimatic.io/blog
- group: start
  title: ''
  type: Signup
  url: https://app.apimatic.io/account/register
- group: start
  title: ''
  type: Login
  url: https://app.apimatic.io/account/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.apimatic.io/changelog/
- group: operate
  title: ''
  type: Support
  url: https://support.apimatic.io/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apimatic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apimatic-limited/
- group: other
  title: ''
  type: X
  url: https://x.com/APIMatic
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@apimatic/cli
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apimatic.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apimatic.io/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/apimatic/apimatic-validator-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/apimatic/skills
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/packages/apimatic-packages.yml
  title: ''
  type: Packages
  url: packages/apimatic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/packages/apimatic-packages.yml
  title: ''
  type: SDKs
  url: packages/apimatic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@apimatic/sdk
- group: build
  title: ''
  type: SDKs
  url: https://docs.apimatic.io/platform-api/#/java/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk
- group: build
  title: ''
  type: SDKs
  url: https://docs.apimatic.io/platform-api/#/net-standard-library/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk
- group: build
  title: ''
  type: SDKs
  url: https://docs.apimatic.io/platform-api/#/php/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk
- group: build
  title: ''
  type: SDKs
  url: https://docs.apimatic.io/platform-api/#/python/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk
- group: build
  title: ''
  type: SDKs
  url: https://docs.apimatic.io/platform-api/#/ruby/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/well-known/apimatic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apimatic-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/mcp/apimatic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apimatic-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/mcp/apimatic-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apimatic-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/llms/apimatic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apimatic-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/conformance/apimatic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apimatic-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/errors/apimatic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apimatic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/lifecycle/apimatic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apimatic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.apimatic.io/web-dashboard-retired/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/scopes/apimatic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apimatic-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/authentication/apimatic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apimatic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/conventions/apimatic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apimatic-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/changelog/apimatic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apimatic-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/cli/apimatic-cli.yml
  title: ''
  type: CLI
  url: cli/apimatic-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/components/apimatic-components.yml
  title: ''
  type: Components
  url: components/apimatic-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/sandbox/apimatic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/apimatic-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/plans/apimatic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apimatic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/rate-limits/apimatic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apimatic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/finops/apimatic-finops.yml
  title: ''
  type: FinOps
  url: finops/apimatic-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apimatic.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apimatic.io/platform-api/
created: '2025-01-08'
description: APIMatic is a developer experience platform for APIs that specializes in automated SDK generation, API documentation portal creation, specification validation and linting, and API format transformation. It supports 15+ API specification formats and generates idiomatic SDKs in 7+ programming languages with CI/CD integration for automating the developer experience suite.
features:
- description: Generate production-ready SDKs in Python, Java, C# .NET, TypeScript, PHP, Ruby, and Go from any API specification.
  name: Idiomatic SDK Generation
- description: Generate interactive developer documentation portals with code samples, guided walkthroughs, and code playground.
  name: API Documentation Portals
- description: Validate and lint API specifications with detailed error reports and best practice recommendations.
  name: API Specification Validation
- description: Convert API definitions between 15+ formats including OpenAPI 3.0, Swagger 2.0, RAML, API Blueprint, and Postman Collections.
  name: API Format Transformation
- description: Generate Model Context Protocol (MCP) servers from API specifications for AI agent integration.
  name: MCP Server Generation
- description: Define and automate your entire developer experience pipeline as code with CI/CD integration.
  name: DX as Code
- description: Automatically validate OpenAPI specifications in GitHub pull requests via the APIMatic linter GitHub App.
  name: OpenAPI Linter GitHub App
finops:
- name: Apimatic Finops
  service_category: API
  slug: apimatic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apimatic.png
integrations:
- description: APIMatic integration for generating SDKs from MuleSoft API definitions.
  name: MuleSoft
- description: Integration for enhanced API documentation workflows.
  name: Redocly
- description: CI/CD integration for automated SDK generation and API validation in GitHub workflows.
  name: GitHub Actions
json_schemas:
- name: ApiValidationSummary
  property_count: 4
  slug: apimatic-api-validation-summary
- name: ExportFormats
  property_count: 0
  slug: apimatic-export-formats
- name: GenerateSdkViaUrlRequest
  property_count: 2
  slug: apimatic-generate-sdk-via-url-request
- name: Platforms
  property_count: 0
  slug: apimatic-platforms
- name: TransformViaUrlRequest
  property_count: 2
  slug: apimatic-transform-via-url-request
- name: Transformation
  property_count: 12
  slug: apimatic-transformation
- name: UserCodeGeneration
  property_count: 10
  slug: apimatic-user-code-generation
jsonld:
- class_count: 22
  name: Apimatic Context
  property_count: 45
  slug: apimatic-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: ''
  name: APIMatic MCP servers (hosted Integration Agent + local validator)
  slug: apimatic-mcp-servers-hosted-integration-agent-local-validator
modified: '2026-09-23'
name: APIMatic
nav: Providers
network: true
overview: 'APIMatic publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Portals API, SDK Generation API, Transformation API, and 1 more. Tagged areas include API Transformation, Code Generation, Developer Experience, Developer Tools, and Documentation.


  The APIMatic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIMatic''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, changelog, and 49 more developer resources.'
plans:
- name: Apimatic Plans Pricing
  plan_count: 4
  slug: apimatic-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 7
  name: Apimatic Rate Limits
  slug: apimatic-rate-limits
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: APIMatic API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: apimatic-rules
scopes:
- name: Apimatic Scopes
  scope_count: 1
  slug: apimatic-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 93.0
    catalog_earned_first_party: 24.0
    catalog_gap: 22.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 77.6
    contract_governance: 33.3
    contract_quality: 28.4
    developer_ergonomics: 95.2
    discoverability: 81.5
    operational_transparency: 57.9
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/screenshots/apimatic-2026-07-25T200631.png
security:
- kind: authentication
  name: Apimatic Authentication
  slug: apimatic-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Apimatic Domain Security
  slug: apimatic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: apimatic-portal
  slug: apimatic-portal
- name: apimatic-sdk
  slug: apimatic-sdk
slug: apimatic
solutions:
- description: Basic SDK generation and API validation for individual developers.
  name: Free Plan
- description: Advanced SDK generation, portal publishing, and team collaboration features.
  name: Team Plan
- description: Full developer experience automation, custom branding, SLA, and dedicated support.
  name: Enterprise Plan
tags:
- API Transformation
- Code Generation
- Developer Experience
- Developer Tools
- Documentation
- SDK Generation
use_cases:
- description: Automatically generate and publish SDKs to npm, PyPI, Maven, and other package registries on every API change.
  name: Automated SDK Publishing
- description: Generate and host comprehensive API documentation portals with interactive examples and code playground.
  name: Developer Portal Generation
- description: Transform legacy Swagger 2.0 or RAML specs to OpenAPI 3.0 for modern tooling compatibility.
  name: API Specification Migration
- description: Integrate API validation and linting into CI/CD pipelines to enforce quality gates on API changes.
  name: CI/CD API Governance
website: https://www.apimatic.io/
---
