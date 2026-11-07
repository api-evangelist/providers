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
  href: https://artifacts.apis.io/tune/well-known/tune-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tune-well-known.yml
- group: other
  href: https://artifacts.apis.io/tune/hosts/tune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tune-hosts.yml
- group: other
  href: https://artifacts.apis.io/tune/vendors/tune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tune-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tune.com/resources/data-and-privacy/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://help.tune.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.tune.com/about/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.tune.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tune.com/network-docs/setup-essentials/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tune.com/
- group: auth
  href: https://artifacts.apis.io/tune/security/tune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tune.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.tune.com/mcp
  - status: 200
    url: https://tune.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Tune provides a partner marketing platform that enables advertisers, networks, and agencies to manage, measure, and pay affiliate and partnership programs. The SaaS solution offers customizable dashboards, real‑time reporting, fraud prevention, and extensive API access with over 650 endpoints for integration, data streaming, and automation across direct‑to‑consumer, financial services, and subscription verticals.
image: https://www.tune.com/wp-content/uploads/2024/03/tune-logo-white-background-1500px.jpg
layout: provider
modified: '2026-10-27'
name: Tune
nav: Providers
network: true
overview: 'Tune is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Affiliates, Software-as-a-Service, Advertising, and Partnerships.


  Tune''s developer surface includes support, engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tune/tune-2026-11-03T145230.png
security:
- kind: domain-security
  name: Tune Domain Security
  slug: tune-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tune
tags:
- Marketing
- Affiliates
- Software-as-a-Service
- Advertising
- Partnerships
website: https://tune.com/
---
