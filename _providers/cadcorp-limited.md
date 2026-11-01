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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GIS developer tools and APIs provided by Cadcorp under NEC Software Solutions.
  name: Cadcorp GIS Developer Tools
  slug: cadcorp-gis-developer-tools
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cadcorp-limited/llms/cadcorp-limited-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cadcorp-limited-llms.txt
- group: agent
  href: https://artifacts.apis.io/cadcorp-limited/well-known/cadcorp-limited-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cadcorp-limited-well-known.yml
- group: other
  href: https://artifacts.apis.io/cadcorp-limited/hosts/cadcorp-limited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cadcorp-limited-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.necsws.com/terms-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://www.necsws.com/news/central-government/mapestry-launched/
- group: other
  title: ''
  type: Leadership
  url: https://www.necsws.com/about-nec-software-solutions/leadership/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cadcorp.com/
- group: auth
  href: https://artifacts.apis.io/cadcorp-limited/security/cadcorp-limited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadcorp-limited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.necsws.com/sectors/geospatial-solutions/
coverage:
  checked: '2026-10-30'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.necsws.com/sectors/geospatial-solutions/applications/gis-developer-tools/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Cadcorp Limited is a UK‑based provider of geographic information system (GIS) software and services, offering mapping, spatial analysis, and data integration solutions for government, utilities, and commercial organisations. Historically an independent firm, Cadcorp’s technology and brand have been integrated into NEC’s geospatial portfolio, reflecting its strong expertise in location‑based applications and enterprise‑grade GIS platforms.
image: https://www.necsws.com/wp-content/uploads/2026/08/Geo_Web-Banner-Image_Blue-scaled.png
layout: provider
modified: '2026-10-28'
name: Cadcorp Limited
nav: Providers
network: true
overview: 'Cadcorp Limited is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, Mapping, Spatial-Analysis, and Enterprise-Software.


  Cadcorp Limited''s developer surface includes documentation and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cadcorp Limited Domain Security
  slug: cadcorp-limited-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cadcorp-limited
tags:
- Company
- GIS
- Mapping
- Spatial-Analysis
- Enterprise-Software
website: https://www.necsws.com/sectors/geospatial-solutions/
---
