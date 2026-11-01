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
  href: https://artifacts.apis.io/trymason-com/vendors/trymason-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trymason-com-vendors.yml
- group: other
  href: https://artifacts.apis.io/trymason-com/hosts/trymason-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trymason-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://genomedika.org/register
- group: company
  title: ''
  type: Website
  url: https://www.trymason.com
- group: auth
  href: https://artifacts.apis.io/trymason-com/security/trymason-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trymason-com-domain-security.yml
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 0
    url: https://api.trymason.com/openapi.json
  - status: 0
    url: https://api.genomedika.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Mason is a technology company focused on providing API-driven solutions for modern businesses. It offers a platform that enables developers to integrate services, automate workflows, and access data through well-documented endpoints. The company aims to simplify digital transformation and accelerate product development for its clients.
layout: provider
modified: '2026-10-28'
name: Mason
nav: Providers
network: true
overview: 'Mason is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Integration, Automation, and Platform.


  Mason''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Trymason Com Domain Security
  slug: trymason-com-domain-security
  summary_line: TLSv1.3
slug: trymason-com
tags:
- Company
- API
- Integration
- Automation
- Platform
website: https://www.trymason.com
---
