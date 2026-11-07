---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/applause/well-known/applause-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applause-well-known.yml
- group: other
  href: https://artifacts.apis.io/applause/hosts/applause-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applause-hosts.yml
- group: other
  href: https://artifacts.apis.io/applause/vendors/applause-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applause-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applause.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.applause.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.applause.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.applause.com/sign-up-for-your-svod-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.applause.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.applause.com/pricing-inquiry/
- group: company
  title: ''
  type: Newsroom
  url: https://www.applause.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.applause.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.applause.com/blog/
- group: auth
  href: https://artifacts.apis.io/applause/security/applause-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applause-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.applause.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.applause.com/mcp
  - status: 403
    url: https://platform.applause.com/mcp
  - status: 200
    url: https://www.applause.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Applause offers managed software testing services that combine a global community of crowdtesters with AI and automation to help enterprises scale testing, improve quality, and accelerate release cycles. It provides functional, security, accessibility, payment, localization, and AI evaluation testing for digital products across web, mobile, and desktop platforms.
image: https://www.applause.com/wp-content/uploads/applause_brand_image.jpg
layout: provider
modified: '2026-10-23'
name: Applause
nav: Providers
network: true
overview: 'Applause is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software Testing, Crowdtesting, AI Testing, Functional Testing, and Accessibility Testing.


  Applause''s developer surface includes support, signup flow, pricing, engineering blog, and 10 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/applause/applause-2026-11-03T121028.png
security:
- kind: domain-security
  name: Applause Domain Security
  slug: applause-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applause
tags:
- Software Testing
- Crowdtesting
- AI Testing
- Functional Testing
- Accessibility Testing
- Payment Testing
- Localization
- Security Testing
website: https://www.applause.com/
---
