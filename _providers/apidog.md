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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apidog Agentic Access
  operation_count: 3
  slug: apidog-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.apidog.com
  baseurl_source: declared
  description: Import and export API specification data in OpenAPI, Swagger, and Postman Collection formats.
  name: Apidog Import And Export API
  slug: apidog-import-and-export-api
arazzos:
- description: Export a project as a backup document, then branch to restore it into a recovery project only when the export succeeds.
  name: Apidog Backup And Restore Project
  slug: apidog-backup-and-restore-project-workflow
- description: Import an OpenAPI spec and a Postman Collection into one project, then export the merged result.
  name: Apidog Consolidate Sources Into One Project
  slug: apidog-consolidate-sources-into-project-workflow
- description: Import a Postman Collection into Apidog and export it back out as OpenAPI.
  name: Apidog Convert Postman Collection To OpenAPI
  slug: apidog-convert-postman-to-openapi-workflow
- description: Import a modern OpenAPI spec into a project and re-export it at an older OpenAPI version.
  name: Apidog Downgrade OpenAPI Version
  slug: apidog-downgrade-oas-version-workflow
- description: Export the same project once as JSON and once as YAML to produce a two-format archive.
  name: Apidog Dual-Format Export Archive
  slug: apidog-dual-format-export-archive-workflow
- description: Import an OpenAPI spec from a remote URL into a project, then export it back to verify.
  name: Apidog Import Spec From URL And Verify
  slug: apidog-import-from-url-and-verify-workflow
- description: Export the API specification from one Apidog project and import it into another.
  name: Apidog Migrate Spec Between Projects
  slug: apidog-migrate-spec-between-projects-workflow
- description: Export a spec from one sprint branch and import it into another branch of the same project.
  name: Apidog Promote Spec Between Branches
  slug: apidog-promote-spec-between-branches-workflow
- description: Export a specific module from one project and import it into a module of another project.
  name: Apidog Sync Module Across Projects
  slug: apidog-sync-module-across-projects-workflow
artifact_total: 59
collections:
- collection_type: postman
  name: Apidog API
  slug: postman-apidog-apidog
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apidog API
  slug: open-apidog-apidog
- collection_type: open
  name: Apidog Import And Export API
  slug: open-apidog-import-and-export-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apidog-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apidog-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apidog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apidog-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apidog/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-backup-and-restore-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-consolidate-sources-into-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-convert-postman-to-openapi-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-downgrade-oas-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-dual-format-export-archive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-import-from-url-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-migrate-spec-between-projects-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-promote-spec-between-branches-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apidog-sync-module-across-projects-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apidog
- group: company
  title: ''
  type: Website
  url: https://apidog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apidog.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apidog.com/overview-644404m0
- group: commercial
  title: ''
  type: Pricing
  url: https://apidog.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://apidog.com/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://apidog.com/blog/product-updates/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apidog.com/
- group: other
  title: ''
  type: Articles
  url: https://apidog.com/articles/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.apidog.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.apidog.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.apidog.com/apidog-support-center-748035m0
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Apidog
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/Apidog/roadmap
- group: build
  title: ''
  type: CLI
  url: https://docs.apidog.com/installing-and-running-apidog-cli-605135m0
- group: build
  title: ''
  type: PackageManager
  url: https://www.npmjs.com/package/apidog-cli
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.apidog.com/apidog-mcp-server
- group: agent
  title: ''
  type: MCPServer
  url: https://www.npmjs.com/package/apidog-mcp-server
- group: agent
  title: ''
  type: MCPClient
  url: https://docs.apidog.com/mcp-client-1930835m0
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Apidog/apidog-locales
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.apidog.com/llms.txt
created: '2025-01-08'
description: 'Apidog is an all-in-one API development platform that connects the entire API lifecycle: visual API design, multi-protocol debugging (HTTP, REST, GraphQL, gRPC, WebSocket, SOAP, SSE), automated testing with a CLI, smart mocking, and published interactive documentation - all in a single collaborative workspace. As of 2026 Apidog also ships native MCP support: an apidog-mcp-server that feeds API specs to AI coding assistants (Cursor, VS Code + Cline) and an MCP Client inside the desktop app that visually debugs MCP servers over STDIO and Streamable HTTP with auto OAuth 2.0 configuration.'
examples:
- key_count: 5
  name: Apidog Export Openapi Example
  slug: apidog-export-openapi-example
- key_count: 5
  name: Apidog Import Openapi Example
  slug: apidog-import-openapi-example
- key_count: 5
  name: Apidog Import Postman Collection Example
  slug: apidog-import-postman-collection-example
features:
- description: Visual OpenAPI/Swagger editor with JSON Schema support, reusable schemas, Git integration, and sprint branches for collaborative development.
  name: API Design
- description: Multi-protocol support for HTTP, REST, GraphQL, gRPC, SOAP, WebSocket, and SSE with auto-validation of responses against API specs and direct database connectivity.
  name: API Debugging
- description: Visual test scenarios with CI/CD integration via the apidog-cli npm package, data-driven testing with CSV/JSON datasets, performance testing, and AI-generated test cases.
  name: API Testing
- description: Zero-configuration smart mock generation from specs, cloud-based and local mock servers, and custom mock rules.
  name: API Mocking
- description: Auto-generated interactive docs with custom domains, auto-generated SSL certificates, Markdown support, and versioning control.
  name: API Documentation
- description: Real-time synchronization, sprint branches for parallel development, role-based access control, and SSO support.
  name: Team Collaboration
- description: Local MCP server (npx apidog-mcp-server) that feeds Apidog projects, published docs, or local/remote OpenAPI files to AI coding assistants like Cursor and VS Code + Cline for grounded code generation.
  name: Apidog MCP Server
- description: Visual MCP debugging built into the Apidog app. Supports STDIO and Streamable HTTP transports with auto OAuth 2.0 configuration and a Tools / Prompts / Resources tree.
  name: Apidog MCP Client
- description: AI Test Engine analyzes API specs to automatically generate positive, error-handling, boundary, and security test cases.
  name: AI Test Case Generation
- description: AI assistance to modify field descriptions and generate mock data directly inside API schemas.
  name: AI Schema Descriptions and Mock
- description: SOC 2 Type II posture with GDPR and ISO 27001 alignment, TLS 1.3+ in transit, AES-256 at rest, plus optional on-premises deployment.
  name: Enterprise Security
finops:
- name: Apidog Finops
  service_category: Developer Tools
  slug: apidog-finops
graphqls:
- description: ''
  name: Apidog GraphQL API
  slug: apidog-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apidog.png
integrations:
- description: Import and export OpenAPI 2.0 / 3.0 / 3.1 specifications, with Apidog-specific x-apidog-* extensions preserved on export.
  name: OpenAPI / Swagger
- description: Postman Collection v2 import with scripting-syntax compatibility.
  name: Postman
- description: Apidog CLI integrates with Jenkins, GitLab CI, GitHub Actions, and Bitbucket Pipelines for automated test runs.
  name: CI/CD Platforms
- description: Connects to MySQL, PostgreSQL, Oracle, SQL Server, and ClickHouse for dynamic test data.
  name: Databases
- description: HashiCorp Vault, Azure Key Vault, and AWS Secrets Manager.
  name: Credential Vaults
- description: SAML 2.0, Microsoft Active Directory, OIDC, and SCIM for enterprise identity management.
  name: Enterprise SSO
- description: IDEA plugin for JavaDoc-driven API definition generation.
  name: IntelliJ IDEA Plugin
- description: Through apidog-mcp-server, Apidog projects and OpenAPI files become directly accessible to MCP-compatible AI coding assistants.
  name: Cursor And VS Code + Cline
json_schemas:
- name: Apidog Error
  property_count: 2
  slug: apidog-error
- name: Apidog Export Result
  property_count: 2
  slug: apidog-export-result
- name: Apidog Import Result
  property_count: 2
  slug: apidog-import-result
- name: Apidog Project
  property_count: 7
  slug: apidog-project
jsonld:
- class_count: 2
  name: Apidog Context
  property_count: 9
  slug: apidog-context
layout: provider
mcp_servers:
- description: ''
  name: Apidog MCP Server
  slug: apidog-mcp-server
- description: ''
  name: Apidog MCP Server
  slug: apidog-mcp-server-2
modified: '2026-05-22'
name: Apidog
nav: Providers
network: true
overview: 'Apidog publishes 1 API on the [APIs.io](https://apis.io/) network: Import And Export API. Tagged areas include AI Coding, API Design, API Lifecycle, API Testing, and Collaboration.


  The Apidog catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apidog''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, release notes, support, and 28 more developer resources.'
plans:
- name: Apidog Plans Pricing
  plan_count: 4
  slug: apidog-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Apidog Rate Limits
  slug: apidog-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apidog API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apidog-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Apidog API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 12
  slug: apidog-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 74.8
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 60.5
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apidog/refs/heads/main/screenshots/apidog-2026-06-20T172233.png
security:
- kind: authentication
  name: Apidog Authentication
  slug: apidog-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apidog Domain Security
  slug: apidog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Apidog Trust Center
  slug: apidog-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: apidog
tags:
- AI Coding
- API Design
- API Lifecycle
- API Testing
- Collaboration
- Design-First
- Documentation
- MCP
- Mocking
- Platform
use_cases:
- description: Design APIs visually before writing code, enabling frontend and backend teams to work in parallel.
  name: API Design-First Development
- description: Build comprehensive regression test suites with CI/CD integration (Jenkins, GitHub Actions, GitLab CI, Bitbucket) via the Apidog CLI.
  name: Automated API Testing
- description: Automatically generate and publish interactive developer documentation from API specifications, with custom domains and white-labeling on paid tiers.
  name: API Documentation Publishing
- description: Enable frontend development independent of backend completion using intelligent mock data generation from specs.
  name: Mock Server Development
- description: Connect Apidog projects to Cursor or VS Code + Cline through the Apidog MCP Server so AI assistants generate DTOs, controllers, and client code aligned with the real API contract.
  name: AI-Assisted API Coding
- description: Use Apidog MCP Client to visually exercise MCP servers (Tools, Prompts, Resources) over STDIO or Streamable HTTP while building AI-agent backends.
  name: AI Agent Debugging
website: https://apidog.com/
---
