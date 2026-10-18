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
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Caliza Agentic Access
  operation_count: 68
  slug: caliza-agentic-access
  summary_line: 68 operations · 38 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Manage beneficiaries (individuals and businesses) and their related resources. Endpoints cover creating, updating, enabling/disabling, deleting beneficiaries, managing wallets, virtual accounts, files
  name: Caliza Beneficiary V1 API
  slug: caliza-beneficiary-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Inspect and list the set of capabilities/features enabled for an integrator account (supported currencies, payment rails, transaction types, limits and special features). Useful to adapt client behavi
  name: Caliza Integrator Capabilities V1 API
  slug: caliza-integrator-capabilities-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: 'Integrator-level configuration and profile endpoints: manage integrator profile, credentials, webhook configuration and secrets, view integrator balances and perform integrator-scoped operations.'
  name: Caliza Integrator V1 API
  slug: caliza-integrator-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Manage KYC (Know Your Customer) and KYB (Know Your Business) verification for beneficiaries. Create interactive verification sessions that redirect users to a third-party provider and track verificati
  name: Caliza KYC/KYB V1 API
  slug: caliza-kyc-kyb-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: 'Payment-specific operations: create payments, attach supporting documents, set/update payment blockchain hashes and retrieve payment instructions. Use these when initiating or inspecting single paymen'
  name: Caliza Payment V1 API
  slug: caliza-payment-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Manage saved payment recipients used as payout destinations. Create, retrieve, update, list and delete recipient profiles including bank/crypto details and verification metadata.
  name: Caliza Recipient V1 API
  slug: caliza-recipient-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: 'Manage related persons (e.g. beneficial owners, directors, representatives) linked to a beneficiary. Create, retrieve, update, list and delete related persons and upload supporting identity documents '
  name: Caliza Related Person API
  slug: caliza-related-person-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Retrieve the current terms & conditions document and record user acceptance. Use these endpoints to present legal terms to users and store auditable acceptance (timestamp, IP, version) required for co
  name: Caliza Terms and Conditions V1 API
  slug: caliza-terms-and-conditions-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Create, simulate, inspect and manage financial transactions. Includes endpoints to create transactions and simulations, retrieve transaction details, update metadata (e.g. blockchain hashes), export r
  name: Caliza Transaction V1 API
  slug: caliza-transaction-v1-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Sandbox-only transaction utilities for integration and testing. Simulate deposits, payouts and webhook notifications (PIX, SPEI, USD, etc.) without real funds to validate integration behavior and webh
  name: Caliza Transaction V1 Sandbox API
  slug: caliza-transaction-v1-sandbox-api
- baseURL: https://api.caliza.com/core-api/v1
  baseurl_source: declared
  description: Crypto Travel Rule compliance endpoints. Collect wallet ownership proofs for self-hosted (non-custodial) wallet recipients — via wallet signature or microtransfer (Satoshi test) — and retrieve the Tra
  name: Caliza Travel Rule V1 API
  slug: caliza-travel-rule-v1-api
artifact_total: 25
asyncapis:
- description: ''
  name: Caliza Webhooks
  slug: caliza-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/agentic-access/caliza-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/caliza-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/rules/caliza-rules.yml
  title: ''
  type: Spectral
  url: rules/caliza-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/json-ld/caliza-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/caliza-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/vocabulary/caliza-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/caliza-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/security/caliza-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/caliza-trust-center.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/lifecycle/caliza-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/caliza-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/hosts/caliza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caliza-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/vendors/caliza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caliza-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.caliza.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.caliza.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.caliza.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.caliza.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.caliza.com/docs/authenticate
- group: company
  title: ''
  type: Blog
  url: https://www.caliza.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.caliza.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.caliza.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.caliza.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.caliza.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/69177a9c7494e512590531d7_Caliza%20US%20Website%20Terms%20-%2007.17.2025.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/698a6522f0a64bd8dedb0942_Caliza%20US%20Privacy%20Policy%20-%20Final%2002.06.2026.docx.pdf
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/authentication/caliza-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caliza-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/scopes/caliza-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/caliza-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/well-known/caliza-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caliza-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/errors/caliza-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/caliza-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/conventions/caliza-conventions.yml
  title: ''
  type: Conventions
  url: conventions/caliza-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/lifecycle/caliza-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/caliza-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/sandbox/caliza-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/caliza-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/data-model/caliza-data-model.yml
  title: ''
  type: DataModel
  url: data-model/caliza-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/mcp/caliza-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/caliza-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/llms/caliza-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caliza-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/conformance/caliza-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caliza-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/security/caliza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caliza-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/asyncapi/caliza-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/caliza-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Caliza is a financial infrastructure company providing compliant, real-time cross-border payments and USD account infrastructure for global businesses. The Caliza Core API lets integrators create individual and business beneficiaries (with KYC/KYB verification), issue named USD digital-dollar and multi-currency virtual accounts, simulate and execute transactions and payments across fiat and stablecoin rails (ACH, WIRE, SWIFT, RTP, PIX, SPEI, and blockchain networks including Ethereum, Polygon, Tron, Stellar, Base and Solana), run batch and sweep payouts, lock FX rates, manage recipients, and receive HMAC-signed webhook notifications for the full transaction and beneficiary lifecycle. Authentication is OAuth 2.0 (OpenID Connect / Keycloak) and a full sandbox environment with mock deposit simulators is provided. Caliza is backed by Initialized Capital and QED Investors.
image: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/6787817b276b304d33d8dd2f_caliza-logo.png
json_schemas:
- name: PersonRequest
  property_count: 18
  slug: caliza-person-request
- name: RecipientResponse
  property_count: 12
  slug: caliza-recipient-response
- name: SimulationRequest
  property_count: 13
  slug: caliza-simulation-request
- name: SimulationV2Request
  property_count: 8
  slug: caliza-simulation-v2-request
- name: TransactionResponse
  property_count: 17
  slug: caliza-transaction-response
- name: TravelRuleProofResponse
  property_count: 11
  slug: caliza-travel-rule-proof-response
jsonld:
- class_count: 109
  name: Caliza Context
  property_count: 318
  slug: caliza-context
layout: provider
modified: '2026-07-18'
name: Caliza
nav: Providers
network: true
overview: 'Caliza publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Beneficiary V1 API, Integrator Capabilities V1 API, Integrator V1 API, and 8 more. Tagged areas include Company, Fintech, Payments, Cross-Border Payments, and Stablecoins.


  The Caliza catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Caliza''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 27 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Caliza API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 2
  slug: caliza-rules
scopes:
- name: Caliza Scopes
  scope_count: 10
  slug: caliza-scopes
  summary_line: 10 scopes · password
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.5
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 71.3
    developer_ergonomics: 53.0
    discoverability: 73.2
    operational_transparency: 27.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/screenshots/caliza-2026-07-25T204235.png
security:
- kind: authentication
  name: Caliza Authentication
  slug: caliza-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Caliza Domain Security
  slug: caliza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Caliza Trust Center
  slug: caliza-trust-center
  summary_line: trust center published
slug: caliza
tags:
- Company
- Fintech
- Payments
- Cross-Border Payments
- Stablecoins
- Remittances
- Foreign Exchange
- Virtual Accounts
- Payouts
- KYC
- Latin America
website: https://www.caliza.com/
---
