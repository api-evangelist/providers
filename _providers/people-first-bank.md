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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: People First Bank Agentic Access
  operation_count: 19
  slug: people-first-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- description: Banking Account Balance endpoints
  name: People First Bank Banking Account Balances API
  slug: people-first-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: People First Bank Banking Account Direct Debits API
  slug: people-first-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: People First Bank Banking Account Scheduled Payments API
  slug: people-first-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: People First Bank Banking Account Transactions API
  slug: people-first-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: People First Bank Banking Accounts API
  slug: people-first-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: People First Bank Banking Payees API
  slug: people-first-bank-banking-payees-api
- description: Banking Product endpoints
  name: People First Bank Banking Products API
  slug: people-first-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-people-first-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-people-first-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-people-first-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-people-first-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-people-first-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-people-first-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-people-first-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/people-first-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/people-first-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/people-first-bank-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/people-first-bank-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/people-first-bank-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/people-first-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/people-first-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/people-first-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/people-first-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/people-first-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/people-first-bank-cds-banking-products-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/people-first-bank-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.peoplefirstbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.peoplefirstbank.com.au/help-and-support/open-banking/open-banking-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.peoplefirstbank.com.au/help-and-support/open-banking
- group: start
  title: ''
  type: GettingStarted
  url: https://www.peoplefirstbank.com.au/help-and-support/open-banking/open-banking-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#consumer-data-standards-banking-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/people-first-bank
- group: company
  title: ''
  type: Blog
  url: https://www.peoplefirstbank.com.au/help-and-support/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peoplefirstbank.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peoplefirstbank.com.au/disclaimer
- group: operate
  title: ''
  type: Support
  url: https://www.peoplefirstbank.com.au/help-and-support/contact-us
created: '2026-07-20'
description: People First Bank is an Australian customer-owned mutual bank, trading name of Heritage and People's Choice Ltd (ABN 11 087 651 125), formed from the 2023 merger of Heritage Bank and People's Choice Credit Union and carrying more than 150 years of combined mutual heritage. As a B Corp certified, member-owned authorised deposit-taking institution (ADI), it offers everyday transaction and savings accounts, home, personal and car loans, and insurance across digital channels and a national branch network. Under Australia's Consumer Data Right (CDR / open banking), the bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body Consumer Data Standards; consumer data sharing beyond PRD runs through the accredited data recipient model secured with OAuth2/OIDC (FAPI) rather than a general-purpose public developer platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/people-first-bank.png
layout: provider
mcp_servers:
- description: ''
  name: People First Bank MCP Server
  slug: people-first-bank-mcp-server
modified: '2026-07-21'
name: People First Bank
nav: Providers
network: true
overview: 'People First Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  People First Bank''s developer surface includes authentication, documentation, getting-started guide, API reference, engineering blog, support, and 17 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 36.6
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
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/people-first-bank/refs/heads/main/screenshots/people-first-bank-2026-07-21T114746.png
security:
- kind: authentication
  name: People First Bank Authentication
  slug: people-first-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: People First Bank Domain Security
  slug: people-first-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: people-first-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.peoplefirstbank.com.au/
---
