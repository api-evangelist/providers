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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Goto Gojek Agentic Access
  operation_count: 13
  slug: goto-gojek-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 8
apis:
- description: GoSend is Gojek's on-demand last-mile courier service. The GoSend API lets e-commerce platforms, marketplaces, and ERP systems book GoSend Instant and Same-Day deliveries, fetch quotes, track couriers
  name: GoSend Logistics API
  slug: gosend
- description: GoBiz is the merchant operating platform for restaurants and retailers selling through GoFood and Gojek's on-demand services. Partner POS / SaaS vendors integrate with GoBiz to manage menus, store ava
  name: GoBiz Merchant Platform
  slug: gobiz
- description: GoPay is GoTo Financial's e-money and digital wallet platform in Indonesia. Online and offline merchants integrate via partner payment service providers (e.g. Midtrans, Xendit, DOKU) to accept GoPay f
  name: GoPay Payments API
  slug: gopay
- description: Midtrans is GoTo Financial's payment service provider business in Indonesia. The Midtrans API offers full payment gateway coverage — credit/debit cards, bank transfer (Permata, Mandiri, BCA, BNI), e-w
  name: Midtrans Payment Gateway API
  slug: midtrans
- description: Moka is GoTo Financial's cloud POS for Indonesian SMBs, acquired in 2020. It exposes integration APIs and webhooks for inventory sync, sales reporting, employee management, and customer loyalty progra
  name: Moka POS Platform
  slug: moka-pos
- description: Following GoTo's 2024 divestment of Tokopedia's e-commerce operations to TikTok Shop, integrations for what was formerly the Tokopedia Open API and Mitra Tokopedia developer surface are now served via
  name: Tokopedia / TikTok Shop Open Platform
  slug: tokopedia-tiktok-shop
- description: The Tokenization API from GoTo Group (Gojek + Tokopedia) — 3 operation(s) for tokenization.
  name: GoTo Group (Gojek + Tokopedia) Tokenization API
  slug: goto-gojek-tokenization-api
- description: The Transactions API from GoTo Group (Gojek + Tokopedia) — 10 operation(s) for transactions.
  name: GoTo Group (Gojek + Tokopedia) Transactions API
  slug: goto-gojek-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Midtrans Core API (GoTo Financial)
  slug: open-goto-gojek
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goto-gojek-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goto-gojek-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goto-gojek-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gotocompany.com/
- group: company
  title: ''
  type: GojekWebsite
  url: https://www.gojek.com/
- group: company
  title: ''
  type: TokopediaWebsite
  url: https://www.tokopedia.com/
- group: other
  title: ''
  type: GoToFinancial
  url: https://www.gotofinancial.com/
- group: other
  title: ''
  type: GoSend
  url: https://www.gojek.com/en-id/gosend/
- group: other
  title: ''
  type: GoBiz
  url: https://gobiz.co.id/
- group: other
  title: ''
  type: GoPay
  url: https://gopay.co.id/
- group: other
  title: ''
  type: Midtrans
  url: https://midtrans.com/
- group: docs
  title: ''
  type: MidtransDocs
  url: https://docs.midtrans.com/
- group: other
  title: ''
  type: MokaPOS
  url: https://www.mokapos.com/
- group: company
  title: ''
  type: TikTokShopPartner
  url: https://partner.tiktokshop.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.gotocompany.com/investor-relations
- group: company
  title: ''
  type: Newsroom
  url: https://www.gotocompany.com/newsroom
- group: other
  title: ''
  type: Sustainability
  url: https://www.gotocompany.com/sustainability
- group: company
  title: ''
  type: Careers
  url: https://www.gotocompany.com/careers
- group: build
  title: ''
  type: GitHubGojek
  url: https://github.com/gojek
- group: build
  title: ''
  type: GitHubTokopedia
  url: https://github.com/tokopedia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gotocompany/
created: '2026-05-23'
description: 'GoTo Group (PT GoTo Gojek Tokopedia Tbk) is Indonesia''s largest digital ecosystem, formed by the 2021 merger of ride-hailing / on-demand superapp Gojek and e-commerce marketplace Tokopedia. It operates three business pillars: On-Demand Services (Gojek — ride hailing GoRide / GoCar, food delivery GoFood, parcel delivery GoSend, logistics GoBox, courier GoSend), E-Commerce (Tokopedia marketplace and Mitra Tokopedia), and Financial Technology (GoTo Financial — GoPay, GoPayLater, GoInvestasi). In 2024 GoTo divested Tokopedia''s e-commerce operations to TikTok Shop / ByteDance, retaining a 25% stake in the combined Tokopedia–TikTok Shop entity; the developer.tokopedia.com portal now redirects to TikTok Shop''s partner platform. GoTo continues to operate Gojek and GoTo Financial directly. There is no single GoTo group-wide developer portal — partner integrations happen at the product level (Gojek partner programs, GoPay PSP integrations, TikTok Shop Open Platform for the former
  Tokopedia surface).'
finops:
- name: Goto Gojek Finops
  service_category: API
  slug: goto-gojek-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goto-gojek.png
layout: provider
modified: '2026-05-23'
name: GoTo Group (Gojek + Tokopedia)
nav: Providers
network: true
overview: 'GoTo Group (Gojek + Tokopedia) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tokenization API and Transactions API. Tagged areas include Superapp, Ride Hailing, Food Delivery, Last-Mile Logistics, and E-commerce.


  GoTo Group (Gojek + Tokopedia)''s developer surface includes authentication and 20 more developer resources.'
plans:
- name: Goto Gojek Plans Pricing
  plan_count: 1
  slug: goto-gojek-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Goto Gojek Rate Limits
  slug: goto-gojek-rate-limits
score:
  band: thin
  composite: 30.6
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goto-gojek/refs/heads/main/screenshots/goto-gojek-2026-06-20T182257.png
security:
- kind: authentication
  name: Goto Gojek Authentication
  slug: goto-gojek-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Goto Gojek Domain Security
  slug: goto-gojek-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: goto-gojek
tags:
- Superapp
- Ride Hailing
- Food Delivery
- Last-Mile Logistics
- E-commerce
- Digital Payments
- Indonesia
- Southeast Asia
- Gojek
- Tokopedia
website: https://www.gotocompany.com/
---
