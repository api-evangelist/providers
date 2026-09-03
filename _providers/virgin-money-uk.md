---
access_model:
  confidence: medium
  label: Self-serve TPP onboarding (Open Banking certificates required)
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
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
  score: 39.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Virgin Money Uk Agentic Access
  operation_count: 12
  slug: virgin-money-uk-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: OBIE Read/Write Account & Transaction Information (AIS) API - retrieve accounts, balances, transactions, beneficiaries, standing orders, direct debits, and statements. Merged brand family (Virgin Mone
  name: Virgin Money UK Account and Transaction API (AIS)
  slug: account-transaction-api
- description: OBIE Read/Write Payment Initiation (PIS) API for domestic immediate payments. Merged brand family, OBIE v3.1.2. FAPI OAuth2/OIDC + mTLS + PSD2 SCA.
  name: Virgin Money UK Domestic Immediate Payment API (PIS)
  slug: domestic-payments-api
- description: OBIE Read/Write Payment Initiation (PIS) API for domestic scheduled payments. Merged brand family, OBIE v3.1.2. FAPI OAuth2/OIDC + mTLS + PSD2 SCA.
  name: Virgin Money UK Domestic Scheduled Payment API (PIS)
  slug: domestic-scheduled-payments-api
- description: OBIE Read/Write Payment Initiation (PIS) API for batch/file payments. Merged brand family, OBIE v3.1.2. FAPI OAuth2/OIDC + mTLS + PSD2 SCA.
  name: Virgin Money UK File Payments API (PIS)
  slug: file-payments-api
- description: OBIE Read/Write Payment Initiation (PIS) API for international payments. Merged brand family, OBIE v3.1.2. FAPI OAuth2/OIDC + mTLS + PSD2 SCA.
  name: Virgin Money UK International Payments API (PIS)
  slug: international-payments-api
- description: OBIE Read/Write Payment Initiation (PIS) API for international scheduled payments. Merged brand family, OBIE v3.1.2. FAPI OAuth2/OIDC + mTLS + PSD2 SCA.
  name: Virgin Money UK International Scheduled Payments API (PIS)
  slug: international-scheduled-payments-api
- description: 'OBIE Read/Write Confirmation of Funds (CBPII) API - allows a Card Based Payment Instrument Issuer to check whether sufficient balance is available to make a payment. Merged brand family, OBIE v3.1.2. '
  name: Virgin Money UK Confirmation of Funds API (CBPII)
  slug: confirmation-of-funds-api
- description: 'Open Banking-compliant OpenID Connect provider for TPP authorisation. Live production discovery document confirmed (HTTP 200, 2026-07-23): issuer https://api.prod.ob.virginmoney.com/vmpsd2-psd2prod/ps'
  name: Virgin Money UK OIDC API
  slug: oidc-api
- description: 'OAuth2 token endpoint for obtaining access tokens used to call the OBIE Read/Write APIs. Documented at v3.0. Confirmed token endpoint (from live OIDC discovery): secureapi.prod.ob.virginmoney.com.'
  name: Virgin Money UK Token API
  slug: token-api
- description: OBIE Dynamic Client Registration (DCR) API allowing TPPs to register with Virgin Money brands using OBIE (OBWAC/OBSeal) or eIDAS (QWAC/QSEAL) certificates. Documented at v3.2. Confirmed registration e
  name: Virgin Money UK Dynamic Client Registration API
  slug: dynamic-client-registration-api
- description: OBIE Read/Write Account & Transaction Information (AIS) API for the Standalone brand family (personal credit cards and sort-code-08 current and savings accounts), documented at OBIE v3.1.1. FAPI OAuth
  name: Virgin Money UK Standalone Account and Transaction API (AIS)
  slug: standalone-account-transaction-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: Virgin Money UK ATM API
  slug: virgin-money-uk-atm-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: Virgin Money UK BCA API
  slug: virgin-money-uk-bca-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: Virgin Money UK Branch API
  slug: virgin-money-uk-branch-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: Virgin Money UK CCC API
  slug: virgin-money-uk-ccc-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: Virgin Money UK PCA API
  slug: virgin-money-uk-pca-api
- baseURL: https://api-ib.cybservices.co.uk/ibapi/v2/banks/CB/open-banking
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: Virgin Money UK SME API
  slug: virgin-money-uk-sme-api
artifact_total: 23
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-api-standard
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/virgin-money-uk-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virgin-money-uk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/virgin-money-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virgin-money-uk-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/virgin-money-uk-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virgin-money-uk-well-known.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/virgin-money-uk-openid-configuration.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/virgin-money-uk-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/virgin-money-uk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virgin-money-uk-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virgin-money-uk-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virgin-money-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/virgin-money-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virgin-money-uk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virgin-money-uk-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/virgin-money-uk-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virgin-money-uk-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/virgin-money-uk-opendata-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virgin-money-uk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/virgin-money-uk-locate-atms-branches.md
- group: company
  title: ''
  type: Website
  url: https://uk.virginmoney.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.virginmoney.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.virginmoney.com/merged/
- group: operate
  title: ''
  type: Support
  url: https://uk.virginmoney.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uk.virginmoney.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uk.virginmoney.com/privacy/
created: '2026-07-23'
description: Virgin Money UK is a full-service UK retail and business bank, operating the Virgin Money, Clydesdale Bank, Yorkshire Bank, and B brands across personal current and savings accounts, mortgages, credit cards, and business banking. Formerly the FTSE-listed Virgin Money UK PLC (the former CYBG plc), it was acquired by Nationwide Building Society on 1 October 2024, making it part of a mutually owned group; its banking business is scheduled to transfer into Nationwide on 2 April 2026. The bank is authorised by the Prudential Regulation Authority and regulated by the FCA and PRA as an ASPSP. It is not one of the original CMA9 but is a fully participating UK Open Banking provider under PSD2 and the Payment Services Regulations 2017, publishing OBIE Read/Write Standard APIs - Account & Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) - through its developer portal at developer.virginmoney.com, split into "Merged" APIs (Virgin Money, Clydesdale
  and Yorkshire accounts, sort codes 05/82) and "Standalone" APIs (personal accounts and credit cards, sort code 08). Access is secured with FAPI-grade OAuth2/OpenID Connect, PSD2 strong customer authentication, mutual-TLS client authentication, and dynamic client registration using OBIE (OBWAC/OBSeal) or eIDAS (QWAC/QSEAL) certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Virgin Money UK
nav: Providers
network: true
overview: 'Virgin Money UK publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Virgin Money UK''s developer surface includes authentication, documentation, support, and 23 more developer resources.'
random_paper: 9
scopes:
- name: Virgin Money Uk Scopes
  scope_count: 4
  slug: virgin-money-uk-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 32.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virgin-money-uk/refs/heads/main/screenshots/virgin-money-uk-2026-09-02T170000.png
security:
- kind: authentication
  name: Virgin Money Uk Authentication
  slug: virgin-money-uk-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Virgin Money Uk Domain Security
  slug: virgin-money-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Virgin Money Uk Vulnerability Disclosure
  slug: virgin-money-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: virgin-money-uk
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
- FAPI
website: https://uk.virginmoney.com/
---
