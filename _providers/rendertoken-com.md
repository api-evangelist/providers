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
  href: https://artifacts.apis.io/rendertoken-com/plans/rendertoken-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rendertoken-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/rendertoken-com/hosts/rendertoken-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rendertoken-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rendertoken-com/vendors/rendertoken-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rendertoken-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://rendernetwork.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://rendernetwork.com/getting-started
- group: auth
  href: https://artifacts.apis.io/rendertoken-com/security/rendertoken-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rendertoken-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rendertoken.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rendertoken.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Render (operating as Render Network) is a decentralized GPU computing platform that enables developers and enterprises to harness distributed GPU resources for high‑performance workloads such as AI model training, rendering, and scientific simulations. The platform provides a marketplace for GPU providers, APIs for job submission, monitoring, and billing, and aims to lower costs while increasing accessibility to powerful compute resources across the globe.
image: https://rendernetwork.com/api/medias/file/SEO-1.jpg
layout: provider
modified: '2026-10-22'
name: Render
nav: Providers
network: true
overview: 'Render is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Decentralized, GPU, Compute, and Platform.


  Render''s developer surface includes pricing, getting-started guide, and 5 more developer resources.'
plans:
- name: Rendertoken Com Plans Pricing
  plan_count: 4
  slug: rendertoken-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.2
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
screenshot: https://apis.io/screenshots/rendertoken-com/rendertoken-com-2026-11-03T142140.png
security:
- kind: domain-security
  name: Rendertoken Com Domain Security
  slug: rendertoken-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rendertoken-com
tags:
- Company
- Decentralized
- GPU
- Compute
- Platform
website: https://rendertoken.com
---
