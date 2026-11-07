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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/my-casa/hosts/my-casa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/my-casa-hosts.yml
- group: other
  href: https://artifacts.apis.io/my-casa/vendors/my-casa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/my-casa-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://getcasa.com/trust
- group: start
  title: ''
  type: SignUp
  url: https://getcasa.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getcasa.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://getcasa.com/press
- group: auth
  href: https://artifacts.apis.io/my-casa/security/my-casa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/my-casa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getcasa.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.getcasa.com/mcp
  - status: 403
    url: https://getcasa.com/mcp
  - status: 200
    url: https://my.casa
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Casa provides a smart home security platform that integrates door locks, cameras, and alarm systems into a unified mobile experience. The company focuses on user‑friendly design, robust encryption, and seamless integration with third‑party IoT devices, offering both subscription and one‑time purchase options for consumers and property managers. Founded in 2020, Casa has grown to serve millions of households across North America and Europe, emphasizing privacy, reliability, and continuous software updates.
image: https://frontdoor-assets.r2.getcasa.com/images/fd411e07d012bd0b1a27557aecf7663d.jpg
layout: provider
modified: '2026-10-25'
name: Casa
nav: Providers
network: true
overview: 'Casa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, Security, IoT, and Subscription.


  Casa''s developer surface includes signup flow and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/my-casa/my-casa-2026-11-03T135931.png
security:
- kind: domain-security
  name: My Casa Domain Security
  slug: my-casa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: my-casa
tags:
- Company
- Smart Home
- Security
- IoT
- Subscription
website: https://getcasa.com
---
