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
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Avenue Bank Agentic Access
  operation_count: 19
  slug: avenue-bank-agentic-access
  summary_line: 19 operations
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Avenue Bank Banking Account Balances API
  slug: avenue-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Avenue Bank Banking Account Direct Debits API
  slug: avenue-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Avenue Bank Banking Account Scheduled Payments API
  slug: avenue-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Avenue Bank Banking Account Transactions API
  slug: avenue-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Avenue Bank Banking Accounts API
  slug: avenue-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Avenue Bank Banking Payees API
  slug: avenue-bank-banking-payees-api
- description: Banking Product endpoints
  name: Avenue Bank Banking Products API
  slug: avenue-bank-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/avenue-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avenue-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avenuebank.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.avenuebank.com.au/news/
- group: operate
  title: ''
  type: Support
  url: https://www.avenuebank.com.au/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avenuebank.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avenuebank.com.au/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/avenuebank
- group: start
  title: ''
  type: SignUp
  url: https://application.avenuebank.com.au
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avenue-bank-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/avenue-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/avenue-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avenue-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avenue-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avenue-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avenue-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/avenue-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/avenue-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/avenue-bank-cds-banking-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: Avenue Bank Ltd (ABN 24 628 073 085, AFSL 520239) is an Australian Authorised Deposit-taking Institution (ADI) regulated by APRA, holding a full (unrestricted) banking licence granted in 2024 after operating as a Restricted ADI from 2021. Founded by Dale Hurley and Colin Porter (co-founders of CreditorWatch) and majority-backed by Sherman Ma's Liberty Financial Group as its largest strategic shareholder, Avenue is a digital business bank that is the first and only Australian bank specialising exclusively in bank guarantees for SMEs, alongside term deposits. As an ADI, Avenue is a designated data holder class under Australia's Consumer Data Right (CDR / Open Banking) and is therefore subject to the shared Data Standards Body (DSB) Consumer Data Standards Banking API surface (Get Products through Get Payees) that every ADI data holder implements verbatim under the /cds-au/v1 path. Avenue holds a permanent ACCC exemption (granted 6 June 2025, s56GD) covering the term-deposit aspect
  of its bank guarantee product, publishes no first-party developer portal, and a probe of its API host on 2026-07-21 returned HTTP 403 (WAF) rather than a CDS-conformant payload, so its live CDR data-holder surface is documented here against the standard but recorded as unverified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avenue-bank.png
layout: provider
mcp_servers:
- description: ''
  name: avenue-bank-mcp.yml
  slug: avenue-bank-mcpyml
modified: '2026-07-21'
name: Avenue Bank
nav: Providers
network: true
overview: 'Avenue Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Avenue Bank''s developer surface includes engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 56
scopes:
- name: Avenue Bank Scopes
  scope_count: 5
  slug: avenue-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 13.6
    developer_ergonomics: 21.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 31.0
  provenance:
    agentic_access: first-party
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avenue-bank/refs/heads/main/screenshots/avenue-bank-2026-07-21T114700.png
security:
- kind: authentication
  name: Avenue Bank Authentication
  slug: avenue-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Avenue Bank Domain Security
  slug: avenue-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avenue-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Business Banking
- Bank Guarantees
- Australia
- ADI
website: https://www.avenuebank.com.au/
---
