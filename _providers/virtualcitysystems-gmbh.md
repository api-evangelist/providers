---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/virtualcitysystems-gmbh/well-known/virtualcitysystems-gmbh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virtualcitysystems-gmbh-well-known.yml
- group: other
  href: https://artifacts.apis.io/virtualcitysystems-gmbh/hosts/virtualcitysystems-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/virtualcitysystems-gmbh-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://vc.systems/en/explore/news/
- group: docs
  title: ''
  type: Documentation
  url: https://help.vc.systems/
- group: auth
  href: https://artifacts.apis.io/virtualcitysystems-gmbh/security/virtualcitysystems-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virtualcitysystems-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vc.systems/en/
- group: company
  title: ''
  type: Blog
  url: https://vc.systems/en/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://vc.systems/en/case-studies/
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are static HTML without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://help.vc.systems/de/vc-suite/2026/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Virtual City Systems GmbH, founded in Chemnitz in 2005, provides digital 3D city models and urban simulation solutions. Their platform enables municipalities, planners, and developers to create, visualize, and analyze digital twins of urban environments, supporting use cases such as blast wave simulation, infrastructure planning, and public engagement. The company emphasizes open data, technical depth, and innovative urban planning tools, positioning itself as a leading provider in the digital twin space.
layout: provider
modified: '2026-10-26'
name: virtualcitySYSTEMS GmbH
nav: Providers
network: true
overview: 'virtualcitySYSTEMS GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DigitalTwin, UrbanPlanning, 3DModels, and Simulation.


  virtualcitySYSTEMS GmbH''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Virtualcitysystems Gmbh Domain Security
  slug: virtualcitysystems-gmbh-domain-security
  summary_line: TLSv1.2 · HSTS
slug: virtualcitysystems-gmbh
tags:
- Company
- DigitalTwin
- UrbanPlanning
- 3DModels
- Simulation
website: https://vc.systems/en/
---
