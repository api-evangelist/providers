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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 36.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Hsbc Australia Agentic Access
  operation_count: 19
  slug: hsbc-australia-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 8
apis:
- description: HSBC Group's global developer portal (develop.hsbc.com) documents commercial / corporate-banking APIs available to HSBC's business and corporate clients, alongside Open Banking APIs for non-Australian
  name: HSBC Developer Portal - Commercial APIs (HSBC Group, partner-gated)
  slug: hsbc-developer-portal-commercial-apis
- description: Banking Account Balance endpoints
  name: HSBC Bank Australia Banking Account Balances API
  slug: hsbc-australia-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: HSBC Bank Australia Banking Account Direct Debits API
  slug: hsbc-australia-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: HSBC Bank Australia Banking Account Scheduled Payments API
  slug: hsbc-australia-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: HSBC Bank Australia Banking Account Transactions API
  slug: hsbc-australia-banking-account-transactions-api
- description: Banking Account endpoints
  name: HSBC Bank Australia Banking Accounts API
  slug: hsbc-australia-banking-accounts-api
- description: Banking Payee endpoints
  name: HSBC Bank Australia Banking Payees API
  slug: hsbc-australia-banking-payees-api
- description: Banking Product endpoints
  name: HSBC Bank Australia Banking Products API
  slug: hsbc-australia-banking-products-api
arazzos:
- description: Browse the HSBC Bank Australia public Consumer Data Right Product Reference Data catalog, then fetch the full detail of the first product returned. Both operations are public and unauthenticated on th
  name: HSBC Australia CDR - Browse Products
  slug: hsbc-australia-browse-products
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-hsbc-australia-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-hsbc-australia-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-hsbc-australia-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-hsbc-australia-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-hsbc-australia-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-hsbc-australia-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-hsbc-australia-banking-products-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hsbc-australia-cds-banking-products-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hsbc-australia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hsbc.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://develop.hsbc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hsbc.com.au/help/open-banking/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hsbc.com.au/help/open-banking/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hsbc.com.au/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hsbc.com.au/legal/consumer-data-right-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hsbc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hsbc
- group: operate
  title: ''
  type: Support
  url: mailto:openbankingsupport@hsbc.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hsbc-australia-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/hsbc-australia-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/hsbc-australia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hsbc-australia-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hsbc-australia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hsbc-australia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hsbc-australia-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hsbc-australia-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hsbc-australia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hsbc-australia-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/hsbc-australia-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hsbc-australia-browse-products.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hsbc-australia-agentic-access.yml
created: '2026-07-20'
description: HSBC Bank Australia Limited is the Australian banking subsidiary of the global HSBC Group (HSBC Holdings plc), operating as an Authorised Deposit-taking Institution (ADI) regulated by APRA and ASIC. It is a wholly owned, shareholder-owned bank (not a customer-owned mutual) offering home loans, everyday and savings accounts, credit cards, term deposits, and business and international banking across Australia. As a designated data holder under Australia's Consumer Data Right (CDR / Open Banking), HSBC Australia exposes a public, unauthenticated Product Reference Data (PRD) API plus the full authenticated CDR Banking surface - accounts, balances, transactions, direct debits, scheduled payments, and payees - conforming to the DSB Consumer Data Standards CDR Banking API (v1.36.0). The public product endpoints are on https://public.ob.hsbc.com.au/cds-au/v1 and the consumer-authorized endpoints on the MTLS host https://mtls.ob.hsbc.com.au/cds-au/v1, accessible only to Accredited Data
  Recipients under the CDR ADR model. HSBC is presently a data holder only and is not accredited to receive third-party banking data. Beyond the Australian CDR surface, HSBC Group operates a global developer portal at develop.hsbc.com covering commercial/corporate banking APIs and non-Australian Open Banking markets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hsbc-australia.png
layout: provider
mcp_servers:
- description: ''
  name: HSBC Bank Australia MCP Server
  slug: hsbc-bank-australia-mcp-server
modified: '2026-07-21'
name: HSBC Bank Australia
nav: Providers
network: true
overview: 'HSBC Bank Australia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  HSBC Bank Australia''s developer surface includes documentation, getting-started guide, support, authentication, and 21 more developer resources.'
random_paper: 20
scopes:
- name: Hsbc Australia Scopes
  scope_count: 10
  slug: hsbc-australia-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 46.4
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 49.7
    developer_ergonomics: 53.0
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 45.7
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
    score: 70.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hsbc-australia/refs/heads/main/screenshots/hsbc-australia-2026-07-21T114727.png
security:
- kind: authentication
  name: Hsbc Australia Authentication
  slug: hsbc-australia-authentication
  summary_line: none/openIdConnect/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Hsbc Australia Domain Security
  slug: hsbc-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hsbc-australia
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
website: https://www.hsbc.com.au/
---
