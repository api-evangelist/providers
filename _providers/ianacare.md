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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://ianacare.com/
- group: operate
  title: ''
  type: Support
  url: https://support.ianacare.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.ianacare.com/
- group: company
  title: ''
  type: Blog
  url: https://ianacare.com/resource-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ianacare.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ianacare.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ianacare-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ianacare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ianacare-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/ianacare-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/ianacare-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ianacare-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ianacare-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ianacare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ianacare-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ianacare-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/ianacare-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/ianacare-packages.yml
coverage:
  checked: '2026-08-22'
  detail: 'ianacare ships software only as an end-user product — an iOS/Android caregiving app and the app.ianacare.com web client sold through employers and health plans — and publishes no developer surface of any kind: the CloudFront-fronted API edge api.ianacare.com answers HTTP 403 {"message":"Forbidden"} on every path including the root, the real application host iana.ianacare.com answers HTTP 401 {"error":{"code":"auth_denied","message":"Missing bearer token"}} with no way to obtain a client, the 49-page site sitemap contains no developer, API or integration page, and the github.com/ianacare organization has 0 public repositories; the only machine-readable contract on any ianacare host is the OIDC discovery document its own Auth0 custom domain serves for its own apps.'
  evidence:
  - status: 403
    url: https://api.ianacare.com/openapi.json
  - status: 401
    url: https://iana.ianacare.com/api/v1
  - status: 404
    url: https://iana.ianacare.com/openapi.json
  - status: 200
    url: https://auth.ianacare.com/.well-known/openid-configuration
  - status: 404
    url: https://auth.ianacare.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/ianacare
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=ianacare
  - status: 202
    url: https://ianacare.com/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'ianacare ("iana" = I Am Not Alone) is a Boston-based caregiver support and navigation platform that sells to employers, health plans and providers as a benefit for the working family caregivers in their populations. Founded in 2018 by Jessica Kim and Steven Lee, it pairs a consumer mobile app — where a caregiver mobilizes an informal care team, coordinates practical tasks, unlocks employer benefits and finds local resources — with human Caregiver Navigators, and positions itself as a partner for fulfilling CMS GUIDE Model dementia-care requirements. The company raised a $12.1M Series A in January 2022 led by Greycroft with 8VC, SemperVirens, Able Partners and the Brown Angel Group. ianacare ships software only as an end-user product: the iOS and Android apps and the app.ianacare.com web client are backed by first-party hosts (iana.ianacare.com behind a JWT bearer token, api.ianacare.com behind a CloudFront 403) and by ianacare''s own Auth0 custom domain auth.ianacare.com, which
  is the single machine-readable contract the company publishes. There is no developer portal, API reference, OpenAPI, SDK, CLI, webhook catalog, MCP server or agent card on any ianacare host.'
image: https://ianacare.com/wp-content/uploads/2024/11/Ianacare_part-3__102-1.webp
layout: provider
modified: '2026-08-22'
name: ianacare
nav: Providers
network: true
overview: 'ianacare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Caregiving, Employee Benefits, and Digital Health.


  ianacare''s developer surface includes support, engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Ianacare Plans Pricing
  plan_count: 0
  slug: ianacare-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ianacare Rate Limits
  slug: ianacare-rate-limits
scopes:
- name: Ianacare Scopes
  scope_count: 0
  slug: ianacare-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 17.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ianacare/refs/heads/main/screenshots/ianacare-2026-09-02T145814.png
security:
- kind: authentication
  name: Ianacare Authentication
  slug: ianacare-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Ianacare Domain Security
  slug: ianacare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ianacare
tags:
- Company
- Healthcare
- Caregiving
- Employee Benefits
- Digital Health
- Care Navigation
- Health Plans
- Mobile Application
- Identity
website: https://ianacare.com/
---
