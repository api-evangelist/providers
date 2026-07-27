---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Payments Canada Agentic Access
  operation_count: 11
  slug: payments-canada-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 10
apis:
- description: Real-Time Rail sandbox API for sending an RTR payment (ISO 20022 pacs.008 Customer Credit Transfer) to another RTR participant and enquiring on payment status (pacs.028), returning a payment status re
  name: RTR Sandbox - Inbound Participant Payment API
  slug: rtr-inbound-participant-payment-api
- description: 'Real-Time Rail sandbox API for sending heartbeat requests between a participant and the RTR exchange (ISO 20022 admi.004 System Event Notification), returning admi.011 System Event Acknowledgement or '
  name: RTR Sandbox - Inbound Exchange Heartbeat API
  slug: rtr-inbound-heartbeat-api
- description: Real-Time Rail sandbox clearing-and-settlement API that calls the C&S system to generate an interest report (ISO 20022 camt.003 Get Account returning camt.004 Return Account with interest data). OAuth
  name: RTR Sandbox - Interest Report API
  slug: rtr-interest-report-api
- description: Real-Time Rail sandbox clearing-and-settlement API that calls the C&S system to generate a payment-capacity balance report (ISO 20022 camt.003 Get Account returning camt.004 Return Account with balanc
  name: RTR Sandbox - Payment Capacity Balance Report API
  slug: rtr-balance-report-api
- description: Sandbox APIs giving members access to test-data interactions with Lynx, Canada's high-value ISO 20022 real-time gross settlement system. Access is member-gated (contact your organization's Access Offi
  name: Lynx Sandbox API
  slug: lynx-sandbox-api
- description: APIs for the Automated Clearing Settlement System (ACSS), Canada's retail batch/ACH clearing rail. Access is member-gated via the developer portal.
  name: ACSS API
  slug: acss-api
- description: Financial Institutions File (FIF) extracts API returning master and weekly updated extract data for Canadian financial institutions. Registered-user access via the developer portal.
  name: FIF Extracts API
  slug: fif-extracts-api
- description: Financial Institutions File (FIF) branch API returning weekly branch extract data for Canadian financial institutions. Registered-user access via the developer portal.
  name: FIF Branch API
  slug: fif-branch-api
- description: Corporate Creditor Identification Number (CCIN) extracts API returning master and updated extract data matching the weekly file distribution. Registered-user access via the developer portal.
  name: CCIN Extracts API
  slug: ccin-extracts-api
- description: Corporate Creditor Identification Number (CCIN) single-lookup API returning weekly extract data for a specific corporate creditor. Registered-user access via the developer portal.
  name: CCIN Lookup API
  slug: ccin-lookup-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payments-canada-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payments-canada-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/payments-canada-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payments-canada-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payments-canada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payments-canada-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payments-canada-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payments-canada-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payments-canada-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/payments-canada-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payments-canada-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/payments-canada-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/payments-canada-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payments-canada-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.payments.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.payments.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.payments.ca/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.payments.ca/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paymentscanada
- group: other
  title: ''
  type: APIStandards
  url: https://developer.payments.ca/payments-canada-api-standards
- group: build
  title: ''
  type: Postman
  url: https://github.com/paymentscanada/api-toolkit/tree/develop/postman-collection
- group: operate
  title: ''
  type: Support
  url: https://developer.payments.ca/content/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.payments.ca/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.payments.ca/legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payments-canada
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/paymentscanada
created: '2026-07-23'
description: Payments Canada (formerly the Canadian Payments Association) is the public-purpose organization created by federal statute (the Canadian Payments Act) that owns and operates Canada's core national payment clearing and settlement infrastructure, under the oversight of the Bank of Canada and the Minister of Finance. Its members are Canada's financial institutions. It operates Lynx (the high-value, ISO 20022 real-time gross settlement system that replaced LVTS), the Automated Clearing Settlement System (ACSS, Canada's retail batch/ACH rail), and is building the Real-Time Rail (RTR) — a 24/7/365 irrevocable faster-payments system fully based on the ISO 20022 messaging standard. Payments Canada is payments infrastructure, distinct from Canada's Consumer-Driven Banking (open banking) framework, which is legislated but not yet operational and overseen by the FCAC. It runs a real, publicly registerable API developer portal (developer.payments.ca, launched February 19, 2020) exposing
  member/registered-user sandbox and data-extract APIs — including downloadable RTR sandbox OpenAPI specifications — secured with OAuth2 client-credentials (Consumer Key/Secret via Apigee); production access is license/agreement gated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: payments-canada-mcp.yml
  slug: payments-canada-mcpyml
modified: '2026-07-23'
name: Payments Canada
nav: Providers
network: true
overview: 'Payments Canada publishes 8 APIs on the [APIs.io](https://apis.io/) network, including RTR Sandbox - Inbound Participant Payment API, RTR Sandbox - Inbound Exchange Heartbeat API, RTR Sandbox - Interest Report API, and 5 more. Tagged areas include Financial Services, Payments, Canada, Payment Infrastructure, and Clearing and Settlement.


  Payments Canada''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, and 22 more developer resources.'
random_paper: 30
scopes:
- name: Payments Canada Scopes
  scope_count: 1
  slug: payments-canada-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.2
    developer_ergonomics: 69.6
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 45.9
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Payments Canada Authentication
  slug: payments-canada-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Payments Canada Domain Security
  slug: payments-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payments-canada
tags:
- Financial Services
- Payments
- Canada
- Payment Infrastructure
- Clearing and Settlement
- Real-Time Rail
- ISO 20022
- Lynx
- Crown Corporation
- Faster Payments
website: https://www.payments.ca/
---
