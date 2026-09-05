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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 27
  human_in_the_loop: 27
  name: Veem Agentic Access
  operation_count: 50
  slug: veem-agentic-access
  summary_line: 50 operations · 27 acting · 27 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Attachment Controller
  name: Veem attachment-controller API
  slug: veem-attachment-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Bank Account Controller
  name: Veem bank-account-controller API
  slug: veem-bank-account-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Beneficial Owner Information Controller
  name: Veem beneficial-owner-information-controller API
  slug: veem-beneficial-owner-information-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Claimless Payment Controller
  name: Veem claimless-payment-controller API
  slug: veem-claimless-payment-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Contact Controller
  name: Veem contact-controller API
  slug: veem-contact-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: For managing crypto wallets, including balances, details, transactions and pay-ins
  name: Veem crypto-wallet-controller API
  slug: veem-crypto-wallet-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Customer Controller
  name: Veem customer-controller API
  slug: veem-customer-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Exchange Rate Controller
  name: Veem exchange-rate-controller API
  slug: veem-exchange-rate-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Invoice Controller
  name: Veem invoice-controller API
  slug: veem-invoice-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Meta Controller
  name: Veem meta-controller API
  slug: veem-meta-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Open Account Controller
  name: Veem open-account-controller API
  slug: veem-open-account-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Payment Controller
  name: Veem payment-controller API
  slug: veem-payment-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Wallet Controller
  name: Veem wallet-controller API
  slug: veem-wallet-controller-api
- baseURL: https://api.veem.com
  baseurl_source: declared
  description: Webhook Controller
  name: Veem webhook-controller API
  slug: veem-webhook-controller-api
artifact_total: 34
asyncapis:
- description: ''
  name: Veem Webhooks
  slug: veem-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veem API v1.2 attachment-controller API
  slug: open-veem-attachment-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller bank-account-controller API
  slug: open-veem-bank-account-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller beneficial-owner-information-controller API
  slug: open-veem-beneficial-owner-information-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller claimless-payment-controller API
  slug: open-veem-claimless-payment-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller contact-controller API
  slug: open-veem-contact-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller crypto-wallet-controller API
  slug: open-veem-crypto-wallet-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller customer-controller API
  slug: open-veem-customer-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller exchange-rate-controller API
  slug: open-veem-exchange-rate-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller invoice-controller API
  slug: open-veem-invoice-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller meta-controller API
  slug: open-veem-meta-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller open-account-controller API
  slug: open-veem-open-account-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller payment-controller API
  slug: open-veem-payment-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller wallet-controller API
  slug: open-veem-wallet-controller-api
- collection_type: open
  name: Veem API v1.2 attachment-controller webhook-controller API
  slug: open-veem-webhook-controller-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/veem-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veem-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.veem.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.veem.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veem.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.veem.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.veem.com/docs/intro-to-veem-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veeminc
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/veem/veem-public-workspace/collection/4dtpa4r/veem-public-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veem.com
- group: start
  title: ''
  type: Login
  url: https://apps.veem.com/CustomerApp/o/signin
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veem-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/veem-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/veem-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/veem-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/veem-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/veem-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/veem-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/veem-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/veem-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veem-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veem-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/veem-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/veem-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/veem-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/veem-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/veem-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/veem-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Veem is a global payments network that lets businesses send, receive, and request payments domestically and across borders. Its Public API covers account creation and KYC (including beneficial ownership), bank accounts and funding methods, claimless payments, invoices, multi-currency wallets, virtual bank accounts, crypto wallets, exchange-rate quotes, and webhooks, with embeddable Web SDK plugins for collecting card, bank, and identity data inside partner apps.
image: https://logo.clearbit.com/veem.com
layout: provider
modified: '2026-07-21'
name: Veem
nav: Providers
network: true
overview: 'Veem publishes 14 APIs on the [APIs.io](https://apis.io/) network, including attachment-controller API, bank-account-controller API, beneficial-owner-information-controller API, and 11 more. Tagged areas include Payments, B2B Payments, Cross-Border Payments, Invoicing, and Wallets.


  The Veem catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Veem''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 24 more developer resources.'
random_paper: 9
scopes:
- name: Veem Scopes
  scope_count: 1
  slug: veem-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 55.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veem/refs/heads/main/screenshots/veem-2026-08-17T082715.png
security:
- kind: authentication
  name: Veem Authentication
  slug: veem-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Veem Domain Security
  slug: veem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veem
tags:
- Payments
- B2B Payments
- Cross-Border Payments
- Invoicing
- Wallets
- Fintech
- Global Payments
website: https://www.veem.com
---
