---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Grab Agentic Access
  operation_count: 12
  slug: grab-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 19
apis:
- description: Grab ID is Grab's OAuth 2.0 / OpenID Connect identity provider. Partner applications use the Login With Grab flow to authenticate Grab consumers and obtain ID and access tokens scoped to a specific Gr
  name: Login With Grab (Grab ID) API
  slug: grab-id
- description: The GrabFood API lets merchant POS / SaaS partners receive, acknowledge, and fulfill GrabFood orders, manage menus and store status, and surface delivery status to the merchant.
  name: GrabFood API
  slug: grabfood
- description: The GrabMart API supports grocery, convenience, and retail merchants integrating with Grab's on-demand marketplace — including catalog ingestion, store-level inventory, order acknowledgement, and fulf
  name: GrabMart API
  slug: grabmart
- description: GrabExpress is Grab's on-demand same-city courier API for ecommerce, retail, and SaaS partners. Partners create delivery requests, fetch quotes, track couriers in real time, and receive webhook update
  name: GrabExpress API
  slug: grab-express
- description: The Farefeed API exposes ride pricing and supply information to ecosystem partners (e.g. mapping, navigation, planning apps) so they can render Grab fare estimates inline.
  name: Farefeed (Partner Ride Pricing) API
  slug: farefeed
- description: Partner Apps Integration lets third-party applications surface services inside the Grab consumer app via a partner-app framework — covering deep links, in-app activation, and event callbacks.
  name: Partner Apps Integration API
  slug: partner-apps
- description: The Grab For Business Partner API supports corporate travel, expense, and HR platforms that need to provision corporate Grab accounts, set ride policies, and pull employee trip and receipt data for ex
  name: Grab For Business Partner API
  slug: grab-for-business
- description: GrabGifts Integration enables partner platforms to issue and redeem Grab e-gift vouchers — used for employee rewards, customer incentives, and loyalty programs across SEA.
  name: GrabGifts Integration API
  slug: grabgifts
- description: GrabDefence exposes Grab's internal fraud, abuse, and risk evaluation platform as an API for partners — covering device risk scoring, account integrity checks, and transaction risk signals.
  name: GrabDefence Risk Evaluation API
  slug: grab-defence
- description: GrabPay QR exposes both merchant-presented (MPM) and consumer-presented (CPM) QR payment flows for in-store merchants accepting GrabPay across SEA.
  name: GrabPay QR API
  slug: grabpay-qr
- description: The One-Time Charge API supports online merchants charging GrabPay wallets via a redirect or app-to-app handoff checkout flow, with payment success and failure webhook notifications.
  name: GrabPay One-Time Charge API
  slug: grabpay-one-time-charge
- description: Tokenisation lets partner merchants store a customer's GrabPay payment instrument as a reusable token for recurring and one-click checkouts, with PCI-scope reduction.
  name: GrabPay Tokenisation API
  slug: grabpay-tokenisation
- description: The Grab POS API integrates physical point-of-sale terminals with GrabPay for in-store payment acceptance, including transaction lifecycle, refund, and reconciliation flows.
  name: Grab POS API
  slug: grab-pos
- description: The Points Earning and GrabRewards Tier APIs let ecosystem partners award GrabRewards points for qualifying activity and check a user's loyalty tier for tier-based offers.
  name: GrabRewards (Points Earning & Tier) APIs
  slug: grab-rewards
- description: Grab Kios Digital Products API powers digital-goods commerce for Grab Kios agents in Indonesia — covering top-ups for mobile credit, data packages, gaming credits, and digital vouchers.
  name: Grab Kios Digital Products API
  slug: grab-kios-digital-products
- description: The Biller Gateway API lets Grab Kios agents accept bill payments for electricity, water, multifinance, and other Indonesian billers, with inquiry, payment, and reversal operations.
  name: Grab Kios Biller Gateway API
  slug: grab-kios-biller-gateway
- description: The GrabExpress API from Grab — 3 operation(s) for grabexpress.
  name: Grab GrabExpress API
  slug: grab-grabexpress-api
- description: The GrabID API from Grab — 4 operation(s) for grabid.
  name: Grab GrabID API
  slug: grab-grabid-api
- description: The GrabPay API from Grab — 4 operation(s) for grabpay.
  name: Grab GrabPay API
  slug: grab-grabpay-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grab Partner APIs (GrabID, GrabPay, ) GrabExpress API
  slug: open-grab-grabexpress-api
- collection_type: open
  name: Grab Partner APIs (, GrabPay, ) GrabExpress GrabID API
  slug: open-grab-grabid-api
- collection_type: open
  name: Grab Partner APIs (GrabID, , ) GrabExpress GrabPay API
  slug: open-grab-grabpay-api
- collection_type: open
  name: Grab Partner APIs (GrabID, GrabPay, GrabExpress)
  slug: open-grab
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/grab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.grab.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.grab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.grab.com/docs
- group: other
  title: ''
  type: GrabPay
  url: https://www.grab.com/sg/pay/
- group: other
  title: ''
  type: GrabForBusiness
  url: https://business.grab.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.grab.com/sg/press/
- group: other
  title: ''
  type: Sustainability
  url: https://www.grab.com/sg/sustainability/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.grab.com/
- group: company
  title: ''
  type: Careers
  url: https://grab.careers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/grab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grabapp/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.grab.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.grab.com/sg/blog/feed/
created: '2026-05-23'
description: Grab is Southeast Asia's leading on-demand superapp, offering ride-hailing (GrabCar / GrabBike / GrabTaxi), food delivery (GrabFood), package delivery (GrabExpress), grocery and retail (GrabMart), digital payments (GrabPay), financial services (GrabFin), and a B2B / enterprise business unit (Grab for Business). Grab exposes a partner-grade developer platform at developer.grab.com covering ride pricing (Farefeed), delivery (Express, GrabFood, GrabMart), payments (GrabPay QR, One-Time Charge, Tokenisation, Grab POS), identity (Login with Grab), loyalty (GrabRewards / Points / GrabGifts), corporate accounts (Grab for Business), and digital products / bill payments via Grab Kios. The platform is OAuth 2.0 based with partner-issued client credentials.
finops:
- name: Grab Finops
  service_category: API
  slug: grab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grab.png
layout: provider
modified: '2026-05-23'
name: Grab
nav: Providers
network: true
overview: 'Grab publishes 3 APIs on the [APIs.io](https://apis.io/) network: GrabExpress API, GrabID API, and GrabPay API. Tagged areas include Ride Hailing, Food Delivery, Last-Mile Logistics, Digital Payments, and Super App.


  Grab''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Grab Plans Pricing
  plan_count: 1
  slug: grab-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Grab Rate Limits
  slug: grab-rate-limits
score:
  band: thin
  composite: 32.7
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grab/refs/heads/main/screenshots/grab-2026-06-20T182311.png
security:
- kind: authentication
  name: Grab Authentication
  slug: grab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Grab Domain Security
  slug: grab-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Grab Vulnerability Disclosure
  slug: grab-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: grab
tags:
- Ride Hailing
- Food Delivery
- Last-Mile Logistics
- Digital Payments
- Super App
- Southeast Asia
- Identity
- Loyalty
- QR Payments
- Authentication
website: https://www.grab.com/
---
