---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Ordo Agentic Access
  operation_count: 54
  slug: ordo-agentic-access
  summary_line: 54 operations · 25 acting
api_count: 6
apis:
- description: Single, one-off open-banking payment initiation — list supported institutions, create a payment, initiate authorisation, and withdraw a payment. Server base is the Ordo Azure API Management gateway. 4
  name: Ordo Single Payments API
  slug: ordo-single-payments-api
- description: Request to Pay / "Smart Request" management for one-off payment requests — create and manage smart requests and their messages, Biller Delivery Request (BDR) links, extensions and withdrawals. 8 docum
  name: Ordo Smart Request Manager API
  slug: ordo-smart-request-manager-api
- description: Variable Recurring Payments — create sweeping and non-sweeping VRP mandates, read mandates, execute mandate payments and read VRP transactions. Enables fixed, variable and ad-hoc recurring collections
  name: Ordo Recurring Payment Mandates (VRP) API
  slug: ordo-recurring-payment-mandates-api
- description: Ordo-hosted Account Information (AIS) and Account Verification — create and manage account information consents, request and read account data, cancel consents, and run account verification against su
  name: Ordo Account Data (Ordo Hosted) API
  slug: ordo-account-data-ordo-hosted-api
- description: Client-hosted Account Information (AIS) and Account Verification — the same consent, data-request and verification lifecycle as the Ordo-hosted variant, but with the integrating client hosting the end
  name: Ordo Account Data (Client Hosted) API
  slug: ordo-account-data-client-hosted-api
- description: Bank account configuration / registry management — create, read and manage the biller bank accounts into which collected payments settle. 3 documented operations.
  name: Ordo Registry Manager API
  slug: ordo-registry-manager-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ordo-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ordo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ordopay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.myordo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.myordo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.myordo.com/docs/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ordohq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ordohq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ordopay.com/legal/merchant-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ordopay.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://ordopay.com/contact
- group: design
  title: ''
  type: Conventions
  url: conventions/ordo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ordo-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ordo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ordo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ordo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ordo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ordo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Ordo (operated by The Smart Request Company Ltd, ordohq.com / ordopay.com) is a United Kingdom open-banking payments provider that lets businesses collect money directly from a customer's bank account over the UK Faster Payments rails, avoiding card fees and chargebacks. Built on PSD2 / Open Banking payment initiation, its fully hosted, white-labelled platform delivers Request to Pay, one-off payment requests, e-commerce, Point of Sale / QR code and contact centre payments, plus Variable Recurring Payments (VRP) for fixed, variable and sweeping collections, and account information (AIS) and account verification services. Ordo is FCA-authorised and an Open Banking regulated provider, with a developer surface historically published as a ReadMe.io portal at docs.myordo.com backed by an Azure API Management gateway (test.api.ordopay.com). Ordo has since ceased trading and been acquired by Neonomics; the marketing site at ordopay.com remains live while the developer portal is now
  offline. Its API posture is documented here honestly from six OpenAPI 3.0.1 definitions harvested verbatim from the archived developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ordo-mcp.yml
  slug: ordo-mcpyml
modified: '2026-07-24'
name: Ordo
nav: Providers
network: true
overview: 'Ordo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Single Payments API, Smart Request Manager API, Recurring Payment Mandates (VRP) API, and 3 more. Tagged areas include Payments, United Kingdom, Open Banking, Account-to-Account, and Payment Initiation.


  Ordo''s developer surface includes authentication, API reference, getting-started guide, support, and 16 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.2
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Ordo Authentication
  slug: ordo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ordo Domain Security
  slug: ordo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ordo
tags:
- Payments
- United Kingdom
- Open Banking
- Account-to-Account
- Payment Initiation
- Variable Recurring Payments
- Request to Pay
- Real-Time Payments
- Faster Payments
- PSD2
- Account Information
website: https://ordopay.com/
---
