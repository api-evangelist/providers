---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-09-03'
api_count: 14
apis:
- description: Bi-directional JSON-RPC 2.0 interface between a Live App (dApp) and a wallet implementing the Wallet API Server, such as Ledger Wallet. Currency-agnostic modules for accounts, currencies, transactions
  name: Ledger Wallet API
  slug: ledger-wallet-api
- description: TypeScript SDK for discovering, connecting to and driving Ledger hardware signers over WebHID, Bluetooth, USB and Speculos — sessions, device state, app management, APDU exchange and chain-specific si
  name: Ledger Device Management Kit
  slug: ledger-device-management-kit
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The 4337 API from Ledger — 5 operation(s) for 4337.
  name: Ledger 4337 API
  slug: ledger-4337-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Accounts API from Ledger — 17 operation(s) for accounts.
  name: Ledger Accounts API
  slug: ledger-accounts-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Authentication API from Ledger — 2 operation(s) for authentication.
  name: Ledger Authentication API
  slug: ledger-authentication-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Buy Redirect API from Ledger — 1 operation(s) for buy redirect.
  name: Ledger Buy Redirect API
  slug: ledger-buy-redirect-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Capabilities API from Ledger — 1 operation(s) for capabilities.
  name: Ledger Capabilities API
  slug: ledger-capabilities-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Cardano API from Ledger — 4 operation(s) for cardano.
  name: Ledger Cardano API
  slug: ledger-cardano-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Compliance API from Ledger — 2 operation(s) for compliance.
  name: Ledger Compliance API
  slug: ledger-compliance-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Crypto Currencies API from Ledger — 1 operation(s) for crypto currencies.
  name: Ledger Crypto Currencies API
  slug: ledger-crypto-currencies-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Currencies API from Ledger — 5 operation(s) for currencies.
  name: Ledger Currencies API
  slug: ledger-currencies-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The delegates API from Ledger — 2 operation(s) for delegates.
  name: Ledger Delegates API
  slug: ledger-delegates-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Digests API from Ledger — 3 operation(s) for digests.
  name: Ledger Digests API
  slug: ledger-digests-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Entities API from Ledger — 4 operation(s) for entities.
  name: Ledger Entities API
  slug: ledger-entities-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Ethereum API from Ledger — 3 operation(s) for ethereum.
  name: Ledger Ethereum API
  slug: ledger-ethereum-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Groups API from Ledger — 3 operation(s) for groups.
  name: Ledger Groups API
  slug: ledger-groups-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Grow API from Ledger — 1 operation(s) for grow.
  name: Ledger Grow API
  slug: ledger-grow-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Labels API from Ledger — 2 operation(s) for labels.
  name: Ledger Labels API
  slug: ledger-labels-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Messages API from Ledger — 3 operation(s) for messages.
  name: Ledger Messages API
  slug: ledger-messages-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The modules API from Ledger — 1 operation(s) for modules.
  name: Ledger Modules API
  slug: ledger-modules-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The notification feature allows you to be notified when an API user receives an important event. To receive a webhook notification, you must first register your target endpoint via `PUT /notifications
  name: Ledger Notifications API
  slug: ledger-notifications-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Organizations API from Ledger — 1 operation(s) for organizations.
  name: Ledger Organizations API
  slug: ledger-organizations-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The owners API from Ledger — 1 operation(s) for owners.
  name: Ledger Owners API
  slug: ledger-owners-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Pairs API from Ledger — 1 operation(s) for pairs.
  name: Ledger Pairs API
  slug: ledger-pairs-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The PKI API from Ledger — 1 operation(s) for pki.
  name: Ledger PKI API
  slug: ledger-pki-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Pledges API from Ledger — 2 operation(s) for pledges.
  name: Ledger Pledges API
  slug: ledger-pledges-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Quote API from Ledger — 1 operation(s) for quote.
  name: Ledger Quote API
  slug: ledger-quote-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: 'A Request represents the intent of creating or changing an object in the system. For example, when you create a transaction, a *Create transaction* request is created. You can observe all the changes '
  name: Ledger Requests API
  slug: ledger-requests-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The safes API from Ledger — 6 operation(s) for safes.
  name: Ledger Safes API
  slug: ledger-safes-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Sell API from Ledger — 1 operation(s) for sell.
  name: Ledger Sell API
  slug: ledger-sell-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Sell Redirect API from Ledger — 1 operation(s) for sell redirect.
  name: Ledger Sell Redirect API
  slug: ledger-sell-redirect-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Settlements API from Ledger — 4 operation(s) for settlements.
  name: Ledger Settlements API
  slug: ledger-settlements-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Solana API from Ledger — 4 operation(s) for solana.
  name: Ledger Solana API
  slug: ledger-solana-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Stakes API from Ledger — 1 operation(s) for stakes.
  name: Ledger Stakes API
  slug: ledger-stakes-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Status API from Ledger — 1 operation(s) for status.
  name: Ledger Status API
  slug: ledger-status-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Swap API from Ledger — 2 operation(s) for swap.
  name: Ledger Swap API
  slug: ledger-swap-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Tezos API from Ledger — 2 operation(s) for tezos.
  name: Ledger Tezos API
  slug: ledger-tezos-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Transaction API from Ledger — 1 operation(s) for transaction.
  name: Ledger Transaction API
  slug: ledger-transaction-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The transactions API from Ledger — 10 operation(s) for transactions.
  name: Ledger Transactions API
  slug: ledger-transactions-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Users API from Ledger — 3 operation(s) for users.
  name: Ledger Users API
  slug: ledger-users-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Webhook API from Ledger — 1 operation(s) for webhook.
  name: Ledger Webhook API
  slug: ledger-webhook-api
- baseURL: https://api.vault.ledger.com
  baseurl_source: declared
  description: The Whitelists API from Ledger — 3 operation(s) for whitelists.
  name: Ledger Whitelists API
  slug: ledger-whitelists-api
artifact_total: 49
asyncapis:
- description: ''
  name: Ledger Exchange Webhooks
  slug: ledger-exchange-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ledger-swap-provider-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ledger-enterprise-vault-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ledger.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ledger.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ledger.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.enterprise.ledger.com/api-documentation/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ledger.com/docs/device-app/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.ledger.com/
- group: operate
  title: ''
  type: Community
  url: https://developers.ledger.com/discord/
- group: company
  title: ''
  type: Blog
  url: https://www.ledger.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LedgerHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ledger.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.ledger.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ledger.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://vault.ledger.com/
- group: auth
  title: ''
  type: Security
  url: https://donjon.ledger.com/bounty/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.ledger.com/docs/news
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ledger-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ledger-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/ledger-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/ledger-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ledger-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ledger-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ledger-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ledger-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ledger-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ledger-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ledger-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.ledger.com/docs/news
- group: design
  title: ''
  type: Conformance
  url: conformance/ledger-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ledger-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ledger-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ledger-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ledger-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://enterprise.ledger.com/about
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ledger-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ledger-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ledger-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ledger-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/ledger-components.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ledger-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ledger-exchange-webhooks.yml
created: '2026-08-25'
description: 'Ledger SAS is the Paris-headquartered maker of the Ledger hardware signer family (Nano, Flex, Stax) and the surrounding self-custody and institutional-custody platform. Its developer surface spans five distinct programs: the Ledger Wallet exchange-provider APIs (Swap, Buy, Sell, Earn and Card OpenAPI contracts an exchange partner implements so its service appears natively inside Ledger Wallet), the Ledger Enterprise "Vault API" for institutional custody — accounts, transactions, governance requests, whitelists, entities, staking, compliance digests and reporting/notification webhooks — the Ledger Enterprise Multisig transaction service for Ledger-secured Safe smart accounts, the Wallet API (a bi-directional JSON-RPC 2.0 bridge that lets a Live App talk to a Ledger signer), and the Device Management Kit plus Clear Signing stack for building native device apps and clear-signed transactions. Ledger also publishes an unusually complete agent surface for a hardware company: an RFC
  9727 /.well-known/api-catalog, an llms.txt on the developer portal, and first-party Agent Skills for coding agents and the Ledger Wallet CLI.'
image: https://www.ledger.com/wp-content/themes/ledger-v2/public/images/ledger-logo-long.svg
layout: provider
modified: '2026-08-25'
name: Ledger
nav: Providers
network: true
overview: 'Ledger publishes 40 APIs on the [APIs.io](https://apis.io/) network, including 4337 API, Accounts API, Authentication API, and 37 more. Tagged areas include Cryptocurrency, Digital Assets, Hardware Wallet, Self-Custody, and institutional-custody.


  The Ledger catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ledger''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 36 more developer resources.'
plans:
- name: Ledger Plans Pricing
  plan_count: 0
  slug: ledger-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Ledger Rate Limits
  slug: ledger-rate-limits
score:
  band: strong
  composite: 60.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 57.3
    developer_ergonomics: 85.7
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 60.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ledger/refs/heads/main/screenshots/ledger-2026-09-02T150235.png
security:
- kind: authentication
  name: Ledger Authentication
  slug: ledger-authentication
  summary_line: apiKey/http-bearer · 7 schemes
- kind: domain-security
  name: Ledger Domain Security
  slug: ledger-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ledger Vulnerability Disclosure
  slug: ledger-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Ledger Trust Center
  slug: ledger-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 22301, CSPN V4 (ANSSI security visa), FIPS 140 Level III, Common Criteria EAL5+
slug: ledger
tags:
- Cryptocurrency
- Digital Assets
- Hardware Wallet
- Self-Custody
- institutional-custody
- Blockchain
- Payments
- Staking
- Security
- Agent Skills
- agent-native
website: https://www.ledger.com/
---
