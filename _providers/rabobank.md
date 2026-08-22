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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: PSD2-compliant Account Information Service. Returns account lists, balances, and transaction history for Rabobank payment accounts after the account-holder grants explicit consent. Aligned with the Be
  name: Rabobank Account Information API (PSD2 AIS)
  slug: account-information
- description: PSD2-compliant Payment Initiation Service. Allows licensed PISPs to initiate SEPA Credit Transfers, SEPA Instant Credit Transfers, and cross-border payments from a customer's Rabobank account after St
  name: Rabobank Payment Initiation API (PSD2 PIS)
  slug: payment-initiation
- description: PSD2-compliant Funds Confirmation Service. Card-issuer payment service providers (CBPIIs) can confirm whether a specific amount is available on a Rabobank payment account at the time of a card-based p
  name: Rabobank Funds Confirmation API (PSD2 PIIS / CBPII)
  slug: funds-confirmation
- description: Commercial premium API for corporate cash management - initiating SEPA Credit Transfers and SEPA Instant Credit Transfers on a contracted Rabobank corporate account without per-payment customer SCA, i
  name: Rabobank Premium Payments / SEPA Credit Transfer API
  slug: premium-payments
- description: Real-time event-notification API delivering payment, account, and consent state changes to a registered callback or webhook endpoint for integrated corporate and TPP applications.
  name: Rabobank Notifications API
  slug: notifications
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rabobank-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rabobank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rabobank
- group: company
  title: ''
  type: Website
  url: https://www.rabobank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developer.rabobank.com/
- group: start
  title: ''
  type: LegacyDeveloperPortal
  url: https://developer.rabobank.nl/
- group: other
  title: ''
  type: Standards
  url: https://www.berlin-group.org/nextgenpsd2-downloads
created: '2026-05-05'
description: Rabobank is a Dutch multinational banking and financial services company organized as a cooperative with a strong focus on the food and agriculture sector. It serves retail, business, corporate, and wholesale customers in the Netherlands and operates a global Food & Agribusiness practice through Rabobank Wholesale & Rural and the Rabobank Group internationally. Rabobank publishes a developer portal at docs.developer.rabobank.com (legacy URL developer.rabobank.nl redirects there) exposing PSD2-mandated open banking APIs (Account Information, Payment Initiation, Funds Confirmation) as well as Premium / Beyond-PSD2 commercial APIs for corporate cash management and notifications, with sandbox endpoints for development and a regulated production tier under PSD2 Strong Customer Authentication. Underlying schemes are aligned with the Berlin Group NextGenPSD2 XS2A Framework.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rabobank.png
layout: provider
modified: '2026-05-09'
name: Rabobank
nav: Providers
network: true
overview: Rabobank publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, Banking, Open Banking, and PSD2.
random_paper: 13
score:
  band: minimal
  composite: 6.1
  delta: -3.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rabobank/refs/heads/main/screenshots/rabobank-2026-06-20T192506.png
security:
- kind: domain-security
  name: Rabobank Domain Security
  slug: rabobank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rabobank
tags:
- Financial
- Banks
- Banking
- Open Banking
- PSD2
- Berlin Group
- Agriculture
- Cooperative
- European Banking
- Netherlands
website: https://www.rabobank.com/
---
