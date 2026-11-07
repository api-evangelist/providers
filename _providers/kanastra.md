---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Accounts API from Kanastra — 3 operation(s) for accounts.
  name: Kanastra Accounts API
  slug: kanastra-accounts-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Amendment API from Kanastra — 1 operation(s) for amendment.
  name: Kanastra Amendment API
  slug: kanastra-amendment-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Authentication API from Kanastra — 2 operation(s) for authentication.
  name: Kanastra Authentication API
  slug: kanastra-authentication-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Balance API from Kanastra — 1 operation(s) for balance.
  name: Kanastra Balance API
  slug: kanastra-balance-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Bank Account Beneficiary API from Kanastra — 2 operation(s) for bank account beneficiary.
  name: Kanastra Bank Account Beneficiary API
  slug: kanastra-bank-account-beneficiary-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Bank Slip (Boleto) API from Kanastra — 5 operation(s) for bank slip (boleto).
  name: Kanastra Bank Slip (Boleto) API
  slug: kanastra-bank-slip-boleto-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The CNAB API from Kanastra — 2 operation(s) for cnab.
  name: Kanastra CNAB API
  slug: kanastra-cnab-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Commercial Note API from Kanastra — 4 operation(s) for commercial note.
  name: Kanastra Commercial Note API
  slug: kanastra-commercial-note-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Create API from Kanastra — 1 operation(s) for create.
  name: Kanastra Create API
  slug: kanastra-create-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The File Return API from Kanastra — 5 operation(s) for file return.
  name: Kanastra File Return API
  slug: kanastra-file-return-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Guarantees API from Kanastra — 6 operation(s) for guarantees.
  name: Kanastra Guarantees API
  slug: kanastra-guarantees-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Issuers API from Kanastra — 2 operation(s) for issuers.
  name: Kanastra Issuers API
  slug: kanastra-issuers-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Pagamentos API from Kanastra — 1 operation(s) for pagamentos.
  name: Kanastra Pagamentos API
  slug: kanastra-pagamentos-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The PIX Deposit API from Kanastra — 2 operation(s) for pix deposit.
  name: Kanastra PIX Deposit API
  slug: kanastra-pix-deposit-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The PIX Keys API from Kanastra — 5 operation(s) for pix keys.
  name: Kanastra PIX Keys API
  slug: kanastra-pix-keys-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The PIX Transfer API from Kanastra — 1 operation(s) for pix transfer.
  name: Kanastra PIX Transfer API
  slug: kanastra-pix-transfer-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The TED Transfer API from Kanastra — 3 operation(s) for ted transfer.
  name: Kanastra TED Transfer API
  slug: kanastra-ted-transfer-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Transactions API from Kanastra — 1 operation(s) for transactions.
  name: Kanastra Transactions API
  slug: kanastra-transactions-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The Wallet API from Kanastra — 2 operation(s) for wallet.
  name: Kanastra Wallet API
  slug: kanastra-wallet-api
- baseURL: https://banking.kanastra.com.br
  baseurl_source: declared
  description: The QR Codes API from Kanastra — 3 operation(s) for qr codes.
  name: Kanastra QR Codes API
  slug: kanastra-qr-codes-api
artifact_total: 49
asyncapis:
- description: Webhook event surface for Kanastra Banking. Subscribing systems receive JSON payloads for bank slip (boleto) lifecycle and CNAB file-processing events. Captured from the provider-published webhook doc
  name: Kanastra Banking Webhooks
  slug: kanastra-banking-asyncapi
collections:
- collection_type: postman
  name: Kanastra Banking
  slug: postman-kanastra-banking
- collection_type: open
  name: Kanastra Banking Accounts API
  slug: open-kanastra-accounts-api
- collection_type: open
  name: Kanastra Banking Accounts Amendment API
  slug: open-kanastra-amendment-api
- collection_type: open
  name: Kanastra Banking Accounts Authentication API
  slug: open-kanastra-authentication-api
- collection_type: open
  name: Kanastra Banking Accounts Balance API
  slug: open-kanastra-balance-api
- collection_type: open
  name: Kanastra Banking Accounts Bank Account Beneficiary API
  slug: open-kanastra-bank-account-beneficiary-api
- collection_type: open
  name: Kanastra Banking Accounts Bank Slip (Boleto) API
  slug: open-kanastra-bank-slip-boleto-api
- collection_type: open
  name: Kanastra Banking Accounts CNAB API
  slug: open-kanastra-cnab-api
- collection_type: open
  name: Kanastra Banking Accounts Commercial Note API
  slug: open-kanastra-commercial-note-api
- collection_type: open
  name: Kanastra Banking Accounts Create API
  slug: open-kanastra-create-api
- collection_type: open
  name: Kanastra Banking Accounts File Return API
  slug: open-kanastra-file-return-api
- collection_type: open
  name: Kanastra Banking Accounts Guarantees API
  slug: open-kanastra-guarantees-api
- collection_type: open
  name: Kanastra Banking Accounts Issuers API
  slug: open-kanastra-issuers-api
- collection_type: open
  name: Kanastra Banking Accounts Pagamentos API
  slug: open-kanastra-pagamentos-api
- collection_type: open
  name: Kanastra Banking Accounts PIX Deposit API
  slug: open-kanastra-pix-deposit-api
- collection_type: open
  name: Kanastra Banking Accounts PIX Keys API
  slug: open-kanastra-pix-keys-api
- collection_type: open
  name: Kanastra Banking Accounts PIX Transfer API
  slug: open-kanastra-pix-transfer-api
- collection_type: open
  name: Kanastra Banking Accounts QRCodes API
  slug: open-kanastra-qrcodes-api
- collection_type: open
  name: Kanastra Banking Accounts TED Transfer API
  slug: open-kanastra-ted-transfer-api
- collection_type: open
  name: Kanastra Banking Accounts Transactions API
  slug: open-kanastra-transactions-api
- collection_type: open
  name: Kanastra Banking Accounts Wallet API
  slug: open-kanastra-wallet-api
common:
- group: company
  title: ''
  type: Blog
  url: https://kanastra.com.br/blog/
- group: other
  href: https://artifacts.apis.io/kanastra/capabilities/kanastra-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kanastra-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kanastra/skills/kanastra-authenticate.md
  title: ''
  type: AgentSkill
  url: skills/kanastra-authenticate.md
- group: agent
  href: https://artifacts.apis.io/kanastra/mcp/kanastra-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kanastra-mcp.yml
- group: other
  href: https://artifacts.apis.io/kanastra/overlays/kanastra-banking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kanastra-banking-overlay.yaml
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
  href: https://artifacts.apis.io/kanastra/authentication/kanastra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kanastra-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kanastra/security/kanastra-domain-security.yml
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
modified: '2026-10-06'
name: Kanastra
nav: Providers
network: true
overview: 'Kanastra publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Amendment API, Authentication API, and 17 more. Tagged areas include Company, Banking, Banking as a Service, Payments, and Pix.


  The Kanastra catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kanastra''s developer surface includes engineering blog, documentation, API reference, authentication, and 8 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Kanastra API Rules
  rule_count: 54
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 4
  slug: kanastra-rules
scopes:
- name: Kanastra Scopes
  scope_count: 5
  slug: kanastra-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 54.3
    developer_ergonomics: 50.6
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 37.3
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
    score: 34.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kanastra/kanastra-2026-07-25T223445.png
security:
- kind: authentication
  name: Kanastra Authentication
  slug: kanastra-authentication
  summary_line: http/private_key_jwt · 1 scheme
- kind: domain-security
  name: Kanastra Domain Security
  slug: kanastra-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Authenticate with Kanastra Banking
  slug: kanastra-authenticate
- name: Issue and track a boleto (bank slip)
  slug: kanastra-issue-boleto
- name: Register a PIX key and send a PIX transfer
  slug: kanastra-pix-transfer
slug: kanastra
tags:
- Company
- Banking
- Banking as a Service
- Payments
- Pix
- Boleto
- Private Credit
- Fintech
- Brazil
- Wealth Management
website: https://kanastra.com.br/
---
