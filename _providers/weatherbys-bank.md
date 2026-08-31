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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Weatherbys Bank Agentic Access
  operation_count: 8
  slug: weatherbys-bank-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: OBIE Read/Write Account and Transaction Information API (AISP). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication) — requires OBIE/eIDAS certificates and dynamic client regist
  name: Weatherbys Bank Account and Transaction Information API (AIS)
  slug: weatherbys-account-transaction-information-api
- description: OBIE Read/Write Payment Initiation API (PISP). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA) — requires OBIE/eIDAS certificates and dynamic client registration. Represented as the documented OBIE R
  name: Weatherbys Bank Payment Initiation API (PIS)
  slug: weatherbys-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds API (CBPII). FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA) — requires OBIE/eIDAS certificates and dynamic client registration. Represented as the documented OB
  name: Weatherbys Bank Confirmation of Funds API (CBPII)
  slug: weatherbys-confirmation-of-funds-api
- description: Endpoint for getting ATM data
  name: Weatherbys Bank ATM API
  slug: weatherbys-bank-atm-api
- description: Endpoint for getting Business Current Account data
  name: Weatherbys Bank BCA API
  slug: weatherbys-bank-bca-api
- description: Endpoint for getting Branch data
  name: Weatherbys Bank Branch API
  slug: weatherbys-bank-branch-api
- description: Endpoint for getting Personal Current Account data
  name: Weatherbys Bank PCA API
  slug: weatherbys-bank-pca-api
artifact_total: 16
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-atm-locator-standard
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-branch-locator-standard
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-business-current-accounts-standard
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-personal-current-accounts-standard
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/weatherbys-bank-capability-edges.yml
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
  name: Weatherbys Bank MCP Server
  slug: weatherbys-bank-mcp-server
modified: '2026-07-23'
name: Weatherbys Bank
nav: Providers
network: true
overview: 'Weatherbys Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 1 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Weatherbys Bank''s developer surface includes authentication, documentation, engineering blog, support, and 22 more developer resources.'
random_paper: 10
scopes:
- name: Weatherbys Bank Scopes
  scope_count: 4
  slug: weatherbys-bank-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.6
    commercial_clarity: 78.6
    contract_governance: 18.2
    contract_quality: 33.7
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 49.1
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
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Financial-Services
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
