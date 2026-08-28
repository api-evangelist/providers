---
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
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: Five OpenAPI contracts (Swap, Buy, Sell, Earn, Card) that an exchange, on/off-ramp, earn or card provider implements so its service is offered natively inside Ledger Wallet. Ledger publishes the speci
  name: Ledger Wallet Exchange Provider APIs
  slug: ledger-wallet-exchange-provider-apis
- description: Institutional custody REST API for the Ledger Enterprise platform — accounts and balances, transaction creation and approval, governance requests and quorums, users and API operators, groups, entities
  name: Ledger Enterprise API (Vault API)
  slug: ledger-enterprise-api-vault-api
- description: Ledger-hosted transaction service for Safe smart accounts, adding Ledger Clear Signing and enterprise governance on top of the open-source Safe backend. Query Safe configuration, balances, collectible
  name: Ledger Enterprise Multisig API
  slug: ledger-enterprise-multisig-api
- description: Bi-directional JSON-RPC 2.0 interface between a Live App (dApp) and a wallet implementing the Wallet API Server, such as Ledger Wallet. Currency-agnostic modules for accounts, currencies, transactions
  name: Ledger Wallet API
  slug: ledger-wallet-api
- description: TypeScript SDK for discovering, connecting to and driving Ledger hardware signers over WebHID, Bluetooth, USB and Speculos — sessions, device state, app management, APDU exchange and chain-specific si
  name: Ledger Device Management Kit
  slug: ledger-device-management-kit
artifact_total: 12
asyncapis:
- description: ''
  name: Ledger Exchange Webhooks
  slug: ledger-exchange-webhooks
common:
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
overview: 'Ledger publishes 3 APIs on the [APIs.io](https://apis.io/) network: Wallet Exchange Provider APIs, Enterprise API (Vault API), and Enterprise Multisig API. Tagged areas include Company, Cryptocurrency, Digital Assets, Hardware Wallet, and Self Custody.


  The Ledger catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ledger''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 34 more developer resources.'
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
  composite: 64.5
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 56.7
    developer_ergonomics: 85.7
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 81.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Company
- Cryptocurrency
- Digital Assets
- Hardware Wallet
- Self Custody
- Institutional Custody
- Blockchain
- Payments
- Staking
- Security
- Agent Skills
- agent-native
website: https://www.ledger.com/
---
