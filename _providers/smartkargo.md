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
  href: https://artifacts.apis.io/smartkargo/hosts/smartkargo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smartkargo-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartkargo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartkargo.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.smartkargo.com/blog
- group: auth
  href: https://artifacts.apis.io/smartkargo/security/smartkargo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smartkargo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smartkargo.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://smartkargo.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: SmartKargo provides a digital platform that enables airlines to monetize unused cargo capacity by connecting e‑commerce shippers with air carriers. Founded in 2006 at MIT, the company offers SaaS solutions for domestic and cross‑border e‑commerce, core cargo management, and AI‑driven applications, serving over 25 airlines worldwide and processing millions of small‑package shipments each year.
layout: provider
modified: '2026-10-28'
name: SmartKargo
nav: Providers
network: true
overview: 'SmartKargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Air Cargo, E-Commerce, and Software-as-a-Service.


  SmartKargo''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/smartkargo/smartkargo-2026-11-03T143345.png
security:
- kind: domain-security
  name: Smartkargo Domain Security
  slug: smartkargo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smartkargo
tags:
- Company
- Logistics
- Air Cargo
- E-Commerce
- Software-as-a-Service
website: https://smartkargo.com/
---
