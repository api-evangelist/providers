---
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Paymentsense Agentic Access
  operation_count: 50
  slug: paymentsense-agentic-access
  summary_line: 50 operations · 28 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Documented WebSockets interface for the Connect platform, offering an event-driven alternative to the REST API for terminal integration. No downloadable OpenAPI/AsyncAPI specification is published; on
  name: Paymentsense Connect WebSockets API
  slug: connect-websockets-api
- description: The Access Token API from Paymentsense — 1 operation(s) for access token.
  name: Paymentsense Access Token API
  slug: paymentsense-access-token-api
- description: The Cross Reference Payment API from Paymentsense — 1 operation(s) for cross reference payment.
  name: Paymentsense Cross Reference Payment API
  slug: paymentsense-cross-reference-payment-api
- description: The Hospitality Reports API from Paymentsense — 2 operation(s) for hospitality reports.
  name: Paymentsense Hospitality Reports API
  slug: paymentsense-hospitality-reports-api
- description: The Hospitality Tables API from Paymentsense — 6 operation(s) for hospitality tables.
  name: Paymentsense Hospitality Tables API
  slug: paymentsense-hospitality-tables-api
- description: The PAC Reports API from Paymentsense — 2 operation(s) for pac reports.
  name: Paymentsense PAC Reports API
  slug: paymentsense-pac-reports-api
- description: The PAC Reports (Ingenico Only) API from Paymentsense — 2 operation(s) for pac reports (ingenico only).
  name: Paymentsense PAC Reports (Ingenico Only) API
  slug: paymentsense-pac-reports-ingenico-only-api
- description: The PAC Terminals API from Paymentsense — 3 operation(s) for pac terminals.
  name: Paymentsense PAC Terminals API
  slug: paymentsense-pac-terminals-api
- description: The PAC Transactions API from Paymentsense — 6 operation(s) for pac transactions.
  name: Paymentsense PAC Transactions API
  slug: paymentsense-pac-transactions-api
- description: The PAT Reports API from Paymentsense — 2 operation(s) for pat reports.
  name: Paymentsense PAT Reports API
  slug: paymentsense-pat-reports-api
- description: The PAT Tables API from Paymentsense — 6 operation(s) for pat tables.
  name: Paymentsense PAT Tables API
  slug: paymentsense-pat-tables-api
- description: The Payment Details API from Paymentsense — 1 operation(s) for payment details.
  name: Paymentsense Payment Details API
  slug: paymentsense-payment-details-api
- description: The Payment Methods API from Paymentsense — 1 operation(s) for payment methods.
  name: Paymentsense Payment Methods API
  slug: paymentsense-payment-methods-api
- description: The Resume Payment API from Paymentsense — 1 operation(s) for resume payment.
  name: Paymentsense Resume Payment API
  slug: paymentsense-resume-payment-api
- description: The Retail Reports API from Paymentsense — 2 operation(s) for retail reports.
  name: Paymentsense Retail Reports API
  slug: paymentsense-retail-reports-api
- description: The Retail Terminals API from Paymentsense — 2 operation(s) for retail terminals.
  name: Paymentsense Retail Terminals API
  slug: paymentsense-retail-terminals-api
- description: The Retail Transactions API from Paymentsense — 3 operation(s) for retail transactions.
  name: Paymentsense Retail Transactions API
  slug: paymentsense-retail-transactions-api
- description: The Revoke Access Token API from Paymentsense — 1 operation(s) for revoke access token.
  name: Paymentsense Revoke Access Token API
  slug: paymentsense-revoke-access-token-api
arazzos:
- description: List a terminal, start a card transaction on it, and poll to the outcome.
  name: Paymentsense Pay-At-Counter — take a card payment
  slug: paymentsense-pac-take-payment
artifact_total: 28
asyncapis:
- description: ''
  name: Paymentsense Connect Events
  slug: paymentsense-connect-events
collections:
- collection_type: open
  name: Connect-E Development Environment
  slug: open-paymentsense-connect-e-v0
- collection_type: open
  name: Connect REST API
  slug: open-paymentsense-connect-v0
- collection_type: open
  name: Connect REST API
  slug: open-paymentsense-connect-v1
- collection_type: open
  name: Connect REST API
  slug: open-paymentsense-connect-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/paymentsense-connect-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paymentsense-connect-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paymentsense-connect-v0-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/paymentsense-connect-e-v0-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paymentsense-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paymentsense-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paymentsense-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/paymentsense-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paymentsense-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/paymentsense-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paymentsense-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/paymentsense-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paymentsense-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paymentsense-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paymentsense-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dojo.tech/articles/what-is-pci-compliance/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paymentsense-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paymentsense-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paymentsense.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paymentsense-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.connect.paymentsense.cloud/rest/changelog
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Login
  url: https://developers.paymentsense.com
- group: company
  title: ''
  type: Website
  url: https://www.paymentsense.com/uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.connect.paymentsense.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.connect.paymentsense.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.connect.paymentsense.cloud/rest/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connect.paymentsense.cloud/rest/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paymentsense-DevSupport
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paymentsense.com/uk/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.paymentsense.com/uk/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.paymentsense.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paymentsense.com/uk/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paymentsense.com/uk/legal/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paymentsense/
created: '2026-07-24'
description: Paymentsense is a United Kingdom payment processing company that provides card payment acceptance to small and medium-sized businesses through card machines (PDQ terminals), online payment gateways, and EPOS integrations. Now part of Dojo, its developer-facing surface centers on the Connect platform, a cloud-hosted integration layer that gives each merchant an isolated host so point-of-sale and hospitality software can drive card terminals without touching card data. Paymentsense publishes a genuine public developer portal at docs.connect.paymentsense.cloud with interactive Swagger reference docs and downloadable OpenAPI/Swagger specifications for the Connect REST API (Pay-At-Counter and Pay-At-Table terminal integration, versions v0/v1/v2) and the Connect-E REST API for online/e-commerce card payments, plus a documented WebSockets interface. Authentication is HTTP Basic using a per-merchant API key supplied by Paymentsense. A separate merchant/software-house management portal
  at developers.paymentsense.com sits behind Google sign-in.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Paymentsense MCP Server
  slug: paymentsense-mcp-server
modified: '2026-07-24'
name: Paymentsense
nav: Providers
network: true
overview: 'Paymentsense publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Cross Reference Payment API, Hospitality Reports API, and 14 more. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Card Payments.


  The Paymentsense catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paymentsense''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 52.9
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paymentsense/refs/heads/main/screenshots/paymentsense-2026-08-07T191642.png
security:
- kind: authentication
  name: Paymentsense Authentication
  slug: paymentsense-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Paymentsense Domain Security
  slug: paymentsense-domain-security
  summary_line: TLSv1.3 · DMARC
slug: paymentsense
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- Card Payments
- Acquiring
- Point-of-Sale
- In-Person Payments
website: https://www.paymentsense.com/uk/
---
