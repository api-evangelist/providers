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
  url: https://www.sidecare.com/
- group: start
  title: ''
  type: Login
  url: https://www.sidecare.com/connexion-hub
- group: operate
  title: ''
  type: Support
  url: https://support.sidecare.com
- group: company
  title: ''
  type: Blog
  url: https://www.sidecare.com/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sidecare.com/cgu-rgpd
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sidecare.com/cgu-rgpd
- group: auth
  title: ''
  type: Authentication
  url: authentication/sidecare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sidecare-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.sidecare.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sidecare-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sidecare-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidecare-domain-security.yml
created: '2026-07-17'
description: SideCare is a French insurtech and HR-benefits platform (operated by Hoggo) that helps companies build, deploy, and manage their employee health policy. It brokers and administers collective health insurance (mutuelle) and disability cover (prévoyance), comparing more than 15,500 contracts, and adds a free SIRH/HR and quality-of-life (QVT) layer, a digital clinic with telemedicine, and the SideCard prepaid health-expense card that advances up to €1,500/month. Over 7,800 companies and 100,000+ insured individuals use the platform. SideCare runs a "Sign in with SideCare" OpenID Connect identity provider and integrates with payroll/HRIS tools such as PayFit, Lucca, and Nibelis. Backed by Partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sidecare.png
layout: provider
modified: '2026-07-21'
name: SideCare
nav: Providers
network: true
overview: 'SideCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Insurance, Insurtech, and Health Insurance.


  SideCare''s developer surface includes support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 13
scopes:
- name: Sidecare Scopes
  scope_count: 4
  slug: sidecare-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 22.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sidecare/refs/heads/main/screenshots/sidecare-2026-09-02T155352.png
security:
- kind: authentication
  name: Sidecare Authentication
  slug: sidecare-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Sidecare Domain Security
  slug: sidecare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sidecare
tags:
- Company
- Financial-Services
- Insurance
- Insurtech
- Health Insurance
- Employee Benefits
- Human Resources
- HRIS
- France
- OpenID Connect
website: https://www.sidecare.com/
---
