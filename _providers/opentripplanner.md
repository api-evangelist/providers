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
api_count: 1
apis:
- description: The OpenTripPlanner API provides routing and trip planning capabilities. Documentation is available at the linked page. No machine‑readable OpenAPI spec was found.
  name: OpenTripPlanner API
  slug: opentripplanner-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/opentripplanner/hosts/opentripplanner-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opentripplanner-hosts.yml
- group: other
  href: https://artifacts.apis.io/opentripplanner/vendors/opentripplanner-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opentripplanner-vendors.yml
- group: auth
  href: https://artifacts.apis.io/opentripplanner/security/opentripplanner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opentripplanner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opentripplanner.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opentripplanner.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentripplanner
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML without a discoverable OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.opentripplanner.org/en/latest/apis/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OpenTripPlanner is an open-source multimodal trip planning system that provides routing for public transit, walking, biking, and driving. It offers a flexible API for developers to integrate journey planning into applications, supporting real-time data, custom fare calculations, and extensive geographic coverage. The platform is community-driven and used worldwide for transit agencies and mobility services.
layout: provider
modified: '2026-10-28'
name: OpenTripPlanner
nav: Providers
network: true
overview: 'OpenTripPlanner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OpenSource, Transportation, Routing, Multimodal, and Community.


  OpenTripPlanner''s developer surface includes documentation and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 5.3
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
  name: Opentripplanner Domain Security
  slug: opentripplanner-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: opentripplanner
tags:
- OpenSource
- Transportation
- Routing
- Multimodal
- Community
website: https://www.opentripplanner.org/
---
