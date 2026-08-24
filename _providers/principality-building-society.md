---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: The UK Open Banking Implementation Entity (OBIE) Open Data API standard - public, unauthenticated reference data covering Branches, ATMs, Personal Current Accounts, Business Current Accounts, Unsecure
  name: OBIE Open Data API (Shared Standard - Unverified for Principality)
  slug: obie-open-data-api
- description: The OBIE Read/Write Account and Transaction Information (AISP) standard for reading account, balance and transaction data. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authentica
  name: OBIE Account & Transaction Information API (AIS - Standard, Out of Scope)
  slug: obie-account-transaction-api
- description: The OBIE Read/Write Payment Initiation (PISP) standard for initiating domestic, scheduled, standing-order, international and file payments. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong cu
  name: OBIE Payment Initiation API (PIS - Standard, Out of Scope)
  slug: obie-payment-initiation-api
- description: The OBIE Read/Write Confirmation of Funds (CBPII) standard for confirming whether funds are available on a payment account. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authentic
  name: OBIE Confirmation of Funds API (CBPII - Standard, Out of Scope)
  slug: obie-confirmation-of-funds-api
artifact_total: 7
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-swagger
common:
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
overview: 'Principality Building Society publishes 1 API on the [APIs.io](https://apis.io/) network: OBIE Open Data API (Shared Standard - Unverified for Principality). Tagged areas include Financial-Services, Banking, Building Society, Savings, and Mortgages.


  Principality Building Society''s developer surface includes authentication, product news, support, and 9 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 37.1
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 33.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 41.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
