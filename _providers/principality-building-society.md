---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 21.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The OBIE Read/Write Account and Transaction Information (AISP) standard for reading account, balance and transaction data. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authentica
  name: OBIE Account & Transaction Information API (AIS - Standard, Out of Scope)
  slug: obie-account-transaction-api
- description: The OBIE Read/Write Payment Initiation (PISP) standard for initiating domestic, scheduled, standing-order, international and file payments. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong cu
  name: OBIE Payment Initiation API (PIS - Standard, Out of Scope)
  slug: obie-payment-initiation-api
- description: The OBIE Read/Write Confirmation of Funds (CBPII) standard for confirming whether funds are available on a payment account. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authentic
  name: OBIE Confirmation of Funds API (CBPII - Standard, Out of Scope)
  slug: obie-confirmation-of-funds-api
- description: Endpoint for getting ATM data
  name: Principality Building Society ATM API
  slug: principality-building-society-atm-api
- description: Endpoint for getting Business Current Account data
  name: Principality Building Society BCA API
  slug: principality-building-society-bca-api
- description: Endpoint for getting Branch data
  name: Principality Building Society Branch API
  slug: principality-building-society-branch-api
- description: Endpoint for getting Commercial Credit Card data
  name: Principality Building Society CCC API
  slug: principality-building-society-ccc-api
- description: Endpoint for getting Personal Current Account data
  name: Principality Building Society PCA API
  slug: principality-building-society-pca-api
- description: Endpoint for getting Unsecured SME Loan data
  name: Principality Building Society SME API
  slug: principality-building-society-sme-api
artifact_total: 12
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/principality-building-society-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OpenBankingUK/opendata-api-spec-compiled/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/principality-building-society-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/principality-building-society-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/principality-building-society-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/principality-building-society-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/principality-building-society-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.principality.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.principality.co.uk/home/about-us
- group: company
  title: ''
  type: News
  url: https://www.principality.co.uk/home/about-us/principality-news
- group: operate
  title: ''
  type: Support
  url: https://www.principality.co.uk/home/contact-us/help-and-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.principality.co.uk/home/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.principality.co.uk/home/terms-of-use/privacy-and-security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/principality-building-society/
created: '2026-07-23'
description: Principality Building Society is the largest building society in Wales and the sixth largest in the United Kingdom, founded in 1860 and headquartered in Cardiff. It is a mutual, owned by and run for the benefit of its members rather than shareholders, holding total assets of more than £11 billion and operating around 71 branches and agencies alongside internet and telephone channels. Its product range is deliberately narrow - savings, residential mortgages and investments, plus a commercial lending division - and it does NOT offer current or payment accounts. Principality is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA, and is a member of the Building Societies Association. It is NOT one of the nine CMA9 banks mandated to deliver UK Open Banking, and because it holds no payment accounts it falls outside the scope of the PSD2 / OBIE Read/Write (AIS, PIS, CBPII) standard. As of this profile Principality publishes
  no public developer portal and no confirmed OBIE Open Data API endpoint; the Open Banking API family below is represented as the shared Open Banking Implementation Entity (OBIE) standard for reference only, not as a Principality-operated contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Principality Building Society
nav: Providers
network: true
overview: 'Principality Building Society publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Building Society, Savings, and Mortgages.


  Principality Building Society''s developer surface includes authentication, product news, support, and 11 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 68.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 32.7
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 5.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Principality Building Society Authentication
  slug: principality-building-society-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Principality Building Society Domain Security
  slug: principality-building-society-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: principality-building-society
tags:
- Financial-Services
- Banking
- Building Society
- Savings
- Mortgages
- Open Banking
- Open Data
- PSD2
- OBIE
- United Kingdom
- Wales
- Mutual
website: https://www.principality.co.uk/
---
