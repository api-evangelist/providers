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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
api_count: 15
apis:
- description: Endpoints for creating and managing loan application contracts
  name: LendKey Application Contracts API
  slug: lendkey-application-contracts-api
- description: The applications API from LendKey — 1 operation(s) for applications.
  name: LendKey applications API
  slug: lendkey-applications-api
- description: The auth API from LendKey — 1 operation(s) for auth.
  name: LendKey auth API
  slug: lendkey-auth-api
- description: OAuth2 authentication endpoints
  name: LendKey Authentication API
  slug: lendkey-authentication-api
- description: The Credit Risk API from LendKey — 4 operation(s) for credit risk.
  name: LendKey Credit Risk API
  slug: lendkey-credit-risk-api
- description: Disbursement processing and cancellation
  name: LendKey Disbursements API
  slug: lendkey-disbursements-api
- description: The email API from LendKey — 2 operation(s) for email.
  name: LendKey email API
  slug: lendkey-email-api
- description: Internal API operations for request logging
  name: LendKey internal API
  slug: lendkey-internal-api
- description: The leads API from LendKey — 1 operation(s) for leads.
  name: LendKey leads API
  slug: lendkey-leads-api
- description: Capital ledger operations
  name: LendKey Ledger Management API
  slug: lendkey-ledger-management-api
- description: Manage DocuSign template assignments for lenders
  name: LendKey Lender Templates API
  slug: lendkey-lender-templates-api
- description: Loan creation and management
  name: LendKey Loans API
  slug: lendkey-loans-api
- description: The onboarding API from LendKey — 1 operation(s) for onboarding.
  name: LendKey onboarding API
  slug: lendkey-onboarding-api
- description: Payment and remittance processing
  name: LendKey Payments API
  slug: lendkey-payments-api
- description: Endpoints for receiving DocuSign webhook notifications
  name: LendKey Webhooks API
  slug: lendkey-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Lendkey Webhooks
  slug: lendkey-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.lendkey.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lendkey.com/default/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lendkey.com/default/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lendkey.com/default/documentation/integration-api
- group: start
  title: ''
  type: SignUp
  url: https://developer.lendkey.com/default/register
- group: start
  title: ''
  type: Login
  url: https://developer.lendkey.com/default/login
- group: operate
  title: ''
  type: Support
  url: https://www.lendkey.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.lendkey.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lendkey
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendkey.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendkey.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lendkey-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lendkey-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lendkey-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lendkey-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lendkey-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lendkey-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lendkey-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lendkey-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lendkey-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lendkey-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lendkey-llms.txt
created: '2026-07-17'
description: LendKey Technologies is a New York based digital lending platform that lets credit unions and community banks originate, fund and service consumer loans without building the technology themselves. Its network-lending model covers private student loans, student loan refinancing, home improvement lending and auto lending, and its ALIRO platform runs loan participations and post-origination liquidity between institutions. LendKey has surpassed $8 billion in loan originations. For integrators it operates a Kong Gateway fronted API estate published through a Kong Developer Portal at developer.lendkey.com, covering origination intake (leads, soft credit pull, credit attributes, scoring and application boarding), treasury management (loan inventory, disbursements, payments and capital ledger), and DocuSign backed e-signature contracts. Access is partner gated, with OAuth2 client-credentials credentials issued through the developer portal.
image: https://www.lendkey.com/wp-content/uploads/2018/08/cropped-LK512.png
layout: provider
mcp_servers:
- description: ''
  name: lendkey-mcp.yml
  slug: lendkey-mcpyml
modified: '2026-07-19'
name: LendKey
nav: Providers
network: true
overview: 'LendKey publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Application Contracts API, applications API, auth API, and 12 more. Tagged areas include Company, Fintech, Lending, Loans, and Student Loans.


  The LendKey catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LendKey''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, sandbox, and 16 more developer resources.'
random_paper: 19
scopes:
- name: Lendkey Scopes
  scope_count: 0
  slug: lendkey-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.8
  delta: -2.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 70.5
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 52.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lendkey/refs/heads/main/screenshots/lendkey-2026-07-25T224904.png
security:
- kind: authentication
  name: Lendkey Authentication
  slug: lendkey-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lendkey Domain Security
  slug: lendkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lendkey
tags:
- Company
- Fintech
- Lending
- Loans
- Student Loans
- Credit Unions
- Banking
- Loan Origination
- Financial Services
- Payments
- E-Signature
- Treasury
website: https://www.lendkey.com/
---
