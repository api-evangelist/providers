---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/openapi-com/well-known/openapi-com-openapi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openapi-com-openapi-com-security.txt
- group: agent
  href: https://artifacts.apis.io/openapi-com/well-known/openapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openapi-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/openapi-com/authentication/openapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openapi-com-authentication.yml
- group: other
  href: https://artifacts.apis.io/openapi-com/hosts/openapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/openapi-com/vendors/openapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openapi.com/terms-conditions-openapi
- group: operate
  title: ''
  type: StatusPage
  url: https://openapi-com.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.openapi.com/en-privacy-policy.html?domain=openapi.com
- group: company
  title: ''
  type: Newsroom
  url: https://openapi.com/press
- group: start
  title: ''
  type: Login
  url: https://console.openapi.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openapi/
- group: docs
  title: ''
  type: APIReference
  url: https://console.openapi.com/apis/trust/documentation
- group: auth
  href: https://artifacts.apis.io/openapi-com/security/openapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://openapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://openapi.com/blog
- group: operate
  title: ''
  type: Support
  url: https://openapi.com/contact-us
coverage:
  checked: '2026-10-31'
  detail: The provider's homepage renders documentation via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://openapi.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Openapi SpA operates an API marketplace offering over 400 services across sectors such as AI, automotive, finance, real estate and more. The platform provides a unified developer portal, documentation, pricing, and partner programs, aiming to accelerate digital transformation for businesses worldwide.
image: https://openapi.com/assets/images/openapi-og-default.png
layout: provider
modified: '2026-10-30'
name: openapi-com
nav: Providers
network: true
overview: 'openapi-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace, B2B, Data Services, Integration, and OpenAPI.


  openapi-com''s developer surface includes authentication, API reference, pricing, engineering blog, support, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 49.1
    operational_transparency: 21.1
  previous_composite: 24.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/openapi-com/openapi-com-2026-11-03T140632.png
security:
- kind: authentication
  name: Openapi Com Authentication
  slug: openapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openapi Com Domain Security
  slug: openapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openapi-com
tags:
- API Marketplace
- B2B
- Data Services
- Integration
- OpenAPI
website: https://openapi.com/
---
