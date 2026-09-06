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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Cuvva''s fleet of public single-purpose service APIs — auth (OAuth 2.0), vehicle lookup, MOT status, motor-coverage quotes/policies, billing, promo, profile, upload, terms, notification and more. Most '
  name: Cuvva Services API
  slug: cuvva-services-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.cuvva.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/cuvva/docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cuvva/docs/tree/master/apis
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/cuvva/docs/tree/master/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuvva
- group: operate
  title: ''
  type: Support
  url: https://support.cuvva.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.cuvva.com/en
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cuvva.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.cuvva.com/en/articles/5907873-cuvva-s-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.cuvva.com/en/articles/5907862-cuvva-s-privacy-notice
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuvva-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cuvva-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/cuvva-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cuvva-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cuvva-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cuvva-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cuvva-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cuvva-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuvva-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cuvva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cuvva-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuvva-llms.txt
created: '2026-07-17'
description: Cuvva is a UK insurtech that pioneered flexible, short-term car and van insurance sold entirely through its mobile apps. Founded in 2015 as the first app to sell temporary car insurance in the UK, it offers policies from one hour up to 28 days, learner-driver cover, drive-away cover for newly purchased vehicles, temporary van and motorhome insurance, and a rolling subscription product (formerly Flexi). Cuvva is FCA-authorised and has sold over 16 million policies to 1.7M+ drivers. Its engineering is built on a fleet of small single-purpose service APIs (auth, vehicle, MOT, motor-coverage, billing, promo, profile, upload, terms, notification and more), publicly documented on GitHub and secured with an in-house OAuth 2.0 implementation using JWT bearer tokens.
image: https://www.cuvva.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Cuvva
nav: Providers
network: true
overview: 'Cuvva publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Car Insurance, and Financial-Services.


  Cuvva''s developer surface includes documentation, API reference, support, authentication, and 18 more developer resources.'
random_paper: 3
scopes:
- name: Cuvva Scopes
  scope_count: 1
  slug: cuvva-scopes
  summary_line: 1 scope · authorizationCode/refreshToken
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 34.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cuvva/refs/heads/main/screenshots/cuvva-2026-07-25T211014.png
security:
- kind: authentication
  name: Cuvva Authentication
  slug: cuvva-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cuvva Domain Security
  slug: cuvva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cuvva Vulnerability Disclosure
  slug: cuvva-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cuvva
tags:
- Company
- Insurance
- Insurtech
- Car Insurance
- Financial-Services
- Mobile
- Authentication
- United Kingdom
website: https://www.cuvva.com
---
