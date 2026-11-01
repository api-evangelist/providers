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
  href: https://artifacts.apis.io/telescope/hosts/telescope-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telescope-hosts.yml
- group: auth
  href: https://artifacts.apis.io/telescope/security/telescope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telescope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gotelescope.ai
coverage:
  checked: '2026-10-29'
  detail: Provider's API specification endpoints return no OpenAPI/AsyncAPI/GraphQL contracts and documentation host is unreachable.
  evidence:
  - status: 0
    url: https://api.gotelescope.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Telescope is a technology company focused on providing advanced data analytics and platform services for businesses. It offers a suite of APIs that enable developers to integrate telemetry, monitoring, and insight generation into their applications. Backed by prominent venture capital firms, Telescope aims to simplify complex data pipelines and deliver actionable intelligence through scalable cloud solutions. The company emphasizes security, reliability, and ease of integration across multiple industries.
layout: provider
modified: '2026-10-29'
name: Telescope
nav: Providers
network: true
overview: Telescope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telescope, API, Data, and Analytics.
random_paper: 4
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  name: Telescope Domain Security
  slug: telescope-domain-security
  summary_line: DMARC
slug: telescope
tags:
- Company
- Telescope
- API
- Data
- Analytics
- Platform
website: https://www.gotelescope.ai
---
