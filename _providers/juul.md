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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juul-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.juullabs.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JuulLabs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.juullabs.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.juullabs.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.juullabs.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.juullabs.com/about/newsroom/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/juul-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/juul-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/juul-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/juul-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/juul-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juul-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/juul-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/juul-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: 'JUUL Labs is a consumer nicotine-products manufacturer with no developer program: the corporate site www.juullabs.com returns a real 404 for /developers, /api and every /.well-known path, and the only machine-readable document on any JUUL host is a first-party OAuth 2.0 discovery doc at https://www.juul.com/.well-known/openid-configuration that has no public client registration.'
  evidence:
  - status: 404
    url: https://www.juullabs.com/developers
  - status: 404
    url: https://www.juullabs.com/api
  - status: 404
    url: https://www.juul.com/openapi.json
  - status: 200
    url: https://www.juul.com/.well-known/openid-configuration
  - status: 403
    url: https://www.juul.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: 'JUUL Labs is the San Francisco-headquartered maker of the JUUL vaporizer, a closed-system electronic nicotine delivery system (ENDS) sold to adult smokers in the United States, the United Kingdom, Canada and a small number of other regulated markets. The company designs and manufactures the JUUL device and its JUULpod cartridges, operates the age-verified direct-to-consumer storefront at juul.com, and pursues FDA Premarket Tobacco Product Application (PMTA) authorization for its products. JUUL Labs is a consumer hardware and regulated tobacco-products company, not a software vendor: it publishes no public API, no developer portal, and no machine-readable API contract. Its engineering organization does maintain a real, actively-released open source presence under the JuulLabs GitHub organization — Kotlin Multiplatform libraries for Bluetooth Low Energy (Kable), CoAP (koap), canvas drawing (krayon), logging (khronicle) and general utilities (tuulbox), published to Maven Central
  under the com.juul.* group IDs — and it serves a real OAuth 2.0 / OpenID Connect discovery document from its consumer commerce host for its own first-party web and mobile sign-in.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-23'
name: JUUL
nav: Providers
network: true
overview: 'JUUL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Products, Nicotine, Vaping, and Hardware.


  JUUL''s developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: Juul Plans Pricing
  plan_count: 0
  slug: juul-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Juul Rate Limits
  slug: juul-rate-limits
scopes:
- name: Juul Scopes
  scope_count: 0
  slug: juul-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/juul/refs/heads/main/screenshots/juul-2026-09-02T150010.png
security:
- kind: authentication
  name: Juul Authentication
  slug: juul-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Juul Domain Security
  slug: juul-domain-security
  summary_line: TLSv1.3 · DMARC
slug: juul
tags:
- Company
- Consumer Products
- Nicotine
- Vaping
- Hardware
- Consumer Electronics
- Bluetooth Low Energy
- Open-Source
- Kotlin Multiplatform
- Regulated Industry
website: https://www.juullabs.com/
---
