---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Payments Canada Agentic Access
  operation_count: 11
  slug: payments-canada-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 8
apis:
- description: Sandbox APIs giving members access to test-data interactions with Lynx, Canada's high-value ISO 20022 real-time gross settlement system. Access is member-gated (contact your organization's Access Offi
  name: Lynx Sandbox API
  slug: lynx-sandbox-api
- description: APIs for the Automated Clearing Settlement System (ACSS), Canada's retail batch/ACH clearing rail. Access is member-gated via the developer portal.
  name: ACSS API
  slug: acss-api
- description: The application level heartbeat API from Payments Canada — 1 operation(s) for application level heartbeat.
  name: Payments Canada application level heartbeat API
  slug: payments-canada-application-level-heartbeat-api
- description: Ccin Extract Resource
  name: Payments Canada Ccin Extract Resource API
  slug: payments-canada-ccin-extract-resource-api
- description: Fif Branches Resource
  name: Payments Canada Fif Branches Resource API
  slug: payments-canada-fif-branches-resource-api
- description: Fif Extracts Resource
  name: Payments Canada Fif Extracts Resource API
  slug: payments-canada-fif-extracts-resource-api
- description: The Interest Report API from Payments Canada — 1 operation(s) for interest report.
  name: Payments Canada Interest Report API
  slug: payments-canada-interest-report-api
- description: Master Extract Resource
  name: Payments Canada Master Extract Resource API
  slug: payments-canada-master-extract-resource-api
- description: The report API from Payments Canada — 1 operation(s) for report.
  name: Payments Canada Report API
  slug: payments-canada-report-api
- description: The single credit transfer API from Payments Canada — 1 operation(s) for single credit transfer.
  name: Payments Canada single credit transfer API
  slug: payments-canada-single-credit-transfer-api
- description: The single credit transfer status enquiry API from Payments Canada — 1 operation(s) for single credit transfer status enquiry.
  name: Payments Canada single credit transfer status enquiry API
  slug: payments-canada-single-credit-transfer-status-enquiry-api
- description: Update Extract Resource
  name: Payments Canada Update Extract Resource API
  slug: payments-canada-update-extract-resource-api
artifact_total: 25
collections:
- collection_type: open
  name: CCIN Output API
  slug: open-ccin-extracts-api
- collection_type: open
  name: CCIN Output API
  slug: open-ccin-lookup-api
- collection_type: open
  name: FIF Output API
  slug: open-fif-branch-api
- collection_type: open
  name: FIF Output API
  slug: open-fif-extracts-api
- collection_type: open
  name: Payment Capacity Balance Report
  slug: open-rtr-balance-report-api
- collection_type: open
  name: Inbound Exchange Heartbeat API
  slug: open-rtr-inbound-csp-heartbeat-api
- collection_type: open
  name: Inbound Participant Payment API
  slug: open-rtr-inbound-participant-payment-api
- collection_type: open
  name: Interest Report
  slug: open-rtr-interest-report-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/payments-canada-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rtr-inbound-participant-payment-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/rtr-inbound-csp-heartbeat-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/rtr-interest-report-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/rtr-balance-report-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fif-extracts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fif-branch-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ccin-extracts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ccin-lookup-api-overlay.yaml
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
  name: Payments Canada MCP Server
  slug: payments-canada-mcp-server
modified: '2026-07-23'
name: Payments Canada
nav: Providers
network: true
overview: 'Payments Canada publishes 10 APIs on the [APIs.io](https://apis.io/) network, including application level heartbeat API, Ccin Extract Resource API, Fif Branches Resource API, and 7 more. Tagged areas include Financial-Services, Payments, Canada, Payment Infrastructure, and Clearing and Settlement.


  Payments Canada''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, and 31 more developer resources.'
random_paper: 14
scopes:
- name: Payments Canada Scopes
  scope_count: 1
  slug: payments-canada-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 47.6
    developer_ergonomics: 68.5
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 67.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payments-canada/refs/heads/main/screenshots/payments-canada-2026-08-07T191642.png
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
- Financial-Services
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
