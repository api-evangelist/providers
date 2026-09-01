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
  name: Judo Bank Agentic Access
  operation_count: 19
  slug: judo-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- description: Banking Account Balance endpoints
  name: Judo Bank Banking Account Balances API
  slug: judo-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Judo Bank Banking Account Direct Debits API
  slug: judo-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Judo Bank Banking Account Scheduled Payments API
  slug: judo-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Judo Bank Banking Account Transactions API
  slug: judo-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Judo Bank Banking Accounts API
  slug: judo-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Judo Bank Banking Payees API
  slug: judo-bank-banking-payees-api
- description: Banking Product endpoints
  name: Judo Bank Banking Products API
  slug: judo-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-judo-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-judo-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-judo-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-judo-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-judo-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-judo-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-judo-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/judo-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/judo-bank-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/judo-bank-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/judo-bank-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/judo-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/judo-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/judo-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/judo-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/judo-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/judo-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/judo-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/judo-bank-product-lookup.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/judo-bank-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/judo-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.judo.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://www.judo.bank/open-banking/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.judo.bank/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/judobank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/judobank
created: '2026-07-20'
description: Judo Bank (Judo Capital Holdings Ltd) is an Australian challenger bank founded in 2016 and headquartered in Melbourne, purpose-built to serve small and medium-sized enterprises (SMEs) with relationship-led business lending alongside personal and business term deposits. It was the first new domestically-owned bank in decades to be granted a full, unrestricted authorised deposit-taking institution (ADI) licence by APRA, in April 2019, and has been publicly listed on the Australian Securities Exchange (ticker ASX JDO) since November 2021 - it is a for-profit, shareholder-owned bank, not a customer-owned mutual. As a designated ADI and data holder under Australia's Consumer Data Right (CDR / Open Banking) regime, Judo Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, while authenticated consumer-data sharing is governed by the accredited data recipient (ADR) model rather than an open self-serve
  developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/judo-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Judo Bank MCP Server
  slug: judo-bank-mcp-server
modified: '2026-07-22'
name: Judo Bank
nav: Providers
network: true
overview: 'Judo Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Judo Bank''s developer surface includes authentication, documentation, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.4
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
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/judo-bank/refs/heads/main/screenshots/judo-bank-2026-07-21T114730.png
security:
- kind: authentication
  name: Judo Bank Authentication
  slug: judo-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Judo Bank Domain Security
  slug: judo-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: judo-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- SME Lending
- Product Reference Data
website: https://www.judo.bank/
---
