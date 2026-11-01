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
- description: Enterprise platform solution for earth observation data providers, includes OGC web services.
  name: Stratos Platform API
  slug: stratos-platform-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cubewerx/hosts/cubewerx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cubewerx-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cubewerx.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.cubewerx.com/blog/
- group: auth
  href: https://artifacts.apis.io/cubewerx/security/cubewerx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubewerx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.cubewerx.com/
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found on CubeWerx domains.
  evidence:
  - status: 404
    url: https://www.cubewerx.com/openapi.json
  - status: 404
    url: https://www.cubewerx.com/openapi.yaml
  - status: 404
    url: https://www.cubewerx.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: CubeWerx provides a geospatial platform and related services that enable organizations to manage, secure, and publish geospatial data as web services. It offers cloud‑hosted and on‑premise solutions, managed services, and self‑serve tools for commercial data providers, government agencies, and defense and intelligence customers. The company also supplies analytics, access control, and consulting to support spatial data infrastructures.
image: https://d8dr4032v6tl6.cloudfront.net/wp-content/uploads/2019/11/CUBEWERX_Logo-Colour_Tagline.png
layout: provider
modified: '2026-10-23'
name: CubeWerx
nav: Providers
network: true
overview: 'CubeWerx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Data Management, Web Mapping, Access Control, and Analytics.


  CubeWerx''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
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
  name: Cubewerx Domain Security
  slug: cubewerx-domain-security
  summary_line: TLSv1.2
slug: cubewerx
tags:
- Geospatial
- Data Management
- Web Mapping
- Access Control
- Analytics
- Managed Services
- Cloud
- On-Premise
website: http://www.cubewerx.com/
---
