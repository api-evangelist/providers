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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Lead Bank Agentic Access
  operation_count: 83
  slug: lead-bank-agentic-access
  summary_line: 83 operations · 58 acting
api_count: 22
apis:
- description: Embedded-credit API supporting term loans, revolving lines of credit, in-app financing, and buy-now-pay-later products. Covers origination, underwriting, servicing, and disbursement.
  name: Lead Bank Lend API
  slug: lend
- description: Money-movement API spanning ACH, instant payments (RTP / FedNow), domestic and international wires, stablecoin transfers, and partner-configurable payment controls.
  name: Lead Bank Move API
  slug: move
- description: Card-issuing API for physical and virtual credit and debit cards plus custom-generated account numbers used in card-program back-ends.
  name: Lead Bank Issue API
  slug: issue
- description: Deposit-account API for opening and managing FDIC-insured accounts on behalf of partner-program end users, including multi-currency balances and flexible account structures.
  name: Lead Bank Store API
  slug: store
- description: File-based integration channel over SFTP for partners that ingest or emit batch files (NACHA, reconciliation, settlement reports).
  name: Lead Bank File Integrations (SFTP)
  slug: file-integrations
- description: Outbound webhook events covering account, payment, card, and lending lifecycle changes. Endpoints configured per partner program.
  name: Lead Bank Webhooks
  slug: webhooks
- description: The Account Number API from Lead Bank — 7 operation(s) for account number.
  name: Lead Bank Account Number API
  slug: lead-bank-account-number-api
- description: The ACH API from Lead Bank — 5 operation(s) for ach.
  name: Lead Bank ACH API
  slug: lead-bank-ach-api
- description: The Blockchain Payment API from Lead Bank — 2 operation(s) for blockchain payment.
  name: Lead Bank Blockchain Payment API
  slug: lead-bank-blockchain-payment-api
- description: The Compliance API from Lead Bank — 11 operation(s) for compliance.
  name: Lead Bank Compliance API
  slug: lead-bank-compliance-api
- description: The Entity API from Lead Bank — 2 operation(s) for entity.
  name: Lead Bank Entity API
  slug: lead-bank-entity-api
- description: The Events API from Lead Bank — 2 operation(s) for events.
  name: Lead Bank Events API
  slug: lead-bank-events-api
- description: The Funding API from Lead Bank — 3 operation(s) for funding.
  name: Lead Bank Funding API
  slug: lead-bank-funding-api
- description: The Instant Payments API from Lead Bank — 7 operation(s) for instant payments.
  name: Lead Bank Instant Payments API
  slug: lead-bank-instant-payments-api
- description: The Internal Transfer API from Lead Bank — 2 operation(s) for internal transfer.
  name: Lead Bank Internal Transfer API
  slug: lead-bank-internal-transfer-api
- description: The Lending API from Lead Bank — 3 operation(s) for lending.
  name: Lead Bank Lending API
  slug: lead-bank-lending-api
- description: The Lending Simulation API from Lead Bank — 1 operation(s) for lending simulation.
  name: Lead Bank Lending Simulation API
  slug: lead-bank-lending-simulation-api
- description: The OAuth API from Lead Bank — 1 operation(s) for oauth.
  name: Lead Bank OAuth API
  slug: lead-bank-oauth-api
- description: The Originator API from Lead Bank — 5 operation(s) for originator.
  name: Lead Bank Originator API
  slug: lead-bank-originator-api
- description: The Simulation API from Lead Bank — 11 operation(s) for simulation.
  name: Lead Bank Simulation API
  slug: lead-bank-simulation-api
- description: The Subledger Balances API from Lead Bank — 2 operation(s) for subledger balances.
  name: Lead Bank Subledger Balances API
  slug: lead-bank-subledger-balances-api
- description: The Wire API from Lead Bank — 4 operation(s) for wire.
  name: Lead Bank Wire API
  slug: lead-bank-wire-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lead Bank Account Number API
  slug: open-lead-bank-account-number-api
- collection_type: open
  name: Lead Bank Account Number ACH API
  slug: open-lead-bank-ach-api
- collection_type: open
  name: Lead Bank Account Number Blockchain Payment API
  slug: open-lead-bank-blockchain-payment-api
- collection_type: open
  name: Lead Bank Account Number Compliance API
  slug: open-lead-bank-compliance-api
- collection_type: open
  name: Lead Bank Account Number Entity API
  slug: open-lead-bank-entity-api
- collection_type: open
  name: Lead Bank Account Number Events API
  slug: open-lead-bank-events-api
- collection_type: open
  name: Lead Bank Account Number Funding API
  slug: open-lead-bank-funding-api
- collection_type: open
  name: Lead Bank Account Number Instant Payments API
  slug: open-lead-bank-instant-payments-api
- collection_type: open
  name: Lead Bank Account Number Internal Transfer API
  slug: open-lead-bank-internal-transfer-api
- collection_type: open
  name: Lead Bank Account Number Lending API
  slug: open-lead-bank-lending-api
- collection_type: open
  name: Lead Bank Account Number Lending Simulation API
  slug: open-lead-bank-lending-simulation-api
- collection_type: open
  name: Lead Bank Account Number OAuth API
  slug: open-lead-bank-oauth-api
- collection_type: open
  name: Lead Bank Account Number Originator API
  slug: open-lead-bank-originator-api
- collection_type: open
  name: Lead Bank Account Number Simulation API
  slug: open-lead-bank-simulation-api
- collection_type: open
  name: Lead Bank Account Number Subledger Balances API
  slug: open-lead-bank-subledger-balances-api
- collection_type: open
  name: Lead Bank Account Number Wire API
  slug: open-lead-bank-wire-api
- collection_type: open
  name: Lead Bank
  slug: open-lead-bank
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lead-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lead-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lead-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lead.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lead.bank/
- group: start
  title: ''
  type: PartnerPortal
  url: https://partners.lead.bank/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lead.bank/changelog
- group: operate
  title: ''
  type: ContactSales
  url: https://lead.bank/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lead-bank
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lead.bank/llms.txt
created: '2026-05-23'
description: Lead Bank is a Kansas City-chartered FDIC-insured bank operating as a sponsor bank and embedded-finance infrastructure provider for fintech partners. The platform is organized around four product pillars - Lend (term loans, lines of credit, BNPL, in-app financing), Move (ACH, instant payments, wires, international wires, stablecoin transfers, payment controls), Issue (physical and virtual credit / debit cards, custom account numbers), and Store (FDIC-insured multi-currency deposit accounts). APIs and file integrations (SFTP) are documented at docs.lead.bank but access is gated through Lead Bank's partner-onboarding process. Recognized on the Forbes Next Billion-Dollar Startups and CNBC Disruptor 50 lists.
finops:
- name: Lead Bank Finops
  service_category: API
  slug: lead-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lead-bank.png
layout: provider
modified: '2026-05-23'
name: Lead Bank
nav: Providers
network: true
overview: 'Lead Bank publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Number API, ACH API, Blockchain Payment API, and 13 more. Tagged areas include Banking, Sponsor Bank, Embedded Finance, Banking as a Service, and Payments.


  Lead Bank''s developer surface includes authentication, documentation, changelog, and 7 more developer resources.'
plans:
- name: Lead Bank Plans Pricing
  plan_count: 1
  slug: lead-bank-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Lead Bank Rate Limits
  slug: lead-bank-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lead-bank/refs/heads/main/screenshots/lead-bank-2026-06-20T184345.png
security:
- kind: authentication
  name: Lead Bank Authentication
  slug: lead-bank-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lead Bank Domain Security
  slug: lead-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lead-bank
tags:
- Banking
- Sponsor Bank
- Embedded Finance
- Banking as a Service
- Payments
- Lending
- Cards
- Deposits
website: https://lead.bank/
---
