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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apimatic Agentic Access
  operation_count: 6
  slug: apimatic-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- description: APIMatic API Transformer converts API definition files between more than 15 supported API specification formats including OpenAPI, RAML, API Blueprint, WSDL, WADL, and Postman Collections.
  name: APIMatic API Transformer API
  slug: apimatic-api-transformer-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: The Portals API from APIMatic — 1 operation(s) for portals.
  name: APIMatic Portals API
  slug: apimatic-portals-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: The SDK Generation API from APIMatic — 1 operation(s) for sdk generation.
  name: APIMatic SDK Generation API
  slug: apimatic-sdk-generation-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: The Transformation API from APIMatic — 1 operation(s) for transformation.
  name: APIMatic Transformation API
  slug: apimatic-transformation-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: The Validation API from APIMatic — 1 operation(s) for validation.
  name: APIMatic Validation API
  slug: apimatic-validation-api
- baseURL: https://api.apimatic.io
  baseurl_source: declared
  description: The APIs API from APIMatic — 1 operation(s) for apis.
  name: APIMatic AP Is API
  slug: apimatic-apis-api
arazzos:
- description: Import, validate, transform to OpenAPI 3, then generate an SDK in one pass.
  name: APIMatic Full SDK Release Pipeline
  slug: apimatic-full-release-pipeline-workflow
- description: Import an API spec once and produce both an SDK and a docs portal from it.
  name: APIMatic Import then Generate SDK and Portal
  slug: apimatic-import-generate-sdk-and-portal-workflow
- description: Import an API spec and convert it to a different specification format.
  name: APIMatic Import and Transform Specification
  slug: apimatic-import-transform-workflow
- description: Import an API spec, lint it, and generate a docs portal when it is valid.
  name: APIMatic Import, Validate and Publish Portal
  slug: apimatic-import-validate-generate-portal-workflow
- description: Import an API spec, lint it, and only generate an SDK when it is valid.
  name: APIMatic Import, Validate and Generate SDK
  slug: apimatic-import-validate-generate-sdk-workflow
- description: List existing API entities and regenerate an SDK for the first one.
  name: APIMatic Regenerate SDK for Existing Entity
  slug: apimatic-list-entities-generate-sdk-workflow
artifact_total: 55
collections:
- collection_type: postman
  name: APIMatic Platform API
  slug: postman-apimatic-platform-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIMatic Platform APIs API
  slug: open-apimatic-apis-api
- collection_type: open
  name: APIMatic Platform APIs Portals API
  slug: open-apimatic-portals-api
- collection_type: open
  name: APIMatic Platform APIs SDK Generation API
  slug: open-apimatic-sdk-generation-api
- collection_type: open
  name: APIMatic Platform APIs Transformation API
  slug: open-apimatic-transformation-api
- collection_type: open
  name: APIMatic Platform APIs Validation API
  slug: open-apimatic-validation-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/agentic-access/apimatic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apimatic-agentic-access.yml
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apimatic/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-full-release-pipeline-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-full-release-pipeline-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-import-generate-sdk-and-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-import-generate-sdk-and-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-import-transform-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-import-transform-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-import-validate-generate-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-import-validate-generate-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-import-validate-generate-sdk-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-import-validate-generate-sdk-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/arazzo/apimatic-list-entities-generate-sdk-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apimatic-list-entities-generate-sdk-workflow.yml
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/overlays/apimatic-apis-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimatic-apis-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/overlays/apimatic-portals-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimatic-portals-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/overlays/apimatic-sdk-generation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimatic-sdk-generation-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/overlays/apimatic-transformation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimatic-transformation-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/overlays/apimatic-validation-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimatic-validation-api-overlay.yaml
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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/data-model/apimatic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apimatic-data-model.yml
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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/vocabulary/apimatic-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/apimatic-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/rules/apimatic-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/apimatic-jsonschema-spectral-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/examples/apimatic-api-entity-example.json
  title: ''
  type: Examples
  url: examples/apimatic-api-entity-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/examples/apimatic-sdk-generation-example.json
  title: ''
  type: Examples
  url: examples/apimatic-sdk-generation-example.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimatic/refs/heads/main/postman/apimatic-platform-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: postman/apimatic-platform-api.postman_collection.json
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
examples:
- key_count: 6
  name: Apimatic Api Entity Example
  slug: apimatic-api-entity-example
- key_count: 3
  name: Apimatic Sdk Generation Example
  slug: apimatic-sdk-generation-example
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
- name: APIMatic API Entity
  property_count: 6
  slug: apimatic-api-entity
- name: APIMatic SDK Generation
  property_count: 3
  slug: apimatic-sdk-generation
json_structures:
- name: Apimatic Api Entity Structure
  property_count: 6
  slug: apimatic-api-entity-structure
- name: Apimatic Sdk Generation Structure
  property_count: 3
  slug: apimatic-sdk-generation-structure
jsonld:
- class_count: 9
  name: Apimatic Context
  property_count: 4
  slug: apimatic-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: ''
  name: APIMatic MCP servers (hosted Integration Agent + local validator)
  slug: apimatic-mcp-servers-hosted-integration-agent-local-validator
modified: '2026-09-15'
name: APIMatic
nav: Providers
network: true
overview: 'APIMatic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Portals API, SDK Generation API, Transformation API, and 2 more. Tagged areas include API Transformation, Code Generation, Developer Experience, Developer Tools, and Documentation.


  The APIMatic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIMatic''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, changelog, and 54 more developer resources.'
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
- effective_rule_count: 5
  extends: []
  name: APIMatic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apimatic-jsonschema-spectral-rules
scopes:
- name: Apimatic Scopes
  scope_count: 1
  slug: apimatic-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 70.0
  coverage:
    artifact_dirs: 35
    catalog_earned: 90.3
    catalog_earned_first_party: 24.0
    catalog_gap: 24.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 43.2
    contract_quality: 70.2
    developer_ergonomics: 86.9
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
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
