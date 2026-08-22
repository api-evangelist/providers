---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 132
  human_in_the_loop: 1
  name: Increase Agentic Access
  operation_count: 238
  slug: increase-agentic-access
  summary_line: 238 operations · 132 acting · 1 human-in-the-loop
api_count: 56
apis:
- description: Each account can have multiple account and routing numbers. We recommend that you use a set per vendor. This is similar to how you use different passwords for different websites. Account numbers can a
  name: Increase Account Numbers API
  slug: increase-account-numbers-api
- description: Account Statements are generated monthly for every active Account. You can access the statement's data via the API or retrieve a PDF with its details via its associated File.
  name: Increase Account Statements API
  slug: increase-account-statements-api
- description: Account transfers move funds between your own accounts at Increase (accounting systems often refer to these as Book Transfers). Account Transfers are free and synchronous. Upon creation they create tw
  name: Increase Account Transfers API
  slug: increase-account-transfers-api
- description: Accounts are your bank accounts with Increase. They store money, receive transfers, and send payments. They earn interest and have depository insurance.
  name: Increase Accounts API
  slug: increase-accounts-api
- description: The Ach Prenotifications API from Increase — 2 operation(s) for ach prenotifications.
  name: Increase Ach Prenotifications API
  slug: increase-ach-prenotifications-api
- description: The Ach Transfers API from Increase — 4 operation(s) for ach transfers.
  name: Increase Ach Transfers API
  slug: increase-ach-transfers-api
- description: If unauthorized activity occurs on a card, you can create a Card Dispute and we'll work with the card networks to return the funds if appropriate.
  name: Increase Card Disputes API
  slug: increase-card-disputes-api
- description: Card Payments group together interactions related to a single card payment, such as an authorization and its corresponding settlement.
  name: Increase Card Payments API
  slug: increase-card-payments-api
- description: Additional information about a card purchase (e.g., settlement or refund), such as level 3 line item data.
  name: Increase Card Purchase Supplements API
  slug: increase-card-purchase-supplements-api
- description: Card Push Transfers send funds to a recipient's payment card in real-time.
  name: Increase Card Push Transfers API
  slug: increase-card-push-transfers-api
- description: Card Tokens represent a tokenized card number that can be used for Card Push Transfers and Card Validations.
  name: Increase Card Tokens API
  slug: increase-card-tokens-api
- description: Card Validations are used to validate a card and its cardholder before sending funds to or pulling funds from a card.
  name: Increase Card Validations API
  slug: increase-card-validations-api
- description: 'Cards may operate on credit, debit, or prepaid BINs. They’ll immediately work for online purchases after you create them. All cards work on a good funds model, and maintain a maximum limit of 100% of '
  name: Increase Cards API
  slug: increase-cards-api
- description: Check Deposits allow you to deposit images of paper checks into your account.
  name: Increase Check Deposits API
  slug: increase-check-deposits-api
- description: Check Transfers move funds from your Increase account by mailing a physical check.
  name: Increase Check Transfers API
  slug: increase-check-transfers-api
- description: Declined Transactions are refused additions and removals of money from your bank account. For example, Declined Transactions are caused when your Account has an insufficient balance or your Limits are
  name: Increase Declined Transactions API
  slug: increase-declined-transactions-api
- description: This contains artwork and metadata relating to a Card's appearance in digital wallet apps like Apple Pay and Google Pay. For more information, see our guide on [digital card artwork](https://increase.
  name: Increase Digital Card Profiles API
  slug: increase-digital-card-profiles-api
- description: A Digital Wallet Token is created when a user adds a Card to their Apple Pay or Google Pay app. The Digital Wallet Token can be used for purchases just like a Card.
  name: Increase Digital Wallet Tokens API
  slug: increase-digital-wallet-tokens-api
- description: Entities are the legal entities that own accounts. They can be people, corporations, partnerships, government authorities, or trusts. To learn more, see [Entities](/documentation/entities).
  name: Increase Entities API
  slug: increase-entities-api
- description: The Entity Beneficial Owners API from Increase — 3 operation(s) for entity beneficial owners.
  name: Increase Entity Beneficial Owners API
  slug: increase-entity-beneficial-owners-api
- description: Entity Onboarding Sessions let your customers onboard themselves by completing Increase-hosted forms. Create a session and redirect your customer to the returned URL. When they're done, they'll be red
  name: Increase Entity Onboarding Sessions API
  slug: increase-entity-onboarding-sessions-api
- description: The Entity Supplemental Documents API from Increase — 1 operation(s) for entity supplemental documents.
  name: Increase Entity Supplemental Documents API
  slug: increase-entity-supplemental-documents-api
- description: Webhooks are event notifications we send to you by HTTPS POST requests. Event Subscriptions are how you configure your application to listen for them. You can create an Event Subscription through your
  name: Increase Event Subscriptions API
  slug: increase-event-subscriptions-api
- description: Events are records of things that happened to objects at Increase. Events are accessible via the List Events endpoint and can be delivered to your application via webhooks. For more information, see o
  name: Increase Events API
  slug: increase-events-api
- description: 'Exports are generated files. Some exports can contain a lot of data, like a CSV of your transactions. Others can be a single document, like a tax form. Since they can take a while, they are generated '
  name: Increase Exports API
  slug: increase-exports-api
- description: External Accounts represent accounts at financial institutions other than Increase. You can use this API to store their details for reuse.
  name: Increase External Accounts API
  slug: increase-external-accounts-api
- description: The Fednow Transfers API from Increase — 4 operation(s) for fednow transfers.
  name: Increase Fednow Transfers API
  slug: increase-fednow-transfers-api
- description: File Links let you generate a URL that can be used to download a File.
  name: Increase File Links API
  slug: increase-file-links-api
- description: Files are objects that represent a file hosted on Increase's servers. The file may have been uploaded by you (for example, when uploading a check image) or it may have been created by Increase (for ex
  name: Increase Files API
  slug: increase-files-api
- description: Groups represent organizations using Increase. You can retrieve information about your own organization via the API. More commonly, OAuth platforms can retrieve information about the organizations tha
  name: Increase Groups API
  slug: increase-groups-api
- description: The Inbound Ach Transfers API from Increase — 5 operation(s) for inbound ach transfers.
  name: Increase Inbound Ach Transfers API
  slug: increase-inbound-ach-transfers-api
- description: Inbound Check Deposits are records of third-parties attempting to deposit checks against your account.
  name: Increase Inbound Check Deposits API
  slug: increase-inbound-check-deposits-api
- description: The Inbound Fednow Transfers API from Increase — 2 operation(s) for inbound fednow transfers.
  name: Increase Inbound Fednow Transfers API
  slug: increase-inbound-fednow-transfers-api
- description: Inbound Mail Items represent pieces of physical mail delivered to a Lockbox Address.
  name: Increase Inbound Mail Items API
  slug: increase-inbound-mail-items-api
- description: The Inbound Real Time Payments Transfers API from Increase — 2 operation(s) for inbound real time payments transfers.
  name: Increase Inbound Real Time Payments Transfers API
  slug: increase-inbound-real-time-payments-transfers-api
- description: Inbound wire drawdown requests are requests from someone else to send them a wire. For more information, see our [Wire Drawdown Requests documentation](/documentation/wire-drawdown-requests).
  name: Increase Inbound Wire Drawdown Requests API
  slug: increase-inbound-wire-drawdown-requests-api
- description: An Inbound Wire Transfer is a wire transfer initiated outside of Increase to your account.
  name: Increase Inbound Wire Transfers API
  slug: increase-inbound-wire-transfers-api
- description: The Intrafi Account Enrollments API from Increase — 3 operation(s) for intrafi account enrollments.
  name: Increase Intrafi Account Enrollments API
  slug: increase-intrafi-account-enrollments-api
- description: The Intrafi Exclusions API from Increase — 3 operation(s) for intrafi exclusions.
  name: Increase Intrafi Exclusions API
  slug: increase-intrafi-exclusions-api
- description: Lockbox Addresses are physical locations that can receive mail containing paper checks.
  name: Increase Lockbox Addresses API
  slug: increase-lockbox-addresses-api
- description: Lockbox Recipients represent an inbox at a Lockbox Address. Checks received for a Lockbox Recipient are deposited into its associated Account.
  name: Increase Lockbox Recipients API
  slug: increase-lockbox-recipients-api
- description: The Oauth API from Increase — 1 operation(s) for oauth.
  name: Increase Oauth API
  slug: increase-oauth-api
- description: The Oauth Applications API from Increase — 2 operation(s) for oauth applications.
  name: Increase Oauth Applications API
  slug: increase-oauth-applications-api
- description: The Oauth Connections API from Increase — 2 operation(s) for oauth connections.
  name: Increase Oauth Connections API
  slug: increase-oauth-connections-api
- description: Pending Transactions are potential future additions and removals of money from your bank account. They impact your available balance, but not your current balance. To learn more, see [Transactions and
  name: Increase Pending Transactions API
  slug: increase-pending-transactions-api
- description: This contains artwork and metadata relating to a Physical Card's appearance. For more information, see our guide on [physical card artwork](https://increase.com/documentation/card-art-physical-cards).
  name: Increase Physical Card Profiles API
  slug: increase-physical-card-profiles-api
- description: Custom physical Visa cards that are shipped to your customers. The artwork is configurable by a connected [Card Profile](/documentation/api#card-profiles). The same Card can be used for multiple Physi
  name: Increase Physical Cards API
  slug: increase-physical-cards-api
- description: Programs determine the compliance and commercial terms of Accounts. By default, you have a Commercial Banking program for managing your own funds. If you are lending or managing funds on behalf of you
  name: Increase Programs API
  slug: increase-programs-api
- description: The Real Time Decisions API from Increase — 2 operation(s) for real time decisions.
  name: Increase Real Time Decisions API
  slug: increase-real-time-decisions-api
- description: The Real Time Payments Transfers API from Increase — 4 operation(s) for real time payments transfers.
  name: Increase Real Time Payments Transfers API
  slug: increase-real-time-payments-transfers-api
- description: Routing numbers are used to identify your bank in a financial transaction.
  name: Increase Routing Numbers API
  slug: increase-routing-numbers-api
- description: The Simulations API from Increase — 48 operation(s) for simulations.
  name: Increase Simulations API
  slug: increase-simulations-api
- description: Swift Transfers send funds internationally.
  name: Increase Swift Transfers API
  slug: increase-swift-transfers-api
- description: Transactions are the immutable additions and removals of money from your bank account. They're the equivalent of line items on your bank statement. To learn more, see [Transactions and Transfers](/doc
  name: Increase Transactions API
  slug: increase-transactions-api
- description: 'Wire drawdown requests enable you to request that someone else send you a wire. Because there is nuance to making sure your counterparty''s bank processes these correctly, we ask that you reach out to '
  name: Increase Wire Drawdown Requests API
  slug: increase-wire-drawdown-requests-api
- description: Wire transfers move funds between your Increase account and any other account accessible by Fedwire.
  name: Increase Wire Transfers API
  slug: increase-wire-transfers-api
artifact_total: 121
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Increase Account Numbers API
  slug: open-increase-account-numbers-api
- collection_type: open
  name: Increase Account Numbers Account Statements API
  slug: open-increase-account-statements-api
- collection_type: open
  name: Increase Account Numbers Account Transfers API
  slug: open-increase-account-transfers-api
- collection_type: open
  name: Increase Account Numbers Accounts API
  slug: open-increase-accounts-api
- collection_type: open
  name: Increase Account Numbers Ach Prenotifications API
  slug: open-increase-ach-prenotifications-api
- collection_type: open
  name: Increase Account Numbers Ach Transfers API
  slug: open-increase-ach-transfers-api
- collection_type: open
  name: Increase Account Numbers Card Disputes API
  slug: open-increase-card-disputes-api
- collection_type: open
  name: Increase Account Numbers Card Payments API
  slug: open-increase-card-payments-api
- collection_type: open
  name: Increase Account Numbers Card Purchase Supplements API
  slug: open-increase-card-purchase-supplements-api
- collection_type: open
  name: Increase Account Numbers Card Push Transfers API
  slug: open-increase-card-push-transfers-api
- collection_type: open
  name: Increase Account Numbers Card Tokens API
  slug: open-increase-card-tokens-api
- collection_type: open
  name: Increase Account Numbers Card Validations API
  slug: open-increase-card-validations-api
- collection_type: open
  name: Increase Account Numbers Cards API
  slug: open-increase-cards-api
- collection_type: open
  name: Increase Account Numbers Check Deposits API
  slug: open-increase-check-deposits-api
- collection_type: open
  name: Increase Account Numbers Check Transfers API
  slug: open-increase-check-transfers-api
- collection_type: open
  name: Increase Account Numbers Declined Transactions API
  slug: open-increase-declined-transactions-api
- collection_type: open
  name: Increase Account Numbers Digital Card Profiles API
  slug: open-increase-digital-card-profiles-api
- collection_type: open
  name: Increase Account Numbers Digital Wallet Tokens API
  slug: open-increase-digital-wallet-tokens-api
- collection_type: open
  name: Increase Account Numbers Entities API
  slug: open-increase-entities-api
- collection_type: open
  name: Increase Account Numbers Entity Beneficial Owners API
  slug: open-increase-entity-beneficial-owners-api
- collection_type: open
  name: Increase Account Numbers Entity Onboarding Sessions API
  slug: open-increase-entity-onboarding-sessions-api
- collection_type: open
  name: Increase Account Numbers Entity Supplemental Documents API
  slug: open-increase-entity-supplemental-documents-api
- collection_type: open
  name: Increase Account Numbers Event Subscriptions API
  slug: open-increase-event-subscriptions-api
- collection_type: open
  name: Increase Account Numbers Events API
  slug: open-increase-events-api
- collection_type: open
  name: Increase Account Numbers Exports API
  slug: open-increase-exports-api
- collection_type: open
  name: Increase Account Numbers External Accounts API
  slug: open-increase-external-accounts-api
- collection_type: open
  name: Increase Account Numbers Fednow Transfers API
  slug: open-increase-fednow-transfers-api
- collection_type: open
  name: Increase Account Numbers File Links API
  slug: open-increase-file-links-api
- collection_type: open
  name: Increase Account Numbers Files API
  slug: open-increase-files-api
- collection_type: open
  name: Increase Account Numbers Groups API
  slug: open-increase-groups-api
- collection_type: open
  name: Increase Account Numbers Inbound Ach Transfers API
  slug: open-increase-inbound-ach-transfers-api
- collection_type: open
  name: Increase Account Numbers Inbound Check Deposits API
  slug: open-increase-inbound-check-deposits-api
- collection_type: open
  name: Increase Account Numbers Inbound Fednow Transfers API
  slug: open-increase-inbound-fednow-transfers-api
- collection_type: open
  name: Increase Account Numbers Inbound Mail Items API
  slug: open-increase-inbound-mail-items-api
- collection_type: open
  name: Increase Account Numbers Inbound Real Time Payments Transfers API
  slug: open-increase-inbound-real-time-payments-transfers-api
- collection_type: open
  name: Increase Account Numbers Inbound Wire Drawdown Requests API
  slug: open-increase-inbound-wire-drawdown-requests-api
- collection_type: open
  name: Increase Account Numbers Inbound Wire Transfers API
  slug: open-increase-inbound-wire-transfers-api
- collection_type: open
  name: Increase Account Numbers Intrafi Account Enrollments API
  slug: open-increase-intrafi-account-enrollments-api
- collection_type: open
  name: Increase Account Numbers Intrafi Exclusions API
  slug: open-increase-intrafi-exclusions-api
- collection_type: open
  name: Increase Account Numbers Lockbox Addresses API
  slug: open-increase-lockbox-addresses-api
- collection_type: open
  name: Increase Account Numbers Lockbox Recipients API
  slug: open-increase-lockbox-recipients-api
- collection_type: open
  name: Increase Account Numbers Oauth API
  slug: open-increase-oauth-api
- collection_type: open
  name: Increase Account Numbers Oauth Applications API
  slug: open-increase-oauth-applications-api
- collection_type: open
  name: Increase Account Numbers Oauth Connections API
  slug: open-increase-oauth-connections-api
- collection_type: open
  name: Increase Account Numbers Pending Transactions API
  slug: open-increase-pending-transactions-api
- collection_type: open
  name: Increase Account Numbers Physical Card Profiles API
  slug: open-increase-physical-card-profiles-api
- collection_type: open
  name: Increase Account Numbers Physical Cards API
  slug: open-increase-physical-cards-api
- collection_type: open
  name: Increase Account Numbers Programs API
  slug: open-increase-programs-api
- collection_type: open
  name: Increase Account Numbers Real Time Decisions API
  slug: open-increase-real-time-decisions-api
- collection_type: open
  name: Increase Account Numbers Real Time Payments Transfers API
  slug: open-increase-real-time-payments-transfers-api
- collection_type: open
  name: Increase Account Numbers Routing Numbers API
  slug: open-increase-routing-numbers-api
- collection_type: open
  name: Increase Account Numbers Simulations API
  slug: open-increase-simulations-api
- collection_type: open
  name: Increase Account Numbers Swift Transfers API
  slug: open-increase-swift-transfers-api
- collection_type: open
  name: Increase Account Numbers Transactions API
  slug: open-increase-transactions-api
- collection_type: open
  name: Increase Account Numbers Wire Drawdown Requests API
  slug: open-increase-wire-drawdown-requests-api
- collection_type: open
  name: Increase Account Numbers Wire Transfers API
  slug: open-increase-wire-transfers-api
- collection_type: open
  name: Increase API
  slug: open-increase
common:
- group: start
  title: ''
  type: Sandbox
  url: https://increase.com/documentation/sandbox
- group: docs
  title: ''
  type: APIReference
  url: https://increase.com/documentation/api/overview
- group: auth
  title: ''
  type: Security
  url: https://increase.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://increase.com/documentation/compliance-overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.increase.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://increase.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://increase.com/terms
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/increase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/increase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/increase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/increase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Increase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/increasebank
- group: company
  title: ''
  type: Website
  url: https://increase.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/increase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/increase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/increase-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://increase.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://increase.com/updates.xml
created: '2026-05-08'
description: Increase is a banking and payments API providing direct ACH, wire, RTP, FedNow, check, and card programs. Bank-direct connectivity (no aggregator middle layer).
finops:
- name: Increase Finops
  service_category: Fintech
  slug: increase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/increase.png
layout: provider
modified: '2026-05-08'
name: Increase
nav: Providers
network: true
overview: 'Increase publishes 56 APIs on the [APIs.io](https://apis.io/) network, including Account Numbers API, Account Statements API, Account Transfers API, and 53 more. Tagged areas include Fintech, Banking, Payments, ACH, and Wires.


  Increase''s developer surface includes sandbox, API reference, authentication, engineering blog, and 15 more developer resources.'
plans:
- name: Increase Plans Pricing
  plan_count: 1
  slug: increase-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Increase Rate Limits
  slug: increase-rate-limits
score:
  band: developing
  composite: 40.1
  delta: 0.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/increase/refs/heads/main/screenshots/increase-2026-06-20T183309.png
security:
- kind: authentication
  name: Increase Authentication
  slug: increase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Increase Domain Security
  slug: increase-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Increase Vulnerability Disclosure
  slug: increase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: increase
tags:
- Fintech
- Banking
- Payments
- ACH
- Wires
website: https://increase.com/
---
