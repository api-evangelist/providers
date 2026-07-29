---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Helcim Agentic Access
  operation_count: 48
  slug: helcim-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 6
apis:
- description: Card payment processing endpoints covering the full transaction lifecycle — Purchase, Preauthorization, Capture, Verify, Refund, Reverse, and Withdraw — under the Helcim API v2. Includes the General c
  name: Helcim Payment API
  slug: helcim-payment-api
- description: Bank-to-bank (ACH / pre-authorized debit) money movement — withdraw, refund, void, cancel, retrieve ACH transactions, and list and settle ACH batches under the Helcim API v2.
  name: Helcim ACH Payment API
  slug: helcim-ach-payment-api
- description: Create, retrieve, and update customers and manage their saved payment instruments — stored cards, bank accounts, and pre-authorized debit agreements (PADs) — under the Helcim API v2.
  name: Helcim Customer API
  slug: helcim-customer-api
- description: Create, retrieve, and update invoices under the Helcim API v2, supporting billing and payment collection workflows.
  name: Helcim Invoice API
  slug: helcim-invoice-api
- description: Read access to processed card transactions and card batches, including listing and retrieving transactions and batches and settling a card batch, under the Helcim API v2.
  name: Helcim Card Transaction & Batch API
  slug: helcim-card-transaction-batch-api
- description: In-person payments through Helcim Smart Terminal hardware — list card terminals and devices, ping a device, and start purchase or refund transactions on a device — under the Helcim API v2.
  name: Helcim Card Terminal & Device API
  slug: helcim-terminal-device-api
artifact_total: 13
asyncapis:
- description: ''
  name: Helcim Webhooks
  slug: helcim-webhooks
collections:
- collection_type: postman
  name: The Helcim API
  slug: postman-helcim-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/helcim/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helcim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helcim-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helcim-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.helcim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devdocs.helcim.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.helcim.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://devdocs.helcim.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://devdocs.helcim.com/docs/overview-of-helcim-api
- group: auth
  title: ''
  type: Authentication
  url: https://devdocs.helcim.com/docs/authentication-with-the-helcim-api-and-helcimpayjs
- group: design
  title: ''
  type: Webhooks
  url: https://devdocs.helcim.com/docs/connected-account-webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helcim
- group: operate
  title: ''
  type: StatusPage
  url: https://status.helcim.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.helcim.com/api-developer-documentation
- group: design
  title: ''
  type: Idempotency
  url: conventions/helcim-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/helcim-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helcim-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/helcim-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/helcim-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/helcim-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://devdocs.helcim.com/docs/api-versions-and-deprecation
- group: start
  title: ''
  type: Sandbox
  url: sandbox/helcim-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/helcim-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/helcim-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/helcim-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/helcim-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://devdocs.helcim.com/docs/pci-compliance-scope
- group: build
  title: ''
  type: Packages
  url: packages/helcim-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/helcim-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/helcim-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/helcim-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/helcim-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/helcim-webhooks.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.helcim.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://hub.helcim.com/signup/register/
- group: start
  title: ''
  type: Login
  url: https://hsso.helcim.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.helcim.com/ca/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.helcim.com/ca/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://devdocs.helcim.com/docs/get-help
created: '2026-07-24'
description: 'Helcim is a Calgary, Canada based payment processor and merchant services provider serving small and medium-sized businesses across Canada and the United States with interchange-plus pricing and no monthly fees. Beyond its merchant dashboard, Smart Terminal hardware, and online store, Helcim ships a genuine developer surface: the versioned Helcim API (v2) for taking card and ACH payments, managing customers, cards, bank accounts and pre-authorized debits (PADs), issuing invoices, settling card and ACH batches, and driving in-person Card Terminal devices, alongside HelcimPay.js hosted checkout and connected-account webhooks. Authentication is a permissioned API access token passed in an api-token header, and the public developer portal publishes a downloadable OpenAPI 3.0 definition. In Canada''s small, concentrated payments market, Helcim is one of the API-native SMB money-movement fintechs building above the incumbent acquiring and Interac rails.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: helcim-mcp.yml
  slug: helcim-mcpyml
modified: '2026-07-24'
name: Helcim
nav: Providers
network: true
overview: 'Helcim publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Payment API, ACH Payment API, Customer API, and 3 more. Tagged areas include Payments, Canada, Payment Gateway, Payment Processing, and Acquiring.


  The Helcim catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Helcim''s developer surface includes authentication, documentation, API reference, getting-started guide, sandbox, changelog, pricing, and 33 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 3
  name: Helcim Rate Limits
  slug: helcim-rate-limits
score:
  band: strong
  composite: 59.1
  delta: -2.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 84.2
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helcim/refs/heads/main/screenshots/helcim-2026-07-25T220910.png
security:
- kind: authentication
  name: Helcim Authentication
  slug: helcim-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Helcim Domain Security
  slug: helcim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helcim
tags:
- Payments
- Canada
- Payment Gateway
- Payment Processing
- Acquiring
- Merchant Services
- ACH
- Invoicing
- Card Terminal
- Small Business
website: https://www.helcim.com/
---
