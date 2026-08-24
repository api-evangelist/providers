---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Tsb Bank Agentic Access
  operation_count: 31
  slug: tsb-bank-agentic-access
  summary_line: 31 operations · 6 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: TSB's public, unauthenticated Open Data API conformant to the OBIE Open Data API Standard, exposing reference data for ATMs, branches, personal current accounts, business current accounts, unsecured S
  name: TSB Open Data API
  slug: tsb-open-data-api
- description: TSB's OBIE Read/Write Account and Transaction Information (AIS) API, providing authorised third-party providers read access to account, balance, transaction, beneficiary, standing order, direct debit,
  name: TSB Account and Transaction Information API (AIS)
  slug: tsb-account-transaction-information-api
- description: TSB's OBIE Read/Write Payment Initiation (PIS) API, enabling authorised third-party providers to initiate domestic and scheduled payments and standing orders on behalf of consenting customers. FAPI-se
  name: TSB Payment Initiation API (PIS)
  slug: tsb-payment-initiation-api
- description: TSB's OBIE Read/Write Confirmation of Funds (CBPII) API, allowing authorised card-based payment instrument issuers to confirm whether funds are available on a customer account. FAPI-secured with OAuth
  name: TSB Confirmation of Funds API (CBPII)
  slug: tsb-confirmation-of-funds-api
- description: TSB's OpenID Connect / OAuth2 authorization server (Curity OAuth Toolkit, OTK Server APIs v4.3.1), backing the FAPI-secured OBIE Read/Write services. Exposes the authorize, token, token-revocation, us
  name: TSB OAuth Toolkit (OTK) Server
  slug: tsb-oauth-toolkit-server
artifact_total: 13
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data
- collection_type: open
  name: OTK Server APIs
  slug: open-tsb-bank-oauth-server
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tsb-bank-obie-open-data-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tsb-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tsb-bank-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tsb-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tsb-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tsb-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tsb-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tsb-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tsb-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tsb-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tsb-bank-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tsb-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tsb.co.uk/.well-known/security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tsb-bank-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tsb-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tsb-bank-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tsb-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tsb-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsb.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.developer.tsb.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tsb.co.uk/help-and-support/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tsb-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tsb.co.uk/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tsb.co.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.tsb.co.uk/help-and-support/
created: '2026-07-23'
description: 'TSB Bank plc is a British retail and commercial bank headquartered in Edinburgh, offering current accounts, savings, mortgages, personal loans, credit cards, and insurance to personal and business customers across the United Kingdom. Spun out of Lloyds Banking Group in 2013 and listed before being acquired in 2015, TSB is a wholly owned subsidiary of the Spanish banking group Banco Sabadell. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As an FCA-authorised account servicing payment service provider (ASPSP) under PSD2, TSB participates in UK Open Banking and publishes its APIs conformant to the Open Banking Implementation Entity (OBIE) standards through a public developer portal at apis.developer.tsb.co.uk. TSB is not one of the nine CMA-mandated banks (CMA9) but implements the same OBIE Open Data and Read/Write API family: unauthenticated Open Data reference APIs plus FAPI-secured Account and Transaction
  Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) services secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: TSB Bank MCP Server
  slug: tsb-bank-mcp-server
modified: '2026-07-23'
name: TSB Bank
nav: Providers
network: true
overview: 'TSB Bank publishes 2 APIs on the [APIs.io](https://apis.io/) network: TSB Open Data API and TSB OAuth Toolkit (OTK) Server. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  TSB Bank''s developer surface includes authentication, documentation, support, and 23 more developer resources.'
random_paper: 9
scopes:
- name: Tsb Bank Scopes
  scope_count: 9
  slug: tsb-bank-scopes
  summary_line: 9 scopes · implicit
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 42.8
    developer_ergonomics: 37.5
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 5.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 88.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Tsb Bank Authentication
  slug: tsb-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Tsb Bank Domain Security
  slug: tsb-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tsb Bank Vulnerability Disclosure
  slug: tsb-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tsb-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- FAPI
- Fintech
website: https://www.tsb.co.uk/
---
