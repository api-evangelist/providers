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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.nekohealth.com
- group: company
  title: ''
  type: About
  url: https://www.nekohealth.com/gb/en/about
- group: operate
  title: ''
  type: Support
  url: https://www.nekohealth.com/us/en/faq
- group: start
  title: ''
  type: SignUp
  url: https://account.nekohealth.com/login/phone
- group: start
  title: ''
  type: Login
  url: https://app.nekohealth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nekohealth.com/se/en/health-scan
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nekohealth.com/se/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.nekohealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nekohealth.com/gb/en/press
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neko-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neko-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/neko-health-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://account.nekohealth.com/.well-known/openid-configuration
- group: design
  title: ''
  type: Conformance
  url: conformance/neko-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neko-health-domain-security.yml
created: '2026-07-17'
description: Neko Health is a Swedish preventive-healthcare company founded in 2018 by Daniel Ek and Hjalmar Nilsonne. It designs, engineers, and assembles its own full-body scanning hardware in Stockholm and operates clinics across Sweden, the UK (London, Manchester, Birmingham) and, following a $700M Series C, the United States. The roughly 60-minute Neko Health Scan is a non-invasive, radiation-free examination that captures millions of data points across the skin, heart, blood, and circulation in a single visit, feeding a consumer patient app. Neko exposes no public third-party developer API; its only public machine surface is a Duende IdentityServer OIDC provider (account.nekohealth.com) that authenticates the patient application. This profile was surfaced as a venture-portfolio lead and enriched from Neko's public web and identity surface.
image: https://www.nekohealth.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Neko Health
nav: Providers
network: true
overview: 'Neko Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Preventive Health, and Medical.


  Neko Health''s developer surface includes support, signup flow, pricing, engineering blog, authentication, and 10 more developer resources.'
random_paper: 12
scopes:
- name: Neko Health Scopes
  scope_count: 4
  slug: neko-health-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 19.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Neko Health Authentication
  slug: neko-health-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Neko Health Domain Security
  slug: neko-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neko-health
tags:
- Company
- Health
- Healthcare
- Preventive Health
- Medical
- Body Scan
- Diagnostics
- Consumer Health
- OpenID Connect
- Sweden
website: https://www.nekohealth.com
---
