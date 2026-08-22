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
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aib Group Uk Agentic Access
  operation_count: 12
  slug: aib-group-uk-agentic-access
  summary_line: 12 operations
api_count: 10
apis:
- description: Public, unauthenticated Open Banking Open Data API (v2.2) publishing Allied Irish Bank (GB) product reference data - personal current accounts, business current accounts, and unsecured SME loans - con
  name: AIB Group (UK) Open Data API
  slug: aib-group-uk-open-data-api
- description: 'OBIE Read/Write Account and Transaction Information API (AIS) v4.0 - account details, balances, transactions, standing orders, direct debits, and statements. FAPI-secured via OAuth2/OIDC consent with '
  name: AIB Group (UK) Accounts Information API
  slug: aib-group-uk-account-information-api
- description: 'OBIE Read/Write Payment Initiation API (PIS) v4.0 - domestic and scheduled payment initiation through a set-up, submit-after-consent, and status-retrieval flow. FAPI-secured via OAuth2/OIDC with PSD2 '
  name: AIB Group (UK) Payments Initiation API
  slug: aib-group-uk-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds API (CBPII) v4.0 - returns a yes/no confirmation of whether funds are available for a specified payment. FAPI-secured via OAuth2/OIDC with PSD2 strong customer au
  name: AIB Group (UK) Confirmation of Funds API
  slug: aib-group-uk-confirmation-of-funds-api
- description: OBIE Read/Write Variable Recurring Payments (VRP) API v4.0, including sweeping, letting authorised TPPs initiate a series of payments under a single long-lived consent. FAPI-secured via OAuth2/OIDC wi
  name: AIB Group (UK) Variable Recurring Payments API
  slug: aib-group-uk-variable-recurring-payments-api
- description: OBIE Dynamic Client Registration API v3.2, allowing authorised third-party providers to programmatically register client credentials using OBIE/eIDAS certificates before consuming the Read/Write APIs.
  name: AIB Group (UK) Dynamic Client Registration API
  slug: aib-group-uk-dynamic-client-registration-api
- description: Credit Cards Information API providing access to credit card account information under the Open Banking consent model.
  name: AIB Group (UK) Credit Cards Information API
  slug: aib-group-uk-credit-cards-information-api
- description: OBIE Event Notification Subscription API v4.0, letting TPPs manage subscriptions to real-time event notifications (aggregated polling / callbacks) for the Read/Write APIs.
  name: AIB Group (UK) Event Notification Subscription API
  slug: aib-group-uk-event-notification-subscription-api
- description: OBIE Aggregated Event Polling API v4.0, allowing TPPs to poll for aggregated event notifications relating to Account Information and Payment consents.
  name: AIB Group (UK) Aggregated Event Polling API
  slug: aib-group-uk-aggregated-event-polling-api
- description: FCA Service Metrics API for Business Current Accounts (BCA), publishing the service availability and performance metrics AIB Group (UK) is required to report under FCA rules.
  name: AIB Group (UK) FCA Service Metrics (BCA) API
  slug: aib-group-uk-fca-service-metrics-bca-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Data API
  slug: open-aib-group-uk-open-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aib-group-uk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aib-group-uk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aib-group-uk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aib-group-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aib-group-uk-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aib-group-uk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aib-group-uk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aib-group-uk-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aib-group-uk-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aib-group-uk-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aib-group-uk-open-data-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/aib-group-uk-open-data-discovery.md
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.aibgb.co.uk/getting-started-gb
- group: start
  title: ''
  type: SignUp
  url: https://developer.aibgb.co.uk/user/register
- group: company
  title: ''
  type: Blog
  url: https://developer.aibgb.co.uk/blog
- group: company
  title: ''
  type: Website
  url: https://www.aibgb.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aibgb.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aibgb.co.uk/apis
- group: operate
  title: ''
  type: Support
  url: https://developer.aibgb.co.uk/faq-page
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.aibgb.co.uk/site-legal-notice-gb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.aibgb.co.uk/developer-portal-privacy-statement-GB
- group: auth
  title: ''
  type: Compliance
  url: https://developer.aibgb.co.uk/fca-service-metrics-bca-gb/apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aib
created: '2026-07-23'
description: AIB Group (UK) p.l.c. is a UK bank incorporated in Northern Ireland (registered number NI018800, registered office 92 Ann Street, Belfast BT1 3HH), authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority. It trades as Allied Irish Bank (GB) and Allied Irish Bank (GB) Savings Direct, and is the UK banking subsidiary of the Irish AIB Group plc. As one of the CMA9 banks mandated under the UK Competition and Markets Authority's Open Banking order, it runs a public developer portal publishing UK Open Banking APIs conformant to the Open Banking Implementation Entity (OBIE) standards - a public, unauthenticated Open Data API (v2.2) exposing personal current account, business current account, and unsecured SME loan product reference data, alongside the FAPI-secured Read/Write family (Account and Transaction Information, Payment Initiation, Confirmation of Funds, and Variable Recurring Payments to OBIE
  v4.0) accessed under OAuth2/OIDC consent with PSD2 strong customer authentication, dynamic client registration, and a sandbox for onboarding and testing before production.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: AIB Group (UK)
nav: Providers
network: true
overview: 'AIB Group (UK) publishes 1 API on the [APIs.io](https://apis.io/) network: Open Data API. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  AIB Group (UK)''s developer surface includes authentication, getting-started guide, signup flow, engineering blog, documentation, support, and 17 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 44.9
  delta: 6.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 37.1
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 64.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/aib-group-uk/refs/heads/main/screenshots/aib-group-uk-2026-07-25T195342.png
security:
- kind: authentication
  name: Aib Group Uk Authentication
  slug: aib-group-uk-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Aib Group Uk Domain Security
  slug: aib-group-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aib-group-uk
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Northern Ireland
website: https://www.aibgb.co.uk/
---
