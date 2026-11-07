---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Paywithmybank Agentic Access
  operation_count: 31
  slug: paywithmybank-agentic-access
  summary_line: 31 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The accounts API from PayWithMyBank (Trustly) — 3 operation(s) for accounts.
  name: PayWithMyBank (Trustly) accounts API
  slug: paywithmybank-accounts-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The countries API from PayWithMyBank (Trustly) — 1 operation(s) for countries.
  name: PayWithMyBank (Trustly) countries API
  slug: paywithmybank-countries-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The customers API from PayWithMyBank (Trustly) — 2 operation(s) for customers.
  name: PayWithMyBank (Trustly) Customers API
  slug: paywithmybank-customers-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The identity API from PayWithMyBank (Trustly) — 3 operation(s) for identity.
  name: PayWithMyBank (Trustly) Identity API
  slug: paywithmybank-identity-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The networkCheckApi API from PayWithMyBank (Trustly) — 1 operation(s) for networkcheckapi.
  name: PayWithMyBank (Trustly) Network Check API
  slug: paywithmybank-networkcheckapi-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The payments API from PayWithMyBank (Trustly) — 2 operation(s) for payments.
  name: PayWithMyBank (Trustly) Payments API
  slug: paywithmybank-payments-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The transactions API from PayWithMyBank (Trustly) — 10 operation(s) for transactions.
  name: PayWithMyBank (Trustly) Transactions API
  slug: paywithmybank-transactions-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The verifyCustomer API from PayWithMyBank (Trustly) — 1 operation(s) for verifycustomer.
  name: PayWithMyBank (Trustly) Verify Customer API
  slug: paywithmybank-verifycustomer-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The API API from PayWithMyBank (Trustly) — 0 operation(s) for api.
  name: PayWithMyBank (Trustly) API
  slug: paywithmybank-api-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The Account Data API from PayWithMyBank (Trustly) — 4 operation(s) for account data.
  name: PayWithMyBank (Trustly) Account Data API
  slug: paywithmybank-account-data-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The Dispute Management API from PayWithMyBank (Trustly) — 1 operation(s) for dispute management.
  name: PayWithMyBank (Trustly) Dispute Management API
  slug: paywithmybank-dispute-management-api
- baseURL: https://api.trustly.one/api/v1
  baseurl_source: declared
  description: The Payment Providers API from PayWithMyBank (Trustly) — 1 operation(s) for payment providers.
  name: PayWithMyBank (Trustly) Payment Providers API
  slug: paywithmybank-payment-providers-api
artifact_total: 31
asyncapis:
- description: ''
  name: Paywithmybank Webhooks
  slug: paywithmybank-webhooks
collections:
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
  href: https://artifacts.apis.io/paywithmybank/capabilities/paywithmybank-capability-edges.yml
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
  href: https://artifacts.apis.io/paywithmybank/openapi/_original/paywithmybank-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/paywithmybank-openapi-original.yml
- group: auth
  href: https://artifacts.apis.io/paywithmybank/authentication/paywithmybank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paywithmybank-authentication.yml
- group: agent
  href: https://artifacts.apis.io/paywithmybank/agentic-access/paywithmybank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/paywithmybank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/paywithmybank/security/paywithmybank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paywithmybank-domain-security.yml
- group: build
  href: https://artifacts.apis.io/paywithmybank/packages/paywithmybank-packages.yml
  title: ''
  type: Packages
  url: packages/paywithmybank-packages.yml
- group: build
  href: https://artifacts.apis.io/paywithmybank/packages/paywithmybank-packages.yml
  title: ''
  type: SDKs
  url: packages/paywithmybank-packages.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/components/paywithmybank-components.yml
  title: ''
  type: Components
  url: components/paywithmybank-components.yml
- group: agent
  href: https://artifacts.apis.io/paywithmybank/mcp/paywithmybank-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paywithmybank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/paywithmybank/llms/paywithmybank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paywithmybank-llms.txt
- group: agent
  href: https://artifacts.apis.io/paywithmybank/well-known/paywithmybank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paywithmybank-well-known.yml
- group: other
  href: https://artifacts.apis.io/paywithmybank/well-known/paywithmybank-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/paywithmybank-api-catalog.json
- group: design
  href: https://artifacts.apis.io/paywithmybank/conventions/paywithmybank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paywithmybank-conventions.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/conventions/paywithmybank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/paywithmybank-conventions.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/errors/paywithmybank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paywithmybank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/lifecycle/paywithmybank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/paywithmybank-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/conformance/paywithmybank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paywithmybank-conformance.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/data-model/paywithmybank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paywithmybank-data-model.yml
- group: start
  href: https://artifacts.apis.io/paywithmybank/sandbox/paywithmybank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/paywithmybank-sandbox.yml
- group: design
  href: https://artifacts.apis.io/paywithmybank/asyncapi/paywithmybank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/paywithmybank-webhooks.yml
- group: other
  href: https://artifacts.apis.io/paywithmybank/overlays/paywithmybank-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paywithmybank-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/paywithmybank/skills/_index.yml
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
  slug: trustly-amer
modified: '2026-07-20'
name: PayWithMyBank (Trustly)
nav: Providers
network: true
overview: 'PayWithMyBank (Trustly) publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including accounts API, countries API, Customers API, and 9 more. Tagged areas include Company, Payments, Pay by Bank, Open Banking, and ACH.


  The PayWithMyBank (Trustly) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PayWithMyBank (Trustly)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: PayWithMyBank (Trustly) API Rules
  rule_count: 50
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 6
  slug: paywithmybank-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 55.9
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/paywithmybank/paywithmybank-2026-08-07T191723.png
security:
- kind: authentication
  name: Paywithmybank Authentication
  slug: paywithmybank-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paywithmybank Domain Security
  slug: paywithmybank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Accept a Pay-by-Bank payment
  slug: paywithmybank-accept-payment
- name: Refund a settled transaction
  slug: paywithmybank-refund-transaction
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
