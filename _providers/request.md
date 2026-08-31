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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Accounts Payable and Receivable REST API for issuing invoices, accepting crypto and fiat payments, running payroll, and managing organizations and clients. JSON request and response bodies, Bearer
  name: Request Finance AP and AR API
  slug: request-finance-ap-and-ar-api
artifact_total: 8
asyncapis:
- description: ''
  name: Request Webhooks
  slug: request-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/request-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/request-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/request-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.request.finance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.request.finance/developers/apps
- group: docs
  title: ''
  type: Documentation
  url: https://docs.request.finance/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.request.finance/invoices
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.request.finance/getting-started
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/request-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://status.request.finance/
- group: operate
  title: ''
  type: Support
  url: mailto:support@request.finance
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.request.finance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RequestFinance
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/request-finance/workspace/request-finance-api-public/
- group: start
  title: ''
  type: SignUp
  url: https://app.request.finance/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/request-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/request-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/request-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/request-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/request-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/request-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/request-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/request-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/request-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/request-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/request-rate-limits.yml
created: '2026-07-17'
description: Request Finance is a crypto and fiat invoicing, payments, and payroll platform that lets businesses issue invoices, accept payments in crypto and fiat, pay contractors and employees, and manage accounts payable and receivable. Its Accounts Payable and Receivable (AP/AR) REST API lets developers programmatically create and send invoices, run off-chain and on-chain payroll payments, track invoice status without polling blockchains or bank accounts, manage organizations and clients, and download invoice PDFs. Invoices are settled through the Request Network protocol across many EVM chains and stablecoins, with crypto-to-fiat settlement via banking partners. The API uses Bearer authentication (API keys for quick starts, OAuth 2.0 / OIDC via Auth0 for production), real-time webhooks with HMAC-signed payloads, and a Sepolia testnet sandbox. Request Finance is backed by Balderton Capital.
image: https://www.request.finance/
layout: provider
mcp_servers:
- description: ''
  name: Request Finance MCP Server
  slug: request-finance-mcp-server
modified: '2026-07-20'
name: Request Finance
nav: Providers
network: true
overview: 'Request Finance publishes 1 API on the [APIs.io](https://apis.io/) network: AP and AR API. Tagged areas include Company, Payments, Invoicing, Crypto, and Web3.


  The Request Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Request Finance''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 20 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 3
  name: Request Rate Limits
  slug: request-rate-limits
scopes:
- name: Request Scopes
  scope_count: 5
  slug: request-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 45.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/request/refs/heads/main/screenshots/request-2026-08-17T081526.png
security:
- kind: authentication
  name: Request Authentication
  slug: request-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Request Domain Security
  slug: request-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Request Trust Center
  slug: request-trust-center
  summary_line: SOC 2
slug: request
tags:
- Company
- Payments
- Invoicing
- Crypto
- Web3
- Payroll
- Stablecoins
- Accounts Payable
- Accounts Receivable
- Fintech
- Blockchain
- REST API
website: https://www.request.finance/
---
