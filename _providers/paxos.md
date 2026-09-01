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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 61
  human_in_the_loop: 3
  name: Paxos Agentic Access
  operation_count: 125
  slug: paxos-agentic-access
  summary_line: 125 operations · 61 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Account Members allow you to associate an Identity with an Account on our Platform. Each Account can be linked to multiple Identities, which supports Joint Accounts (where two Identities have the abil
  name: Paxos Account Members API
  slug: paxos-account-members-api
- description: 'Accounts connect Identities (persons or institutions) to Profiles (asset balances). Key features include: - **Balance Management**: Track and manage profile balances via [Subledgering](https://docs.pa'
  name: Paxos Accounts API
  slug: paxos-accounts-api
- description: The Address Verification API from Paxos — 3 operation(s) for address verification.
  name: Paxos Address Verification API
  slug: paxos-address-verification-api
- description: API credentials allow programmatic access to Paxos APIs. These endpoints enable you to manage and view your API credentials.
  name: Paxos API Credentials API
  slug: paxos-api-credentials-api
- description: Claims represent rewards paid out on-chain. Use claim schedules to automate daily reward claims. *These endpoints are only relevant for whitelisted Rewards partners.*
  name: Paxos Claims API
  slug: paxos-claims-api
- description: For [Paxos Global PTE Ltd](https://help.paxos.com/hc/en-us/articles/9647005243284) users, update or reject a crypto deposit that does not contain the required [travel rule](https://help.paxos.com/hc/e
  name: Paxos Crypto Deposits API
  slug: paxos-crypto-deposits-api
- description: The Crypto Withdrawals API from Paxos — 3 operation(s) for crypto withdrawals.
  name: Paxos Crypto Withdrawals API
  slug: paxos-crypto-withdrawals-api
- description: The Deposit Addresses API from Paxos — 1 operation(s) for deposit addresses.
  name: Paxos Deposit Addresses API
  slug: paxos-deposit-addresses-api
- description: The Events API allows you to fetch events that occurred on the Paxos platform with the full event payload. This REST API can be used as part of your webhook integrations (including rebuilding your eve
  name: Paxos Events API
  slug: paxos-events-api
- description: The ExchangePublic API from Paxos — 2 operation(s) for exchangepublic.
  name: Paxos ExchangePublic API
  slug: paxos-exchangepublic-api
- description: The Fees API from Paxos — 1 operation(s) for fees.
  name: Paxos Fees API
  slug: paxos-fees-api
- description: 'The Fiat Transfers API allows clients to deposit and withdraw fiat via the following Fiat Networks: Wire (Fedwire and SWIFT) and CUBIX. The supported asset is USD. The full set of Fiat Transfers API e'
  name: Paxos Fiat Transfers API
  slug: paxos-fiat-transfers-api
- description: An Identity represents a person or institution who is able to take actions on the Paxos Platform. Depending on your integration type you might not need to create Identities for your end users. Identit
  name: Paxos Identity API
  slug: paxos-identity-api
- description: The Identity Controls API from Paxos — 1 operation(s) for identity controls.
  name: Paxos Identity Controls API
  slug: paxos-identity-controls-api
- description: 'The Identity Documents API allows clients to send documents to Paxos to validate identities during the KYC process. Files can be updated multiple times by re-sending the document type for processing. '
  name: Paxos Identity Documents API
  slug: paxos-identity-documents-api
- description: Institution Members allow you to associate persons with an institution on our Platform. Each institution can have multiple members, with each member representing the relationship to a person identity.
  name: Paxos Institution Members API
  slug: paxos-institution-members-api
- description: The Internal Transfers API from Paxos — 1 operation(s) for internal transfers.
  name: Paxos Internal Transfers API
  slug: paxos-internal-transfers-api
- description: Issuer Quotes are "held rates" offered by Paxos to mint or redeem Paxos-issued assets at a specific price within a period of time - for example, the option to buy PAXG within the next 5 seconds for $3
  name: Paxos Issuer Quotes API
  slug: paxos-issuer-quotes-api
- description: The Limits API from Paxos — 1 operation(s) for limits.
  name: Paxos Limits API
  slug: paxos-limits-api
- description: Market data provides various parameters of the order book and historical order data.
  name: Paxos Market Data API
  slug: paxos-market-data-api
- description: A Monitoring Address is a blockchain address that Paxos monitors daily for eligible stablecoin activity and determines the amount of rewards your organization will earn. We recommend adding any addres
  name: Paxos Monitoring Addresses API
  slug: paxos-monitoring-addresses-api
- description: The Orchestration Rules API from Paxos — 2 operation(s) for orchestration rules.
  name: Paxos Orchestration Rules API
  slug: paxos-orchestration-rules-api
- description: The Orchestrations API from Paxos — 2 operation(s) for orchestrations.
  name: Paxos Orchestrations API
  slug: paxos-orchestrations-api
- description: '<p>There are three types of orders: market, limit and post-only.</p> <p>Market orders guarantee execution at a variable price and quantity. Limit orders guarantee price and quantity at the time of exe'
  name: Paxos Orders API
  slug: paxos-orders-api
- description: Move assets between two Entities belonging to the same Organization or to a different Organization on the Paxos platform. > Transferring USD between Entities is prohibited in some jurisdictions. Conta
  name: Paxos Paxos Transfers API
  slug: paxos-paxos-transfers-api
- description: Payments represent actual transfers of rewards to the payout address associated with a given statement. Payments are made on-chain to a specified payout address. Payments tie 1:1 with a statement amou
  name: Paxos Payments API
  slug: paxos-payments-api
- description: Payout groups encapsulate common rewards characteristics. All monitored addresses that reference a payout group accumulate rewards at the same rate and claim to the payout destination specified for th
  name: Paxos Payout Groups API
  slug: paxos-payout-groups-api
- description: 'Pricing provides historical data related to charting of asset prices. Note: Some Pricing API markets may be unavailable for trading.'
  name: Paxos Pricing API
  slug: paxos-pricing-api
- description: Profiles hold asset balances, and every Paxos transaction is on a particular profile. Depending on your integration type, Profiles may be used to reflect both corporate balances or individual user bal
  name: Paxos Profiles API
  slug: paxos-profiles-api
- description: Quote Executions buy or sell assets using a Quote obtained from the [Quotes](#tag/Quotes) flow.
  name: Paxos Quote Executions API
  slug: paxos-quote-executions-api
- description: Quotes are "held rates" offered by Paxos to buy or sell assets at a specific price within a period of time - for example, the option to buy BTC within the next 30 seconds for $8,000. The typical Quote
  name: Paxos Quotes API
  slug: paxos-quotes-api
- description: 'Reward addresses are blockchain addresses registered for reward attribution. Custody Rewards: For EVM chains, Paxos registers these addresses on-chain for reward calculation and accrual in the token c'
  name: Paxos Reward Addresses API
  slug: paxos-reward-addresses-api
- description: Rewards details including current reward rates, next accrual time, lifetime earned amounts, and estimated next accrual. *These endpoints are only relevant for whitelisted Rewards partners.*
  name: Paxos Rewards API
  slug: paxos-rewards-api
- description: The Rewards Statements API from Paxos — 2 operation(s) for rewards statements.
  name: Paxos Rewards Statements API
  slug: paxos-rewards-statements-api
- description: The Sandbox Deposits API from Paxos — 1 operation(s) for sandbox deposits.
  name: Paxos Sandbox Deposits API
  slug: paxos-sandbox-deposits-api
- description: The Sandbox Fiat Transfers API from Paxos — 1 operation(s) for sandbox fiat transfers.
  name: Paxos Sandbox Fiat Transfers API
  slug: paxos-sandbox-fiat-transfers-api
- description: The Sandbox Identity API from Paxos — 4 operation(s) for sandbox identity.
  name: Paxos Sandbox Identity API
  slug: paxos-sandbox-identity-api
- description: 'Use the Settlements API to facilitate simultaneous exchange of pre-funded assets. Automate a variety of use cases that require two-party approval, including net settlement of over-the-counter trades, '
  name: Paxos Settlement API
  slug: paxos-settlement-api
- description: <p>Convert between fiat and stablecoin using <a href="#operation/CreateStablecoinConversion">Create Stablecoin Conversion</a> and check the status of a <a href="#operation/GetStablecoinConversion">sin
  name: Paxos Stablecoin Conversion API
  slug: paxos-stablecoin-conversion-api
- description: A Statement summarizes all eligible stablecoin rewards for a given organization over a fixed time period. It aggregates earned reward types (e.g., custody, mint, acceptance) and records whether the st
  name: Paxos Statements API
  slug: paxos-statements-api
- description: All tax forms are associated to a single account_id. An account_id can have multiple tax forms associated with it. US 1099-B and 1099-Misc tax forms for the previous fiscal year will be available in F
  name: Paxos Tax Forms API
  slug: paxos-tax-forms-api
- description: Each deposit to and withdrawal from a Paxos account is a Transfer. A Transfer is associated with a particular Profile, and increases or decreases the available balance of a single asset in that Profil
  name: Paxos Transfers API
  slug: paxos-transfers-api
- description: The TravelRulePublic API from Paxos — 2 operation(s) for travelrulepublic.
  name: Paxos TravelRulePublic API
  slug: paxos-travelrulepublic-api
artifact_total: 93
asyncapis:
- description: ''
  name: Paxos Webhooks
  slug: paxos-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paxos Account Members API
  slug: open-paxos-account-members-api
- collection_type: open
  name: Paxos Account Members Accounts API
  slug: open-paxos-accounts-api
- collection_type: open
  name: Paxos Account Members Address Verification API
  slug: open-paxos-address-verification-api
- collection_type: open
  name: Paxos Account Members API Credentials API
  slug: open-paxos-api-credentials-api
- collection_type: open
  name: Paxos Account Members Claims API
  slug: open-paxos-claims-api
- collection_type: open
  name: Paxos Account Members Crypto Deposits API
  slug: open-paxos-crypto-deposits-api
- collection_type: open
  name: Paxos Account Members Crypto Withdrawals API
  slug: open-paxos-crypto-withdrawals-api
- collection_type: open
  name: Paxos Account Members Deposit Addresses API
  slug: open-paxos-deposit-addresses-api
- collection_type: open
  name: Paxos Account Members Events API
  slug: open-paxos-events-api
- collection_type: open
  name: Paxos Account Members ExchangePublic API
  slug: open-paxos-exchangepublic-api
- collection_type: open
  name: Paxos Account Members Fees API
  slug: open-paxos-fees-api
- collection_type: open
  name: Paxos Account Members Fiat Transfers API
  slug: open-paxos-fiat-transfers-api
- collection_type: open
  name: Paxos Account Members Identity API
  slug: open-paxos-identity-api
- collection_type: open
  name: Paxos Account Members Identity Controls API
  slug: open-paxos-identity-controls-api
- collection_type: open
  name: Paxos Account Members Identity Documents API
  slug: open-paxos-identity-documents-api
- collection_type: open
  name: Paxos Account Members Institution Members API
  slug: open-paxos-institution-members-api
- collection_type: open
  name: Paxos Account Members Internal Transfers API
  slug: open-paxos-internal-transfers-api
- collection_type: open
  name: Paxos Account Members Issuer Quotes API
  slug: open-paxos-issuer-quotes-api
- collection_type: open
  name: Paxos Account Members Limits API
  slug: open-paxos-limits-api
- collection_type: open
  name: Paxos Account Members Market Data API
  slug: open-paxos-market-data-api
- collection_type: open
  name: Paxos Account Members Monitoring Addresses API
  slug: open-paxos-monitoring-addresses-api
- collection_type: open
  name: Paxos Account Members Orchestration Rules API
  slug: open-paxos-orchestration-rules-api
- collection_type: open
  name: Paxos Account Members Orchestrations API
  slug: open-paxos-orchestrations-api
- collection_type: open
  name: Paxos Account Members Orders API
  slug: open-paxos-orders-api
- collection_type: open
  name: Paxos Account Members Paxos Transfers API
  slug: open-paxos-paxos-transfers-api
- collection_type: open
  name: Paxos Account Members Payments API
  slug: open-paxos-payments-api
- collection_type: open
  name: Paxos Account Members Payout Groups API
  slug: open-paxos-payout-groups-api
- collection_type: open
  name: Paxos Account Members Pricing API
  slug: open-paxos-pricing-api
- collection_type: open
  name: Paxos Account Members Profiles API
  slug: open-paxos-profiles-api
- collection_type: open
  name: Paxos Account Members Quote Executions API
  slug: open-paxos-quote-executions-api
- collection_type: open
  name: Paxos Account Members Quotes API
  slug: open-paxos-quotes-api
- collection_type: open
  name: Paxos Account Members Reward Addresses API
  slug: open-paxos-reward-addresses-api
- collection_type: open
  name: Paxos Account Members Rewards API
  slug: open-paxos-rewards-api
- collection_type: open
  name: Paxos Account Members Rewards Statements API
  slug: open-paxos-rewards-statements-api
- collection_type: open
  name: Paxos Account Members Sandbox Deposits API
  slug: open-paxos-sandbox-deposits-api
- collection_type: open
  name: Paxos Account Members Sandbox Fiat Transfers API
  slug: open-paxos-sandbox-fiat-transfers-api
- collection_type: open
  name: Paxos Account Members Sandbox Identity API
  slug: open-paxos-sandbox-identity-api
- collection_type: open
  name: Paxos Account Members Settlement API
  slug: open-paxos-settlement-api
- collection_type: open
  name: Paxos Account Members Stablecoin Conversion API
  slug: open-paxos-stablecoin-conversion-api
- collection_type: open
  name: Paxos Account Members Statements API
  slug: open-paxos-statements-api
- collection_type: open
  name: Paxos Account Members Tax Forms API
  slug: open-paxos-tax-forms-api
- collection_type: open
  name: Paxos Account Members Transfers API
  slug: open-paxos-transfers-api
- collection_type: open
  name: Paxos Account Members TravelRulePublic API
  slug: open-paxos-travelrulepublic-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paxos-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paxos.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paxos.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paxos.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paxos.com/guides/developer/account
- group: company
  title: ''
  type: Blog
  url: https://paxos.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.paxos.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paxosglobal
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.paxos.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paxos.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.paxos.com/changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.paxos.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paxos.com/terms-and-conditions/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paxos.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/paxos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paxos-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/paxos-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paxos-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paxos-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paxos-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paxos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paxos-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paxos-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paxos-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paxos-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paxos-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paxos-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paxos-v2-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paxos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paxos-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paxos-changelog.yml
- group: company
  title: ''
  type: Website
  url: https://paxos.com
created: '2026-07-17'
description: Paxos is a regulated blockchain and stablecoin infrastructure company that lets enterprises move any asset, any time, through a single API. The Paxos v2 REST/FIX/WebSocket platform covers stablecoin issuance and 1:1 conversion (USDG, PYUSD, USDP, PAXG), crypto brokerage and order-book trading, held-rate quotes, custody, fiat and crypto transfers, identity/KYC and account onboarding, orchestration workflows, rewards, tax forms, and Travel Rule compliance. Authentication is OAuth 2.0 client credentials, errors are RFC 9457 problem+json, and a full sandbox with test tooling is provided. Paxos issues PayPal USD (PYUSD) and the Global Dollar (USDG).
image: https://framerusercontent.com/assets/vwdNglaGheOU0cQGcNuxFH2LUHQ.jpg
layout: provider
mcp_servers:
- description: ''
  name: Paxos MCP Server
  slug: paxos-mcp-server
modified: '2026-07-20'
name: Paxos
nav: Providers
network: true
overview: 'Paxos publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Account Members API, Accounts API, Address Verification API, and 40 more. Tagged areas include Company, Stablecoins, Cryptocurrency, Payments, and Crypto Brokerage.


  The Paxos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paxos'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 26 more developer resources.'
random_paper: 9
scopes:
- name: Paxos Scopes
  scope_count: 66
  slug: paxos-scopes
  summary_line: 66 scopes · clientCredentials
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 63.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paxos/refs/heads/main/screenshots/paxos-2026-08-07T191628.png
security:
- kind: authentication
  name: Paxos Authentication
  slug: paxos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Paxos Domain Security
  slug: paxos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paxos
tags:
- Company
- Stablecoins
- Cryptocurrency
- Payments
- Crypto Brokerage
- Trading
- Custody
- Blockchain
- Financial-Services
- Digital Assets
website: https://paxos.com
---
