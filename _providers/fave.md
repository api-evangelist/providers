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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Fave Agentic Access
  operation_count: 6
  slug: fave-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Create charges via QR code or merchant scan.
  name: Fave Payments API
  slug: fave-payments-api
- description: Look up, list, acknowledge and refund transactions.
  name: Fave Transactions API
  slug: fave-transactions-api
arazzos:
- description: Create a QR-code charge, confirm it succeeded via transaction lookup, then issue a full refund. All operationIds are verified against the FavePay Omni OpenAPI.
  name: Accept a FavePay Omni payment and refund it
  slug: fave-accept-and-refund
- description: Charge a customer via merchant scan, then list the outlet's recent transactions and acknowledge the new one. All operationIds are verified against the FavePay Omni OpenAPI.
  name: Merchant-scan charge and reconcile
  slug: fave-scan-and-reconcile
artifact_total: 13
asyncapis:
- description: Webhook (callback) event surface for FavePay Omni. Fave POSTs the transaction object to the partner's callback_url whenever a transaction changes status. Each payload carries a `sign` (HMAC-SHA256) fi
  name: FavePay Omni Webhooks
  slug: fave-favepay-omni-asyncapi
- description: ''
  name: Fave Favepay Omni Webhooks
  slug: fave-favepay-omni-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FavePay Omni (FPO) Payments API
  slug: open-fave-payments-api
- collection_type: open
  name: FavePay Omni (FPO) Payments Transactions API
  slug: open-fave-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://myfave.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.myfave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.myfave.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.myfave.com/fpo-guide.html
- group: operate
  title: ''
  type: Support
  url: https://help.myfave.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.favebiz.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.favebiz.com/sign-up?ref=favebiz
- group: start
  title: ''
  type: Login
  url: https://app.favebiz.com/?ref=favebiz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.myfave.com/hc/en-us/sections/205050988-Terms-of-Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.myfave.com/hc/en-us/sections/205051008-Privacy-Policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/fave-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/fave-favepay-omni-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/fave-favepay-omni-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fave-favepay-omni-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fave-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fave-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fave-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fave-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fave-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fave-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fave-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fave-favepay-omni-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fave-llms.txt
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fave-accept-and-refund.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fave-scan-and-reconcile.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fave-domain-security.yml
created: '2026-07-17'
description: 'Fave is a Malaysia- and Singapore-based lifestyle and payments app offering deals, cashback, rewards, eCards, and QR-code payments, operated by Fave Asia Technologies and owned by Pine Labs. For merchants and platforms, Fave exposes the FavePay Omni (FPO) partner API: create single-use QR codes or payment URLs, process customer-presented (merchant-scan) charges, look up, list, and acknowledge transactions, issue full or partial refunds, and receive signed webhook callbacks on every status change. Every request is signed with HMAC-SHA256 using a secret key Fave issues during partner onboarding. FavePay Omni operates across Malaysia (MY), Singapore (SG), and Indonesia (ID).'
image: https://myfave.com/banner.png
layout: provider
mcp_servers:
- description: ''
  name: Fave MCP Server
  slug: fave-mcp-server
modified: '2026-07-19'
name: Fave
nav: Providers
network: true
overview: 'Fave publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payments API and Transactions API. Tagged areas include Company, Payments, Fintech, QR Payments, and Loyalty.


  The Fave catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Fave''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, sandbox, and 21 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 21.9
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fave/refs/heads/main/screenshots/fave-2026-07-25T214253.png
security:
- kind: authentication
  name: Fave Authentication
  slug: fave-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fave Domain Security
  slug: fave-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fave
tags:
- Company
- Payments
- Fintech
- QR Payments
- Loyalty
- Cashback
- Merchant Services
- Southeast Asia
- Webhook
website: https://myfave.com
---
