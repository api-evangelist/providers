---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: Asynchronous payouts designed for Money Transfer Organizations (MTOs) and disbursement partners. Partners create payments to mobile money wallets, cash pickup points, and bank accounts; results are de
  name: Onafriq Async Payouts API
  slug: onafriq-async-payouts-api
- description: Synchronous payouts custom-built for Mobile Network Operators (MNOs) and partners that require synchronous responses. Transaction results are returned within seconds as a response to the trans_com cal
  name: Onafriq Sync Payouts API
  slug: onafriq-sync-payouts-api
- description: Synchronous bank transfer API for sending funds directly to bank accounts across the Onafriq network with real-time response semantics.
  name: Onafriq Sync Bank Transfers API
  slug: onafriq-sync-bank-transfers-api
- description: Collections (Payins) API for receiving funds from customers across cards, cash agent networks, and mobile money wallets. Supports merchant-pull and subscriber-initiated models with real-time transacti
  name: Onafriq Collections API
  slug: onafriq-collections-api
- description: Programmatic access to daily foreign-exchange rates used by the Onafriq network so partners can price cross-border transactions and perform pre-trade quoting before submitting a payout.
  name: Onafriq Get Rates API
  slug: onafriq-rates-api
- description: Instant Payment Notification (IPN) webhooks delivered asynchronously to partner endpoints as transaction state changes — used in combination with the Async Payouts and Async Collections flows.
  name: Onafriq Async Webhooks API
  slug: onafriq-webhooks-api
- description: Contacts API for adding and retrieving customer (payer / payee) records used across Payins, Payouts, and reconciliation workflows on the Enterprise Platform.
  name: Onafriq Contacts API
  slug: onafriq-contacts-api
- description: Onafriq's Nigerian agent-banking platform (Baxi) exposes Virtual Account, Fingerprint (POS biometric activation), and Account Debit (cardless cash-out) APIs spanning a 460,000+ agent network across al
  name: Baxi Agent Banking API
  slug: baxi-agent-banking-api
- description: Card issuance and processing platform for partners launching physical and virtual prepaid card programs, including Visa virtual card creation, lifecycle management, and globally accepted spend.
  name: Onafriq Card Issuance API
  slug: onafriq-card-issuance-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/onafriq-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onafriq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onafriq.com
- group: company
  title: ''
  type: About
  url: https://onafriq.com/about
- group: start
  title: ''
  type: Portal
  url: https://developers.onafriq.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com/docs/api-overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com/docs/combined-api-information
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com/docs/api-endpoints
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com/docs/communication-protocols
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mfsafrica.com/docs/schedule-a-response-codes-2
- group: build
  title: ''
  type: Collections
  url: https://onafriq.com/services/collections
- group: other
  title: ''
  type: Disbursements
  url: https://onafriq.com/services/disbursements
- group: other
  title: ''
  type: CardIssuance
  url: https://onafriq.com/services/card-issuance-and-processing
- group: other
  title: ''
  type: AgentBanking
  url: https://onafriq.com/services/agent-banking
- group: other
  title: ''
  type: TreasuryServices
  url: https://onafriq.com/services/treasury-services
- group: company
  title: ''
  type: Blog
  url: https://onafriq.com/insights
- group: company
  title: ''
  type: Careers
  url: https://onafriq.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://onafriq.com/contact
- group: other
  title: ''
  type: LegacyBrand
  url: https://mfsafrica.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mfsafrica
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Onafriq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onafriq
created: '2026-05-24'
description: Onafriq (formerly MFS Africa) is a pan-African digital payments network headquartered in London with operating entities across Mauritius, Ghana, Nigeria, Tanzania, Rwanda, Uganda, the DRC, and the UK. Founded by CEO Dare Okoudjou, Onafriq operates what it calls "Africa's largest digital payments gateway" — a network of networks connecting roughly one billion mobile money wallets and 500 million bank accounts across 40+ African countries through 2,000+ cross-border corridors. The platform exposes a REST API surface for partners including Money Transfer Organizations (MTOs), Mobile Network Operators (MNOs), banks, NGOs, governments, and enterprises. Core developer products include Async Payouts (the recommended path for MTOs and bulk disbursement partners, with webhook-based status updates), Sync Payouts (custom-built for MNOs requiring synchronous responses), Sync Bank Transfers, Collections APIs (Payins) for receiving funds from cards, cash agents, and mobile wallets, a Contacts
  API for managing payer/payee records, a Get Rates API for daily foreign exchange rates, and Async Webhooks for Instant Payment Notifications. Two distinct portal endpoints serve domestic (api.mfsafrica.com/api) and cross-border (mfsafrica.beyonicpartners.com/api) workloads. Beyond cross-border remittance and disbursement, Onafriq operates Baxi — a Nigerian agent banking network of 460,000+ agents across all 36 states with its own Virtual Account, Fingerprint, and Account Debit APIs — plus card issuance and processing for physical/virtual prepaid programs and multi-currency treasury services. Onafriq has raised $200M+ in Series C funding from Vitruvian Partners, AXA Investment Managers, and Goodwell, and holds 16 payment licenses including FSC (Mauritius) and FCA (UK) authorization. The legacy MFS Africa developer hub (developer.mfsafrica.com) remains the canonical reference documentation, with a newer developers.onafriq.com portal reflecting the post-rebrand identity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onafriq.png
layout: provider
modified: '2026-05-24'
name: Onafriq
nav: Providers
network: true
overview: 'Onafriq publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Mobile Money, Remittance, Cross-Border Payments, and Disbursements.


  Onafriq''s developer surface includes developer portal, documentation, engineering blog, and 20 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.4
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onafriq/refs/heads/main/screenshots/onafriq-2026-06-20T190708.png
security:
- kind: domain-security
  name: Onafriq Domain Security
  slug: onafriq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Onafriq Trust Center
  slug: onafriq-trust-center
  summary_line: ISO 27001, PCI DSS
slug: onafriq
tags:
- Payments
- Mobile Money
- Remittance
- Cross-Border Payments
- Disbursements
- Payouts
- Collection
- Bank Transfers
- Card Issuance
- Agent Banking
- Treasury
- Foreign Exchange
- Webhook
- Africa
- Fintech
- Financial-Services
- MFS Africa
- Onafriq
- Baxi
website: https://onafriq.com
---
