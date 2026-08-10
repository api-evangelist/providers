---
access_model:
  confidence: low
  label: No public developer portal identified
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - manual-research
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: UK Open Banking Open Data standard - public, unauthenticated reference data (branches, ATMs, personal and business current accounts, unsecured SME loans, commercial credit cards) as defined by the OBI
  name: Skipton Open Banking Open Data API (OBIE Standard)
  slug: skipton-open-data-api
- description: Account and Transaction Information Services (AIS) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication). Represented here as the
  name: Skipton Account & Transaction Information API (OBIE Read/Write Standard)
  slug: skipton-account-information-api
- description: Payment Initiation Services (PIS) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA). Represented here as the shared OBIE standard; Skipton ASPSP publica
  name: Skipton Payment Initiation API (OBIE Read/Write Standard)
  slug: skipton-payment-initiation-api
- description: Confirmation of Funds Services (CBPII) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA). Represented here as the shared OBIE standard; Skipton ASPSP pu
  name: Skipton Confirmation of Funds API (OBIE Read/Write Standard)
  slug: skipton-confirmation-of-funds-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skipton-building-society-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skipton.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.skipton.co.uk/about-us
- group: other
  title: ''
  type: BranchLocator
  url: https://www.skipton.co.uk/help-and-support/branch-finder
- group: operate
  title: ''
  type: Support
  url: https://www.skipton.co.uk/help-and-support/contact-us
- group: auth
  title: ''
  type: Security
  url: https://www.skipton.co.uk/help-and-support/fraud-and-security
- group: company
  title: ''
  type: Blog
  url: https://www.skipton.co.uk/press-office
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skipton.co.uk/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skipton.co.uk/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skipton-building-society
- group: other
  title: ''
  type: Standard
  url: https://github.com/OpenBankingUK/opendata-api-spec-compiled
- group: other
  title: ''
  type: Standard
  url: https://github.com/OpenBankingUK/read-write-api-specs
- group: auth
  title: ''
  type: Authentication
  url: authentication/skipton-building-society-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skipton-building-society-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skipton-building-society-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skipton-building-society-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skipton-building-society-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skipton-building-society-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/skipton-building-society-obie-opendata-overlay.yaml
created: '2026-07-23'
description: Skipton Building Society is a UK mutual building society founded in 1853 and headquartered in Skipton, North Yorkshire. It is the fourth-largest building society in the United Kingdom, owned by and run for the benefit of its members rather than shareholders, and is the parent of the wider Skipton Group (which includes the Connells estate-agency group and Skipton International). Skipton is authorised by the Prudential Regulation Authority (PRA) and regulated by the Financial Conduct Authority (FCA) and PRA, and is a member of the Building Societies Association. Its core business is retail savings and residential mortgages together with financial advice; it does not offer personal current accounts. Within UK Open Banking (PSD2 / OBIE) Skipton has historically acted as a consumer of Open Banking data - notably using Experian's Open Banking service to verify mortgage-affordability from applicant bank data - rather than as an account-servicing payment service provider (ASPSP) publishing
  a public developer platform. As of this profile Skipton exposes no public developer portal and is not listed among the CMA9 or the wider set of banks and building societies that publish live UK Open Banking Open Data or Read/Write APIs; the Open Banking API entries below are represented as the shared OBIE standard the society would conform to if it published these surfaces, and are explicitly unverified for Skipton.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Skipton Building Society
nav: Providers
network: true
overview: 'Skipton Building Society publishes 1 API on the [APIs.io](https://apis.io/) network: Skipton Open Banking Open Data API (OBIE Standard). Tagged areas include Financial Services, Banking, Building Society, Open Banking, and PSD2.


  Skipton Building Society''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 41.1
    developer_ergonomics: 17.4
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 31.0
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Skipton Building Society Authentication
  slug: skipton-building-society-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Skipton Building Society Domain Security
  slug: skipton-building-society-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skipton-building-society
tags:
- Financial Services
- Banking
- Building Society
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Mortgages
- Savings
- Account Information
- Payments
website: https://www.skipton.co.uk/
---
