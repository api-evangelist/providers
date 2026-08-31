---
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
    error_semantics: false
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
  score: 15.1
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/place-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/place-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/place-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/place-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/place-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/place-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PLACE-INC
- group: company
  title: ''
  type: Website
  url: https://place.com/
- group: other
  title: ''
  type: Platform
  url: https://place.com/platform/
- group: other
  title: ''
  type: Technology
  url: https://place.com/real-estate-technology/
- group: company
  title: ''
  type: About
  url: https://place.com/about-place/
- group: company
  title: ''
  type: Blog
  url: https://place.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://place.com/feed/
- group: company
  title: ''
  type: Press
  url: https://place.com/press/
- group: operate
  title: ''
  type: Support
  url: https://place.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://place.com/join/
- group: start
  title: ''
  type: Login
  url: https://place.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://place.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://place.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://place.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/placeinc
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/place_stock/
coverage:
  checked: '2026-08-05'
  detail: PLACE ships its real-estate operating platform only to contracted teams behind Okta single sign-on — there is no developer.place.com, docs.place.com or api.place.com host in DNS, the platform page never mentions an API, and the only machine-readable documents on any PLACE host are the OIDC/OAuth discovery blobs its sign-on servers emit.
  evidence:
  - status: 0
    url: https://developer.place.com/
  - status: 404
    url: https://place.com/llms.txt
  - status: 404
    url: https://place.com/.well-known/api-catalog
  - status: 200
    url: https://place.com/platform/
  - status: 200
    url: https://sso.place.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: PLACE, Inc. is a Bellingham, Washington real estate technology and business-services company founded in 2020 by Ben Kinney and Chris Suarez. It sells an end-to-end operating platform to real estate teams, agents and brokerages — a CRM with lead-generation websites, transaction management, automated marketing, mobile apps and AI tooling — bundled with shared back-office services covering accounting, hiring, training, finance and digital advertising, plus adjacent mortgage, title and escrow, insurance, property management and home-services offerings. PLACE partners with teams in 500+ locations across the United States and Canada, raised a $100M Series A led by a division of Goldman Sachs Asset Management at unicorn valuation, and acquired MLS data platform Remine to extend its technology ecosystem. The platform is delivered only to contracted teams behind single sign-on; PLACE publishes no public API, developer portal, SDK or machine-readable specification.
image: https://place.com/wp-content/uploads/2025/12/Group-8805.jpg
layout: provider
modified: '2026-08-05'
name: PLACE
nav: Providers
network: true
overview: 'PLACE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Property Technology, PropTech, and CRM.


  PLACE''s developer surface includes authentication, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 13
scopes:
- name: Place Scopes
  scope_count: 8
  slug: place-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 20.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Place Authentication
  slug: place-authentication
  summary_line: openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Place Domain Security
  slug: place-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: place
tags:
- Company
- Real-Estate
- Property Technology
- PropTech
- CRM
- Transaction Management
- Brokerage
- MLS
- Mortgage
- Title and Escrow
- Business Services
- Identity
website: https://place.com/
---
