---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    delegated_identity: false
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
  score: 10.8
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://better.com
- group: company
  title: ''
  type: AboutUs
  url: https://better.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://better.com/content
- group: operate
  title: ''
  type: Support
  url: https://better.com/about-us/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://better.com/mortgage-rates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://better.com/about-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://better.com/about-us/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/better-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/better-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/better-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/better-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/better-domain-security.yml
created: '2026-07-17'
description: 'Better (Better Home & Finance Company, NASDAQ: BETR) is a New York-based digital homeownership company founded in 2014 by Vishal Garg. Its Tinman-powered platform delivers an end-to-end online mortgage experience - purchase loans, refinancing, cash-out refinancing, HELOCs, VA loans, and crypto-backed mortgages - alongside real estate agent matching, title and closing services, and homeowners insurance through Better+. Better became a Fannie Mae-approved seller/servicer in 2016, has funded over $100B in mortgages, and launched One Day Mortgage in 2023. It is backed by SoftBank Vision Fund, Bond Capital, Ally, Citi, Ping An, Goldman Sachs, KPCB, and American Express. Better publishes no public developer API; this profile captures its public web, consumer identity (AWS Cognito OIDC), and domain-security surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/better.png
layout: provider
modified: '2026-07-18'
name: Better
nav: Providers
network: true
overview: 'Better is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Lending, Fintech, and Real-Estate.


  Better''s developer surface includes engineering blog, support, pricing, authentication, and 8 more developer resources.'
random_paper: 16
scopes:
- name: Better Scopes
  scope_count: 4
  slug: better-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/better/refs/heads/main/screenshots/better-2026-07-25T202802.png
security:
- kind: authentication
  name: Better Authentication
  slug: better-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Better Domain Security
  slug: better-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: better
tags:
- Company
- Mortgage
- Lending
- Fintech
- Real-Estate
- Home Equity
- Insurance
- Financial-Services
website: https://better.com
---
