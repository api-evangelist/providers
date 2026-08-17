---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Bank Of Ireland Uk Agentic Access
  operation_count: 86
  slug: bank-of-ireland-uk-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 5
apis:
- description: Public, unauthenticated OBIE Open Data API for Bank of Ireland (UK) plc, serving reference data for ATMs, branches, personal current accounts, business current accounts, unsecured SME loans and commer
  name: Bank of Ireland (UK) Open Data API
  slug: bank-of-ireland-uk-open-data-api
- description: OBIE Read/Write Account & Transaction Information (AIS) API for Bank of Ireland (UK) plc, allowing authorised AISPs to access account, balance, transaction, beneficiary, standing order, direct debit a
  name: Bank of Ireland (UK) Account & Transaction Information API
  slug: bank-of-ireland-uk-account-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API for Bank of Ireland (UK) plc, enabling authorised PISPs to initiate domestic and international single, scheduled, standing-order and file payments with the
  name: Bank of Ireland (UK) Payment Initiation API
  slug: bank-of-ireland-uk-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for Bank of Ireland (UK) plc, allowing authorised card-based payment instrument issuers to confirm the availability of funds on a customer account wit
  name: Bank of Ireland (UK) Confirmation of Funds API
  slug: bank-of-ireland-uk-confirmation-of-funds-api
- description: OBIE Dynamic Client Registration (DCR) API documented on the Bank of Ireland Developer Hub for onboarding third-party provider applications using OBIE/eIDAS certificates, ahead of consuming the Read/W
  name: Bank of Ireland (UK) Dynamic Client Registration API
  slug: bank-of-ireland-uk-dynamic-client-registration-api
artifact_total: 11
collections:
- collection_type: open
  name: Open Data API
  slug: open-bank-of-ireland-uk-open-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-ireland-uk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-ireland-uk-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-ireland-uk-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-ireland-uk-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bank-of-ireland-uk-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-ireland-uk-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-ireland-uk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-ireland-uk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-of-ireland-uk-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-ireland-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bank-of-ireland-uk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-ireland-uk-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-of-ireland-uk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-ireland-uk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-ireland-uk-open-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-ireland-uk-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-ireland-uk-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-ireland-uk-confirmation-funds-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://eu1.anypoint.mulesoft.com/exchange/portals/bankofireland/pages/Getting%20Started/
- group: company
  title: ''
  type: Website
  url: https://www.bankofirelanduk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bankofireland.com/
- group: start
  title: ''
  type: Portal
  url: https://eu1.anypoint.mulesoft.com/exchange/portals/bankofireland/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bankofireland.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankofirelanduk.com/personal/api-statistics/
- group: auth
  title: ''
  type: Compliance
  url: https://www.bankofirelanduk.com/personal/api-statistics/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-ireland/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofirelanduk.com/site-links/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bankofirelanduk.com/help-and-support/
- group: commercial
  title: ''
  type: License
  url: https://www.openbanking.org.uk/open-licence
created: '2026-07-23'
description: Bank of Ireland (UK) plc is the UK banking arm of Bank of Ireland Group plc, Ireland's oldest bank, founded in 1783 and headquartered in Dublin with a listing on Euronext Dublin and the London Stock Exchange. In the United Kingdom it is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA, and as one of the nine CMA-mandated banks (the CMA9) it participates fully in the UK Open Banking programme under PSD2. Bank of Ireland (UK) and Bank of Ireland (ROI) are separate legal entities on the Open Banking Directory and TPPs must onboard to each separately. The bank publishes a public, unauthenticated Open Data API (ATMs, branches, personal and business current accounts, unsecured SME loans and commercial credit cards) conformant to the OBIE Open Data Standard, alongside the OBIE Read/Write API family - Account & Transaction Information (AIS), Payment Initiation (PIS) and Confirmation of Funds (CBPII) - secured with FAPI-grade
  OAuth2/OIDC, PSD2 strong customer authentication and mutual-TLS client authentication using OBIE/eIDAS certificates, onboarded through the Bank of Ireland Developer Hub with a sandbox for testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: bank-of-ireland-uk-mcp.yml
  slug: bank-of-ireland-uk-mcpyml
modified: '2026-07-23'
name: Bank of Ireland (UK)
nav: Providers
network: true
overview: 'Bank of Ireland (UK) publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account & Transaction Information API, Payment Initiation API, and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Bank of Ireland (UK)''s developer surface includes authentication, getting-started guide, developer portal, documentation, support, and 25 more developer resources.'
random_paper: 80
scopes:
- name: Bank Of Ireland Uk Scopes
  scope_count: 4
  slug: bank-of-ireland-uk-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.0
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-ireland-uk/refs/heads/main/screenshots/bank-of-ireland-uk-2026-07-25T202335.png
security:
- kind: authentication
  name: Bank Of Ireland Uk Authentication
  slug: bank-of-ireland-uk-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Bank Of Ireland Uk Domain Security
  slug: bank-of-ireland-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bank-of-ireland-uk
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Open Data
- FAPI
- Fintech
website: https://www.bankofirelanduk.com/
---
