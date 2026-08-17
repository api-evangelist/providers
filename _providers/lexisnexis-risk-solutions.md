---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-17'
api_count: 7
apis:
- description: C.L.U.E. Auto is a contributory claim-history information exchange containing up to seven years of personal automobile claims matching the search criteria, used by carriers during quoting and underwri
  name: C.L.U.E. Auto
  slug: clue-auto
- description: C.L.U.E. Auto combined with Current Carrier, which identifies the carriers of existing or previous insurance policies so an underwriter can validate coverage and underwriting information and assess au
  name: C.L.U.E. Auto with Current Carrier
  slug: clue-auto-with-current-carrier
- description: Driver Discovery identifies potentially undisclosed drivers residing at an applicant's address, helping auto insurance carriers detect additional household drivers that were not declared on the applic
  name: Driver Discovery
  slug: driver-discovery
- description: InsurView leverages one of the industry's largest collections of public records and other data sources to provide a view of the consumer that complements traditional insurance scoring. Listed as an AP
  name: InsurView
  slug: insurview
- description: Motor Vehicle Record data allows insurance companies to evaluate driver histories consistently in all fifty states, sourced from state departments of motor vehicles. Listed as an API product on the Le
  name: Motor Vehicle Record (MVR)
  slug: motor-vehicle-record
- description: VIN Services provides vehicle registration and title data keyed on the vehicle identification number, used in auto quoting, underwriting and prefill. Listed as an API product on the LexisNexis Risk So
  name: VIN Services
  slug: vin-services
- description: LexisNexis Emailage is an email and IP address fraud-risk scoring API acquired by LexisNexis Risk Solutions in 2020. It returns a real-time risk score and advice band for an email address and/or IP ad
  name: LexisNexis Emailage
  slug: emailage
artifact_total: 11
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/lexisnexis-risk-solutions/emailage-public-clients/blob/main/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/lexisnexis-risk-solutions/emailage-public-clients/blob/main/LICENSE
- group: auth
  title: ''
  type: TrustCenter
  url: security/lexisnexis-risk-solutions-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexisnexis-risk-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://risk.lexisnexis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lexisnexisrisk.com/
- group: other
  title: ''
  type: Insurance
  url: https://risk.lexisnexis.com/insurance
- group: other
  title: ''
  type: Products
  url: https://risk.lexisnexis.com/products
- group: company
  title: ''
  type: Partners
  url: https://risk.lexisnexis.com/about-us/alliance-partnerships/insurance
- group: other
  title: ''
  type: Standards
  url: https://risk.lexisnexis.com/about-us/alliance-partnerships/insurance/industry-organization
- group: operate
  title: ''
  type: Support
  url: https://lnrs.my.site.com/CustomerSupportHub/s/
- group: start
  title: ''
  type: Login
  url: https://risk.lexisnexis.com/insurance
- group: company
  title: ''
  type: Blog
  url: https://risk.lexisnexis.com/insights-resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexisnexis-risk-solutions
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LexisNexisRisk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://risk.lexisnexis.com/corporate/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://risk.lexisnexis.com/terms
- group: commercial
  title: ''
  type: LegalNotices
  url: https://risk.lexisnexis.com/legal-notices
- group: other
  title: ''
  type: CookiePolicy
  url: https://risk.lexisnexis.com/corporate/cookie-policy
- group: commercial
  title: ''
  type: DataPrivacy
  url: https://risk.lexisnexis.com/corporate/data-privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lexisnexisrisk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lexisnexis-risk-solutions
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lexisnexis-risk-solutions/emailage-public-clients
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lexisnexisrisk.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lexisnexis-risk-solutions-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lexisnexis.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lexisnexis-risk-solutions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lexisnexis-risk-solutions-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lexisnexis-risk-solutions-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lexisnexis.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/lexisnexis-risk-solutions-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/lexisnexis-risk-solutions-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lexisnexis-risk-solutions-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lexisnexis-risk-solutions-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lexisnexis-risk-solutions-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lexisnexis-risk-solutions-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lexisnexis-risk-solutions-llms.txt
created: '2026-07-25'
description: 'LexisNexis Risk Solutions is the risk-data and analytics arm of RELX, headquartered in Alpharetta, Georgia, and one of the small number of intermediaries that sit between United States property and casualty carriers and the distribution channel. In insurance it does not underwrite risk; it sells the contributory databases and scores that carriers rate against — C.L.U.E. Auto claims history, Current Carrier prior-coverage verification, Motor Vehicle Records across all fifty states, Driver Discovery undisclosed-driver detection, InsurView public-records attributes and VIN Services vehicle data — alongside telematics exchange, data prefill, fraud detection, claims and life-insurance underwriting products. Because the United States has no federal insurance regulator and no open-insurance mandate, value in this market accrued to exactly this layer rather than to the carriers, and LexisNexis Risk reaches its customers through carrier policy-administration and rating systems (a Guidewire
  PolicyCenter marketplace listing for Motor Vehicle Records is the visible example) rather than through an open API. Its API posture reflects that: a real first-party developer portal exists at developer.lexisnexisrisk.com, built on SwaggerHub Portal, and it publicly enumerates six insurance API products with descriptions — but every product page redirects an anonymous visitor to a session-expired login screen. No OpenAPI or Swagger definition, no base URL, no scopes, no webhook catalog and no Postman collection are published to the open web. Access is contract-first and partner-gated; the six entries below are recorded as named, first-party-documented API products whose reference documentation is behind authentication.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: LexisNexis Risk Solutions
nav: Providers
network: true
overview: 'LexisNexis Risk Solutions publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Risk Data, Property and Casualty, and Underwriting.


  LexisNexis Risk Solutions'' developer surface includes documentation, support, engineering blog, authentication, sandbox, and 32 more developer resources.'
random_paper: 106
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 36.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexisnexis-risk-solutions/refs/heads/main/screenshots/lexisnexis-risk-solutions-2026-07-25T224959.png
security:
- kind: authentication
  name: Lexisnexis Risk Solutions Authentication
  slug: lexisnexis-risk-solutions-authentication
  summary_line: oauth1/oauth2 · 2 schemes
- kind: domain-security
  name: Lexisnexis Risk Solutions Domain Security
  slug: lexisnexis-risk-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lexisnexis Risk Solutions Vulnerability Disclosure
  slug: lexisnexis-risk-solutions-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Lexisnexis Risk Solutions Trust Center
  slug: lexisnexis-risk-solutions-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: lexisnexis-risk-solutions
tags:
- Insurance
- United States
- Risk Data
- Property and Casualty
- Underwriting
- Claims
- Life Insurance
- Auto Insurance
- Data Analytics
- Partner Gated
website: https://risk.lexisnexis.com/
---
