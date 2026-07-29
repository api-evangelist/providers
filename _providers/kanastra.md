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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 20
apis:
- description: The Accounts API from Kanastra — 3 operation(s) for accounts.
  name: Kanastra Accounts API
  slug: kanastra-accounts-api
- description: The Amendment API from Kanastra — 1 operation(s) for amendment.
  name: Kanastra Amendment API
  slug: kanastra-amendment-api
- description: The Authentication API from Kanastra — 2 operation(s) for authentication.
  name: Kanastra Authentication API
  slug: kanastra-authentication-api
- description: The Balance API from Kanastra — 1 operation(s) for balance.
  name: Kanastra Balance API
  slug: kanastra-balance-api
- description: The Bank Account Beneficiary API from Kanastra — 2 operation(s) for bank account beneficiary.
  name: Kanastra Bank Account Beneficiary API
  slug: kanastra-bank-account-beneficiary-api
- description: The Bank Slip (Boleto) API from Kanastra — 5 operation(s) for bank slip (boleto).
  name: Kanastra Bank Slip (Boleto) API
  slug: kanastra-bank-slip-boleto-api
- description: The CNAB API from Kanastra — 2 operation(s) for cnab.
  name: Kanastra CNAB API
  slug: kanastra-cnab-api
- description: The Commercial Note API from Kanastra — 4 operation(s) for commercial note.
  name: Kanastra Commercial Note API
  slug: kanastra-commercial-note-api
- description: The Create API from Kanastra — 1 operation(s) for create.
  name: Kanastra Create API
  slug: kanastra-create-api
- description: The File Return API from Kanastra — 5 operation(s) for file return.
  name: Kanastra File Return API
  slug: kanastra-file-return-api
- description: The Guarantees API from Kanastra — 6 operation(s) for guarantees.
  name: Kanastra Guarantees API
  slug: kanastra-guarantees-api
- description: The Issuers API from Kanastra — 2 operation(s) for issuers.
  name: Kanastra Issuers API
  slug: kanastra-issuers-api
- description: The Pagamentos API from Kanastra — 1 operation(s) for pagamentos.
  name: Kanastra Pagamentos API
  slug: kanastra-pagamentos-api
- description: The PIX Deposit API from Kanastra — 2 operation(s) for pix deposit.
  name: Kanastra PIX Deposit API
  slug: kanastra-pix-deposit-api
- description: The PIX Keys API from Kanastra — 5 operation(s) for pix keys.
  name: Kanastra PIX Keys API
  slug: kanastra-pix-keys-api
- description: The PIX Transfer API from Kanastra — 1 operation(s) for pix transfer.
  name: Kanastra PIX Transfer API
  slug: kanastra-pix-transfer-api
- description: The QRCodes API from Kanastra — 3 operation(s) for qrcodes.
  name: Kanastra QRCodes API
  slug: kanastra-qrcodes-api
- description: The TED Transfer API from Kanastra — 3 operation(s) for ted transfer.
  name: Kanastra TED Transfer API
  slug: kanastra-ted-transfer-api
- description: The Transactions API from Kanastra — 1 operation(s) for transactions.
  name: Kanastra Transactions API
  slug: kanastra-transactions-api
- description: The Wallet API from Kanastra — 2 operation(s) for wallet.
  name: Kanastra Wallet API
  slug: kanastra-wallet-api
artifact_total: 25
asyncapis:
- description: Webhook event surface for Kanastra Banking. Subscribing systems receive JSON payloads for bank slip (boleto) lifecycle and CNAB file-processing events. Captured from the provider-published webhook doc
  name: Kanastra Banking Webhooks
  slug: kanastra-banking-asyncapi
collections:
- collection_type: postman
  name: Kanastra Banking
  slug: postman-kanastra-banking
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://banking-docs.kanastra.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://banking-docs.kanastra.com.br/
- group: docs
  title: ''
  type: APIReference
  url: https://banking-docs.kanastra.com.br/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kanastra-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kanastra-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kanastra
- group: company
  title: ''
  type: Website
  url: https://kanastra.com.br/
created: '2026-07-17'
description: 'Kanastra is a Brazilian fintech building full-stack infrastructure for banking and the private credit market. Its Banking API offers banking-as-a-service capabilities to financial institutions, funds and securitization vehicles: financial (checking) accounts with balances and transactions, PIX (key registration, transfers, deposits, and static/dynamic QR Codes on the BR Code / EMV-QRCPS standard), boleto (bank slip) issuance with CNAB return-file processing settled via the Nuclea clearing house, TED transfers, wallets, commercial notes (CCB) with guarantees and documents, and issuers. Authentication uses a private_key_jwt (ES512 client-assertion) flow that returns a scoped Bearer JWT, and a webhook surface streams bank slip and CNAB lifecycle events. Kanastra is backed by QED Investors, Kaszek, Valor Capital, Quona Capital, Itau, IFC and F-Prime.'
image: https://kanastra.com.br/favicon.ico
layout: provider
modified: '2026-07-19'
name: Kanastra
nav: Providers
network: true
overview: 'Kanastra publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Amendment API, Authentication API, and 17 more. Tagged areas include Company, Banking, Banking as a Service, Payments, and PIX.


  The Kanastra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kanastra''s developer surface includes documentation, API reference, authentication, and 4 more developer resources.'
random_paper: 43
scopes:
- name: Kanastra Scopes
  scope_count: 5
  slug: kanastra-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 37.3
  delta: 2.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 65.7
    developer_ergonomics: 34.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 35.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 49.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kanastra/refs/heads/main/screenshots/kanastra-2026-07-25T223445.png
security:
- kind: authentication
  name: Kanastra Authentication
  slug: kanastra-authentication
  summary_line: http/private_key_jwt · 1 scheme
- kind: domain-security
  name: Kanastra Domain Security
  slug: kanastra-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kanastra
tags:
- Company
- Banking
- Banking as a Service
- Payments
- PIX
- Boleto
- Private Credit
- Fintech
- Brazil
- Wealth Management
website: https://kanastra.com.br/
---
