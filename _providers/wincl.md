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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 127
  human_in_the_loop: 1
  name: Wincl Agentic Access
  operation_count: 271
  slug: wincl-agentic-access
  summary_line: 271 operations · 127 acting · 1 human-in-the-loop
api_count: 44
apis:
- description: Admin Controller
  name: WinCL Admin API
  slug: wincl-admin-api
- description: Admin Auth Controller
  name: WinCL Admin Auth API
  slug: wincl-admin-auth-api
- description: Admin Faq Controller
  name: WinCL Admin FAQ API
  slug: wincl-admin-faq-api
- description: Admin Hedera Controller
  name: WinCL Admin Hedera API
  slug: wincl-admin-hedera-api
- description: Admin Info Controller
  name: WinCL Admin Info API
  slug: wincl-admin-info-api
- description: Admin News Controller
  name: WinCL Admin News API
  slug: wincl-admin-news-api
- description: Admin Notice Controller
  name: WinCL Admin Notice API
  slug: wincl-admin-notice-api
- description: Admin Order Controller
  name: WinCL Admin Order API
  slug: wincl-admin-order-api
- description: 결제 완료된 건을 관리자가 환불
  name: WinCL Admin Payment API
  slug: wincl-admin-payment-api
- description: Admin Product Controller
  name: WinCL Admin Product API
  slug: wincl-admin-product-api
- description: Admin Project Controller
  name: WinCL Admin Project API
  slug: wincl-admin-project-api
- description: Admin Qna Controller
  name: WinCL Admin QnA API
  slug: wincl-admin-qna-api
- description: Admin Reward Program Controller
  name: WinCL Admin Reward API
  slug: wincl-admin-reward-api
- description: Admin Smart Contract Controller
  name: WinCL Admin Smart Contract API
  slug: wincl-admin-smart-contract-api
- description: 가입자 목록 조회
  name: WinCL Admin User API
  slug: wincl-admin-user-api
- description: Admin Utils Controller
  name: WinCL Admin Utils API
  slug: wincl-admin-utils-api
- description: Admin Wallet Controller
  name: WinCL Admin Wallet API
  slug: wincl-admin-wallet-api
- description: B 2 B Store Controller
  name: WinCL APIs for the B2B service (ex. Bespin) API
  slug: wincl-apis-for-the-b2b-service-ex-bespin-api
- description: Auth Controller
  name: WinCL Auth API
  slug: wincl-auth-api
- description: Certificate Box Controller
  name: WinCL CertificateBox API
  slug: wincl-certificatebox-api
- description: Coupon Controller
  name: WinCL Coupon API
  slug: wincl-coupon-api
- description: Credit Box Controller
  name: WinCL CreditBox API
  slug: wincl-creditbox-api
- description: Dashboard Controller
  name: WinCL Dashboard API
  slug: wincl-dashboard-api
- description: Faq Controller
  name: WinCL FAQ API
  slug: wincl-faq-api
- description: Health Check Controller
  name: WinCL health-check-controller API
  slug: wincl-health-check-controller-api
- description: Hedera Contract Controller
  name: WinCL Hedera Contract Info API
  slug: wincl-hedera-contract-info-api
- description: Info Controller
  name: WinCL Info API
  slug: wincl-info-api
- description: Internal Reward Company Controller
  name: WinCL Internal Reward API
  slug: wincl-internal-reward-api
- description: News Controller
  name: WinCL News API
  slug: wincl-news-api
- description: Notice Controller
  name: WinCL Notice API
  slug: wincl-notice-api
- description: 결제 전 주문 단계
  name: WinCL Order API
  slug: wincl-order-api
- description: Partner Controller
  name: WinCL Partner API
  slug: wincl-partner-api
- description: 주문 후 PG사 결제 단계 (Payco)
  name: WinCL Payment API
  slug: wincl-payment-api
- description: Product Controller
  name: WinCL Product API
  slug: wincl-product-api
- description: Project Controller
  name: WinCL Project API
  slug: wincl-project-api
- description: Qna Controller
  name: WinCL QnA API
  slug: wincl-qna-api
- description: Rank Controller
  name: WinCL Ranking API
  slug: wincl-ranking-api
- description: Reward Company Controller
  name: WinCL Reward API
  slug: wincl-reward-api
- description: Shopping Controller
  name: WinCL Shopping API
  slug: wincl-shopping-api
- description: Store Controller
  name: WinCL Store API
  slug: wincl-store-api
- description: User Controller
  name: WinCL User API
  slug: wincl-user-api
- description: Utils Controller
  name: WinCL Utils API
  slug: wincl-utils-api
- description: Wallet Controller
  name: WinCL Wallet API
  slug: wincl-wallet-api
- description: Webhook Controller
  name: WinCL Webhook API
  slug: wincl-webhook-api
artifact_total: 48
common:
- group: company
  title: ''
  type: Website
  url: https://wincl.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.wincl.io/wincl-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.wincl.io/v3/api-docs
- group: auth
  title: ''
  type: Authentication
  url: authentication/wincl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wincl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wincl-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wincl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wincl-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wincl-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wincl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wincl-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wincl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wincl-domain-security.yml
created: '2026-07-17'
description: WinCL (윈클) is a Korean integrated carbon-management platform that helps enterprises calculate greenhouse-gas emissions, produce climate disclosures and reports, and offset their footprint end-to-end. It combines WinCL Monitoring (emissions accounting and climate disclosure), a WinCL Marketplace for buying globally certified carbon credits (Verra, Gold Standard) and I-REC renewable-energy certificates, a WinCL Reward marketing layer, and consulting services. The WinCL API (api.wincl.io, 271 operations, Bearer JWT) exposes wallet, credit box, certificate box, product, order, Stripe/KCP payment, and Hedera on-chain minting/offset operations so customers can embed carbon purchasing and credit retirement directly into their own applications.
image: https://static.wixstatic.com/media/7a0600_6dd50be2bc40458f9398c57c7c238c15~mv2.png/v1/fill/w_432,h_228,al_c/7a0600_6dd50be2bc40458f9398c57c7c238c15~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: wincl-mcp.yml
  slug: wincl-mcpyml
modified: '2026-07-21'
name: WinCL
nav: Providers
network: true
overview: 'WinCL publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Admin Auth API, Admin FAQ API, and 41 more. Tagged areas include Company, Carbon Management, Sustainability, Greenhouse Gas, and Carbon Credits.


  WinCL''s developer surface includes documentation, API reference, authentication, and 11 more developer resources.'
random_paper: 89
score:
  band: thin
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 52.1
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Wincl Authentication
  slug: wincl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wincl Domain Security
  slug: wincl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wincl
tags:
- Company
- Carbon Management
- Sustainability
- Greenhouse Gas
- Carbon Credits
- Carbon Offset
- ESG
- Climate
- Marketplace
- Payments
- Blockchain
- Hedera
website: https://wincl.io
---
