---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://help.soothe.com
  baseurl_source: declared
  description: The auto-generated OpenAPI 3.1.0 schema published by the FastAPI application Soothe runs at help.soothe.com to serve a self-hosted mirror of its Document360 help centre. It describes the mirror servic
  name: Soothe Help Center Mirror
  slug: soothe-help-center-mirror
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.soothe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.soothe.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.soothe.com/
- group: operate
  title: ''
  type: Support
  url: https://www.soothe.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.soothe.com/articles/
- group: start
  title: ''
  type: SignUp
  url: https://www.soothe.com/sign_on/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soothe.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soothe.com/legal/privacy/us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soothe
- group: auth
  title: ''
  type: Authentication
  url: authentication/soothe-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soothe-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soothe-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soothe-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soothe-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soothe-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/soothe-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/soothe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soothe-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Soothe's API host api.soothe.com 301s every path to a Rails/Devise session sign-in form (page title "Api | Log In") and returns that same login HTML for every URL including a random-path control, so no contract, reference or error shape is reachable without credentials; the only machine-readable document Soothe serves publicly is the auto-generated FastAPI schema of its self-hosted help-centre mirror at help.soothe.com, which describes page serving and a health check rather than the booking marketplace.
  evidence:
  - status: 301
    url: https://api.soothe.com/
  - status: 200
    url: https://api.soothe.com/users/sign_in
  - status: 200
    url: https://api.soothe.com/openapi.json
  - status: 200
    url: https://help.soothe.com/openapi.json
  - status: 404
    url: https://www.soothe.com/docs
  reason: partner-login
  state: gated
created: '2026-08-28'
description: 'Soothe is a Los Angeles-based on-demand wellness marketplace, founded in 2013, that connects consumers and businesses with independent, licensed wellness professionals who deliver services at the customer''s own location. The marketplace covers massage (Swedish, deep tissue, sports, prenatal, chair, percussive, reflexology, lymphatic, acupressure, Thai and myofascial), facials and skincare, and hair and beauty services, booked through the Soothe consumer app and web booking flow and fulfilled through the separate Soothe for Providers app. Alongside the B2C business, Soothe runs a B2B practice covering corporate and employee wellness programs, hospitality and spa staffing, residential communities and event chair massage, plus a SoothePass subscription membership. It operates in 40+ US cities across roughly 32 states and Washington D.C., and internationally in Australia, Canada and the United Kingdom. Soothe publishes no public developer program: its API host, api.soothe.com,
  is a credentialed sign-in wall, and the partner booking platform it markets to hospitality and corporate customers is reached through a contact-sales form rather than public documentation.'
image: https://www.soothe.com/wp-content/uploads/2021/09/cropped-cropped-soothe-logo-hands-blue-32x32.png
layout: provider
modified: '2026-08-28'
name: Soothe
nav: Providers
network: true
overview: 'Soothe publishes 1 API on the [APIs.io](https://apis.io/) network: Help Center Mirror. Tagged areas include Company, Wellness, Health and Wellness, Massage, and Marketplace.


  Soothe''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 14 more developer resources.'
plans:
- name: Soothe Plans Pricing
  plan_count: 0
  slug: soothe-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Soothe Rate Limits
  slug: soothe-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 34.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soothe/refs/heads/main/screenshots/soothe-2026-09-02T160236.png
security:
- kind: authentication
  name: Soothe Authentication
  slug: soothe-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Soothe Domain Security
  slug: soothe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soothe
tags:
- Company
- Wellness
- Health and Wellness
- Massage
- Marketplace
- On-Demand Services
- Beauty
- Corporate Wellness
- Hospitality
- Consumer Services
- Local Services
- Booking
website: https://www.soothe.com/
---
