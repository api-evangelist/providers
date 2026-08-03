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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cynergy Bank Agentic Access
  operation_count: 74
  slug: cynergy-bank-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: Cynergy Bank's implementation of the OBIE Read/Write Account & Transaction Information (AISP) API, allowing FCA/EEA-regulated Account Information Service Providers to retrieve customer account, balanc
  name: Cynergy Bank Account & Transaction Information API (AIS)
  slug: cynergy-bank-account-information-api
- description: Cynergy Bank's implementation of the OBIE Read/Write Payment Initiation (PISP) API, allowing FCA/EEA-regulated Payment Initiation Service Providers to initiate domestic and scheduled payments on behal
  name: Cynergy Bank Payment Initiation API (PIS)
  slug: cynergy-bank-payment-initiation-api
- description: 'Cynergy Bank''s implementation of the OBIE Read/Write Confirmation of Funds (CBPII) API, allowing regulated Card Based Payment Instrument Issuers to confirm whether sufficient funds are available on a '
  name: Cynergy Bank Confirmation of Funds API (CBPII)
  slug: cynergy-bank-confirmation-of-funds-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cynergy-bank-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cynergy-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cynergy-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cynergy-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cynergy-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cynergy-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cynergy-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cynergy-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cynergy-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cynergy-bank-tool-crosswalk.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cynergy-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cynergy-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cynergy-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cynergybank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openbanking.cynergybank.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cynergybank.co.uk/support/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/cynergy-bank
- group: operate
  title: ''
  type: Support
  url: https://www.cynergybank.co.uk/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cynergybank.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cynergybank.co.uk/privacy-policy/legal-cynergy-bank
- group: build
  title: ''
  type: DocumentLibrary
  url: https://www.cynergybank.co.uk/document-library
- group: auth
  title: ''
  type: Security
  url: https://www.cynergybank.co.uk/support/security-and-fraud/information-security
created: '2026-07-23'
description: Cynergy Bank is an FCA- and PRA-authorised UK specialist bank (FCA reference 575105) serving the blended personal and business banking needs of business owners, property entrepreneurs, and family businesses. It was formed in December 2018 when Cynergy Capital acquired Bank of Cyprus UK for approximately £103m and rebranded the business as Cynergy Bank. Although it is not one of the nine CMA-mandated banks (CMA9), as a UK ASPSP it complies with PSD2 and the UK Open Banking Standard, publishing a dedicated third-party interface for the Open Banking Implementation Entity (OBIE) Read/Write APIs — Account & Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII). Access is restricted to FCA- or EEA-regulated Third Party Providers and is secured with FAPI-grade OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication using OBIE/eIDAS certificates, onboarded through the bank's Open Banking developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: cynergy-bank-mcp.yml
  slug: cynergy-bank-mcpyml
modified: '2026-07-24'
name: Cynergy Bank
nav: Providers
network: true
overview: 'Cynergy Bank publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account & Transaction Information API (AIS), Payment Initiation API (PIS), and Confirmation of Funds API (CBPII). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Cynergy Bank''s developer surface includes authentication, documentation, support, and 20 more developer resources.'
random_paper: 86
scopes:
- name: Cynergy Bank Scopes
  scope_count: 3
  slug: cynergy-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.7
    developer_ergonomics: 36.4
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cynergy-bank/refs/heads/main/screenshots/cynergy-bank-2026-07-25T211048.png
security:
- kind: authentication
  name: Cynergy Bank Authentication
  slug: cynergy-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cynergy Bank Domain Security
  slug: cynergy-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cynergy-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Specialist Lender
website: https://www.cynergybank.co.uk/
---
