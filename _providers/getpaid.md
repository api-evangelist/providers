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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Getpaid Agentic Access
  operation_count: 16
  slug: getpaid-agentic-access
  summary_line: 16 operations · 12 acting
api_count: 1
apis:
- description: Getpaid accounts created for sellers so they can start accepting payments and receiving payouts.
  name: GetPaid Accounts API
  slug: getpaid-accounts-api
- description: Onboarding applications to collect the necessary information from sellers to create their Getpaid accounts and start accepting payments.
  name: GetPaid Applications API
  slug: getpaid-applications-api
- description: <!-- markdownlint-disable link-fragments --> In order to authenticate with Getpaid API you need to request an OAuth 2.0 access token using your client ID and secret by calling the [Request access toke
  name: GetPaid Authentication API
  slug: getpaid-authentication-api
- description: Payment checkout sessions for one-time payments that the buyer can complete using Getpaid hosted checkout.
  name: GetPaid Checkouts API
  slug: getpaid-checkouts-api
- description: Create and manage payments initiated by the platform on behalf of the buyer. For recurring and unscheduled payments based on a previous standing instruction.
  name: GetPaid Payments API
  slug: getpaid-payments-api
- description: List resources filtering and sorting them as needed.
  name: GetPaid Queries API
  slug: getpaid-queries-api
- description: Webhooks related to accepting payment events.
  name: GetPaid Accept payments webhooks API
  slug: getpaid-accept-payments-webhooks-api
- description: Webhooks related to onboarding and accounts events.
  name: GetPaid Onboard sellers webhooks API
  slug: getpaid-onboard-sellers-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Getpaid Webhooks
  slug: getpaid-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Getpaid Accounts API
  slug: open-getpaid-accounts-api
- collection_type: open
  name: Getpaid Accounts Applications API
  slug: open-getpaid-applications-api
- collection_type: open
  name: Getpaid Accounts Authentication API
  slug: open-getpaid-authentication-api
- collection_type: open
  name: Getpaid Accounts Checkouts API
  slug: open-getpaid-checkouts-api
- collection_type: open
  name: Getpaid Accounts Payments API
  slug: open-getpaid-payments-api
- collection_type: open
  name: Getpaid Accounts Queries API
  slug: open-getpaid-queries-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/getpaid-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getpaid.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getpaid.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getpaid.io/api
- group: start
  title: ''
  type: Quickstart
  url: https://docs.getpaid.io/integration/api
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.getpaid.io
- group: operate
  title: ''
  type: Support
  url: mailto:support@getpaid.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getpaid.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://docs.getpaid.io/integration/api/postman
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getpaid-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/getpaid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/getpaid-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getpaid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getpaid-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/getpaid-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getpaid-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/getpaid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getpaid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getpaid-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/getpaid-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getpaid-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getpaid-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/getpaid-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getpaid-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/getpaid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://getpaid.io/compliance
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Getpaid is a licensed European (EEA) embedded-payments platform that lets software platforms and marketplaces process payments while keeping the merchant relationship and capturing the transaction margin. It provides white-labeled hosted checkout across 30+ payment methods, atomic real-time split settlement that distributes a single transaction across sellers, the platform and agents, seller onboarding with KYC/KYB, subscriptions and invoicing with SEPA Direct Debit, and an AI-native agent-payments API with scoped authority tokens and spending limits. The v2 REST API uses OAuth 2.0 client-credentials auth, cursor pagination, RFC 7807 problem-details errors, an idempotency-key header, and 10 webhook events. Getpaid is a PCI-DSS Level 1, GDPR- and PSD2/SCA-aligned licensed payment institution with hubs in Germany, Spain and Finland.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getpaid.png
layout: provider
mcp_servers:
- description: ''
  name: GetPaid MCP Server
  slug: getpaid-mcp-server
modified: '2026-07-19'
name: GetPaid
nav: Providers
network: true
overview: 'GetPaid publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Applications API, Authentication API, and 5 more. Tagged areas include Company, Payments, Embedded Payments, Split Settlement, and Checkout.


  The GetPaid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GetPaid''s developer surface includes documentation, API reference, quickstart, signup flow, support, changelog, authentication, and 20 more developer resources.'
random_paper: 20
scopes:
- name: Getpaid Scopes
  scope_count: 4
  slug: getpaid-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 63.8
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getpaid/refs/heads/main/screenshots/getpaid-2026-07-25T215736.png
security:
- kind: authentication
  name: Getpaid Authentication
  slug: getpaid-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Getpaid Domain Security
  slug: getpaid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getpaid
tags:
- Company
- Payments
- Embedded Payments
- Split Settlement
- Checkout
- Marketplace
- Onboarding
- Subscription
- Agent Payments
- Europe
website: https://docs.getpaid.io
---
