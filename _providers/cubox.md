---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cubox/plans/cubox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cubox-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/cubox/hosts/cubox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cubox-hosts.yml
- group: build
  href: https://artifacts.apis.io/cubox/packages/cubox-packages.yml
  title: ''
  type: SDKs
  url: packages/cubox-packages.yml
- group: build
  href: https://artifacts.apis.io/cubox/packages/cubox-packages.yml
  title: ''
  type: Packages
  url: packages/cubox-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cubox.pro/pricing
- group: start
  title: ''
  type: Login
  url: https://cubox.pro/web/signin
- group: docs
  title: ''
  type: Documentation
  url: https://help.cubox.pro/
- group: auth
  href: https://artifacts.apis.io/cubox/security/cubox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cubox.pro/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation pages contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://help.cubox.pro/save/89d3/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Cubox provides an AI‑enhanced reading assistant that helps users collect, annotate, and organize web articles and documents across devices. The platform offers features such as automatic content extraction, AI‑generated summaries, tagging, and a personal knowledge vault that syncs between iOS, Android, macOS, Windows, and browser extensions. Users can subscribe to free or paid plans for increased storage, AI credits, and advanced collaboration tools, while the service emphasizes data ownership and privacy.
image: https://image.cubox.pro/webogimage.jpg
layout: provider
modified: '2026-10-28'
name: Cubox
nav: Providers
network: true
overview: 'Cubox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Reading, Knowledge Management, and Productivity.


  Cubox''s developer surface includes pricing, documentation, and 7 more developer resources.'
plans:
- name: Cubox Plans Pricing
  plan_count: 2
  slug: cubox-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cubox/cubox-2026-11-03T125744.png
security:
- kind: domain-security
  name: Cubox Domain Security
  slug: cubox-domain-security
  summary_line: TLSv1.2
slug: cubox
tags:
- Company
- Artificial Intelligence
- Reading
- Knowledge Management
- Productivity
- Cross-Platform
website: https://cubox.pro/
---
