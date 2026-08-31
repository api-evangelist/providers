---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Niural Agentic Access
  operation_count: 15
  slug: niural-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- description: The Authentication API from Niural — 1 operation(s) for authentication.
  name: Niural Authentication API
  slug: niural-authentication-api
- description: The Contracts API from Niural — 4 operation(s) for contracts.
  name: Niural Contracts API
  slug: niural-contracts-api
- description: The Invoices API from Niural — 2 operation(s) for invoices.
  name: Niural Invoices API
  slug: niural-invoices-api
- description: The Transactions API from Niural — 4 operation(s) for transactions.
  name: Niural Transactions API
  slug: niural-transactions-api
artifact_total: 18
asyncapis:
- description: ''
  name: Niural Webhooks
  slug: niural-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Niural Public Authentication API
  slug: open-niural-authentication-api
- collection_type: open
  name: Niural Public Contracts API
  slug: open-niural-contracts-api
- collection_type: open
  name: Niural Public Invoices API
  slug: open-niural-invoices-api
- collection_type: open
  name: Niural Public Transactions API
  slug: open-niural-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.niural.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.niural.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.niural.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.niural.com/reference/post_authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.niural.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://help.niural.com/
- group: company
  title: ''
  type: Blog
  url: https://www.niural.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Niural
- group: commercial
  title: ''
  type: Pricing
  url: https://www.niural.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.niural.com/auth/employer/register
- group: start
  title: ''
  type: Login
  url: https://app.niural.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.niural.com/legal/customer-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.niural.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.niural.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/niural-trust-center.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/niural-public-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/niural-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/niural-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/niural-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/niural-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/niural-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/niural-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/niural-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/niural-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/niural-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/niural-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/niural-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/niural-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/niural-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/niural-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/niural-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/niural-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/niural-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/niural-agentic-access.yml
created: '2026-08-04'
description: 'Niural is a US-headquartered global workforce platform that unifies US payroll, PEO, employer of record (EOR), agent of record (AOR), contractor management and cross-border contractor payments in 150+ countries inside a single system, with an AI layer (EMMA) that orchestrates payroll, compliance and expense approvals. Its public developer surface — the Niural Public API, documented on ReadMe at docs.niural.com — is narrower than the product: an OpenAPI 3.0.3 contract of 15 operations across four resources (authentication, pay-on-demand contractor contracts, invoices and transactions), served from separate sandbox and live hosts, authenticated with a client-credential exchange that returns a bearer JWT, with cursor pagination, a 25 requests/second rate limit, and three HMAC-SHA256-signed webhook events. Payroll, PEO, EOR and benefits are not exposed on the public API.'
image: https://www.niural.com/favicon.ico
layout: provider
mcp_servers:
- description: Niural operates no hosted or remote MCP server. Searched docs.niural.com (full llms.txt page index), niural.com, the Niural GitHub org, npm and the public MCP registries — no result; mcp.niural.com do
  name: Niural MCP Server
  slug: niural-mcp-server
modified: '2026-08-04'
name: Niural
nav: Providers
network: true
overview: 'Niural publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Invoices API, and 1 more. Tagged areas include Company, Payroll, Human Resources, Employer of Record, and Contractor Management.


  The Niural catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Niural''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Niural Plans Pricing
  plan_count: 8
  slug: niural-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Niural Rate Limits
  slug: niural-rate-limits
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 41.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/niural/refs/heads/main/screenshots/niural-2026-08-07T185346.png
security:
- kind: authentication
  name: Niural Authentication
  slug: niural-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Niural Domain Security
  slug: niural-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Niural Vulnerability Disclosure
  slug: niural-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Niural Trust Center
  slug: niural-trust-center
  summary_line: SOC 2 Type II
slug: niural
tags:
- Company
- Payroll
- Human Resources
- Employer of Record
- Contractor Management
- Global Payments
- Invoicing
- Compliance
- Fintech
website: https://www.niural.com/
---
