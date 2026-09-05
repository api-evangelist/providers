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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Account and Transaction Information Services (AIS) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication). Represented here as the
  name: Skipton Account & Transaction Information API (OBIE Read/Write Standard)
  slug: skipton-account-information-api
- description: Payment Initiation Services (PIS) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA). Represented here as the shared OBIE standard; Skipton ASPSP publica
  name: Skipton Payment Initiation API (OBIE Read/Write Standard)
  slug: skipton-payment-initiation-api
- description: Confirmation of Funds Services (CBPII) as defined by the OBIE Read/Write API Standard - FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA). Represented here as the shared OBIE standard; Skipton ASPSP pu
  name: Skipton Confirmation of Funds API (OBIE Read/Write Standard)
  slug: skipton-confirmation-of-funds-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting ATM data
  name: Skipton Building Society ATM API
  slug: skipton-building-society-atm-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Business Current Account data
  name: Skipton Building Society BCA API
  slug: skipton-building-society-bca-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Branch data
  name: Skipton Building Society Branch API
  slug: skipton-building-society-branch-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Commercial Credit Card data
  name: Skipton Building Society CCC API
  slug: skipton-building-society-ccc-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Personal Current Account data
  name: Skipton Building Society PCA API
  slug: skipton-building-society-pca-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Unsecured SME Loan data
  name: Skipton Building Society SME API
  slug: skipton-building-society-sme-api
artifact_total: 12
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/skipton-building-society-capability-edges.yml
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
overview: 'Skipton Building Society publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Building Society, Open Banking, and PSD2.


  Skipton Building Society''s developer surface includes support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 32.7
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 35.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skipton-building-society/refs/heads/main/screenshots/skipton-building-society-2026-09-02T155735.png
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
- Financial-Services
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
