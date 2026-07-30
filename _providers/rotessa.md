---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Rotessa Agentic Access
  operation_count: 13
  slug: rotessa-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 3
apis:
- description: Create, retrieve, and update the customers (bank-account holders) that Rotessa withdraws recurring payments from. Supports lookup by Rotessa customer ID or by a merchant-supplied custom identifier, an
  name: Rotessa Customers API
  slug: rotessa-customers-api
- description: Create and manage one-time and recurring pre-authorized debit / ACH transaction schedules against a customer's bank account, including schedule frequency, creation by Rotessa customer ID or custom ide
  name: Rotessa Transaction Schedules API
  slug: rotessa-transaction-schedules-api
- description: Retrieve financial transaction records and their status (and status reasons) for reconciliation and reporting via the transaction report endpoint. Base URL https://api.rotessa.com/v1; API-key authenti
  name: Rotessa Transaction Report API
  slug: rotessa-transaction-report-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rotessa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rotessa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rotessa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://rotessa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rotessa.com/our-customers/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://rotessa.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://rotessa.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.rotessa.com/rotessas-sandbox-and-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rotessa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rotessa
- group: commercial
  title: ''
  type: Pricing
  url: https://rotessa.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://rotessa.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.rotessa.com/
- group: start
  title: ''
  type: SignUp
  url: https://rotessa.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://app.rotessa.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rotessa.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rotessa.com/legal/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/rotessa-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rotessa-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/rotessa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rotessa-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/rotessa-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rotessa-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rotessa-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rotessa-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rotessa-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/rotessa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rotessa-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rotessa-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rotessa-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Rotessa is a Winnipeg, Manitoba-based fintech that helps small and mid-sized North American businesses collect recurring payments directly from their customers' bank accounts. In Canada it moves money over the pre-authorized debit (PAD) rails and in the United States over ACH, positioning itself as a low-cost, bank-account-native alternative to card processing for invoices, memberships, subscriptions, tuition, and rent. Rotessa exposes a genuine public REST API (https://api.rotessa.com/v1) that lets platforms and businesses programmatically create customers, verify bank details (including via the Flinks aggregator), and schedule one-time or recurring transactions, backed by a free sandbox (sandbox.rotessa.com) and API-key authentication. As an API-native SMB money-movement fintech, it sits in the thin-but-real account-to-account layer of Canada's payments market, alongside peers like VoPay, Plooto, and Helcim, operating through bank rails and aggregators rather than any live
  open-banking payment mandate.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: rotessa-mcp.yml
  slug: rotessa-mcpyml
modified: '2026-07-25'
name: Rotessa
nav: Providers
network: true
overview: 'Rotessa publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Canada, Pre-Authorized Debit, ACH, and Account-to-Account.


  Rotessa''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 24 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 34.3
  delta: -3.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 8.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rotessa Authentication
  slug: rotessa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rotessa Domain Security
  slug: rotessa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rotessa
tags:
- Payments
- Canada
- Pre-Authorized Debit
- ACH
- Account-to-Account
- Bank Payments
- Recurring Payments
- Subscriptions
- Direct Debit
- Money Movement
- Open Banking
website: https://rotessa.com/
---
