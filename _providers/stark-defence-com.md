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
  href: https://artifacts.apis.io/stark-defence-com/hosts/stark-defence-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stark-defence-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stark-defence-com/vendors/stark-defence-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stark-defence-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stark-defence.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://stark-defence.com/en/news
- group: auth
  href: https://artifacts.apis.io/stark-defence-com/security/stark-defence-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stark-defence-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stark-defence.com/en
coverage:
  checked: '2026-10-24'
  detail: The provider's website is a JavaScript‑rendered Next.js app with no machine‑readable API spec discovered.
  evidence:
  - status: 404
    url: https://stark-defence.com/openapi.json
  - status: 404
    url: https://stark-defence.com/api/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: STARK is a defence technology company specializing in autonomous unmanned systems and advanced weaponry integration. It provides cutting‑edge solutions for rapid deployment and precise targeting, serving both government and commercial sectors worldwide.
image: https://cdn.sanity.io/images/kk5p0dy5/production/cedd97ac2d469340e7a0acd497624cd84cabf5a4-3026x2018.png?rect=0,219,3026,1581&w=1200&h=627&fit=crop
layout: provider
modified: '2026-10-23'
name: STARK
nav: Providers
network: true
overview: STARK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defence, Autonomous, Unmanned Systems, Weaponry Integration, and Government.
random_paper: 16
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stark Defence Com Domain Security
  slug: stark-defence-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stark-defence-com
tags:
- Defence
- Autonomous
- Unmanned Systems
- Weaponry Integration
- Government
- Commercial
website: https://stark-defence.com/en
---
