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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Connexis Cash Agentic Access
  operation_count: 6
  slug: connexis-cash-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 8
apis:
- description: A PSD2-compliant Account Information Service (AISP) API exposed by BNP Paribas Corporate and Institutional Banking. Third-party providers consume this REST/JSON API, which follows the STET PSD2 standa
  name: Connexis Cash PSD2 Account Information API (STET)
  slug: psd2-account-information
- description: A documented Strong Customer Authentication flow that BNP Paribas provides for Connexis Cash to satisfy PSD2 SCA requirements. TPPs integrate the SCA flow into their PSD2 journeys so that Connexis Cas
  name: Connexis Cash Strong Customer Authentication (SCA)
  slug: strong-authentication
- description: The Connexis Cash digital banking application itself. While not a public REST API, it is the user-facing platform that powers payment initiation, real-time tracking, reconciliation, account reporting,
  name: Connexis Cash Digital Banking Platform
  slug: digital-banking-platform
- description: The Accounts API from Connexis Cash — 2 operation(s) for accounts.
  name: Connexis Cash Accounts API
  slug: connexis-cash-accounts-api
- description: The Balances API from Connexis Cash — 1 operation(s) for balances.
  name: Connexis Cash Balances API
  slug: connexis-cash-balances-api
- description: The Beneficiaries API from Connexis Cash — 1 operation(s) for beneficiaries.
  name: Connexis Cash Beneficiaries API
  slug: connexis-cash-beneficiaries-api
- description: The Consents API from Connexis Cash — 1 operation(s) for consents.
  name: Connexis Cash Consents API
  slug: connexis-cash-consents-api
- description: The Transactions API from Connexis Cash — 1 operation(s) for transactions.
  name: Connexis Cash Transactions API
  slug: connexis-cash-transactions-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts API
  slug: open-connexis-cash-accounts-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Balances API
  slug: open-connexis-cash-balances-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Beneficiaries API
  slug: open-connexis-cash-beneficiaries-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Consents API
  slug: open-connexis-cash-consents-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP) Accounts Transactions API
  slug: open-connexis-cash-transactions-api
- collection_type: open
  name: BNP Paribas Connexis Cash - STET PSD2 Account Information (AISP)
  slug: open-connexis-cash
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/connexis-cash-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connexis-cash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connexis-cash-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/connexis-cash-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://cashmanagement.bnpparibas.com/solutions/digital-channels
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cib.bnpparibas.com/
- group: other
  title: ''
  type: Open Banking Tracker
  url: https://www.openbankingtracker.com/provider/connexis-cash
- group: other
  title: ''
  type: BNP Paribas CIB
  url: https://cib.bnpparibas/
- group: other
  title: ''
  type: Mobile App
  url: https://apps.apple.com/us/app/connexis-cash-mobile/id1053068521
- group: operate
  title: ''
  type: Support
  url: ''
created: '2024-01-01'
description: Connexis Cash is BNP Paribas's corporate digital banking and cash management platform. It gives multinational corporates a unified online channel for payment initiation, real-time payment tracking, account reporting, reconciliation, and liquidity management across BNP Paribas's global network. Connexis Cash also exposes PSD2-compliant Open Banking APIs through the BNP Paribas CIB developer portal so that third-party providers (TPPs) can retrieve account information and initiate payments on behalf of Connexis Cash users, as well as a Strong Customer Authentication (SCA) flow.
finops:
- name: Connexis Cash Finops
  service_category: API
  slug: connexis-cash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/connexis-cash.png
layout: provider
modified: '2026-04-28'
name: Connexis Cash
nav: Providers
network: true
overview: 'Connexis Cash publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balances API, Beneficiaries API, and 2 more. Tagged areas include Account Information, BNP Paribas, Cash Management, Corporate Banking, and Digital Banking.


  Connexis Cash''s developer surface includes authentication, support, and 7 more developer resources.'
plans:
- name: Connexis Cash Plans Pricing
  plan_count: 3
  slug: connexis-cash-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Connexis Cash Rate Limits
  slug: connexis-cash-rate-limits
scopes:
- name: Connexis Cash Scopes
  scope_count: 1
  slug: connexis-cash-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 30.5
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connexis-cash/refs/heads/main/screenshots/connexis-cash-2026-06-20T174906.png
security:
- kind: authentication
  name: Connexis Cash Authentication
  slug: connexis-cash-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Connexis Cash Domain Security
  slug: connexis-cash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connexis-cash
tags:
- Account Information
- BNP Paribas
- Cash Management
- Corporate Banking
- Digital Banking
- Liquidity Management
- Open Banking
- Payments
- PSD2
- SCA
- STET
website: https://cashmanagement.bnpparibas.com/solutions/digital-channels
---
