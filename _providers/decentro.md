---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
- acting_count: 16
  human_in_the_loop: 0
  name: Decentro Agentic Access
  operation_count: 22
  slug: decentro-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 11
apis:
- description: Identity verification, customer onboarding, DigiLocker integration, Aadhaar OTP, document classification, and face match.
  name: Decentro KYC & Onboarding API
  slug: kyc-api
- description: Create and manage virtual bank accounts, balances, statements, and remitter whitelisting for collections and reconciliation.
  name: Decentro Virtual Accounts API
  slug: virtual-accounts-api
- description: The Accounts API from Decentro — 2 operation(s) for accounts.
  name: Decentro Accounts API
  slug: decentro-accounts-api
- description: The Collections API from Decentro — 2 operation(s) for collections.
  name: Decentro Collections API
  slug: decentro-collections-api
- description: The Forensics API from Decentro — 2 operation(s) for forensics.
  name: Decentro Forensics API
  slug: decentro-forensics-api
- description: The Journals API from Decentro — 1 operation(s) for journals.
  name: Decentro Journals API
  slug: decentro-journals-api
- description: The Mandates API from Decentro — 2 operation(s) for mandates.
  name: Decentro Mandates API
  slug: decentro-mandates-api
- description: The Payouts API from Decentro — 2 operation(s) for payouts.
  name: Decentro Payouts API
  slug: decentro-payouts-api
- description: The Settlements API from Decentro — 1 operation(s) for settlements.
  name: Decentro Settlements API
  slug: decentro-settlements-api
- description: The Transactions API from Decentro — 1 operation(s) for transactions.
  name: Decentro Transactions API
  slug: decentro-transactions-api
- description: The Verification API from Decentro — 1 operation(s) for verification.
  name: Decentro Verification API
  slug: decentro-verification-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Decentro KYC & Onboarding Accounts API
  slug: open-decentro-accounts-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Collections API
  slug: open-decentro-collections-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Forensics API
  slug: open-decentro-forensics-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Journals API
  slug: open-decentro-journals-api
- collection_type: open
  name: Decentro & Onboarding Accounts KYC API
  slug: open-decentro-kyc-api
- collection_type: open
  name: Decentro Ledger API
  slug: open-decentro-ledger-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Mandates API
  slug: open-decentro-mandates-api
- collection_type: open
  name: Decentro Payments API
  slug: open-decentro-payments-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Payouts API
  slug: open-decentro-payouts-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Settlements API
  slug: open-decentro-settlements-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Transactions API
  slug: open-decentro-transactions-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Verification API
  slug: open-decentro-verification-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Virtual Accounts API
  slug: open-decentro-virtual-accounts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/decentro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decentro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/decentro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decentro-in
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/decentro
- group: company
  title: ''
  type: Website
  url: https://decentro.tech/
- group: start
  title: ''
  type: Portal
  url: https://docs.decentro.tech/
- group: docs
  title: ''
  type: Reference
  url: https://docs.decentro.tech/reference
- group: company
  title: ''
  type: Blog
  url: https://decentro.tech/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://decentro.tech/pricing/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/decentro-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/decentro-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.decentro.tech/llms.txt
created: '2025-02-24'
description: 'Decentro is a banking-as-a-service platform that provides businesses with seamless integration to Indian banking infrastructure - including payments (UPI, IMPS, NEFT, RTGS), virtual accounts, KYC, ledger primitives, and credit-bureau data. Decentro publishes a developer portal and Postman collection covering six API categories: KYC & Onboarding, Bytes (alternate data), Scanner (forensics), Payments, Virtual Accounts, and Ledger.'
finops:
- name: Decentro Finops
  service_category: Banking-as-a-Service
  slug: decentro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decentro.png
json_schemas:
- name: Decentro Payout
  property_count: 10
  slug: decentro-payout
- name: Decentro Virtual Account
  property_count: 8
  slug: decentro-virtual-account
jsonld:
- class_count: 4
  name: Decentro Context
  property_count: 8
  slug: decentro-context
layout: provider
modified: '2026-05-19'
name: Decentro
nav: Providers
network: true
overview: 'Decentro publishes 11 APIs on the [APIs.io](https://apis.io/) network, including KYC & Onboarding API, Virtual Accounts API, Accounts API, and 8 more. Tagged areas include Banking, Banking as a Service, Fintech, India, and KYC.


  The Decentro catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Decentro''s developer surface includes authentication, developer portal, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Decentro Plans Pricing
  plan_count: 2
  slug: decentro-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Decentro Rate Limits
  slug: decentro-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Decentro API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: decentro-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Decentro API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: decentro-payments-api-rules
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 59.4
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decentro/refs/heads/main/screenshots/decentro-2026-06-20T175753.png
security:
- kind: authentication
  name: Decentro Authentication
  slug: decentro-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Decentro Domain Security
  slug: decentro-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: decentro
tags:
- Banking
- Banking as a Service
- Fintech
- India
- KYC
- Ledger
- Payments
- UPI
- Virtual Accounts
website: https://decentro.tech/
---
