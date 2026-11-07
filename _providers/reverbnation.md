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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/reverbnation/hosts/reverbnation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reverbnation-hosts.yml
- group: other
  href: https://artifacts.apis.io/reverbnation/vendors/reverbnation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reverbnation-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.reverbnation.com/login
- group: auth
  href: https://artifacts.apis.io/reverbnation/security/reverbnation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reverbnation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reverbnation.com/
- group: docs
  title: ''
  type: Documentation
  url: https://legacy.reverbnation.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://legacy.reverbnation.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.reverbnation.com/registration/new
- group: operate
  title: ''
  type: Support
  url: https://help.reverbnation.com
- group: company
  title: ''
  type: Blog
  url: https://blog.reverbnation.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reverbnation.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reverbnation.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reverbnation.com/privacy
coverage:
  checked: '2026-10-28'
  detail: ReverbNation provides HTML help pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://help.reverbnation.com/hc/en-us
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: ReverbNation is a music platform that helps artists grow their careers by offering distribution, promotion tools, publishing, and opportunities to connect with industry professionals. Musicians can release music to major streaming services, access marketing resources, and explore revenue options through cash advances and sync licensing. The service provides a suite of tools for audience building, fan engagement, and career development, supporting both emerging and established artists worldwide.
layout: provider
modified: '2026-10-28'
name: ReverbNation
nav: Providers
network: true
overview: 'ReverbNation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Distribution, Promotion, Artists, and Platform.


  ReverbNation''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reverbnation/reverbnation-2026-11-03T142230.png
security:
- kind: domain-security
  name: Reverbnation Domain Security
  slug: reverbnation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reverbnation
tags:
- Music
- Distribution
- Promotion
- Artists
- Platform
- Company
website: https://www.reverbnation.com/
---
