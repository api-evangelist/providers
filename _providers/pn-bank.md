---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    consent_identity: true
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
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pn Bank Agentic Access
  operation_count: 19
  slug: pn-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: P&N Bank Banking Account Balances API
  slug: pn-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: P&N Bank Banking Account Direct Debits API
  slug: pn-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: P&N Bank Banking Account Scheduled Payments API
  slug: pn-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: P&N Bank Banking Account Transactions API
  slug: pn-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: P&N Bank Banking Accounts API
  slug: pn-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: P&N Bank Banking Payees API
  slug: pn-bank-banking-payees-api
- description: Banking Product endpoints
  name: P&N Bank Banking Products API
  slug: pn-bank-banking-products-api
artifact_total: 12
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://public.cdr-api.pnbank.com.au/cds-au/v1/discovery/status
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pn-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pn-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pn-bank-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pnbank.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pn-bank-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pn-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pn-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pn-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pn-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pn-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pn-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pn-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pn-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pn-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pn-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/pn-bank-get-products.md
- group: company
  title: ''
  type: Website
  url: https://www.pnbank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pnbank.com.au/help-and-support/open-banking/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pnbank.com.au/important-information/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pnbank.com.au/important-information/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.pnbank.com.au/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/p&n-bank
created: '2026-07-20'
description: P&N Bank is the retail banking brand of Police & Nurses Limited (ABN 69 087 651 876, AFSL/Australian Credit Licence 240701), a customer-owned (mutual) bank owned by its members rather than shareholders and one of Western Australia's largest locally based banks, headquartered in Perth. It grew out of the Police & Nurses Credit Society and today sits within the broader P&N Group, which also operates the bcu brand on the New South Wales / Queensland east coast, offering everyday transaction and savings accounts, term deposits, home and personal loans, credit cards, and insurance. As an Authorised Deposit-taking Institution (ADI) it participates in Australia's Consumer Data Right (CDR / Open Banking), exposing a public, unauthenticated Product Reference Data (PRD) API built to the Data Standards Body (DSB) Consumer Data Standards; consumer data sharing beyond product reference data requires accredited data recipient status and the CDR OAuth2/OIDC FAPI authorization model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pn-bank.png
layout: provider
mcp_servers:
- description: ''
  name: pn-bank-mcp.yml
  slug: pn-bank-mcpyml
modified: '2026-07-21T17:00:00Z'
name: P&N Bank
nav: Providers
network: true
overview: 'P&N Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  P&N Bank''s developer surface includes authentication, documentation, support, and 20 more developer resources.'
random_paper: 99
score:
  band: thin
  composite: 37.2
  delta: -0.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.2
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pn-bank/refs/heads/main/screenshots/pn-bank-2026-07-21T114741.png
security:
- kind: authentication
  name: Pn Bank Authentication
  slug: pn-bank-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Pn Bank Domain Security
  slug: pn-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pn Bank Vulnerability Disclosure
  slug: pn-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pn-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Customer Owned
- Product Reference Data
website: https://www.pnbank.com.au/
---
