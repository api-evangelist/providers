---
access_model:
  confidence: medium
  label: Paid · Partner onboarding (sandbox available)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - documentation
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Tyro Agentic Access
  operation_count: 57
  slug: tyro-agentic-access
  summary_line: 57 operations · 26 acting
api_count: 13
apis:
- description: 'Server-side companion to Tyro.js and the Tyro mobile SDKs for accepting online card payments on the web and in apps. Manages pay requests, saved pay methods (tokenization), and refunds, including 3-D '
  name: Tyro Connect Pay API
  slug: tyro-connect-pay-api
- description: Cloud API that lets a Point of Sale send payment and refund requests to Tyro EFTPOS terminals in-store, pairing a POS to merchant terminals and driving card-present transactions over Tyro's merchant-a
  name: Tyro Pay Terminal API
  slug: tyro-pos-pay-terminal-api
- description: Backend API supporting Tyro's Tap to Pay on iPhone and Android SDKs (SoftPOS), letting POS partners onboard merchants, manage device connections, and process card-present transactions and refunds dire
  name: Tyro Embedded Payments API
  slug: tyro-pos-embedded-payments-api
- description: Exchanges booking and reservation information between reservation apps and Point of Sale systems in the Tyro Connect hospitality network, syncing seating bookings and reflecting bill-driven status cha
  name: Tyro Connect Booking API
  slug: tyro-connect-booking-api
- description: Sends food and retail orders from app partners into merchant Point of Sale systems across the Tyro Connect network, with order lifecycle status tracked back to the originating application.
  name: Tyro Connect Ordering API
  slug: tyro-connect-ordering-api
- description: Synchronises published menu and catalogue data from merchant Point of Sale systems to app partners in the Tyro Connect network, so ordering and delivery apps present the merchant's current menu.
  name: Tyro Connect Menu API
  slug: tyro-connect-menu-api
- description: Reads and manages table (floor-plan) information from merchant Point of Sale systems, underpinning pay-at-table and table-service workflows across the Tyro Connect hospitality network.
  name: Tyro Connect Tables Management API
  slug: tyro-connect-tables-api
- description: Exposes itemised sales transaction data captured from merchant Point of Sale systems, letting app partners build reporting, analytics, accounting and reconciliation tools over Tyro Connect merchant ac
  name: Tyro Connect Sales Data API
  slug: tyro-connect-sales-api
- description: Provides merchant settlement and transaction reporting for Tyro-acquired payments, returning settlement batches and dated transaction listings for reconciliation and financial reporting by app partner
  name: Tyro Connect Reporting API
  slug: tyro-connect-reporting-api
- description: Connects loyalty and rewards providers to Tyro merchants, managing loyalty members, activities and card-linked registrations so points and rewards can be applied at the Point of Sale and payment termi
  name: Tyro Connect Loyalty Data API
  slug: tyro-connect-loyalty-api
- description: Searches prior Tyro transactions and issues refunds against them, giving app and POS partners a dedicated search-and-refund flow over Tyro-acquired merchant payments.
  name: Tyro Connect Refunds API
  slug: tyro-connect-refunds-api
- description: Returns merchant location details keyed by Tyro Connect location identifier, used by partners to resolve and validate the merchant sites they are integrated with across the network.
  name: Tyro Connect Location API
  slug: tyro-connect-locations-api
- description: Lets partners submit and track merchant referrals into Tyro, supporting partner-driven merchant acquisition and onboarding workflows within the Tyro Connect ecosystem.
  name: Tyro Connect Referrals API
  slug: tyro-connect-referrals-api
artifact_total: 31
asyncapis:
- description: ''
  name: Tyro Webhooks
  slug: tyro-webhooks
collections:
- collection_type: open
  name: Booking API
  slug: open-tyro-connect-booking
- collection_type: open
  name: Location API
  slug: open-tyro-connect-locations
- collection_type: open
  name: Loyalty Data API
  slug: open-tyro-connect-loyalty
- collection_type: open
  name: Menu API
  slug: open-tyro-connect-menu
- collection_type: open
  name: Ordering API for App Partners
  slug: open-tyro-connect-ordering
- collection_type: open
  name: Pay API
  slug: open-tyro-connect-pay
- collection_type: open
  name: Referrals API
  slug: open-tyro-connect-referrals
- collection_type: open
  name: Refunds API
  slug: open-tyro-connect-refunds
- collection_type: open
  name: Reporting API
  slug: open-tyro-connect-reporting
- collection_type: open
  name: Sales Data API
  slug: open-tyro-connect-sales
- collection_type: open
  name: Table API
  slug: open-tyro-connect-tables
- collection_type: open
  name: Embedded Payments API
  slug: open-tyro-pos-embedded-payments
- collection_type: open
  name: Pay Terminal API
  slug: open-tyro-pos-pay-terminal
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tyro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tyro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tyro-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tyro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tyro.com/resources/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.connect.tyro.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.connect.tyro.com/app/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connect.tyro.com/app/authentication
- group: auth
  title: ''
  type: Authentication
  url: https://docs.connect.tyro.com/app/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.connect.tyro.com/app/webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tyro
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tyro.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tyro.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.tyro.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.tyro.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tyro.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tyro.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.tyro.com/security/
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/tyro-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tyro-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tyro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tyro-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/tyro-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tyro-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tyro-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tyro-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/tyro-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tyro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tyro-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tyro-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tyro-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tyro-llms.txt
created: '2026-07-24'
description: 'Tyro Payments is an ASX-listed Australian payments company and one of the country''s largest merchant acquirers outside the major banks, holding its own banking licence. Founded in 2003, Tyro provides EFTPOS terminals, in-person and online card acceptance, and integrated payments for more than 70,000 Australian merchants across hospitality, retail and health. Its developer surface, Tyro Connect, is a genuinely API-first platform: a REST API family (served from https://api.tyro.com/connect and secured with OpenID Connect / OAuth 2.0) that links Point of Sale software, ordering, booking, loyalty and reporting apps to Tyro merchants, alongside Tyro.js, mobile SDKs and Tap to Pay (SoftPOS) for card-present and online payments. Home market is Australia.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: tyro-mcp.yml
  slug: tyro-mcpyml
modified: '2026-07-24'
name: Tyro Payments
nav: Providers
network: true
overview: 'Tyro Payments publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Tyro Connect Pay API, Tyro Pay Terminal API, Tyro Embedded Payments API, and 10 more. Tagged areas include Payments, Australia, Merchant Acquiring, Payment Gateway, and In-Person Payments.


  The Tyro Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tyro Payments'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 26 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 46.0
  delta: -6.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 67.2
    developer_ergonomics: 49.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tyro/refs/heads/main/screenshots/tyro-2026-08-17T082516.png
security:
- kind: authentication
  name: Tyro Authentication
  slug: tyro-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Tyro Domain Security
  slug: tyro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tyro
tags:
- Payments
- Australia
- Merchant Acquiring
- Payment Gateway
- In-Person Payments
- EFTPOS
- Point of Sale
- Online Payments
- Tap to Pay
website: https://www.tyro.com/
---
