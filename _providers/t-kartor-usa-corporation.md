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
- description: Geospatial API providing mapping and location intelligence services.
  name: T-Kartor API
  slug: t-kartor-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/t-kartor-usa-corporation/llms/t-kartor-usa-corporation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/t-kartor-usa-corporation-llms.txt
- group: other
  href: https://artifacts.apis.io/t-kartor-usa-corporation/hosts/t-kartor-usa-corporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/t-kartor-usa-corporation-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.t-kartor.com/news/introducing-iris-2-10
- group: company
  title: ''
  type: Blog
  url: https://www.t-kartor.com/blog/modernizing-geospatial-with-ai-and-ml
- group: auth
  href: https://artifacts.apis.io/t-kartor-usa-corporation/security/t-kartor-usa-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/t-kartor-usa-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.t-kartor.com
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec was found on the API host or docs host.
  evidence:
  - status: 404
    url: https://api.t-kartor.com/openapi.json
  - status: 404
    url: https://api.t-kartor.com/openapi.yaml
  - status: 404
    url: https://api.t-kartor.com/swagger.json
  - status: 404
    url: https://www.t-kartor.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: T-Kartor USA Corporation provides custom geospatial solutions, transforming complex spatial data into actionable insights for navigation, wayfinding, and analytics. With over 35 years of experience, the company offers products, services, and consulting to help organizations improve safety, security, and operational efficiency through advanced mapping and location intelligence technologies.
image: https://irp.cdn-website.com/39a33c4d/dms3rep/multi/opt/2024_image_duda-open-graph_tkartor-32fc0e76-1920w.png
layout: provider
modified: '2026-10-26'
name: T-Kartor USA Corporation
nav: Providers
network: true
overview: 'T-Kartor USA Corporation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Mapping, Wayfinding, and Analytics.


  T-Kartor USA Corporation''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 8
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: T Kartor Usa Corporation Domain Security
  slug: t-kartor-usa-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: t-kartor-usa-corporation
tags:
- Company
- Geospatial
- Mapping
- Wayfinding
- Analytics
website: https://www.t-kartor.com
---
