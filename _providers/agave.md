---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 226
  human_in_the_loop: 3
  name: Agave Agentic Access
  operation_count: 438
  slug: agave-agentic-access
  summary_line: 438 operations · 226 acting · 3 human-in-the-loop
api_count: 18
apis:
- description: 'Agave Link is a front-end component that enables users to select source systems, authenticate with their construction software accounts, and share data with your application, handling OAuth flows for '
  name: Agave Link Component
  slug: agave-link
- description: Agave File Manager is a front-end component that allows users to pick files and folders from linked construction software accounts to share with your application.
  name: Agave File Manager Component
  slug: agave-file-manager
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Project budget and cost management resources.
  name: Agave Budgets API
  slug: agave-budgets-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Prime contracts and commitment management.
  name: Agave Contracts API
  slug: agave-contracts-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Job cost codes and cost types.
  name: Agave Cost Codes API
  slug: agave-cost-codes-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Employee records and workforce management.
  name: Agave Employees API
  slug: agave-employees-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Accounts payable invoices and billing.
  name: Agave Invoices API
  slug: agave-invoices-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Agave Link session management for user authentication.
  name: Agave Link Sessions API
  slug: agave-link-sessions-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Construction project management resources.
  name: Agave Projects API
  slug: agave-projects-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Employee timesheet and labor tracking.
  name: Agave Timesheets API
  slug: agave-timesheets-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Vendor and subcontractor management.
  name: Agave Vendors API
  slug: agave-vendors-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Common resources in the Agave unified construction API.
  name: Agave Common API
  slug: agave-common-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Customer Management resources in the Agave unified construction API.
  name: Agave Customer Management API
  slug: agave-customer-management-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: File Management resources in the Agave unified construction API.
  name: Agave File Management API
  slug: agave-file-management-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Financials Management resources in the Agave unified construction API.
  name: Agave Financials Management API
  slug: agave-financials-management-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Project Management resources in the Agave unified construction API.
  name: Agave Project Management API
  slug: agave-project-management-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Service Management resources in the Agave unified construction API.
  name: Agave Service Management API
  slug: agave-service-management-api
- baseURL: https://api.agaveapi.com
  baseurl_source: declared
  description: Webhooks resources in the Agave unified construction API.
  name: Agave Webhooks API
  slug: agave-webhooks-api
artifact_total: 113
asyncapis:
- description: ''
  name: Agave Webhooks
  slug: agave-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agave Unified Construction Budgets API
  slug: open-agave-budgets-api
- collection_type: open
  name: Agave Unified Construction Budgets Contracts API
  slug: open-agave-contracts-api
- collection_type: open
  name: Agave Unified Construction Budgets Cost Codes API
  slug: open-agave-cost-codes-api
- collection_type: open
  name: Agave Unified Construction Budgets Employees API
  slug: open-agave-employees-api
- collection_type: open
  name: Agave Unified Construction Budgets Invoices API
  slug: open-agave-invoices-api
- collection_type: open
  name: Agave Unified Construction Budgets Link Sessions API
  slug: open-agave-link-sessions-api
- collection_type: open
  name: Agave Unified Construction Budgets Projects API
  slug: open-agave-projects-api
- collection_type: open
  name: Agave Unified Construction Budgets Timesheets API
  slug: open-agave-timesheets-api
- collection_type: open
  name: Agave Unified Construction API
  slug: open-agave-unified-api
- collection_type: open
  name: Agave Unified Construction Budgets Vendors API
  slug: open-agave-vendors-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/agentic-access/agave-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agave-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/security/agave-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agave-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/security/agave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agave-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/authentication/agave-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agave-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agave-api
- group: start
  title: ''
  type: Portal
  url: https://docs.agaveapi.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agaveapi.com/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.agaveapi.com/agave-api/identifiers
- group: commercial
  title: ''
  type: Pricing
  url: https://useagave.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://security.agaveapi.com/
- group: company
  title: ''
  type: Partners
  url: https://useagave.com/partner-hub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agave-api
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/packages/agave-packages.yml
  title: ''
  type: SDKs
  url: packages/agave-packages.yml
- group: build
  title: React SDK (archived)
  type: SDKs
  url: https://github.com/agave-api/react-agave-link
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/openapi/_ae-authored/agave-unified-api-from-postman-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/agave-unified-api-from-postman-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/openapi/_ae-authored/agave-unified-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/agave-unified-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-budget-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-budget-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-budget-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-budget-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-contract-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-contract-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-contract-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-contract-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-cost-code-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-cost-code-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-cost-code-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-cost-code-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-employee-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-employee-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-employee-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-employee-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-invoice-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-invoice-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-request-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-invoice-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-invoice-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-link-session-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-link-session-request-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-link-session-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-link-session-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-project-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-project-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-project-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-timesheet-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-timesheet-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-timesheet-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-timesheet-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-vendor-list-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-vendor-list-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-schema/unified-api-vendor-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/unified-api-vendor-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-budget-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-budget-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-budget-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-budget-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-contract-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-contract-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-contract-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-contract-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-cost-code-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-cost-code-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-cost-code-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-cost-code-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-employee-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-employee-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-employee-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-employee-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-invoice-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-invoice-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-request-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-invoice-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-invoice-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-link-session-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-link-session-request-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-link-session-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-link-session-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-project-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-project-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-project-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-project-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-timesheet-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-timesheet-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-timesheet-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-timesheet-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-vendor-list-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-vendor-list-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-structure/unified-api-vendor-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/unified-api-vendor-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-ld/agave-unified-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agave-unified-context.jsonld
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-budget-example.json
  title: ''
  type: Examples
  url: examples/unified-api-budget-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-budget-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-budget-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-contract-example.json
  title: ''
  type: Examples
  url: examples/unified-api-contract-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-contract-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-contract-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-cost-code-example.json
  title: ''
  type: Examples
  url: examples/unified-api-cost-code-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-cost-code-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-cost-code-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-employee-example.json
  title: ''
  type: Examples
  url: examples/unified-api-employee-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-employee-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-employee-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-invoice-example.json
  title: ''
  type: Examples
  url: examples/unified-api-invoice-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-invoice-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-invoice-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-invoice-request-example.json
  title: ''
  type: Examples
  url: examples/unified-api-invoice-request-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-link-session-example.json
  title: ''
  type: Examples
  url: examples/unified-api-link-session-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-link-session-request-example.json
  title: ''
  type: Examples
  url: examples/unified-api-link-session-request-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-project-example.json
  title: ''
  type: Examples
  url: examples/unified-api-project-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-project-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-project-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-timesheet-example.json
  title: ''
  type: Examples
  url: examples/unified-api-timesheet-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-timesheet-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-timesheet-list-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-vendor-example.json
  title: ''
  type: Examples
  url: examples/unified-api-vendor-example.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/examples/unified-api-vendor-list-example.json
  title: ''
  type: Examples
  url: examples/unified-api-vendor-list-example.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/rules/agave-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/agave-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/vocabulary/agave-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/agave-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://useagave.com/blog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/packages/agave-packages.yml
  title: ''
  type: Packages
  url: packages/agave-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/well-known/agave-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/agave-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/mcp/agave-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agave-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/mcp/agave-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agave-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/llms/agave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agave-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/overlays/agave-unified-api-from-postman-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agave-unified-api-from-postman-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/conformance/agave-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agave-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.agaveapi.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/errors/agave-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agave-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/lifecycle/agave-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agave-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agaveapi.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/changelog/agave-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agave-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://useagave.com/product-updates
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/conventions/agave-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agave-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/conventions/agave-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agave-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/rate-limits/agave-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agave-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/plans/agave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agave-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/sandbox/agave-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agave-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/components/agave-components.yml
  title: ''
  type: Components
  url: components/agave-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/data-model/agave-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agave-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/asyncapi/agave-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agave-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://docs.agaveapi.com/agave-api/postman-collection
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/collections/agave-api-provider.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/agave-api-provider.postman_collection.json
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agaveapi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agaveapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agaveapi.com/reference
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@agaveapi.com
- group: start
  title: ''
  type: SignUp
  url: https://useagave.com/get-access
- group: start
  title: ''
  type: Login
  url: https://app.agaveapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://useagave.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useagave.com/privacy
- group: company
  title: ''
  type: Website
  url: https://useagave.com
created: '2025-03-01'
description: Agave is a unified API platform for the construction industry, enabling software companies and contractors to read and write data across 100+ construction and accounting software systems including Procore, Autodesk Build, QuickBooks, Sage, Viewpoint, and more.
examples:
- key_count: 8
  name: Unified Api Budget Example
  slug: unified-api-budget-example
- key_count: 3
  name: Unified Api Budget List Example
  slug: unified-api-budget-list-example
- key_count: 8
  name: Unified Api Contract Example
  slug: unified-api-contract-example
- key_count: 3
  name: Unified Api Contract List Example
  slug: unified-api-contract-list-example
- key_count: 5
  name: Unified Api Cost Code Example
  slug: unified-api-cost-code-example
- key_count: 3
  name: Unified Api Cost Code List Example
  slug: unified-api-cost-code-list-example
- key_count: 7
  name: Unified Api Employee Example
  slug: unified-api-employee-example
- key_count: 3
  name: Unified Api Employee List Example
  slug: unified-api-employee-list-example
- key_count: 8
  name: Unified Api Invoice Example
  slug: unified-api-invoice-example
- key_count: 3
  name: Unified Api Invoice List Example
  slug: unified-api-invoice-list-example
- key_count: 5
  name: Unified Api Invoice Request Example
  slug: unified-api-invoice-request-example
- key_count: 3
  name: Unified Api Link Session Example
  slug: unified-api-link-session-example
- key_count: 2
  name: Unified Api Link Session Request Example
  slug: unified-api-link-session-request-example
- key_count: 11
  name: Unified Api Project Example
  slug: unified-api-project-example
- key_count: 3
  name: Unified Api Project List Example
  slug: unified-api-project-list-example
- key_count: 8
  name: Unified Api Timesheet Example
  slug: unified-api-timesheet-example
- key_count: 3
  name: Unified Api Timesheet List Example
  slug: unified-api-timesheet-list-example
- key_count: 7
  name: Unified Api Vendor Example
  slug: unified-api-vendor-example
- key_count: 3
  name: Unified Api Vendor List Example
  slug: unified-api-vendor-list-example
features:
- description: Single REST API to read and write data across 100+ construction and accounting software systems with normalized data models.
  name: Unified Construction API
- description: Pre-built front-end component for user authentication that handles OAuth flows for all supported construction software platforms.
  name: Agave Link Authentication
- description: Automatic synchronization of jobs, financials, timesheets, and cost data between field systems and ERP platforms.
  name: ERP Sync
- description: AI-powered invoice capture, job matching, cost code coding, approval routing, and ERP sync for accounts payable workflows.
  name: AP Invoice Automation
- description: Direct passthrough of requests to source system APIs with Agave handling authentication and protocol translation.
  name: Passthrough Requests
- description: Real-time webhook notifications for data changes in connected construction software systems.
  name: Webhooks
- description: Sandbox mode for testing integrations without affecting production data in connected systems.
  name: Sandbox Environments
- description: Pre-built front-end component for browsing and selecting files from connected construction document storage systems.
  name: Agave File Manager
finops:
- name: Agave Finops
  service_category: Construction Tech / Integration
  slug: agave-finops
graphqls:
- description: '> **NOT A PROVIDER ENDPOINT.** Agave ships no GraphQL API. This document and'
  name: Agave GraphQL Schema
  slug: agave-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agave.png
json_schemas:
- name: BudgetList
  property_count: 3
  slug: unified-api-budget-list
- name: Budget
  property_count: 8
  slug: unified-api-budget
- name: ContractList
  property_count: 3
  slug: unified-api-contract-list
- name: Contract
  property_count: 8
  slug: unified-api-contract
- name: CostCodeList
  property_count: 3
  slug: unified-api-cost-code-list
- name: CostCode
  property_count: 5
  slug: unified-api-cost-code
- name: EmployeeList
  property_count: 3
  slug: unified-api-employee-list
- name: Employee
  property_count: 7
  slug: unified-api-employee
- name: InvoiceList
  property_count: 3
  slug: unified-api-invoice-list
- name: InvoiceRequest
  property_count: 5
  slug: unified-api-invoice-request
- name: Invoice
  property_count: 8
  slug: unified-api-invoice
- name: LinkSessionRequest
  property_count: 2
  slug: unified-api-link-session-request
- name: LinkSession
  property_count: 3
  slug: unified-api-link-session
- name: ProjectList
  property_count: 3
  slug: unified-api-project-list
- name: Project
  property_count: 11
  slug: unified-api-project
- name: TimesheetList
  property_count: 3
  slug: unified-api-timesheet-list
- name: Timesheet
  property_count: 8
  slug: unified-api-timesheet
- name: VendorList
  property_count: 3
  slug: unified-api-vendor-list
- name: Vendor
  property_count: 7
  slug: unified-api-vendor
json_structures:
- name: Unified Api Budget List Structure
  property_count: 3
  slug: unified-api-budget-list-structure
- name: Unified Api Budget Structure
  property_count: 8
  slug: unified-api-budget-structure
- name: Unified Api Contract List Structure
  property_count: 3
  slug: unified-api-contract-list-structure
- name: Unified Api Contract Structure
  property_count: 8
  slug: unified-api-contract-structure
- name: Unified Api Cost Code List Structure
  property_count: 3
  slug: unified-api-cost-code-list-structure
- name: Unified Api Cost Code Structure
  property_count: 5
  slug: unified-api-cost-code-structure
- name: Unified Api Employee List Structure
  property_count: 3
  slug: unified-api-employee-list-structure
- name: Unified Api Employee Structure
  property_count: 7
  slug: unified-api-employee-structure
- name: Unified Api Invoice List Structure
  property_count: 3
  slug: unified-api-invoice-list-structure
- name: Unified Api Invoice Request Structure
  property_count: 5
  slug: unified-api-invoice-request-structure
- name: Unified Api Invoice Structure
  property_count: 8
  slug: unified-api-invoice-structure
- name: Unified Api Link Session Request Structure
  property_count: 2
  slug: unified-api-link-session-request-structure
- name: Unified Api Link Session Structure
  property_count: 3
  slug: unified-api-link-session-structure
- name: Unified Api Project List Structure
  property_count: 3
  slug: unified-api-project-list-structure
- name: Unified Api Project Structure
  property_count: 11
  slug: unified-api-project-structure
- name: Unified Api Timesheet List Structure
  property_count: 3
  slug: unified-api-timesheet-list-structure
- name: Unified Api Timesheet Structure
  property_count: 8
  slug: unified-api-timesheet-structure
- name: Unified Api Vendor List Structure
  property_count: 3
  slug: unified-api-vendor-list-structure
- name: Unified Api Vendor Structure
  property_count: 7
  slug: unified-api-vendor-structure
jsonld:
- class_count: 24
  name: Agave Unified Context
  property_count: 42
  slug: agave-unified-context
layout: provider
mcp_servers:
- description: 'Agave MCP is a shipped, named Agave product — "Interact with your ERP & PM data securely in ChatGPT, Claude, or Copilot" — listed in the site navigation, the pricing page and the footer alongside ERP '
  name: Agave MCP - shipped product, endpoint not published
  slug: agave-mcp-shipped-product-endpoint-not-published
modified: '2026-08-30'
name: Agave
nav: Providers
network: true
overview: 'Agave publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Budgets API, Contracts API, Cost Codes API, and 13 more. Tagged areas include Accounting, Construction, Integration, ERP, and Project Management.


  The Agave catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Agave''s developer surface includes authentication, developer portal, getting-started guide, pricing, code examples, engineering blog, changelog, and 103 more developer resources.'
plans:
- name: Agave Plans Pricing
  plan_count: 0
  slug: agave-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Agave Rate Limits
  slug: agave-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agave-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Agave API Rules
  rule_count: 29
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 15
  slug: agave-spectral-rules
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 75.5
    catalog_earned_first_party: 12.0
    catalog_gap: 39.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 33.3
    contract_quality: 40.5
    developer_ergonomics: 78.0
    discoverability: 74.1
    operational_transparency: 84.2
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/screenshots/agave-2026-06-20T165757.png
security:
- kind: authentication
  name: Agave Authentication
  slug: agave-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Agave Domain Security
  slug: agave-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Agave Trust Center
  slug: agave-trust-center
  summary_line: SOC 2, GDPR
slug: agave
tags:
- Accounting
- Construction
- Integration
- ERP
- Project Management
- Unified-API
- iPaaS
- Webhook
- Field Service
- Invoicing
use_cases:
- description: Construction software companies integrate with 100+ other platforms via a single API instead of building and maintaining individual integrations.
  name: Construction Software Integration
- description: Automatically sync jobs, cost codes, and financials between project management systems like Procore and ERP systems like QuickBooks or Sage.
  name: ERP and PM Sync
- description: Automate AP invoice capture, job matching, and ERP posting using AI-powered invoice processing workflows.
  name: Invoice Processing Automation
- description: Pull budget, contract, commitment, and cost data from construction software for real-time job cost analysis and reporting.
  name: Job Costing
- description: Sync employee timesheets from field systems to accounting ERPs to eliminate manual payroll data entry.
  name: Timesheet Integration
- description: Enable users to select and share files from connected construction document storage systems using Agave File Manager.
  name: Document Management
website: https://useagave.com
---
