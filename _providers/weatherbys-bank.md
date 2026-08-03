---
access_model:
  confidence: medium
  label: OBIE onboarding (eIDAS/OBIE certificates)
  onboarding: unknown
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Weatherbys Bank Agentic Access
  operation_count: 8
  slug: weatherbys-bank-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: PUBLIC, unauthenticated OBIE Open Data ATM Locator API — reference data for the bank's ATMs (postal address, geographic coordinates, services). Conforms to the OBIE Open Data API Standard v2.3. Docume
  name: Weatherbys Bank Open Data ATM Locator API
  slug: weatherbys-open-data-atm-locator-api
- description: PUBLIC, unauthenticated OBIE Open Data Branch Locator API — reference data for the bank's branches. Conforms to the OBIE Open Data API Standard v2.3. Documented/standard for this ASPSP; the live endpo
  name: Weatherbys Bank Open Data Branch Locator API
  slug: weatherbys-open-data-branch-locator-api
- description: PUBLIC, unauthenticated OBIE Open Data Personal Current Accounts (PCA) API — reference product data (features, fees, rates, eligibility) for personal current accounts. Conforms to the OBIE Open Data A
  name: Weatherbys Bank Open Data Personal Current Accounts API
  slug: weatherbys-open-data-personal-current-accounts-api
- description: PUBLIC, unauthenticated OBIE Open Data Business Current Accounts (BCA) API — reference product data for business current accounts. Conforms to the OBIE Open Data API Standard v2.4. Documented/standard
  name: Weatherbys Bank Open Data Business Current Accounts API
  slug: weatherbys-open-data-business-current-accounts-api
- description: OBIE Read/Write Account and Transaction Information API (AISP). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication) — requires OBIE/eIDAS certificates and dynamic client regist
  name: Weatherbys Bank Account and Transaction Information API (AIS)
  slug: weatherbys-account-transaction-information-api
- description: OBIE Read/Write Payment Initiation API (PISP). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA) — requires OBIE/eIDAS certificates and dynamic client registration. Represented as the documented OBIE R
  name: Weatherbys Bank Payment Initiation API (PIS)
  slug: weatherbys-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds API (CBPII). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA) — requires OBIE/eIDAS certificates and dynamic client registration. Represented as the documented OB
  name: Weatherbys Bank Confirmation of Funds API (CBPII)
  slug: weatherbys-confirmation-of-funds-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weatherbys-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weatherbys-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weatherbys-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weatherbys-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/weatherbys-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/weatherbys-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weatherbys-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.openbanking.org.uk/regulated-providers/weatherbys-bank-limited/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/weatherbys-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weatherbys-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weatherbys-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weatherbys-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/weatherbys-bank-atm-locator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/weatherbys-bank-branch-locator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/weatherbys-bank-personal-current-accounts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/weatherbys-bank-business-current-accounts-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.weatherbys.bank/
- group: other
  title: ''
  type: SignIn
  url: https://odbx.weatherbysbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openbanking.org.uk/regulated-providers/weatherbys-bank-limited/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weatherbys-banking-group
- group: company
  title: ''
  type: Blog
  url: https://www.weatherbys.bank/insights/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.weatherbys.bank/help-and-support/service-updates/
- group: operate
  title: ''
  type: Support
  url: https://www.weatherbys.bank/help-and-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weatherbys.bank/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weatherbys.bank/privacy-policy/
created: '2026-07-23'
description: Weatherbys Bank is a small, family-owned UK private bank, part of the Weatherbys Banking Group, trading since James Weatherby founded the family business in 1770 and incorporated as Weatherbys Bank Limited in 1994. It serves private, business, and racing customers through Weatherbys Private Bank and Weatherbys Racing Bank from offices in London, Wellingborough, and Edinburgh, and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority (FCA firm reference under Weatherbys Bank Limited). As an FCA-authorised ASPSP it is a regulated participant in UK Open Banking (PSD2), publishing OBIE-conformant surfaces - PUBLIC, unauthenticated Open Data reference APIs (ATM and branch locators, personal and business current account product data) and the FAPI-secured OBIE Read/Write APIs for Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII). It is not one of the CMA9 mandated banks. Its Open Banking
  gateway is hosted on Oracle Banking APIs (BaaS) at openbanking.weatherbysbank.com; there is no separately branded public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: weatherbys-bank-mcp.yml
  slug: weatherbys-bank-mcpyml
modified: '2026-07-23'
name: Weatherbys Bank
nav: Providers
network: true
overview: 'Weatherbys Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data ATM Locator API, Open Data Branch Locator API, Open Data Personal Current Accounts API, and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Weatherbys Bank''s developer surface includes authentication, documentation, engineering blog, support, and 21 more developer resources.'
random_paper: 23
scopes:
- name: Weatherbys Bank Scopes
  scope_count: 4
  slug: weatherbys-bank-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 28.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Weatherbys Bank Authentication
  slug: weatherbys-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Weatherbys Bank Domain Security
  slug: weatherbys-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: weatherbys-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Private Banking
website: https://www.weatherbys.bank/
---
