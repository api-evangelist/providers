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
- acting_count: 33
  human_in_the_loop: 0
  name: Fintecture Agentic Access
  operation_count: 69
  slug: fintecture-agentic-access
  summary_line: 69 operations · 33 acting
api_count: 22
apis:
- description: Register and manage merchant customers, attach their bank accounts, and run identity verifications. Persisted customer records pre-fill payment fields and accelerate repeat checkouts; verifications co
  name: Fintecture Customers API
  slug: fintecture-customers-api
- description: Issues access tokens via authorization_code and client_credentials grants. Distinct scopes for PIS, AIS, Customers, E-Mandates, and OAC (Organisation Access Credentials, beta). Access tokens are valid
  name: Fintecture OAuth and Tokens API
  slug: fintecture-oauth-api
- description: Inspect transactions and settlements. Settlements represent outgoing disbursements from the merchant's Local Acquiring account to their own bank account. Sandbox includes a transaction simulator endpo
  name: Fintecture Transactions and Settlements API
  slug: fintecture-transactions-api
- description: Bank accounts, balances, and holders
  name: Fintecture Accounts API
  slug: fintecture-accounts-api
- description: The Applications API from Fintecture — 3 operation(s) for applications.
  name: Fintecture Applications API
  slug: fintecture-applications-api
- description: PSU bank authentication
  name: Fintecture Authentication API
  slug: fintecture-authentication-api
- description: Customer bank accounts
  name: Fintecture Bank Accounts API
  slug: fintecture-bank-accounts-api
- description: The Companies API from Fintecture — 2 operation(s) for companies.
  name: Fintecture Companies API
  slug: fintecture-companies-api
- description: Customer e-mandates
  name: Fintecture E-Mandates API
  slug: fintecture-e-mandates-api
- description: The Memberships API from Fintecture — 2 operation(s) for memberships.
  name: Fintecture Memberships API
  slug: fintecture-memberships-api
- description: The Organisation Nodes API from Fintecture — 4 operation(s) for organisation nodes.
  name: Fintecture Organisation Nodes API
  slug: fintecture-organisation-nodes-api
- description: Create and inspect payment sessions
  name: Fintecture Payments API
  slug: fintecture-payments-api
- description: Verified payouts and request-for-payout
  name: Fintecture Payouts API
  slug: fintecture-payouts-api
- description: Bank providers / coverage
  name: Fintecture Providers API
  slug: fintecture-providers-api
- description: Initiate immediate refunds
  name: Fintecture Refunds API
  slug: fintecture-refunds-api
- description: Generate Fintecture payment links
  name: Fintecture Request To Pay API
  slug: fintecture-request-to-pay-api
- description: The Sandbox API from Fintecture — 1 operation(s) for sandbox.
  name: Fintecture Sandbox API
  slug: fintecture-sandbox-api
- description: Local Acquiring disbursements
  name: Fintecture Settlements API
  slug: fintecture-settlements-api
- description: Sandbox test accounts
  name: Fintecture Test Accounts API
  slug: fintecture-test-accounts-api
- description: The Users API from Fintecture — 2 operation(s) for users.
  name: Fintecture Users API
  slug: fintecture-users-api
- description: AIS-based identity verification
  name: Fintecture Verification API
  slug: fintecture-verification-api
- description: Customer identity verifications
  name: Fintecture Verifications API
  slug: fintecture-verifications-api
arazzos:
- description: List a connection's accounts, read the first account's holders, then run an AIS identity verification.
  name: Fintecture Account Holders and Identity Verification
  slug: fintecture-account-holders-identity-workflow
- description: Open an AIS connect session, list the linked accounts, then pull one account's transactions.
  name: Fintecture Connect, List Accounts, and Pull Transactions
  slug: fintecture-connect-accounts-transactions-workflow
- description: Register a merchant customer, attach their bank account, then open a payment session for them.
  name: Fintecture Onboard Customer and Initiate Payment
  slug: fintecture-customer-onboard-payment-workflow
- description: Register a customer, start an AIS identity verification, then poll until it resolves.
  name: Fintecture Customer Verification with Polling
  slug: fintecture-customer-verification-poll-workflow
- description: Authenticate a PSU with the decoupled (mobile-app) model, poll until approved, then list accounts.
  name: Fintecture Decoupled Authentication then List Accounts
  slug: fintecture-decoupled-auth-accounts-workflow
- description: Discover supported bank providers, then open a payment session and inspect its status.
  name: Fintecture List Providers and Initiate Payment
  slug: fintecture-list-providers-initiate-payment-workflow
- description: Verify a payment is completed, issue a refund against it, then list the payment's refunds.
  name: Fintecture Refund a Completed Payment
  slug: fintecture-payment-refund-workflow
- description: Open a payment session and poll its status until it settles, branching on the outcome.
  name: Fintecture Create Payment and Poll Status
  slug: fintecture-payment-status-poll-workflow
- description: Generate a payment link, find the resulting payment by status filter, then read its details.
  name: Fintecture Request To Pay and Track Status
  slug: fintecture-request-to-pay-status-workflow
- description: Pick a sandbox test account, open a payment session against its bank, then poll for completion.
  name: Fintecture Sandbox Test Payment
  slug: fintecture-sandbox-test-payment-workflow
- description: List settlements, read one settlement's detail, then pull merchant transactions to reconcile.
  name: Fintecture Settlement Reconciliation
  slug: fintecture-settlement-reconciliation-workflow
- description: Mint a client-credentials access token, open a payment session, and read its status.
  name: Fintecture Mint Token then Initiate Payment
  slug: fintecture-token-then-payment-workflow
- description: Read a payment, patch its communication while it is still pending, then re-read to confirm.
  name: Fintecture Update Payment Communication
  slug: fintecture-update-payment-communication-workflow
artifact_total: 86
collections:
- collection_type: postman
  name: Fintecture Account Information Services API
  slug: postman-fintecture-ais-api
- collection_type: postman
  name: Fintecture Customers API
  slug: postman-fintecture-customers-api
- collection_type: postman
  name: Fintecture E-Mandates API
  slug: postman-fintecture-emandates-api
- collection_type: postman
  name: Fintecture Organisation Access Credentials API
  slug: postman-fintecture-oac-api
- collection_type: postman
  name: Fintecture OAuth and Tokens API
  slug: postman-fintecture-oauth-api
- collection_type: postman
  name: Fintecture Payment Initiation Services API
  slug: postman-fintecture-pis-api
- collection_type: postman
  name: Fintecture Resources API
  slug: postman-fintecture-resources-api
- collection_type: postman
  name: Fintecture Transactions and Settlements API
  slug: postman-fintecture-transactions-api
- collection_type: open
  name: Fintecture Account Information Services API
  slug: open-fintecture-ais-api
- collection_type: open
  name: Fintecture Customers API
  slug: open-fintecture-customers-api
- collection_type: open
  name: Fintecture E-Mandates API
  slug: open-fintecture-emandates-api
- collection_type: open
  name: Fintecture Organisation Access Credentials API
  slug: open-fintecture-oac-api
- collection_type: open
  name: Fintecture OAuth and Tokens API
  slug: open-fintecture-oauth-api
- collection_type: open
  name: Fintecture Payment Initiation Services API
  slug: open-fintecture-pis-api
- collection_type: open
  name: Fintecture Resources API
  slug: open-fintecture-resources-api
- collection_type: open
  name: Fintecture Transactions and Settlements API
  slug: open-fintecture-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fintecture-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fintecture-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fintecture-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fintecture/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-account-holders-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-connect-accounts-transactions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-customer-onboard-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-customer-verification-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-decoupled-auth-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-list-providers-initiate-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-payment-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-payment-status-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-request-to-pay-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-sandbox-test-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-settlement-reconciliation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-token-then-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fintecture-update-payment-communication-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fintecture
- group: start
  title: ''
  type: Portal
  url: https://fintecture.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com/docs/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.fintecture.com/docs/api-overview
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com/docs/api-http-signature
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com/docs/api-webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com/docs/demo-bank
- group: docs
  title: ''
  type: Documentation
  url: https://doc.fintecture.com/docs/testing-complete-payment-flows-in-sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.fintecture.com/changelog
- group: start
  title: ''
  type: Signup
  url: https://console.fintecture.com/
- group: start
  title: ''
  type: Sandbox
  url: https://console-sandbox.fintecture.com/
- group: build
  title: ''
  type: Postman
  url: https://doc.fintecture.com/docs/api-take-on-our-postman-collection
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fintecture
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fintecture/fintecture-sdk-javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fintecture/fintecture-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fintecture/fintecture-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fintecture/fintecture-sdk-ruby
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/Fintecture/sample-nodejs
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/Fintecture/sample-ror
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/Fintecture/signature-guide
- group: build
  title: ''
  type: Plugins
  url: https://github.com/Fintecture/magento
- group: build
  title: ''
  type: Plugins
  url: https://github.com/Fintecture/magento-hyva
- group: build
  title: ''
  type: Plugins
  url: https://github.com/Fintecture/magento19
- group: build
  title: ''
  type: Plugins
  url: https://github.com/Fintecture/odoo
- group: commercial
  title: ''
  type: Pricing
  url: https://fintecture.com/tarifs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fintecture.com/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fintecture.com/politique-de-confidentialite
- group: operate
  title: ''
  type: Support
  url: https://fintecture.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fintecture.com
- group: company
  title: ''
  type: Blog
  url: https://fintecture.com/blog
- group: other
  title: ''
  type: Regions
  url: ''
- group: other
  title: ''
  type: Regulator
  url: https://acpr.banque-france.fr/
created: '2026-05-25T00:00:00.000Z'
description: Fintecture is a French Open Banking payments platform and ACPR-authorised payment institution (#17248). Its API stack covers PSD2 Payment Initiation (Immediate Transfer, Smart Transfer, Request To Pay, Buy Now Pay Later, Verified Payout, Immediate Refund), PSD2 Account Information (accounts, holders, transactions, identity verification), Customers, E-Mandates, and a beta Organisation Access Credentials surface for managing multi-tenant enterprise estates. Clients include Auchan, Bricoman, Pluxee, PMU, and Edenred, with 2M+ end payers served. Plug-and-play modules for PrestaShop, Magento, Shopify, WordPress, Odoo, Intershop, and Oasis sit on top of official JavaScript, Python, PHP, and Ruby SDKs.
examples:
- key_count: 2
  name: Fintecture Get Accounts Example
  slug: fintecture-get-accounts-example
- key_count: 2
  name: Fintecture Immediate Transfer Example
  slug: fintecture-immediate-transfer-example
- key_count: 2
  name: Fintecture Request To Pay Example
  slug: fintecture-request-to-pay-example
features:
- Immediate Transfer — pay-by-bank Open Banking transfers without IBAN entry, near-instant settlement
- Smart Transfer — auto-reconciled transfers using merchant-allocated virtual unique IBANs
- Request To Pay — payment links delivered via email, SMS, QR code, or invoice
- Verified Payout — refunds and customer reimbursements to verified bank accounts
- Buy Now Pay Later — BNPL composed inside the Payment Hub
- Immediate Refund — initiate full or partial refunds to original or alternative bank accounts
- Account Information Services (AIS) — accounts, holders, balances, transactions
- AIS-backed customer identity verification
- E-Mandates — SEPA-style mandates with unique RUM identifier and cancel/revoke lifecycle
- Payment Hub — single endpoint that orchestrates Immediate Transfer, Smart Transfer, and BNPL in one session
- Local Acquiring — merchant funds collected then settled to merchant bank account
- Decoupled bank authentication via PSU mobile banking app
- HTTP message signature security (RFC draft-cavage-http-signatures) with digest and x-request-id mandatory on production
- Webhook events with signature verification and an in-console Event Simulator
- Sandbox Demo Bank plus real test accounts for each provider bank
- Organisation Access Credentials (OAC, beta) — hierarchical Organisation Nodes, Companies, Memberships, Users
- Multi-currency PIS rails — SEPA, iSCT (SEPA Instant), FPS (UK), PLN (Poland), INT (international)
- Official SDKs for JavaScript / TypeScript, PHP, Python, Ruby
- Plug-and-play modules for PrestaShop, Magento (2, 1.9, Hyva), WooCommerce / WordPress, Shopify, Odoo, Intershop, Oasis
- Console with payment session tracking, application registration, SSO configuration, webhook setup, and pre-fill controls
- Fraud detection and transaction monitoring beyond regulatory minimums
finops:
- name: Fintecture Finops
  service_category: Financial Services
  slug: fintecture-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fintecture.png
json_schemas:
- name: Fintecture Bank Account
  property_count: 7
  slug: fintecture-account
- name: Fintecture Payment
  property_count: 6
  slug: fintecture-payment
jsonld:
- class_count: 0
  name: Fintecture Context
  property_count: 7
  slug: fintecture-context
layout: provider
modified: '2026-05-25'
name: Fintecture
nav: Providers
network: true
overview: 'Fintecture publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Customers API, OAuth and Tokens API, Transactions and Settlements API, and 19 more. Tagged areas include Open Banking, Payments, PSD2, France, and Account Information.


  The Fintecture catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Fintecture''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, signup flow, sandbox, and 42 more developer resources.'
plans:
- name: Fintecture Plans Pricing
  plan_count: 9
  slug: fintecture-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 4
  name: Fintecture Rate Limits
  slug: fintecture-rate-limits
rules:
- name: Fintecture API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fintecture-jsonschema-spectral-rules
- name: Fintecture API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: fintecture-rules
score:
  band: strong
  composite: 62.2
  delta: -6.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 68.9
    developer_ergonomics: 71.7
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 68.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fintecture/refs/heads/main/screenshots/fintecture-2026-06-20T181225.png
security:
- kind: authentication
  name: Fintecture Authentication
  slug: fintecture-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fintecture Domain Security
  slug: fintecture-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fintecture
tags:
- Open Banking
- Payments
- PSD2
- France
- Account Information
- Payment Initiation
- Instant Payments
- SEPA
- Smart Transfer
- Request To Pay
- Buy Now Pay Later
- E-Mandates
- Account-to-Account
- KYC
website: https://fintecture.com
---
