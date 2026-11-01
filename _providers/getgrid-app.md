---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/getgrid-app/hosts/getgrid-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getgrid-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getgrid.app/terms
- group: operate
  title: ''
  type: Support
  url: https://getgrid.app/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getgrid.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://getgrid.app/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.getgrid.app
- group: auth
  href: https://artifacts.apis.io/getgrid-app/security/getgrid-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getgrid-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getgrid.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://getgrid.app/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Grid provides a mobile app that offers users cash advances of up to $200 and a PayBoost feature that can increase a paycheck by up to $250. The service is aimed at individuals with a bank account or card who need quick access to funds and want to build their credit score. Users receive advances that are transferred to their bank, with limits that may grow based on account activity, direct deposits, repayment history, and other risk‑based factors.
layout: provider
modified: '2026-10-22'
name: Grid
nav: Providers
network: true
overview: 'Grid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cash Advance and PayBoost.


  Grid''s developer surface includes support, pricing, engineering blog, and 5 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getgrid App Domain Security
  slug: getgrid-app-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: getgrid-app
tags:
- Cash Advance
- PayBoost
website: https://getgrid.app/
---
