---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - review
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
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
  score: 15.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The OBIE Read/Write Account and Transaction Information (AIS) standard for retrieving account, balance, transaction, and beneficiary data with customer consent, secured with FAPI-grade OAuth2/OIDC, mu
  name: OBIE Account and Transaction Information API (AIS, shared standard)
  slug: obie-account-transaction-information-api
- description: The OBIE Read/Write Payment Initiation (PIS) standard for initiating domestic, scheduled, standing-order, international, and file payments with customer consent, secured with FAPI OAuth2/OIDC, mutual-
  name: OBIE Payment Initiation API (PIS, shared standard)
  slug: obie-payment-initiation-api
- description: The OBIE Read/Write Confirmation of Funds (CBPII) standard for confirming whether funds are available on a payment account, secured with FAPI OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authenti
  name: OBIE Confirmation of Funds API (CBPII, shared standard)
  slug: obie-confirmation-of-funds-api
- description: Endpoint for getting ATM data
  name: Leeds Building Society ATM API
  slug: leeds-building-society-atm-api
- description: Endpoint for getting Business Current Account data
  name: Leeds Building Society BCA API
  slug: leeds-building-society-bca-api
- description: Endpoint for getting Branch data
  name: Leeds Building Society Branch API
  slug: leeds-building-society-branch-api
- description: Endpoint for getting Commercial Credit Card data
  name: Leeds Building Society CCC API
  slug: leeds-building-society-ccc-api
- description: Endpoint for getting Personal Current Account data
  name: Leeds Building Society PCA API
  slug: leeds-building-society-pca-api
- description: Endpoint for getting Unsecured SME Loan data
  name: Leeds Building Society SME API
  slug: leeds-building-society-sme-api
artifact_total: 11
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-standard-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leeds-building-society-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leeds-building-society-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leeds-building-society-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.leedsbuildingsociety.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.leedsbuildingsociety.co.uk/help-and-contact/
- group: company
  title: ''
  type: Blog
  url: https://www.leedsbuildingsociety.co.uk/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leedsbuildingsociety.co.uk/legal-notice-and-website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leedsbuildingsociety.co.uk/security/use-of-personal-information/
- group: auth
  title: ''
  type: Security
  url: https://www.leedsbuildingsociety.co.uk/security/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leeds-building-society
created: '2026-07-23'
description: Leeds Building Society is the fifth-largest building society in the United Kingdom, a mutual owned by and run for the benefit of its members rather than shareholders. Founded in 1875 and headquartered in Leeds, West Yorkshire, it holds over GBP 31 billion in assets and serves more than 991,000 members, focusing on savings and residential mortgages (including shared-ownership and later-life lending) rather than current accounts. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. Because Leeds Building Society does not provide payment or current accounts, it is not one of the CMA9 mandated banks and is not an Account Servicing Payment Service Provider (ASPSP) under PSD2 / UK Open Banking; it participates in Open Banking as a data consumer (for example using Experian Boost and Account Information data to speed mortgage affordability decisions) rather than as an API provider. As of this review it publishes no public
  developer portal, no OBIE Open Data endpoint, and no OBIE Read/Write APIs. The OBIE standard specifications below are captured as shared-standard references, not as Leeds Building Society API contracts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Leeds Building Society
nav: Providers
network: true
overview: 'Leeds Building Society publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Building Society, Mutual, and Savings.


  Leeds Building Society''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 68.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 0.0
    contract_quality: 32.7
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leeds-building-society/refs/heads/main/screenshots/leeds-building-society-2026-07-25T224818.png
security:
- kind: domain-security
  name: Leeds Building Society Domain Security
  slug: leeds-building-society-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: leeds-building-society
tags:
- Financial-Services
- Banking
- Building Society
- Mutual
- Savings
- Mortgages
- Open Banking
- PSD2
- OBIE
- United Kingdom
website: https://www.leedsbuildingsociety.co.uk/
---
