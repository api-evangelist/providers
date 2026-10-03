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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bellaroseapparel/refs/heads/main/hosts/bellaroseapparel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bellaroseapparel-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bellaroseapparel/refs/heads/main/vendors/bellaroseapparel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bellaroseapparel-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bellaroseapparel/refs/heads/main/security/bellaroseapparel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bellaroseapparel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bellaroseapparel.com
- group: other
  title: ''
  type: Image
  url: https://bellaroseapparel.com/wp-content/uploads/2022/06/logo9.png
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bellaroseapparel
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bella Rose Apparel is a professional apparel manufacturer based in India, operating since 2007 with facilities in Bangladesh, China, UAE, USA and Hong Kong. The company offers global sourcing, quality control, and a range of knitted and woven wear products, serving international markets through its group of companies and sales partners.
layout: provider
modified: '2026-09-27'
name: Bellaroseapparel
nav: Providers
network: true
overview: Bellaroseapparel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Manufacturing, India, Global Sourcing, and Textile.
random_paper: 0
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bellaroseapparel Domain Security
  slug: bellaroseapparel-domain-security
  summary_line: TLSv1.3
slug: bellaroseapparel
tags:
- Apparel
- Manufacturing
- India
- Global Sourcing
- Textile
website: https://bellaroseapparel.com
---
