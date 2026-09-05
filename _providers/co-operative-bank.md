---
access_model:
  confidence: medium
  label: TPP onboarding (manual)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Co Operative Bank Agentic Access
  operation_count: 12
  slug: co-operative-bank-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: 'OBIE Read/Write Account & Transaction Information (AISP) API for The Co-operative Bank and smile brands — account-access consents, accounts, balances, transactions, direct debits, standing orders and '
  name: The Co-operative Bank Account Information API (AIS)
  slug: account-information-api
- description: 'OBIE Read/Write Payment Initiation (PISP) API for The Co-operative Bank and smile brands — domestic payments, domestic scheduled payments and domestic standing orders, with their associated consents. '
  name: The Co-operative Bank Payment Initiation API (PIS)
  slug: payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII / Card-Based Payment Instrument) API — funds-confirmation consent and funds-confirmation checks for The Co-operative Bank and smile brands. FAPI-secured (O
  name: The Co-operative Bank Confirmation of Funds API (CBPII)
  slug: confirmation-of-funds-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: The Co-operative Bank ATM API
  slug: co-operative-bank-atm-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: The Co-operative Bank BCA API
  slug: co-operative-bank-bca-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: The Co-operative Bank Branch API
  slug: co-operative-bank-branch-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: The Co-operative Bank CCC API
  slug: co-operative-bank-ccc-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: The Co-operative Bank PCA API
  slug: co-operative-bank-pca-api
- baseURL: https://openbanking-retail.apis.co-operativebank.co.uk/apis/retail/open-banking/v3.1/aisp
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: The Co-operative Bank SME API
  slug: co-operative-bank-sme-api
artifact_total: 15
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-api-standard-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/co-operative-bank-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/co-operative-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/co-operative-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/co-operative-bank-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.co-operativebank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developer.co-operativebank.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.developer.co-operativebank.co.uk/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.developer.co-operativebank.co.uk/get-started/
- group: auth
  title: ''
  type: Authentication
  url: https://www.developer.co-operativebank.co.uk/apis/general-specifications/
- group: start
  title: ''
  type: Sandbox
  url: https://www.developer.co-operativebank.co.uk/help-and-support/sandbox-environment/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.developer.co-operativebank.co.uk/help-and-support/service-status/
- group: operate
  title: ''
  type: Support
  url: https://www.developer.co-operativebank.co.uk/help-and-support/frequently-asked-questions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.developer.co-operativebank.co.uk/help-and-support/privacy-cookie-policies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-co-operative-bank
- group: start
  title: ''
  type: SignUp
  url: https://www.developer.co-operativebank.co.uk/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/co-operative-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/co-operative-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/co-operative-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/co-operative-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/co-operative-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/co-operative-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/co-operative-bank-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/co-operative-bank-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/co-operative-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/co-operative-bank-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.co-operativebank.co.uk/help-and-support/fraud-and-security/responsible-security-disclosure/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/co-operative-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/co-operative-bank-open-data-overlay.yaml
created: '2026-07-23'
description: The Co-operative Bank plc is a UK high-street retail and commercial bank, headquartered in Manchester and long known for its customer-led ethical banking policy. Following its 2013-2017 recapitalisation it was owned by institutional bondholders, and in January 2025 it completed its acquisition by Coventry Building Society, becoming part of the member-owned Coventry Building Society Group; it also operates the online-only "smile" brand. Authorised by the PRA and regulated by the FCA and PRA, it is an FCA-authorised ASPSP under PSD2 and the UK Open Banking regime. While it is not one of the nine CMA-mandated banks (CMA9), it implements the Open Banking Implementation Entity (OBIE) Read/Write API Standard (v3.1) and publishes a public developer portal at developer.co-operativebank.co.uk exposing Account Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) APIs for both the Co-operative Bank and smile brands, secured with FAPI-grade OAuth2/OIDC, mutual-TLS
  client authentication using Open Banking directory certificates, and PSD2 strong customer authentication, with a manual TPP onboarding process and a sandbox for testing before production.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: The Co-operative Bank
nav: Providers
network: true
overview: 'The Co-operative Bank publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  The Co-operative Bank''s developer surface includes documentation, getting-started guide, authentication, sandbox, support, signup flow, and 22 more developer resources.'
random_paper: 7
scopes:
- name: Co Operative Bank Scopes
  scope_count: 6
  slug: co-operative-bank-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 32.7
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 73.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/co-operative-bank/refs/heads/main/screenshots/co-operative-bank-2026-07-25T205806.png
security:
- kind: authentication
  name: Co Operative Bank Authentication
  slug: co-operative-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Co Operative Bank Domain Security
  slug: co-operative-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Co Operative Bank Vulnerability Disclosure
  slug: co-operative-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: co-operative-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Fintech
website: https://www.co-operativebank.co.uk/
---
