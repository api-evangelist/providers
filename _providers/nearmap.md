---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://api.nearmap.com
  baseurl_source: declared
  description: The Coverage API from Nearmap — 6 operation(s) for coverage.
  name: Nearmap Coverage API
  slug: nearmap-coverage-api
- baseURL: https://api.nearmap.com
  baseurl_source: declared
  description: The Tiles API from Nearmap — 2 operation(s) for tiles.
  name: Nearmap Tiles API
  slug: nearmap-tiles-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/rules/nearmap-rules.yml
  title: ''
  type: Spectral
  url: rules/nearmap-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/json-ld/nearmap-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nearmap-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/vocabulary/nearmap-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nearmap-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/data-model/nearmap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nearmap-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/authentication/nearmap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nearmap-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/conformance/nearmap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nearmap-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/llms/nearmap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nearmap-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/well-known/nearmap-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nearmap-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/well-known/nearmap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nearmap-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/hosts/nearmap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nearmap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/vendors/nearmap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nearmap-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/packages/nearmap-packages.yml
  title: ''
  type: SDKs
  url: packages/nearmap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/packages/nearmap-packages.yml
  title: ''
  type: Packages
  url: packages/nearmap-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.nearmap.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nearmap.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nearmap.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.nearmap.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.nearmap.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nearmap.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nearmap.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nearmap
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nearmap/refs/heads/main/security/nearmap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nearmap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nearmap.com/
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides API reference but no OpenAPI/Swagger spec was found.
  evidence:
  - status: 404
    url: https://developer.nearmap.com/openapi.json
  - status: 404
    url: https://api.nearmap.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Nearmap provides high‑resolution aerial imagery and property intelligence platforms, delivering up‑to‑date geospatial data, AI‑driven analytics, and APIs for developers to integrate mapping, analytics, and workflow applications across insurance, architecture, government, and other industries. Their services cover 97% of the U.S. population and 95% of U.S. buildings, with frequent updates and a suite of tools for property decision‑making.
image: https://a-us.storyblok.com/f/1018982/2400x1260/3348039c64/nearmap-property-intelligence.png
json_schemas:
- name: GetCoverageV2CoordZXYResponse
  property_count: 4
  slug: nearmap-get-coverage-v2-coord-zxyresponse
- name: GetCoverageV2PointCoordResponse
  property_count: 4
  slug: nearmap-get-coverage-v2-point-coord-response
- name: GetCoverageV2PolyPolygonResponse
  property_count: 4
  slug: nearmap-get-coverage-v2-poly-polygon-response
- name: GetCoverageV2V2IdBoundariesFileformatResponse
  property_count: 2
  slug: nearmap-get-coverage-v2-v2-id-boundaries-fileformat-response
- name: PostCoverageV2AoiRequest
  property_count: 1
  slug: nearmap-post-coverage-v2-aoi-request
- name: PostCoverageV2AoiResponse
  property_count: 4
  slug: nearmap-post-coverage-v2-aoi-response
jsonld:
- class_count: 7
  name: Nearmap Context
  property_count: 7
  slug: nearmap-context
layout: provider
modified: '2026-10-13'
name: Nearmap
nav: Providers
network: true
overview: 'Nearmap is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Coverage API and Tiles API. Tagged areas include Company, AerialImagery, Geospatial, and PropertyIntelligence.


  The Nearmap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nearmap''s developer surface includes authentication, support, engineering blog, API reference, documentation, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Nearmap API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: nearmap-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Nearmap Authentication
  slug: nearmap-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nearmap Domain Security
  slug: nearmap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nearmap
tags:
- Company
- AerialImagery
- Geospatial
- PropertyIntelligence
website: https://www.nearmap.com/
---
