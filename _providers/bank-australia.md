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
  score: 38.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Australia Agentic Access
  operation_count: 19
  slug: bank-australia-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bank Australia Banking Account Balances API
  slug: bank-australia-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bank Australia Banking Account Direct Debits API
  slug: bank-australia-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bank Australia Banking Account Scheduled Payments API
  slug: bank-australia-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bank Australia Banking Account Transactions API
  slug: bank-australia-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bank Australia Banking Accounts API
  slug: bank-australia-banking-accounts-api
- description: Banking Payee endpoints
  name: Bank Australia Banking Payees API
  slug: bank-australia-banking-payees-api
- description: Banking Product endpoints
  name: Bank Australia Banking Products API
  slug: bank-australia-banking-products-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-australia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankaust.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankaust.com.au/support/open-banking/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankaust.com.au/support/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/bankaust
- group: company
  title: ''
  type: Blog
  url: https://www.bankaust.com.au/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankaust.com.au/support/website-security-and-privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankaust.com.au/support/disclosures
- group: operate
  title: ''
  type: Support
  url: https://www.bankaust.com.au/support
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankaust.com.au/status
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-australia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-australia-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-australia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-australia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-australia-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-australia-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-australia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-australia-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bank-australia-lookup-banking-products.md
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-australia-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-australia-cds-banking-overlay.yaml
created: '2026-07-20'
description: 'Bank Australia is a customer-owned (mutual) bank headquartered in Collingwood, Victoria, tracing its origins to the 1957 CSIRO Co-operative Credit Society and formed through the merger of more than 70 credit unions and co-operatives (via mecu and bankmecu) before adopting the Bank Australia name in 2015. As an APRA-regulated authorised deposit-taking institution (ADI) and a certified B Corporation, it is owned by its customers rather than shareholders and is known for responsible, fossil-fuel-free lending. Under Australia''s Consumer Data Right (CDR / Open Banking), Bank Australia operates as a data holder: it exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, and offers accredited-recipient consumer data sharing to eligible customers through its app and internet banking.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-australia.png
layout: provider
mcp_servers:
- description: ''
  name: bank-australia-mcp.yml
  slug: bank-australia-mcpyml
modified: '2026-07-21T12:30:00Z'
name: Bank Australia
nav: Providers
network: true
overview: 'Bank Australia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Bank Australia''s developer surface includes documentation, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 93
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.3
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 40.2
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
    score: 39.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-australia/refs/heads/main/screenshots/bank-australia-2026-07-21T114657.png
security:
- kind: authentication
  name: Bank Australia Authentication
  slug: bank-australia-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Bank Australia Domain Security
  slug: bank-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bank-australia
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Mutual Bank
website: https://www.bankaust.com.au/
---
