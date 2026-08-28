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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Macquarie Bank Agentic Access
  operation_count: 19
  slug: macquarie-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 9
apis:
- description: Macquarie's connectivity / data APIs for business, documented through the registered Macquarie developer portal, let approved businesses and software partners automate account information retrieval an
  name: Macquarie Connectivity & Data API
  slug: macquarie-connectivity-data-api
- description: Macquarie's DEFT payments platform, surfaced through the registered Macquarie developer portal, lets businesses build branded payment experiences with tokenised credit card, bank account and direct de
  name: Macquarie DEFT Payments API
  slug: macquarie-deft-payments-api
- description: Banking Account Balance endpoints
  name: Macquarie Bank Banking Account Balances API
  slug: macquarie-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Macquarie Bank Banking Account Direct Debits API
  slug: macquarie-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Macquarie Bank Banking Account Scheduled Payments API
  slug: macquarie-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Macquarie Bank Banking Account Transactions API
  slug: macquarie-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Macquarie Bank Banking Accounts API
  slug: macquarie-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Macquarie Bank Banking Payees API
  slug: macquarie-bank-banking-payees-api
- description: Banking Product endpoints
  name: Macquarie Bank Banking Products API
  slug: macquarie-bank-banking-products-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-macquarie-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-macquarie-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-macquarie-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-macquarie-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-macquarie-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-macquarie-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-macquarie-bank-banking-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macquarie-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/macquarie-bank-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/macquarie-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/macquarie-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/macquarie-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/macquarie-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/macquarie-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.macquariebank.io/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/macquarie-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/macquarie-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/macquarie-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/macquarie-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/macquarie-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/macquarie-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/macquarie-bank-sandbox.yml
- group: company
  title: ''
  type: Website
  url: https://www.macquarie.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.macquariebank.io/devportal/
- group: docs
  title: ''
  type: Documentation
  url: https://www.macquarie.com.au/digital-banking/open-banking.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/macquarie-group/
- group: start
  title: ''
  type: CDRRegister
  url: https://www.cdr.gov.au/find-a-provider
- group: operate
  title: ''
  type: Support
  url: https://www.macquarie.com.au/help.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.macquarie.com.au/privacy-and-security.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.macquarie.com.au/terms-and-conditions.html
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/macquarie-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.macquarie.com/us/en/disclosures/cybersecurity.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.macquarie.com/us/en/disclosures/cybersecurity.html
- group: start
  title: ''
  type: SignUp
  url: https://developer.macquariebank.io/devportal/
created: '2026-07-20'
description: Macquarie Bank Limited is an Australian authorised deposit-taking institution (ADI) and the retail and business banking arm of Macquarie Group Limited, the ASX-listed (ASX:MQG) global financial services group headquartered in Sydney. It is not a mutual or customer-owned bank; it is a wholly-owned, shareholder-owned subsidiary of a publicly listed parent. Its digital bank offers transaction and savings accounts, home loans, credit and charge cards, term deposits, overdrafts and business lending. As a designated data holder under Australia's Consumer Data Right (CDR / Open Banking), Macquarie Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards (CDS), alongside accredited-data-recipient data sharing and a registered developer portal that documents its DEFT payments platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macquarie-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Macquarie Bank MCP Server
  slug: macquarie-bank-mcp-server
modified: '2026-07-21'
name: Macquarie Bank
nav: Providers
network: true
overview: 'Macquarie Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Macquarie Bank''s developer surface includes authentication, sandbox, documentation, support, API reference, signup flow, and 23 more developer resources.'
random_paper: 2
scopes:
- name: Macquarie Bank Scopes
  scope_count: 10
  slug: macquarie-bank-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 43.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 51.8
    discoverability: 64.8
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 43.9
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
    score: 64.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macquarie-bank/refs/heads/main/screenshots/macquarie-bank-2026-07-21T130910.png
security:
- kind: authentication
  name: Macquarie Bank Authentication
  slug: macquarie-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Macquarie Bank Domain Security
  slug: macquarie-bank-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Macquarie Bank Vulnerability Disclosure
  slug: macquarie-bank-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: macquarie-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
- Payments
website: https://www.macquarie.com.au/
---
