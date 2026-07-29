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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Finix Agentic Access
  operation_count: 91
  slug: finix-agentic-access
  summary_line: 91 operations · 39 acting
api_count: 19
apis:
- description: '{''$ref'': ''api-descriptions/tags/authorizations.md''}'
  name: Finix Authorizations API
  slug: finix-authorizations-api
- description: '{''$ref'': ''api-descriptions/tags/balance-transfers.md''}'
  name: Finix Balance Transfers API
  slug: finix-balance-transfers-api
- description: '{''$ref'': ''api-descriptions/tags/compliance-forms.md''}'
  name: Finix Compliance Forms API
  slug: finix-compliance-forms-api
- description: '{''$ref'': ''api-descriptions/tags/devices.md''}'
  name: Finix Devices API
  slug: finix-devices-api
- description: '{''$ref'': ''api-descriptions/tags/disputes.md''}'
  name: Finix Disputes API
  slug: finix-disputes-api
- description: '{''$ref'': ''api-descriptions/tags/fee-profiles.md''}'
  name: Finix Fee Profiles API
  slug: finix-fee-profiles-api
- description: '{''$ref'': ''api-descriptions/tags/files.md''}'
  name: Finix Files API
  slug: finix-files-api
- description: '{''$ref'': ''api-descriptions/tags/identities.md''}'
  name: Finix Identities API
  slug: finix-identities-api
- description: '{''$ref'': ''api-descriptions/tags/instrument-updates.md''}'
  name: Finix Instrument Updates API
  slug: finix-instrument-updates-api
- description: '{''$ref'': ''api-descriptions/tags/merchant-profiles.md''}'
  name: Finix Merchant Profiles API
  slug: finix-merchant-profiles-api
- description: '{''$ref'': ''api-descriptions/tags/merchants.md''}'
  name: Finix Merchants API
  slug: finix-merchants-api
- description: '{''$ref'': ''api-descriptions/tags/onboarding-forms.md''}'
  name: Finix Onboarding Forms API
  slug: finix-onboarding-forms-api
- description: '{''$ref'': ''api-descriptions/tags/payment-instruments.md''}'
  name: Finix Payment Instruments API
  slug: finix-payment-instruments-api
- description: '{''$ref'': ''api-descriptions/tags/payout-profiles.md''}'
  name: Finix Payout Profiles API
  slug: finix-payout-profiles-api
- description: '{''$ref'': ''api-descriptions/tags/settlements.md''}'
  name: Finix Settlements API
  slug: finix-settlements-api
- description: '{''$ref'': ''api-descriptions/tags/split-transfers.md''}'
  name: Finix Split Transfers API
  slug: finix-split-transfers-api
- description: '{''$ref'': ''api-descriptions/tags/transfers.md''}'
  name: Finix Transfers API
  slug: finix-transfers-api
- description: '{''$ref'': ''api-descriptions/tags/verifications.md''}'
  name: Finix Verifications API
  slug: finix-verifications-api
- description: '{''$ref'': ''api-descriptions/tags/webhooks.md''}'
  name: Finix Webhooks API
  slug: finix-webhooks-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a buyer Identity and card, place an Authorization, then capture it.
  name: Finix Authorize and Capture
  slug: finix-authorize-and-capture-workflow
- description: Create a merchant Identity, attach a bank account, provision the Merchant, and run verification.
  name: Finix Onboard Merchant
  slug: finix-onboard-merchant-workflow
- description: Look up a Transfer and issue a reversal (refund).
  name: Finix Refund Transfer
  slug: finix-refund-transfer-workflow
- description: Convert a finix.js token into a Payment Instrument and create a Transfer (sale).
  name: Finix Tokenize and Charge
  slug: finix-tokenize-and-charge-workflow
artifact_total: 51
asyncapis:
- description: Finix delivers real-time event notifications via webhooks (HTTP POST) when resources change. Subscribe with POST /webhooks. Each delivery carries an envelope { id, type, entity, occurred_at, system_ge
  name: Finix Webhook Events
  slug: finix-events-asyncapi
collections:
- collection_type: postman
  name: Finix Authorizations API
  slug: postman-finix-authorizations-api
- collection_type: postman
  name: Finix Authorizations Balance Transfers API
  slug: postman-finix-balance-transfers-api
- collection_type: postman
  name: Finix Authorizations Compliance Forms API
  slug: postman-finix-compliance-forms-api
- collection_type: postman
  name: Finix Authorizations Devices API
  slug: postman-finix-devices-api
- collection_type: postman
  name: Finix Authorizations Disputes API
  slug: postman-finix-disputes-api
- collection_type: postman
  name: Finix Authorizations Fee Profiles API
  slug: postman-finix-fee-profiles-api
- collection_type: postman
  name: Finix Authorizations Files API
  slug: postman-finix-files-api
- collection_type: postman
  name: Finix Authorizations Identities API
  slug: postman-finix-identities-api
- collection_type: postman
  name: Finix Authorizations Instrument Updates API
  slug: postman-finix-instrument-updates-api
- collection_type: postman
  name: Finix Authorizations Merchant Profiles API
  slug: postman-finix-merchant-profiles-api
- collection_type: postman
  name: Finix Authorizations Merchants API
  slug: postman-finix-merchants-api
- collection_type: postman
  name: Finix Authorizations Onboarding Forms API
  slug: postman-finix-onboarding-forms-api
- collection_type: postman
  name: Finix Authorizations Payment Instruments API
  slug: postman-finix-payment-instruments-api
- collection_type: postman
  name: Finix Authorizations Payout Profiles API
  slug: postman-finix-payout-profiles-api
- collection_type: postman
  name: Finix Authorizations Settlements API
  slug: postman-finix-settlements-api
- collection_type: postman
  name: Finix Authorizations Split Transfers API
  slug: postman-finix-split-transfers-api
- collection_type: postman
  name: Finix Authorizations Transfers API
  slug: postman-finix-transfers-api
- collection_type: postman
  name: Finix Authorizations Verifications API
  slug: postman-finix-verifications-api
- collection_type: postman
  name: Finix Authorizations Webhooks API
  slug: postman-finix-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://finix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.finix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finix.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.finix.com/guides/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.finix.com/guides/getting-started/support-at-finix
- group: company
  title: ''
  type: Blog
  url: https://finix.com/resources/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finix-payments
- group: commercial
  title: ''
  type: Pricing
  url: https://finix.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://finix.payments-dashboard.com/signup
- group: start
  title: ''
  type: Login
  url: https://finix.payments-dashboard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finix.com/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finix.com/terms-and-policies/privacy-policy
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/finix/overview
- group: design
  title: ''
  type: Versioning
  url: https://docs.finix.com/additional-resources/developers/authentication-and-api-basics/versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://status.finix.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finix-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/finix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finix-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/finix-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finix-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/finix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/finix-packages.yml
- group: design
  title: ''
  type: Components
  url: components/finix-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/finix-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finix-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/finix-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finix-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/finix-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finix-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.finix.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/finix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/finix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.finix.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finix-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finix-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finix-events-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/finix-events-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.finix.com/mcp
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-onboard-merchant-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-authorize-and-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-tokenize-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-refund-transfer-workflow.yml
created: '2026-07-17'
description: Finix is a full-stack payments technology provider that lets software platforms, marketplaces, and merchants accept and send payments online and in person. The Finix API is a HAL/HATEOAS REST API (HTTP Basic authentication per RFC 7617, date-based Finix-Version header, cursor pagination, idempotency_id) covering Identities, Merchants, Payment Instruments, Authorizations, Transfers, Settlements, Disputes, Fee Profiles, Verifications, Onboarding Forms, Devices, Balance Transfers, Split Transfers, and Webhooks, plus low-code Checkout, Payment Links, Subscriptions, and Payouts. It is Level 1 PCI DSS certified with finix.js browser tokenization, native iOS/Android SDKs, and official Python, Node.js, Java, and PHP client libraries. This profile was enriched from Finix's own public developer surface.
image: https://images.ctfassets.net/kqru4vgwujx6/3dBfyfPS31FWqFPTwf4dRv/417cc8b5e94029726cffb9aa85230111/OG_Image.png?w=1200&q=90
layout: provider
mcp_servers:
- description: Finix's official remote MCP server (HTTP transport, no auth) exposes live Finix documentation and OpenAPI to MCP clients via tools search, list-apis, get-endpoints, get-endpoint-info, get-security-sch
  name: Finix MCP Server
  slug: finix-mcp-server
modified: '2026-07-19'
name: Finix
nav: Providers
network: true
overview: 'Finix publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Balance Transfers API, Compliance Forms API, and 16 more. Tagged areas include Company, Fintech, Payments, Payment Processing, and Payment Facilitation.


  The Finix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Finix Rate Limits
  slug: finix-rate-limits
score:
  band: strong
  composite: 65.5
  delta: 0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.9
    developer_ergonomics: 79.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finix/refs/heads/main/screenshots/finix-2026-07-25T214523.png
security:
- kind: authentication
  name: Finix Authentication
  slug: finix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Finix Domain Security
  slug: finix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Finix Vulnerability Disclosure
  slug: finix-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Finix Trust Center
  slug: finix-trust-center
  summary_line: SOC 1, SOC 2, PCI DSS
slug: finix
tags:
- Company
- Fintech
- Payments
- Payment Processing
- Payment Facilitation
- Merchant Onboarding
- Payouts
- Marketplaces
website: https://finix.com/
---
