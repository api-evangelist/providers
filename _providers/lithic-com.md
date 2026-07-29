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
- acting_count: 109
  human_in_the_loop: 1
  name: Lithic Com Agentic Access
  operation_count: 215
  slug: lithic-com-agentic-access
  summary_line: 215 operations · 109 acting · 1 human-in-the-loop
api_count: 31
apis:
- description: 3D Secure e-commerce authentication and decisioning.
  name: Lithic 3DS API
  slug: lithic-com-3ds-api
- description: Top-level program accounts and their spend limits.
  name: Lithic Account API
  slug: lithic-com-account-api
- description: KYC/KYB onboarding and management of individual and business account holders.
  name: Lithic Account Holder API
  slug: lithic-com-account-holder-api
- description: Programmable v2 authorization rules, versions, drafts, backtests, and evaluation results.
  name: Lithic Auth Rules API
  slug: lithic-com-auth-rules-api
- description: Real-time HTTP webhook authorization decisioning in the transaction path.
  name: Lithic Auth Stream Access (ASA) API
  slug: lithic-com-auth-stream-access-asa-api
- description: Available and pending balances for financial accounts.
  name: Lithic Balance API
  slug: lithic-com-balance-api
- description: Internal ledger transfers between financial accounts.
  name: Lithic Book Transfer API
  slug: lithic-com-book-transfer-api
- description: Virtual and physical card issuance, lifecycle, and digital wallet provisioning.
  name: Lithic Card API
  slug: lithic-com-card-api
- description: Responses to real-time authorization challenges.
  name: Lithic Card Authorizations API
  slug: lithic-com-card-authorizations-api
- description: Bulk physical card ordering.
  name: Lithic Card Bulk Orders API
  slug: lithic-com-card-bulk-orders-api
- description: Legacy v1 dispute (chargeback) submission and evidence.
  name: Lithic Chargeback API
  slug: lithic-com-chargeback-api
- description: Credit product configuration, extended credit, and prime rates.
  name: Lithic Credit Product API
  slug: lithic-com-credit-product-api
- description: Events API and webhook event subscription management.
  name: Lithic Event API
  slug: lithic-com-event-api
- description: External bank accounts used for ACH payments, with prenote and micro-deposit verification.
  name: Lithic External Bank Account API
  slug: lithic-com-external-bank-account-api
- description: Recording and reconciling payments that move outside of Lithic-initiated rails.
  name: Lithic External Payments API
  slug: lithic-com-external-payments-api
- description: Ledgered financial accounts, credit configuration, and account activity.
  name: Lithic Financial Account API
  slug: lithic-com-financial-account-api
- description: Fraud reporting on card transactions.
  name: Lithic Fraud Report API
  slug: lithic-com-fraud-report-api
- description: Card program funding event reporting.
  name: Lithic Funding Events API
  slug: lithic-com-funding-events-api
- description: Holds placed against financial account balances.
  name: Lithic Hold API
  slug: lithic-com-hold-api
- description: v2 managed disputes (read surface for Lithic-managed dispute handling).
  name: Lithic Managed Disputes API
  slug: lithic-com-managed-disputes-api
- description: Manual ledger adjustments and corrections.
  name: Lithic Management Operations API
  slug: lithic-com-management-operations-api
- description: Card network program metadata.
  name: Lithic Network Program API
  slug: lithic-com-network-program-api
- description: ACH payments between Lithic financial accounts and external bank accounts.
  name: Lithic Payment API
  slug: lithic-com-payment-api
- description: Registration of HTTP endpoints that receive Auth Stream Access (ASA) requests.
  name: Lithic Responder Endpoints API
  slug: lithic-com-responder-endpoints-api
- description: Daily settlement detail, summary, and network total reporting.
  name: Lithic Settlement Report API
  slug: lithic-com-settlement-report-api
- description: Financial account statements, line items, and loan tapes for credit products.
  name: Lithic Statements API
  slug: lithic-com-statements-api
- description: API status check.
  name: Lithic Status API
  slug: lithic-com-status-api
- description: Digital wallet tokenization (Apple Pay / Google Pay / Samsung Pay) lifecycle and decisioning.
  name: Lithic Tokenization API
  slug: lithic-com-tokenization-api
- description: Card transaction authorization, clearing, and simulation.
  name: Lithic Transaction API
  slug: lithic-com-transaction-api
- description: Fraud/AML case and queue management for flagged transactions.
  name: Lithic Transaction Monitoring API
  slug: lithic-com-transaction-monitoring-api
- description: The Transfer Limits API from Lithic — 1 operation(s) for transfer limits.
  name: Lithic Transfer Limits API
  slug: lithic-com-transfer-limits-api
artifact_total: 40
collections:
- collection_type: open
  name: Lithic API
  slug: open-lithic-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lithic-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lithic-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lithic-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lithic-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lithic-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lithic-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lithic
- group: company
  title: ''
  type: Website
  url: https://www.lithic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lithic.com
- group: commercial
  title: ''
  type: Plans
  url: plans/lithic-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lithic-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lithic-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lithic.com/blog
created: '2026-07-02'
description: Lithic is a card issuing and issuer-processor API platform for building virtual and physical card programs - authorization, clearing, KYC/KYB account holder onboarding, programmable authorization rules, real-time Auth Stream Access (ASA) decisioning, disputes, digital wallet tokenization, 3DS authentication, ACH payments, ledgered financial accounts, and settlement reporting. Lithic publishes a full OpenAPI 3.1 specification (github.com/lithic-com/lithic-openapi) backing official Node, Python, Go, Java, and Kotlin SDKs, with a sandbox at sandbox.lithic.com that mirrors production functionality.
finops:
- name: Lithic Com Finops
  service_category: Fintech and Payments
  slug: lithic-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lithic-com.png
layout: provider
modified: '2026-07-02'
name: Lithic
nav: Providers
network: true
overview: 'Lithic publishes 31 APIs on the [APIs.io](https://apis.io/) network, including 3DS API, Account API, Account Holder API, and 28 more. Tagged areas include Fintech, Card Issuing, Payments, Issuer Processor, and KYC.


  Lithic''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Lithic Com Plans Pricing
  plan_count: 4
  slug: lithic-com-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 13
  name: Lithic Com Rate Limits
  slug: lithic-com-rate-limits
score:
  band: thin
  composite: 39.8
  delta: -3.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lithic-com/refs/heads/main/screenshots/lithic-com-2026-07-25T225335.png
security:
- kind: authentication
  name: Lithic Com Authentication
  slug: lithic-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lithic Com Domain Security
  slug: lithic-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lithic Com Vulnerability Disclosure
  slug: lithic-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lithic Com Trust Center
  slug: lithic-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: lithic-com
tags:
- Fintech
- Card Issuing
- Payments
- Issuer Processor
- KYC
- Banking as a Service
website: https://www.lithic.com
---
