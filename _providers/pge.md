---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pge Agentic Access
  operation_count: 7
  slug: pge-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'The OAuth 2.0 authorization server behind Share My Data, implemented to meet the NAESB ESPI authorization profile. Two token classes are issued separately: a client access token via the client_credent'
  name: PG&E Share My Data OAuth 2.0 Authorization API
  slug: pge-share-my-data-oauth-api
- baseURL: https://api.pge.com/GreenButtonConnect/espi/1_1/resource
  baseurl_source: declared
  description: Application Information endpoints
  name: Pacific Gas and Electric Application Information API
  slug: pge-applicationinformation-api
- baseURL: https://api.pge.com/GreenButtonConnect/espi/1_1/resource
  baseurl_source: declared
  description: Authorization endpoints
  name: Pacific Gas and Electric Authorization API
  slug: pge-authorization-api
- baseURL: https://api.pge.com/GreenButtonConnect/espi/1_1/resource
  baseurl_source: declared
  description: Batch data transfer endpoints
  name: Pacific Gas and Electric Batch API
  slug: pge-batch-api
- baseURL: https://api.pge.com/GreenButtonConnect/espi/1_1/resource
  baseurl_source: declared
  description: Usage Point endpoints
  name: Pacific Gas and Electric Usage Point API
  slug: pge-usagepoint-api
artifact_total: 13
asyncapis:
- description: ''
  name: Pge Share My Data Notifications
  slug: pge-share-my-data-notifications
collections:
- collection_type: open
  name: Green Button API Documentation
  slug: open-green-button-alliance-espi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pge-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pge-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html
- group: other
  title: ''
  type: Registration
  url: https://sharemydata.pge.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pgetech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pacificgasandelectric
- group: company
  title: ''
  type: Blog
  url: https://www.pge.com/en/newsroom/currents.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.pge.com/en/about/company-information/vulnerability-disclosure-policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pge.com/en/about/company-information/vulnerability-disclosure-policy.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pge.com/en/privacy-center.html
- group: company
  title: ''
  type: About
  url: https://www.pge.com/en/about/company-information/company-profile.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.pge.com/assets/pge/docs/save-energy-and-money/energy-savings-programs/Supported-APIs.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pge.com/en/save-energy-and-money/energy-saving-programs/smartmeter/third-party-companies.html#getstarted
- group: operate
  title: ''
  type: Support
  url: mailto:ShareMyData@pge.com
- group: start
  title: ''
  type: SignUp
  url: https://sharemydata.pge.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pge.com/assets/pge/docs/save-energy-and-money/energy-savings-programs/ShareMyData_Platform_TermsofUse.pdf
- group: build
  title: ''
  type: Packages
  url: packages/pge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pge-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pge-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pge-green-button-alliance-espi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pge-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pge-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pge-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pge-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pge-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pge-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pge-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pge-share-my-data-notifications.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Reference
  url: https://pge-energydatarequest.com/
- group: docs
  title: ''
  type: Reference
  url: https://www.greenbuttondata.org/
created: '2026-07-27'
description: 'Pacific Gas and Electric Company is the investor-owned electric and natural gas utility for northern and central California — incorporated in California in 1905, headquartered in Oakland, roughly 23,000 employees, a 70,000-square- mile service area, about 5.5 million electric accounts and 4.5 million gas accounts, and a subsidiary of PG&E Corporation. It sits in the wires, pipes and metering layer of the United States value chain: a vertically integrated regulated distribution utility that owns the meter and the customer relationship, does not run the wholesale market (CAISO does), and is regulated by the California Public Utilities Commission. Its API posture is the outlier of the American utility sector and deserves to be recorded precisely, because the United States has no federal energy consumer-data mandate at all. PG&E runs Share My Data, its production Green Button Connect My Data implementation, on a live MuleSoft API gateway at https://api.pge.com — a NAESB REQ.21
  ESPI 1.1 surface with roughly two dozen documented resources under /GreenButtonConnect/espi/1_1/resource/, an OAuth 2.0 authorization server at /datacustodian/oauth/v2/, and a separate published test environment at /datacustodian/test/oauth/v2/. Unlike almost every other US utility, PG&E publishes the whole contract anonymously: a complete supported-API reference, an OAuth/ESPI authorization guide, a relational data model, supported data elements, function-block scope-string mappings, the ESPI and Share My Data XSD schemas, sample MeterReadings XML, Python and JavaScript SDKs with development guides, published rate limits (one request per second per vendor, 2,000 calls per hour and 20,000 calls per 24 hours per client ID) and a SoapUI walkthrough — all reachable without a login at pge.com. What is not open is the data itself. Share My Data is application-approval gated: a third party needs a US EIN, eligible standing with the CPUC, a CA-issued TLS 1.2 X.509 certificate (self-signed rejected),
  acceptance of the CPUC-filed Customer Data Access Tariff, and successful connectivity and OAuth testing before approval, after which every production call runs over mutual TLS with bearer tokens scoped to an individual customer''s authorization. The mandate story is equally specific and must not be flattened into "voluntary Green Button": California compels third-party access through state law and CPUC tariff — Public Utilities Code section 8380 (SB 1476, 2010), the Customer Information Service Request for Share My Data tariff form (Cal. P.U.C. Sheet 55826-E, Sample Form 79-1186, Advice 6900-E, effective 1 April 2023), and Electric Rule 24 / Gas Rule 25 for demand response providers — but no federal obligation and no Ontario-style Green Button regulation applies. The consumer-versus-market split is stark: consumer data is a real, verified, standards-conformant API behind consent and approval, while PG&E publishes no open market or grid API whatsoever. Its aggregated ZIP-code electric and
  gas usage datasets, released quarterly under CPUC Decision 14-05-016 through the Energy Data Request Program, are CSV-in- ZIP downloads behind an organization/name/email form and a data-use agreement, not an anonymous feed; California wholesale market data belongs to CAISO.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Pacific Gas and Electric
nav: Providers
network: true
overview: 'Pacific Gas and Electric publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application Information API, Authorization API, Batch API, and 1 more. Tagged areas include Energy, United States, Utilities, Electricity, and Gas.


  The Pacific Gas and Electric catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pacific Gas and Electric''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 30 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 3
  name: Pge Rate Limits
  slug: pge-rate-limits
scopes:
- name: Pge Scopes
  scope_count: 21
  slug: pge-scopes
  summary_line: 21 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 21.9
    developer_ergonomics: 82.7
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pge/refs/heads/main/screenshots/pge-2026-08-17T081205.png
security:
- kind: authentication
  name: Pge Authentication
  slug: pge-authentication
  summary_line: oauth2/mutualTLS/http · 5 schemes
- kind: domain-security
  name: Pge Domain Security
  slug: pge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pge Vulnerability Disclosure
  slug: pge-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: pge
tags:
- Energy
- United States
- Utilities
- Electricity
- Gas
- California
- Smart Metering
- Green Button
- ESPI
- Energy Data
- Grid
- Demand Response
- Investor-Owned Utility
website: https://www.pge.com/
---
