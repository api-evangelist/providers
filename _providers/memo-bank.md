---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'Account assessments allow you to assess SEPA counterparty accounts before initiating transactions with them. An assessment provides: * **Risk indicators**: Detection of fraudulent activity, suspicious'
  name: Memo Bank Account assessments API
  slug: memo-bank-account-assessments-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'Accounts are any bank account that your company owns: current account, ring-fenced account, settlement account, specially dedicated account, trust account, meal voucher account, booster account, etc. '
  name: Memo Bank Accounts API
  slug: memo-bank-accounts-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Account Information Service. Consent is given using the **OAuth2 as a pre-step** authentication flow described in NextGenPSD2 specifications. This means you don't have to manage consents using the ded
  name: Memo Bank AIS API
  slug: memo-bank-ais-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Documents attached to transactions.
  name: Memo Bank Attachments API
  slug: memo-bank-attachments-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Collections are SEPA direct debit collections, including SEPA CORE direct debits and SEPA B2B direct debits. To initiate a direct debit, a **mandate** signed by the debtor is required. You have the op
  name: Memo Bank Collections API
  slug: memo-bank-collections-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'IBANs are identifiers for bank accounts. There are two types of IBANs at Memo Bank: * Main IBANs, which act as primary identifiers for a bank account. There is exactly one main IBAN per bank account. '
  name: Memo Bank IBA Ns API
  slug: memo-bank-ibans-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Mandate signature requests are a way to prepare and send collection mandates for signature. The mandate debtor receives an email with a link so they can complete and sign the mandate. Once it has been
  name: Memo Bank Mandate signature requests API
  slug: memo-bank-mandate-signature-requests-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: OAuth2 token management endpoints.
  name: Memo Bank O Auth2 API
  slug: memo-bank-oauth2-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Payment Initiation Service. Payment initiation is done using the **integrated OAuth2** authentication flow described in NextGenPSD2 specifications. This means you first have to initiate a payment usin
  name: Memo Bank PIS API
  slug: memo-bank-pis-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Sandbox only endpoints.
  name: Memo Bank Sandbox API
  slug: memo-bank-sandbox-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Transactions are any debit and credit operations on an account. <img src="https://assets.memo.bank/memobankapi/transactions-lifecycle-api-v2.png" alt="Transactions lifecycle" width="750"> Note that th
  name: Memo Bank Transactions API
  slug: memo-bank-transactions-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Transfers are transfers within the SEPA-zone, including SEPA standard transfers, SEPA instant transfers and Target 2 transfers. They can be initiated asynchronously, one by one or in bulk. They have a
  name: Memo Bank Transfers API
  slug: memo-bank-transfers-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: '# Events When something interesting happens on your Memo Bank workspace, such as a new transaction being created, Memo Bank can reach out to your application so that you can take action (such as sendi'
  name: Memo Bank Webhook API
  slug: memo-bank-webhook-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Manage webhooks for your application. Webhooks allow you to receive real-time notifications when events occur on your Memo Bank workspace. Please refer to the [Webhook](https://docs.api.memo.bank/grou
  name: Memo Bank Webhooks API
  slug: memo-bank-webhooks-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Wire transfers are transfers going through Swift. They allow you to send funds outside the SEPA network and to transfer money in foreign currencies. Initiating a wire transfer may require you to uploa
  name: Memo Bank Wire Transfers API
  slug: memo-bank-wire-transfers-api
artifact_total: 23
asyncapis:
- description: ''
  name: Memo Bank Webhooks
  slug: memo-bank-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/memo-bank-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/memo-bank-premium-bank-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/memo-bank-marketplace-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/memo-bank-nextgenpsd2-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memo-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memo.bank/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.memo.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.memo.bank/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.memo.bank/version-2/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.memo.bank/topic/topic-getting-started
- group: operate
  title: ''
  type: Support
  url: https://aide.memo.bank/
- group: company
  title: ''
  type: Blog
  url: https://memo.bank/en/magazine/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/memobank
- group: commercial
  title: ''
  type: Pricing
  url: https://memo.bank/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://memo.bank/en/sign-up/
- group: start
  title: ''
  type: Login
  url: https://client.memo.bank/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memo.bank/en/agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memo.bank/en/personal-data/
- group: auth
  title: ''
  type: Compliance
  url: https://memo.bank/en/about/security-operations/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.memo.bank/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.api.memo.bank/changes
- group: agent
  title: ''
  type: MCPServer
  url: mcp/memo-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memo-bank-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/memo-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/memo-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/memo-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memo-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/memo-bank-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memo-bank-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/memo-bank-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memo-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.api.memo.bank/topic/topic-versioning-and-backwards-compatibility
- group: design
  title: ''
  type: Conformance
  url: conformance/memo-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/memo-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/memo-bank-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/memo-bank-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/memo-bank-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/memo-bank-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/memo-bank-tool-crosswalk.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/memo-bank-changelog.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/memo-bank-decline-codes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/memo-bank-vulnerability-disclosure.yml
created: '2026-08-17'
description: Memo Bank is an independent French commercial bank, accredited as a credit institution by the European Central Bank and supervised by the ACPR, that serves small and mid-sized companies with current accounts, loans, savings and an API-first payments platform. Its Premium Bank API is a REST/JSON contract authenticated with RS256-signed JWT/JWS request tokens, covering accounts, transactions, bi-directional virtual IBANs, SEPA credit transfers, SEPA Direct Debit collections and mandate signature requests, SWIFT/RTGS wire transfers, bulk payment batches, attachments and account assessments, with 34 webhook event types for asynchronous reconciliation. A Marketplace API adds an OAuth 2.0 layer so third-party developers can act on customer resources, a NextGenPSD2 API implements the Berlin Group AIS/PIS interface for licensed third-party providers, and a hosted MCP server exposes read-only banking data plus attachment upload to AI assistants.
image: https://media.memo.bank/home_hero_602cdab270/home_hero_602cdab270.jpg
layout: provider
mcp_servers:
- description: ''
  name: Memo Bank MCP Server
  slug: memo-bank-mcp-server
modified: '2026-08-17'
name: Memo Bank
nav: Providers
network: true
overview: 'Memo Bank publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account assessments API, Accounts API, AIS API, and 12 more. Tagged areas include Company, Fintech Insurtech, Banking, Business Banking, and Payments.


  The Memo Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Memo Bank''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Memo Bank Plans Pricing
  plan_count: 2
  slug: memo-bank-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Memo Bank Rate Limits
  slug: memo-bank-rate-limits
scopes:
- name: Memo Bank Scopes
  scope_count: 2
  slug: memo-bank-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 59.5
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 66.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: berlin-group-nextgenpsd2
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 87.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/screenshots/memo-bank-2026-09-02T150506.png
security:
- kind: authentication
  name: Memo Bank Authentication
  slug: memo-bank-authentication
  summary_line: http/oauth2/mutualTLS · 4 schemes
- kind: domain-security
  name: Memo Bank Domain Security
  slug: memo-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Memo Bank Vulnerability Disclosure
  slug: memo-bank-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: memo-bank
tags:
- Company
- Fintech Insurtech
- Banking
- Business Banking
- Payments
- SEPA
- SEPA Direct Debit
- virtual-iban
- Wire Transfers
- Open Banking
- PSD2
- Berlin Group
- Webhook
- MCP
- France
website: https://memo.bank/
---
