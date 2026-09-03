---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Check's REST API for embedding full-service payroll — companies, employees, contractors, pay schedules, payrolls, payments, tax filings, documents, bank accounts, and webhooks — into a platform produc
  name: Check Payroll API
  slug: check-payroll-api
artifact_total: 6
asyncapis:
- description: ''
  name: Check Technologies Webhooks
  slug: check-technologies-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/check-technologies-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.checkhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkhq.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.checkhq.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.checkhq.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/check-technologies-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.checkhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.checkhq.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/check-technologies
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.checkhq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checkhq.com/company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkhq.com/company/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.checkhq.com/company/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.checkhq.com/company/security
- group: design
  title: ''
  type: Conformance
  url: conformance/check-technologies-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/check-technologies-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.checkhq.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/check-technologies-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/check-technologies-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/check-technologies-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/check-technologies-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/check-technologies-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/check-technologies-cli.yml
- group: design
  title: ''
  type: Components
  url: components/check-technologies-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/check-technologies-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/check-technologies-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/check-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/check-technologies-error-codes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/check-technologies-llms.txt
created: '2026-07-17'
description: Check Technologies (Check) is a Stripe-incubated embedded-payroll infrastructure company whose API lets vertical SaaS, HR, and time-tracking platforms embed full-service payroll directly into their own products. The Check API handles the hard parts of running payroll — worker onboarding, pay schedules, earnings and deductions, tax calculation, filing and remittance across federal, state, and local jurisdictions, contractor payments, and money movement — behind a white-labeled, developer-first surface. Platforms integrate through the REST API, embeddable white-labeled React Components (Company Onboard, Run Payroll, W-4 / tax setup, bank connection via Plaid, filing authorization), webhooks, a Model Context Protocol server for AI agents, and a Python CLI. Check is backed by Stripe, Index Ventures, Thrive Capital, Bedrock Capital, and Battery Ventures, and powers payroll for platforms including Homebase.
image: https://cdn.prod.website-files.com/671a2c705660d0119de1cc9f/671ac14172962caffbc11039_OG-IMAGE-1.png
layout: provider
mcp_servers:
- description: Official Check MCP server exposing the Check Payroll API as Model Context Protocol tools for AI agents and operator copilots. Available hosted (remote, run by Check) and self-hosted.
  name: Check Technologies MCP Server
  slug: check-technologies-mcp-server
modified: '2026-07-18'
name: Check Technologies
nav: Providers
network: true
overview: 'Check Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payroll, Embedded Finance, Fintech, and Payments.


  The Check Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Check Technologies'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 48.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/check-technologies/refs/heads/main/screenshots/check-technologies-2026-07-25T205128.png
security:
- kind: authentication
  name: Check Technologies Authentication
  slug: check-technologies-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Check Technologies Domain Security
  slug: check-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Check Technologies Vulnerability Disclosure
  slug: check-technologies-vulnerability-disclosure
  summary_line: disclosure policy published
slug: check-technologies
tags:
- Company
- Payroll
- Embedded Finance
- Fintech
- Payments
- Human Resources
- Tax
- Compliance
- Developer Tools
website: https://docs.checkhq.com/
---
