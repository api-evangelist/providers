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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: St George Bank Agentic Access
  operation_count: 19
  slug: st-george-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: St.George Bank Banking Account Balances API
  slug: st-george-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: St.George Bank Banking Account Direct Debits API
  slug: st-george-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: St.George Bank Banking Account Scheduled Payments API
  slug: st-george-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: St.George Bank Banking Account Transactions API
  slug: st-george-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: St.George Bank Banking Accounts API
  slug: st-george-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: St.George Bank Banking Payees API
  slug: st-george-bank-banking-payees-api
- description: Banking Product endpoints
  name: St.George Bank Banking Products API
  slug: st-george-bank-banking-products-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/st-george-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/st-george-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stgeorge.com.au/
- group: start
  title: ''
  type: Portal
  url: https://www.stgeorge.com.au/online-services/open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://www.stgeorge.com.au/online-services/open-banking/error-mapping
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stgeorge.com.au/privacy/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stgeorge.com.au/help/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.stgeorge.com.au/online-services/security-centre
- group: other
  title: ''
  type: Overlay
  url: overlays/st-george-bank-cds-banking-products-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/st-george-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/st-george-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/st-george-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/st-george-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/st-george-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.stgeorge.com.au/content/dam/public/wbc/documents/pdf/aw/WBC_CDR_Policy.pdf
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/st-george-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/st-george-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/st-george-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/st-george-bank-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/st-george-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.westpac.com.au/security/how-to-report/responsible-disclosure/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: St.George Bank is one of Australia's largest retail and business banks and a division of Westpac Banking Corporation (ASX:WBC), one of the country's "Big Four" banks. Originally a New South Wales building society that grew into an independent ADI, St.George merged into the Westpac Group in 2008 and today operates as a Westpac brand alongside BankSA, Bank of Melbourne and RAMS. As an authorised deposit-taking institution it is a designated Data Holder under Australia's Consumer Data Right (CDR / Open Banking), and therefore exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the consented, ADR-gated CDR data-sharing APIs. St.George does not operate a broad public developer portal beyond its CDR Open Banking surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/st-george-bank.png
layout: provider
mcp_servers:
- description: ''
  name: st-george-bank-mcp.yml
  slug: st-george-bank-mcpyml
modified: '2026-07-21'
name: St.George Bank
nav: Providers
network: true
overview: 'St.George Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  St.George Bank''s developer surface includes developer portal, documentation, support, authentication, and 19 more developer resources.'
random_paper: 6
scopes:
- name: St George Bank Scopes
  scope_count: 9
  slug: st-george-bank-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 46.5
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 18.4
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 84.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/st-george-bank/refs/heads/main/screenshots/st-george-bank-2026-07-21T114749.png
security:
- kind: authentication
  name: St George Bank Authentication
  slug: st-george-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: St George Bank Domain Security
  slug: st-george-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: St George Bank Vulnerability Disclosure
  slug: st-george-bank-vulnerability-disclosure
  summary_line: disclosure policy published
slug: st-george-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- Westpac Group
website: https://www.stgeorge.com.au/
---
