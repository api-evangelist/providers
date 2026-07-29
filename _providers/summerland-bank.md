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
  name: Summerland Bank Agentic Access
  operation_count: 19
  slug: summerland-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Summerland Bank Banking Account Balances API
  slug: summerland-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Summerland Bank Banking Account Direct Debits API
  slug: summerland-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Summerland Bank Banking Account Scheduled Payments API
  slug: summerland-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Summerland Bank Banking Account Transactions API
  slug: summerland-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Summerland Bank Banking Accounts API
  slug: summerland-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Summerland Bank Banking Payees API
  slug: summerland-bank-banking-payees-api
- description: Banking Product endpoints
  name: Summerland Bank Banking Products API
  slug: summerland-bank-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/summerland-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/summerland-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.summerland.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.summerland.com.au/services/digital-and-payments/open-banking/
- group: docs
  title: ''
  type: Documentation
  url: https://www.summerland.com.au/services/digital-and-payments/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/summerlandbank
- group: company
  title: ''
  type: Blog
  url: https://www.summerland.com.au/about-us/news-insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.summerland.com.au/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.summerland.com.au/legal-and-disclosure-documents/
- group: operate
  title: ''
  type: Support
  url: https://www.summerland.com.au/contact-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.summerland.com.au/services/digital-and-payments/open-banking/
- group: auth
  title: ''
  type: Authentication
  url: authentication/summerland-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/summerland-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/summerland-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/summerland-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/summerland-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/summerland-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/summerland-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/summerland-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/summerland-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/summerland-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/summerland-bank-product-reference-data.md
created: '2026-07-20'
description: 'Summerland Bank is a customer-owned (mutual) bank based in Lismore in the Northern Rivers region of New South Wales, Australia, tracing its origins to the former Summerland Credit Union (Summerland Financial Services Limited, ABN 21 087 650 360, AFSL and Australian Credit Licence 241167) and rebranded as Summerland Bank in 2023. As an APRA-regulated authorised deposit-taking institution (ADI) and certified B Corporation, it is owned by its customers rather than shareholders and has announced plans to merge with fellow customer-owned Regional Australia Bank. Under Australia''s Consumer Data Right (CDR / Open Banking), Summerland Bank operates as a data holder: it exposes a live, public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, and offers accredited-recipient consumer data sharing to eligible customers through its app and internet banking under the ACCC/OAIC-governed CDR regime.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/summerland-bank.png
layout: provider
mcp_servers:
- description: ''
  name: summerland-bank-mcp.yml
  slug: summerland-bank-mcpyml
modified: '2026-07-21'
name: Summerland Bank
nav: Providers
network: true
overview: 'Summerland Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Summerland Bank''s developer surface includes documentation, engineering blog, support, getting-started guide, authentication, and 18 more developer resources.'
random_paper: 74
scopes:
- name: Summerland Bank Scopes
  scope_count: 5
  slug: summerland-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 40.7
  delta: -5.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.0
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 46.1
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
    score: 60.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/summerland-bank/refs/heads/main/screenshots/summerland-bank-2026-07-21T114749.png
security:
- kind: authentication
  name: Summerland Bank Authentication
  slug: summerland-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Summerland Bank Domain Security
  slug: summerland-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: summerland-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Mutual Bank
website: https://www.summerland.com.au/
---
