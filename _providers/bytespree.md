---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bytespree/hosts/bytespree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bytespree-hosts.yml
- group: other
  href: https://artifacts.apis.io/bytespree/vendors/bytespree-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bytespree-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bytespree.com/
- group: auth
  href: https://artifacts.apis.io/bytespree/security/bytespree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bytespree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bytespree.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bytespree.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bytespree.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://bytespree.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://bytespree.com/pricing/
- group: company
  title: ''
  type: About
  url: https://bytespree.com/about/
coverage:
  checked: '2026-10-27'
  detail: Documentation pages return HTML shells and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 301
    url: https://bytespree.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Bytespree provides a nonprofit data platform that aggregates, cleans, and visualizes data for charitable organizations. It offers APIs to access donor information, fundraising metrics, program impact statistics, and financial reports, enabling nonprofits to integrate data into their own systems and dashboards. The platform emphasizes data transparency, security, and ease of integration for developers building tools for the nonprofit sector.
layout: provider
modified: '2026-10-27'
name: Bytespree
nav: Providers
network: true
overview: 'Bytespree is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nonprofit, DataPlatform, API, and OpenSource.


  Bytespree''s developer surface includes documentation, API reference, getting-started guide, pricing, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 15.8
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
  name: Bytespree Domain Security
  slug: bytespree-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bytespree
tags:
- Company
- Nonprofit
- DataPlatform
- API
- OpenSource
website: https://bytespree.com/
---
