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
    error_semantics: verified
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Paywithmybank Agentic Access
  operation_count: 31
  slug: paywithmybank-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 11
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
artifact_total: 16
asyncapis:
- description: ''
  name: Paywithmybank Webhooks
  slug: paywithmybank-webhooks
common:
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
  url: openapi/paywithmybank-openapi-original.yml
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
- description: ''
  name: paywithmybank-mcp.yml
  slug: paywithmybank-mcpyml
modified: '2026-07-20'
name: PayWithMyBank (Trustly)
nav: Providers
network: true
overview: 'PayWithMyBank (Trustly) publishes 11 APIs on the [APIs.io](https://apis.io/) network, including accountData API, accounts API, countries API, and 8 more. Tagged areas include Company, Payments, Pay by Bank, Open Banking, and ACH.


  The PayWithMyBank (Trustly) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayWithMyBank (Trustly)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 26 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 47.5
  delta: -3.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.0
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 50.7
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Webhooks
website: https://www.trustly.com/us
---
