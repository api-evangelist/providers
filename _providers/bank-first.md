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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank First Agentic Access
  operation_count: 19
  slug: bank-first-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-bank-first-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-bank-first-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-bank-first-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-bank-first-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-bank-first-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-bank-first-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-bank-first-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bank-first-capability-edges.yml
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
  name: Bank First MCP Server
  slug: bank-first-mcp-server
modified: '2026-07-21'
name: Bank First
nav: Providers
network: true
overview: 'Bank First publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank First''s developer surface includes documentation, support, getting-started guide, authentication, and 22 more developer resources.'
random_paper: 1
scopes:
- name: Bank First Scopes
  scope_count: 7
  slug: bank-first-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 47.8
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
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
