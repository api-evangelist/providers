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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tapastic-com/hosts/tapastic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tapastic-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/tapastic-com/security/tapastic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tapastic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tapastic.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://tapastic.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Tapastic is a digital publishing platform that enables creators to share webcomics, graphic novels, and illustrated stories with a global audience. The service provides tools for uploading, hosting, and monetizing content, offering both free and premium distribution options. Tapastic supports mobile and web readers, integrates social sharing features, and offers analytics for creators to track engagement. Backed by 500-global, the company focuses on empowering independent artists and storytellers to reach readers worldwide through an accessible, ad-supported ecosystem.
layout: provider
modified: '2026-10-25'
name: Tapastic
nav: Providers
network: true
overview: Tapastic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tapastic Com Domain Security
  slug: tapastic-com-domain-security
  summary_line: no transport/DNS hardening detected
slug: tapastic-com
tags:
- Company
website: https://tapastic.com
---
