---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  href: https://artifacts.apis.io/appfactor/plans/appfactor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appfactor-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/appfactor/hosts/appfactor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appfactor-hosts.yml
- group: other
  href: https://artifacts.apis.io/appfactor/vendors/appfactor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appfactor-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appfactor.io/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appfactor.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.appfactor.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appfactor.io/
- group: auth
  href: https://artifacts.apis.io/appfactor/security/appfactor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appfactor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appfactor.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.appfactor.io
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: AppFactor provides an agentic platform that discovers, assesses, modernizes, builds, deploys, and maintains enterprise software systems. The platform is self‑hosted and runs within a customer’s network, supporting regulated industries such as financial services, healthcare, government, retail, and manufacturing. It uses AI agents to automate SDLC steps while engineers retain governance through approval gates.
image: https://cdn.prod.website-files.com/67dac14729b1734516151fa9/67ec2f20d2486a56be065aa0_OG%207.jpg
layout: provider
modified: '2026-10-21'
name: AppFactor
nav: Providers
network: true
overview: 'AppFactor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Software, Legacy Modernization, AI Agents, Self-Hosted, and Regulated Industries.


  AppFactor''s developer surface includes pricing, engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Appfactor Plans Pricing
  plan_count: 4
  slug: appfactor-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 42.1
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
  previous_composite: 16.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appfactor/appfactor-2026-11-03T121025.png
security:
- kind: domain-security
  name: Appfactor Domain Security
  slug: appfactor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appfactor
tags:
- Enterprise Software
- Legacy Modernization
- AI Agents
- Self-Hosted
- Regulated Industries
- Software Maintenance
website: https://www.appfactor.io
---
