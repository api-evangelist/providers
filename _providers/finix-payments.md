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
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Finix Payments Agentic Access
  operation_count: 91
  slug: finix-payments-agentic-access
  summary_line: 91 operations · 39 acting
api_count: 1
apis:
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/authorizations.md''}'
  name: Finix Payments Authorizations API
  slug: finix-payments-authorizations-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/balance-transfers.md''}'
  name: Finix Payments Balance Transfers API
  slug: finix-payments-balance-transfers-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/compliance-forms.md''}'
  name: Finix Payments Compliance Forms API
  slug: finix-payments-compliance-forms-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/devices.md''}'
  name: Finix Payments Devices API
  slug: finix-payments-devices-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/disputes.md''}'
  name: Finix Payments Disputes API
  slug: finix-payments-disputes-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/fee-profiles.md''}'
  name: Finix Payments Fee Profiles API
  slug: finix-payments-fee-profiles-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/files.md''}'
  name: Finix Payments Files API
  slug: finix-payments-files-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/identities.md''}'
  name: Finix Payments Identities API
  slug: finix-payments-identities-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/instrument-updates.md''}'
  name: Finix Payments Instrument Updates API
  slug: finix-payments-instrument-updates-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/merchant-profiles.md''}'
  name: Finix Payments Merchant Profiles API
  slug: finix-payments-merchant-profiles-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/merchants.md''}'
  name: Finix Payments Merchants API
  slug: finix-payments-merchants-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/onboarding-forms.md''}'
  name: Finix Payments Onboarding Forms API
  slug: finix-payments-onboarding-forms-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/payment-instruments.md''}'
  name: Finix Payments Payment Instruments API
  slug: finix-payments-payment-instruments-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/payout-profiles.md''}'
  name: Finix Payments Payout Profiles API
  slug: finix-payments-payout-profiles-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/settlements.md''}'
  name: Finix Payments Settlements API
  slug: finix-payments-settlements-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/split-transfers.md''}'
  name: Finix Payments Split Transfers API
  slug: finix-payments-split-transfers-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/transfers.md''}'
  name: Finix Payments Transfers API
  slug: finix-payments-transfers-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/verifications.md''}'
  name: Finix Payments Verifications API
  slug: finix-payments-verifications-api
- baseURL: https://finix.live-payments-api.com
  baseurl_source: declared
  description: '{''$ref'': ''api-descriptions/tags/webhooks.md''}'
  name: Finix Payments Webhooks API
  slug: finix-payments-webhooks-api
arazzos:
- description: Create a buyer Identity, tokenize a card, authorize, then capture into a Transfer.
  name: Finix — Accept a card payment (auth + capture)
  slug: finix-payments-accept-a-card-payment
- description: Create a seller Identity, provision a Merchant, and run verification/underwriting.
  name: Finix — Onboard a seller/merchant
  slug: finix-payments-onboard-a-merchant
artifact_total: 66
asyncapis:
- description: ''
  name: Finix Payments Webhooks
  slug: finix-payments-webhooks
collections:
- collection_type: postman
  name: Finix Authorizations API
  slug: postman-finix-payments-authorizations-api
- collection_type: postman
  name: Finix Authorizations Balance Transfers API
  slug: postman-finix-payments-balance-transfers-api
- collection_type: postman
  name: Finix Authorizations Compliance Forms API
  slug: postman-finix-payments-compliance-forms-api
- collection_type: postman
  name: Finix Authorizations Devices API
  slug: postman-finix-payments-devices-api
- collection_type: postman
  name: Finix Authorizations Disputes API
  slug: postman-finix-payments-disputes-api
- collection_type: postman
  name: Finix Authorizations Fee Profiles API
  slug: postman-finix-payments-fee-profiles-api
- collection_type: postman
  name: Finix Authorizations Files API
  slug: postman-finix-payments-files-api
- collection_type: postman
  name: Finix Authorizations Identities API
  slug: postman-finix-payments-identities-api
- collection_type: postman
  name: Finix Authorizations Instrument Updates API
  slug: postman-finix-payments-instrument-updates-api
- collection_type: postman
  name: Finix Authorizations Merchant Profiles API
  slug: postman-finix-payments-merchant-profiles-api
- collection_type: postman
  name: Finix Authorizations Merchants API
  slug: postman-finix-payments-merchants-api
- collection_type: postman
  name: Finix Authorizations Onboarding Forms API
  slug: postman-finix-payments-onboarding-forms-api
- collection_type: postman
  name: Finix Authorizations Payment Instruments API
  slug: postman-finix-payments-payment-instruments-api
- collection_type: postman
  name: Finix Authorizations Payout Profiles API
  slug: postman-finix-payments-payout-profiles-api
- collection_type: postman
  name: Finix Authorizations Settlements API
  slug: postman-finix-payments-settlements-api
- collection_type: postman
  name: Finix Authorizations Split Transfers API
  slug: postman-finix-payments-split-transfers-api
- collection_type: postman
  name: Finix Authorizations Transfers API
  slug: postman-finix-payments-transfers-api
- collection_type: postman
  name: Finix Authorizations Verifications API
  slug: postman-finix-payments-verifications-api
- collection_type: postman
  name: Finix Authorizations Webhooks API
  slug: postman-finix-payments-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Finix Authorizations API
  slug: open-finix-payments-authorizations-api
- collection_type: open
  name: Finix Authorizations Balance Transfers API
  slug: open-finix-payments-balance-transfers-api
- collection_type: open
  name: Finix Authorizations Compliance Forms API
  slug: open-finix-payments-compliance-forms-api
- collection_type: open
  name: Finix Authorizations Devices API
  slug: open-finix-payments-devices-api
- collection_type: open
  name: Finix Authorizations Disputes API
  slug: open-finix-payments-disputes-api
- collection_type: open
  name: Finix Authorizations Fee Profiles API
  slug: open-finix-payments-fee-profiles-api
- collection_type: open
  name: Finix Authorizations Files API
  slug: open-finix-payments-files-api
- collection_type: open
  name: Finix Authorizations Identities API
  slug: open-finix-payments-identities-api
- collection_type: open
  name: Finix Authorizations Instrument Updates API
  slug: open-finix-payments-instrument-updates-api
- collection_type: open
  name: Finix Authorizations Merchant Profiles API
  slug: open-finix-payments-merchant-profiles-api
- collection_type: open
  name: Finix Authorizations Merchants API
  slug: open-finix-payments-merchants-api
- collection_type: open
  name: Finix Authorizations Onboarding Forms API
  slug: open-finix-payments-onboarding-forms-api
- collection_type: open
  name: Finix Authorizations Payment Instruments API
  slug: open-finix-payments-payment-instruments-api
- collection_type: open
  name: Finix Authorizations Payout Profiles API
  slug: open-finix-payments-payout-profiles-api
- collection_type: open
  name: Finix Authorizations Settlements API
  slug: open-finix-payments-settlements-api
- collection_type: open
  name: Finix Authorizations Split Transfers API
  slug: open-finix-payments-split-transfers-api
- collection_type: open
  name: Finix Authorizations Transfers API
  slug: open-finix-payments-transfers-api
- collection_type: open
  name: Finix Authorizations Verifications API
  slug: open-finix-payments-verifications-api
- collection_type: open
  name: Finix Authorizations Webhooks API
  slug: open-finix-payments-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/finix-payments-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/finix-payments/overview
- group: company
  title: ''
  type: Website
  url: https://www.finixpayments.com/
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
  url: https://finix.com/docs/api
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
  url: https://dashboard.finixpayments.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finix.com/terms-and-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finix.com/terms-and-policies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.finix.com
- group: build
  title: ''
  type: Packages
  url: packages/finix-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/finix-payments-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finix-payments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finix-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/finix-payments-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finix-payments-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finix-payments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/finix-payments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finix-payments-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.finix.com/additional-resources/developers/authentication-and-api-basics/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/finix-payments-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/finix-payments-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/finix-payments-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finix-payments-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finix-payments-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/finix-payments-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finix-payments-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finix-payments-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finix-payments-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finix-payments-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finix-payments-domain-security.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-payments-accept-a-card-payment.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/finix-payments-onboard-a-merchant.yml
created: '2026-07-17'
description: Finix is a full-stack payments technology provider that lets businesses, software platforms, and marketplaces accept and send payments online and in person. Its REST API (version 2022-02-01) covers the full payments lifecycle — Identities, Merchants, Payment Instruments, Authorizations, Transfers, Settlements, Disputes, Verifications, Fee/Payout Profiles, Devices/terminals, and Webhooks — enabling card, ACH, EFT, digital-wallet, and Buy-Now-Pay-Later acceptance, seller onboarding/underwriting, split transfers, payouts, and payment facilitation (PayFac-as-a-service). Finix is a Level 1 PCI DSS certified platform with browser (finix.js) and mobile tokenization SDKs, hosted checkout pages, and payment links. Authentication is HTTP Basic Auth with environment-scoped API keys; the API uses cursor pagination, idempotency_id request-level idempotency, HAL responses, and dated versioning via the Finix-Version header.
image: https://images.ctfassets.net/kqru4vgwujx6/3dBfyfPS31FWqFPTwf4dRv/417cc8b5e94029726cffb9aa85230111/OG_Image.png?w=1200&q=90
layout: provider
mcp_servers:
- description: ''
  name: Finix Payments MCP Server
  slug: finix-payments-mcp-server
modified: '2026-07-19'
name: Finix Payments
nav: Providers
network: true
overview: 'Finix Payments publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Balance Transfers API, Compliance Forms API, and 16 more. Tagged areas include Company, Payments, Payment Processing, Payment Facilitation, and Embedded Finance.


  The Finix Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finix Payments'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 2
  name: Finix Payments Rate Limits
  slug: finix-payments-rate-limits
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 62.5
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finix-payments/refs/heads/main/screenshots/finix-payments-2026-07-25T214524.png
security:
- kind: authentication
  name: Finix Payments Authentication
  slug: finix-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Finix Payments Domain Security
  slug: finix-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finix-payments
tags:
- Company
- Payments
- Payment Processing
- Payment Facilitation
- Embedded Finance
- Marketplaces
- ACH
- Card Acceptance
- Fintech
- PCI DSS
website: https://www.finixpayments.com/
---
