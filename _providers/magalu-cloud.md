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
  href: https://artifacts.apis.io/magalu-cloud/vendors/magalu-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/magalu-cloud-vendors.yml
- group: agent
  href: https://artifacts.apis.io/magalu-cloud/llms/magalu-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/magalu-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/magalu-cloud/hosts/magalu-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/magalu-cloud-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.magalu.cloud/hc/pt-br
- group: operate
  title: ''
  type: StatusPage
  url: https://status.magalu.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.magalu.cloud/docs/release-notes
- group: company
  title: ''
  type: Blog
  url: https://magalu.cloud/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.magalu.cloud/docs/tags/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.magalu.cloud/
- group: auth
  href: https://artifacts.apis.io/magalu-cloud/security/magalu-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/magalu-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://magalu.cloud/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered HTML without machine‑readable specs.
  evidence:
  - status: 200
    url: https://docs.magalu.cloud/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Magalu Cloud is a Brazilian public cloud platform offering managed compute, storage, networking, database and security services for enterprise workloads. It emphasizes simplicity and fair pricing, aiming to accelerate business digital transformation with a local presence and support.
image: https://magalu.cloud/og-default.png
layout: provider
modified: '2026-10-27'
name: Magalu Cloud
nav: Providers
network: true
overview: 'Magalu Cloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, Brazil, Public Cloud, and Platform.


  Magalu Cloud''s developer surface includes support, changelog, engineering blog, getting-started guide, documentation, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/magalu-cloud/magalu-cloud-2026-11-03T135214.png
security:
- kind: domain-security
  name: Magalu Cloud Domain Security
  slug: magalu-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: magalu-cloud
tags:
- Cloud
- Infrastructure
- Brazil
- Public Cloud
- Platform
- Company
website: https://magalu.cloud/
---
