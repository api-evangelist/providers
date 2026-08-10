---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.4
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 84
  human_in_the_loop: 4
  name: Customers Bank Agentic Access
  operation_count: 211
  slug: customers-bank-agentic-access
  summary_line: 211 operations · 84 acting · 4 human-in-the-loop
api_count: 10
apis:
- description: 'First-party embedded-banking Accounts API for listing accounts, retrieving account and subaccount detail, searching transactions, managing tags and account entitlements, and downloading account data. '
  name: Customers Bank Accounts API
  slug: customers-bank-accounts-api
- description: ACH payment origination and management API for the Customers Bank embedded-banking platform. OpenAPI 3.0.1, OAuth2 client-credentials.
  name: Customers Bank ACH API
  slug: customers-bank-ach-api
- description: Consumer Lending API for creating and searching loan applications, retrieving program (policy) details, and originating, funding, completing and cancelling loans. OpenAPI 3.0.1, OAuth2 client-credenti
  name: Customers Bank Consumer Lending API
  slug: customers-bank-consumer-lending-api
- description: Instant Payments API for real-time payment origination and management on the Customers Bank platform. OpenAPI 3.0.1, OAuth2 client-credentials.
  name: Customers Bank Instant Payments API
  slug: customers-bank-instant-payments-api
- description: IT Operations / reference-data API providing bank lookups (ABA, BIC), correspondent (SSI) instructions across payment rails, and WebPubSub client access. OpenAPI 3.0.1, OAuth2 client-credentials.
  name: Customers Bank IT Operations API
  slug: customers-bank-it-operations-api
- description: Partner-administration API for managing partners, users, customers, messages, API credentials and client credentials (M2M application registration) on the embedded-banking platform. OpenAPI 3.0.1, OAu
  name: Customers Bank Partners API
  slug: customers-bank-partners-api
- description: OAuth2 token/security API. Issues bearer access tokens via the client-credentials grant for machine-to-machine access to all Customers Bank embedded-banking APIs. OpenAPI 3.0.1.
  name: Customers Bank Security API
  slug: customers-bank-security-api
- description: Transfers API covering book transfers, address-book payee management and approvals, account-link settings, instant-transfer approvals, and account entitlements. OpenAPI 3.0.1, OAuth2 client-credential
  name: Customers Bank Transfers API
  slug: customers-bank-transfers-api
- description: Webhooks API for subscribing to platform event types, delivering signed event payloads (HMAC signature validation), and managing webhook IP allowlists. OpenAPI 3.0.1, OAuth2 client-credentials.
  name: Customers Bank Webhooks API
  slug: customers-bank-webhooks-api
- description: Wires API (v2) for originating and managing incoming and outgoing wire transfers, retrieving purpose and reference-data codes, and managing wire account entitlements. OpenAPI 3.0.1, OAuth2 client-cred
  name: Customers Bank Wires API
  slug: customers-bank-wires-api
artifact_total: 16
asyncapis:
- description: ''
  name: Customers Bank Webhooks
  slug: customers-bank-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customers-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customers-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.customersbank.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cubiapi.readme.io
- group: docs
  title: ''
  type: Documentation
  url: https://cubiapi.readme.io/docs/getting-started
- group: agent
  title: ''
  type: MCPServer
  url: https://cubiapi.readme.io/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/customers-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/customers-bank-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CustomersBank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customers-bank
- group: start
  title: ''
  type: GettingStarted
  url: https://cubiapi.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://cubiapi.readme.io/reference
- group: auth
  title: ''
  type: Authentication
  url: authentication/customers-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/customers-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/customers-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/customers-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/customers-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/customers-bank-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/customers-bank-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/customers-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/customers-bank-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/customers-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/customers-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.customersbank.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.customersbank.com/terms-of-use/
created: '2026-07-23'
description: Customers Bank is a Pennsylvania state-chartered, FDIC-insured full-service commercial bank and the principal subsidiary of Customers Bancorp, Inc. (NYSE CUBI), a super-regional bank holding company with roughly $22 billion in assets headquartered in West Reading, Pennsylvania. Beyond traditional commercial and consumer banking it operates a national embedded-banking / Banking-as-a-Service platform, exposing a first-party, OAuth2-secured REST API surface (accounts, ACH, wires, instant payments, book transfers, consumer lending, plus partner, IT-operations and webhook management) to fintech and corporate partners through a public ReadMe developer portal at cubiapi.readme.io, complete with a hosted Model Context Protocol (MCP) server for AI agents. This is proprietary, partner-gated integration infrastructure rather than an FDX or CFPB Section 1033 consumer-permissioned data-sharing API; no FDX-conformant or Section 1033 data-access endpoint is publicly documented, and the surface
  is a sandbox-first partner API secured by OAuth2 client-credentials with HMAC-signed webhooks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: customers-bank-mcp.yml
  slug: customers-bank-mcpyml
modified: '2026-07-23'
name: Customers Bank
nav: Providers
network: true
overview: 'Customers Bank publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, ACH API, Consumer Lending API, and 7 more. Tagged areas include Financial Services, Banking, United States, Banking-as-a-Service, and Embedded Finance.


  The Customers Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Customers Bank''s developer surface includes documentation, getting-started guide, API reference, authentication, changelog, sandbox, and 20 more developer resources.'
random_paper: 62
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customers-bank/refs/heads/main/screenshots/customers-bank-2026-07-25T211012.png
security:
- kind: authentication
  name: Customers Bank Authentication
  slug: customers-bank-authentication
  summary_line: oauth2/http-bearer/hmac · 3 schemes
- kind: domain-security
  name: Customers Bank Domain Security
  slug: customers-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: customers-bank
tags:
- Financial Services
- Banking
- United States
- Banking-as-a-Service
- Embedded Finance
- Payments
- Commercial Banking
website: https://www.customersbank.com
---
