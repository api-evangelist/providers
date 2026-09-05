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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'CCC''s only publicly named API product. Secure Share is described by CCC as "a network using cloud-based APIs to permit more than 22,000 collision repairers to connect to apps using the CIECA BMS data '
  name: CCC Secure Share API
  slug: ccc-secure-share-api
- description: CCC's production API gateway. GET https://api.cccis.com/v1 returns HTTP 401 with an RFC 6750 Bearer challenge and an Apigee fault body ({"fault":{"faultstring":"Invalid access token","detail":{"errorc
  name: CCC Platform API Gateway
  slug: ccc-platform-api
- description: The Okta-hosted identity service behind CCC Connect and the CCC customer and partner portals, running on the custom domain auth.cccis.com (cccis.customdomains.okta.com). This is the only CCC surface t
  name: CCC Identity (OpenID Connect)
  slug: ccc-identity-oidc
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.cccis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cccis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cccis.com/product-documentation
- group: company
  title: ''
  type: Blog
  url: https://www.cccis.com/news-and-insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cccis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ccc-intelligent-solutions
- group: company
  title: ''
  type: Partners
  url: https://www.cccis.com/about/partners
- group: operate
  title: ''
  type: Support
  url: https://www.cccis.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.cccis.com/contact
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.cccis.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cccis.com/policy/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cccis.com/policy/terms-and-conditions
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.cccis.com/policy/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cccis.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cccis.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.cccis.com/policy/information-security-program
- group: auth
  title: ''
  type: Security
  url: https://www.cccis.com/policy/information-security-program
- group: start
  title: ''
  type: SignUp
  url: https://www.cccsecureshare.com/Register
- group: start
  title: ''
  type: Login
  url: https://connect.cccis.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ccc-intelligent-solutions-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ccc-intelligent-solutions-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ccc-intelligent-solutions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ccc-intelligent-solutions-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ccc-intelligent-solutions-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ccc-intelligent-solutions-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ccc-intelligent-solutions-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ccc-intelligent-solutions-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/ccc-intelligent-solutions-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ccc-intelligent-solutions-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ccc-intelligent-solutions-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/ccc-intelligent-solutions-security-policy.yml
created: '2026-07-25'
description: CCC Intelligent Solutions (CCCIS, NASDAQ CCCS) is a Chicago-headquartered cloud software company that sits between US property and casualty insurance carriers and the auto claims economy. Its IX Cloud platform and CCC ONE estimating products run auto physical damage estimating, total-loss valuation, reinspection, subrogation, first- and third-party casualty medical bill review, parts procurement, and claim payments across tens of thousands of insurers, collision repair facilities, automakers, parts suppliers and lenders. CCC is a claims-technology intermediary rather than a risk carrier, and it is one of the software layers that accumulated value in a US market with no federal insurance regulator and no open-insurance mandate. Its API posture is honest to that seam and is entirely partner-gated - there is no public, self-serve developer portal, no downloadable OpenAPI, and no public API reference. The production gateway at api.cccis.com is live but answers unauthenticated calls
  with an OAuth 2.0 bearer token fault, portal access runs through an Okta-hosted OAuth 2.0 authorization-code flow at auth.cccis.com, and the one named public API product - CCC Secure Share - publishes only a marketing developer page whose documentation, samples and dashboard require registration, CCC approval and active CIECA membership. CCC's data-standards posture is CIECA (BMS/EMS) rather than ACORD. The only machine-readable surfaces CCC serves anonymously are the Okta OpenID Connect discovery documents at auth.cccis.com and an llms.txt at www.cccis.com that maps the marketing and policy site but names no API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: CCC Intelligent Solutions
nav: Providers
network: true
overview: 'CCC Intelligent Solutions publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Property and Casualty, Claims, and Auto Physical Damage.


  CCC Intelligent Solutions'' developer surface includes documentation, engineering blog, support, signup flow, authentication, and 26 more developer resources.'
random_paper: 16
scopes:
- name: Ccc Intelligent Solutions Scopes
  scope_count: 9
  slug: ccc-intelligent-solutions-scopes
  summary_line: 9 scopes · authorizationCode/implicit/deviceCode/clientCredentials
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 32.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ccc-intelligent-solutions/refs/heads/main/screenshots/ccc-intelligent-solutions-2026-07-25T204826.png
security:
- kind: authentication
  name: Ccc Intelligent Solutions Authentication
  slug: ccc-intelligent-solutions-authentication
  summary_line: oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Ccc Intelligent Solutions Domain Security
  slug: ccc-intelligent-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ccc Intelligent Solutions Trust Center
  slug: ccc-intelligent-solutions-trust-center
  summary_line: trust center published
slug: ccc-intelligent-solutions
tags:
- Insurance
- United States
- Property and Casualty
- Claims
- Auto Physical Damage
- Collision Repair
- Insurtech
- Claims Technology
- CIECA
- Partner Gated
- Authentication
- OpenID Connect
website: https://www.cccis.com/
---
