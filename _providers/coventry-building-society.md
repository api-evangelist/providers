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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Coventry Building Society Agentic Access
  operation_count: 86
  slug: coventry-building-society-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: Public, unauthenticated OBIE Open Data endpoint publishing FCA service metrics for personal current accounts at Coventry Building Society (CBS v1.0). Live JSON host confirmed responding at the documen
  name: Coventry Building Society Open Data FCA Service Metrics API
  slug: coventry-building-society-open-data-fca-service-metrics-api
- description: OBIE Read/Write Account and Transaction Information Services (AIS) API, CBS v2.0, providing consented third-party read access to account, balance, transaction, standing order, direct debit, beneficiar
  name: Coventry Building Society Account & Transaction Information API (AIS)
  slug: coventry-building-society-account-information-api
- description: 'OBIE Read/Write Payment Initiation Services (PIS) API, CBS v2.0, enabling consented third-party initiation of domestic single, scheduled, standing order, and file payments. FAPI-secured (OAuth2/OIDC, '
  name: Coventry Building Society Payment Initiation API (PIS)
  slug: coventry-building-society-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds Services (CBPII) API, CBS v2.0, allowing a consented card-based payment instrument issuer to confirm whether funds are available on an account. FAPI-secured (OAut
  name: Coventry Building Society Confirmation of Funds API (CBPII)
  slug: coventry-building-society-confirmation-of-funds-api
artifact_total: 10
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-swagger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coventry-building-society-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coventry-building-society-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coventry-building-society-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coventry-building-society-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coventry-building-society-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coventry-building-society-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coventrybuildingsociety.co.uk/member/help/savings/open-banking.html
- group: design
  title: ''
  type: DataModel
  url: data-model/coventry-building-society-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coventry-building-society-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coventry-building-society-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/coventry-building-society-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coventry-building-society-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coventry-building-society-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coventry-building-society-confirmation-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/coventry-building-society-opendata-overlay.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coventrybuildingsociety.co.uk/member/help/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coventrybuildingsociety.co.uk/consumer/help/privacy-policy.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coventry-building-society-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coventry-building-society-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coventry-building-society-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.coventrybuildingsociety.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coventrybuildingsociety.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coventrybuildingsociety.co.uk/
- group: other
  title: ''
  type: OpenBanking
  url: https://www.coventrybuildingsociety.co.uk/member/help/savings/open-banking.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coventry-building-society
- group: operate
  title: ''
  type: Support
  url: https://developer.coventrybuildingsociety.co.uk/
created: '2026-07-23'
description: Coventry Building Society is the United Kingdom's second-largest building society, a member-owned mutual founded in 1884 and headquartered in Coventry, England, offering savings and residential mortgages to millions of members and in January 2025 completing its acquisition of The Co-operative Bank. As an FCA-authorised and PRA-regulated deposit-taker and Account Servicing Payment Service Provider (ASPSP), it participates in UK Open Banking under PSD2 and the Open Banking Implementation Entity (OBIE) standards. It is not one of the CMA9 mandated banks, but operates a public developer portal at developer.coventrybuildingsociety.co.uk that publishes CBS v2.0 Open Banking APIs - Account Information Services (AIS), Payment Initiation Services (PIS), and Confirmation of Funds (CBPII) - conformant to the OBIE Read/Write API Standard, alongside a public FCA Service Metrics open-data endpoint and a sandbox for TPP onboarding. Read/Write access is secured with FAPI-grade OAuth2/OIDC,
  PSD2 strong customer authentication, and mutual-TLS using Open Banking WAC or eIDAS QWAC certificates, with registered TPP onboarding handled via open.banking@thecoventry.co.uk.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: coventry-building-society-mcp.yml
  slug: coventry-building-society-mcpyml
modified: '2026-07-23'
name: Coventry Building Society
nav: Providers
network: true
overview: 'Coventry Building Society publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data FCA Service Metrics API, Account & Transaction Information API (AIS), Payment Initiation API (PIS), and 1 more. Tagged areas include Financial Services, Banking, Building Society, Open Banking, and PSD2.


  Coventry Building Society''s developer surface includes authentication, documentation, support, and 24 more developer resources.'
random_paper: 11
scopes:
- name: Coventry Building Society Scopes
  scope_count: 3
  slug: coventry-building-society-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 44.7
  delta: 5.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 51.2
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 87.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/coventry-building-society/refs/heads/main/screenshots/coventry-building-society-2026-07-25T210542.png
security:
- kind: authentication
  name: Coventry Building Society Authentication
  slug: coventry-building-society-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Coventry Building Society Domain Security
  slug: coventry-building-society-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: coventry-building-society
tags:
- Financial Services
- Banking
- Building Society
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Fintech
website: https://www.coventrybuildingsociety.co.uk/
---
