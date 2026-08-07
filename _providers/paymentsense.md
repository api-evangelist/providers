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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Paymentsense Agentic Access
  operation_count: 50
  slug: paymentsense-agentic-access
  summary_line: 50 operations · 28 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Cloud REST API for driving Paymentsense card terminals from EPOS software. Covers Pay-At-Counter (/pac) transactions and reports and Pay-At-Table (/pat) hospitality flows against a per-merchant Connec
  name: Paymentsense Connect REST API
  slug: connect-rest-api
- description: OpenAPI 3.0 REST API for online / e-commerce card payments. Issues access-tokens, processes and resumes payments, runs cross-reference (repeat) payments, and lists supported payment methods against th
  name: Paymentsense Connect-E REST API
  slug: connect-e-rest-api
- description: Documented WebSockets interface for the Connect platform, offering an event-driven alternative to the REST API for terminal integration. No downloadable OpenAPI/AsyncAPI specification is published; on
  name: Paymentsense Connect WebSockets API
  slug: connect-websockets-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List a terminal, start a card transaction on it, and poll to the outcome.
  name: Paymentsense Pay-At-Counter — take a card payment
  slug: paymentsense-pac-take-payment
artifact_total: 10
asyncapis:
- description: ''
  name: Paymentsense Connect Events
  slug: paymentsense-connect-events
common:
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
  name: paymentsense-mcp.yml
  slug: paymentsense-mcpyml
modified: '2026-07-24'
name: Paymentsense
nav: Providers
network: true
overview: 'Paymentsense publishes 2 APIs on the [APIs.io](https://apis.io/) network: Connect REST API and Connect-E REST API. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Card Payments.


  The Paymentsense catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paymentsense''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 24 more developer resources.'
random_paper: 65
score:
  band: strong
  composite: 56.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
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
    score: 68.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Point of Sale
- In-Person Payments
website: https://www.paymentsense.com/uk/
---
