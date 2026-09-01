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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Paywithmybank Agentic Access
  operation_count: 31
  slug: paywithmybank-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 1
apis:
- description: The accountData API from PayWithMyBank (Trustly) — 4 operation(s) for accountdata.
  name: PayWithMyBank (Trustly) accountData API
  slug: paywithmybank-accountdata-api
- description: The accounts API from PayWithMyBank (Trustly) — 3 operation(s) for accounts.
  name: PayWithMyBank (Trustly) accounts API
  slug: paywithmybank-accounts-api
- description: The countries API from PayWithMyBank (Trustly) — 1 operation(s) for countries.
  name: PayWithMyBank (Trustly) countries API
  slug: paywithmybank-countries-api
- description: The customers API from PayWithMyBank (Trustly) — 2 operation(s) for customers.
  name: PayWithMyBank (Trustly) customers API
  slug: paywithmybank-customers-api
- description: The disputeManagement API from PayWithMyBank (Trustly) — 1 operation(s) for disputemanagement.
  name: PayWithMyBank (Trustly) disputeManagement API
  slug: paywithmybank-disputemanagement-api
- description: The identity API from PayWithMyBank (Trustly) — 3 operation(s) for identity.
  name: PayWithMyBank (Trustly) identity API
  slug: paywithmybank-identity-api
- description: The networkCheckApi API from PayWithMyBank (Trustly) — 1 operation(s) for networkcheckapi.
  name: PayWithMyBank (Trustly) networkCheckApi API
  slug: paywithmybank-networkcheckapi-api
- description: The paymentProviders API from PayWithMyBank (Trustly) — 1 operation(s) for paymentproviders.
  name: PayWithMyBank (Trustly) paymentProviders API
  slug: paywithmybank-paymentproviders-api
- description: The payments API from PayWithMyBank (Trustly) — 2 operation(s) for payments.
  name: PayWithMyBank (Trustly) payments API
  slug: paywithmybank-payments-api
- description: The transactions API from PayWithMyBank (Trustly) — 10 operation(s) for transactions.
  name: PayWithMyBank (Trustly) transactions API
  slug: paywithmybank-transactions-api
- description: The verifyCustomer API from PayWithMyBank (Trustly) — 1 operation(s) for verifycustomer.
  name: PayWithMyBank (Trustly) verifyCustomer API
  slug: paywithmybank-verifycustomer-api
- description: The API API from PayWithMyBank (Trustly) — 0 operation(s) for api.
  name: PayWithMyBank (Trustly) API
  slug: paywithmybank-api-api
artifact_total: 29
asyncapis:
- description: ''
  name: Paywithmybank Webhooks
  slug: paywithmybank-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: accountData API
  slug: open-paywithmybank-accountdata-api
- collection_type: open
  name: accountData accounts API
  slug: open-paywithmybank-accounts-api
- collection_type: open
  name: accountData countries API
  slug: open-paywithmybank-countries-api
- collection_type: open
  name: accountData customers API
  slug: open-paywithmybank-customers-api
- collection_type: open
  name: accountData disputeManagement API
  slug: open-paywithmybank-disputemanagement-api
- collection_type: open
  name: accountData identity API
  slug: open-paywithmybank-identity-api
- collection_type: open
  name: accountData networkCheckApi API
  slug: open-paywithmybank-networkcheckapi-api
- collection_type: open
  name: accountData paymentProviders API
  slug: open-paywithmybank-paymentproviders-api
- collection_type: open
  name: accountData payments API
  slug: open-paywithmybank-payments-api
- collection_type: open
  name: accountData transactions API
  slug: open-paywithmybank-transactions-api
- collection_type: open
  name: accountData verifyCustomer API
  slug: open-paywithmybank-verifycustomer-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paywithmybank-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustly.com/us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amer.developers.trustly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://amer.developers.trustly.com/payments/docs/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://amer.developers.trustly.com/api-reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://amer.developers.trustly.com/integrate/get-started/explore-solutions
- group: operate
  title: ''
  type: Support
  url: https://amer.developers.trustly.com/integrate/get-started/get-support
- group: company
  title: ''
  type: Blog
  url: https://www.trustly.com/us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrustlyInc
- group: start
  title: ''
  type: SignUp
  url: https://trustly.one/merchant-portal/
- group: start
  title: ''
  type: Login
  url: https://my.trustly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustly.com/us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustly.com/us/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/paywithmybank-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paywithmybank-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paywithmybank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paywithmybank-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/paywithmybank-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paywithmybank-packages.yml
- group: design
  title: ''
  type: Components
  url: components/paywithmybank-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paywithmybank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paywithmybank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paywithmybank-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/paywithmybank-api-catalog.json
- group: design
  title: ''
  type: Conventions
  url: conventions/paywithmybank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paywithmybank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paywithmybank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paywithmybank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paywithmybank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paywithmybank-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paywithmybank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paywithmybank-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paywithmybank-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: PayWithMyBank is the U.S. "Pay by Bank" brand of Trustly, a global open-banking payments provider that lets merchants accept payments directly from a consumer's bank account as an alternative to cards. The paywithmybank.com domain now redirects to Trustly, whose AMER developer platform exposes a REST Payments API (OpenAPI 3.1) covering transactions (establish, capture, deposit, cancel, reclaim, refund), payments retrieval, bank-account tokenization and verification, customer records, identity (Trustly ID), account data, dispute recovery, and asynchronous event notifications (webhooks). Authentication is HTTP Basic with a provisioned accessId/accessKey plus a server-generated requestSignature for the client-side Lightbox. Trustly operates the largest open-banking payments network with 12,000+ connected banks across 30+ countries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paywithmybank.png
layout: provider
mcp_servers:
- description: Official hosted MCP server published by Trustly (PayWithMyBank) for AI client integration (Claude Code, Cursor, etc.), advertised in the developer docs llms.txt. Serves the AMER Trustly Payments API d
  name: PayWithMyBank (Trustly) MCP Server
  slug: paywithmybank-trustly-mcp-server
modified: '2026-07-20'
name: PayWithMyBank (Trustly)
nav: Providers
network: true
overview: 'PayWithMyBank (Trustly) publishes 12 APIs on the [APIs.io](https://apis.io/) network, including accountData API, accounts API, countries API, and 9 more. Tagged areas include Company, Payments, Pay by Bank, Open Banking, and ACH.


  The PayWithMyBank (Trustly) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayWithMyBank (Trustly)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paywithmybank/refs/heads/main/screenshots/paywithmybank-2026-08-07T191723.png
security:
- kind: authentication
  name: Paywithmybank Authentication
  slug: paywithmybank-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paywithmybank Domain Security
  slug: paywithmybank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paywithmybank
tags:
- Company
- Payments
- Pay by Bank
- Open Banking
- ACH
- Bank Transfers
- Fintech
- Identity Verification
- Webhook
website: https://www.trustly.com/us
---
