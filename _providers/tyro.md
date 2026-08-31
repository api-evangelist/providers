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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Tyro Agentic Access
  operation_count: 57
  slug: tyro-agentic-access
  summary_line: 57 operations · 26 acting
api_count: 13
apis:
- description: The Bookings API from Tyro Payments — 2 operation(s) for bookings.
  name: Tyro Payments Bookings API
  slug: tyro-bookings-api
- description: The Connections API from Tyro Payments — 1 operation(s) for connections.
  name: Tyro Payments Connections API
  slug: tyro-connections-api
- description: The Locations API from Tyro Payments — 2 operation(s) for locations.
  name: Tyro Payments Locations API
  slug: tyro-locations-api
- description: The Loyalty API from Tyro Payments — 1 operation(s) for loyalty.
  name: Tyro Payments Loyalty API
  slug: tyro-loyalty-api
- description: The Member API from Tyro Payments — 1 operation(s) for member.
  name: Tyro Payments Member API
  slug: tyro-member-api
- description: The Menus API from Tyro Payments — 2 operation(s) for menus.
  name: Tyro Payments Menus API
  slug: tyro-menus-api
- description: The Merchants API from Tyro Payments — 7 operation(s) for merchants.
  name: Tyro Payments Merchants API
  slug: tyro-merchants-api
- description: The Onboarding API from Tyro Payments — 1 operation(s) for onboarding.
  name: Tyro Payments Onboarding API
  slug: tyro-onboarding-api
- description: The Orders API from Tyro Payments — 2 operation(s) for orders.
  name: Tyro Payments Orders API
  slug: tyro-orders-api
- description: The Pay Methods API from Tyro Payments — 2 operation(s) for pay methods.
  name: Tyro Payments Pay Methods API
  slug: tyro-pay-methods-api
- description: The Pay Refunds API from Tyro Payments — 2 operation(s) for pay refunds.
  name: Tyro Payments Pay Refunds API
  slug: tyro-pay-refunds-api
- description: The Pay Requests API from Tyro Payments — 4 operation(s) for pay requests.
  name: Tyro Payments Pay Requests API
  slug: tyro-pay-requests-api
- description: The Payments API from Tyro Payments — 1 operation(s) for payments.
  name: Tyro Payments Payments API
  slug: tyro-payments-api
- description: The Readers API from Tyro Payments — 2 operation(s) for readers.
  name: Tyro Payments Readers API
  slug: tyro-readers-api
- description: The Referrals API from Tyro Payments — 2 operation(s) for referrals.
  name: Tyro Payments Referrals API
  slug: tyro-referrals-api
- description: The Refunds API from Tyro Payments — 1 operation(s) for refunds.
  name: Tyro Payments Refunds API
  slug: tyro-refunds-api
- description: The Registered Card API from Tyro Payments — 1 operation(s) for registered card.
  name: Tyro Payments Registered Card API
  slug: tyro-registered-card-api
- description: The Reporting API from Tyro Payments — 2 operation(s) for reporting.
  name: Tyro Payments Reporting API
  slug: tyro-reporting-api
- description: The Sales API from Tyro Payments — 2 operation(s) for sales.
  name: Tyro Payments Sales API
  slug: tyro-sales-api
- description: The Tables API from Tyro Payments — 2 operation(s) for tables.
  name: Tyro Payments Tables API
  slug: tyro-tables-api
- description: The Transactions API from Tyro Payments — 2 operation(s) for transactions.
  name: Tyro Payments Transactions API
  slug: tyro-transactions-api
artifact_total: 39
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
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-pay-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-pos-pay-terminal-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-pos-embedded-payments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-booking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-ordering-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-menu-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-tables-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-sales-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-loyalty-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-refunds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-locations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tyro-connect-referrals-overlay.yaml
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
  name: Tyro Payments MCP Server
  slug: tyro-payments-mcp-server
modified: '2026-07-24'
name: Tyro Payments
nav: Providers
network: true
overview: 'Tyro Payments publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Connections API, Locations API, and 18 more. Tagged areas include Payments, Australia, Merchant Acquiring, Payment Gateway, and In-Person Payments.


  The Tyro Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tyro Payments'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 39 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 67.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 42.9
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Point-of-Sale
- Online Payments
- Tap to Pay
website: https://www.tyro.com/
---
