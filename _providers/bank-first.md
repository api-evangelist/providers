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
  name: Bank First Agentic Access
  operation_count: 19
  slug: bank-first-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bank First Banking Account Balances API
  slug: bank-first-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bank First Banking Account Direct Debits API
  slug: bank-first-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bank First Banking Account Scheduled Payments API
  slug: bank-first-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bank First Banking Account Transactions API
  slug: bank-first-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bank First Banking Accounts API
  slug: bank-first-banking-accounts-api
- description: Banking Payee endpoints
  name: Bank First Banking Payees API
  slug: bank-first-banking-payees-api
- description: Banking Product endpoints
  name: Bank First Banking Products API
  slug: bank-first-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-first-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-first-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankfirst.com.au/
- group: company
  title: ''
  type: About
  url: https://www.bankfirst.com.au/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankfirst.com.au/open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankfirst.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankfirst.com.au/disclosure-documents
- group: operate
  title: ''
  type: Support
  url: https://www.bankfirst.com.au/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bankfirst.com.au/open-banking
- group: auth
  title: ''
  type: Compliance
  url: https://www.bankfirst.com.au/cdr-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-first
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-first-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-first-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-first-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-first-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-first-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-first-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-first-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-first-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-first-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-first-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-first-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-first-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: Bank First is an Australian customer-owned mutual bank headquartered in Hawthorn East, Victoria. Founded in 1972 as VTU Credit Union by members of the Victorian Teachers Union and rebranded from Victoria Teachers Mutual Bank in December 2017, it is owned by its 90,000-plus members rather than external shareholders and serves the education and healthcare communities with savings, loans, and insurance. As an Authorised Deposit-taking Institution, Bank First is a data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes a public, unauthenticated Product Reference Data API built to the Data Standards Body Consumer Data Standards, alongside an accreditation-gated consumer data sharing surface for Accredited Data Recipients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-first.png
layout: provider
mcp_servers:
- description: ''
  name: bank-first-mcp.yml
  slug: bank-first-mcpyml
modified: '2026-07-21'
name: Bank First
nav: Providers
network: true
overview: 'Bank First publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank First''s developer surface includes documentation, support, getting-started guide, authentication, and 21 more developer resources.'
random_paper: 25
scopes:
- name: Bank First Scopes
  scope_count: 7
  slug: bank-first-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 46.0
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 49.2
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
    score: 77.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-first/refs/heads/main/screenshots/bank-first-2026-07-21T114722.png
security:
- kind: authentication
  name: Bank First Authentication
  slug: bank-first-authentication
  summary_line: none/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Bank First Domain Security
  slug: bank-first-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bank-first
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.bankfirst.com.au/
---
