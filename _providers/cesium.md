---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Cesium ion REST API for tiling and streaming capabilities
  name: Cesium ion API
  slug: cesium-ion-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: 'Archives allow you to make downloadable versions of your assets for offline use or hosting outside of Cesium ion. With archives you can: * Create a full copy of an asset as a zip file * Clip out a sub'
  name: Cesium Archives API
  slug: cesium-archives-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: The Asset Elements API provides a mechanism to query individual elements within an asset.
  name: Cesium Asset Elements API
  slug: cesium-asset-elements-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: Whether you have imagery, terrain, 3D buildings, point clouds, photogrammetry, or one of the many other types of data we support, ion creates what we refer to as an asset. There are seven types of ass
  name: Cesium Assets API
  slug: cesium-assets-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: Experimental API lets users test emerging capabilities and help shape future improvements. These endpoints are not intended for production use and may be removed without notice.
  name: Cesium Experimental API
  slug: cesium-experimental-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: Allows you to export the files for a particular asset to an Amazon S3 bucket of your choice. These files can then be hosted through a custom server or downloaded for local/offline use. The number of b
  name: Cesium Exports API
  slug: cesium-exports-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: Labels let you organize assets and stories with reusable metadata tags. The Labels API provides a mechanism to list, create, update, and delete account labels. Asset-label assignment is documented wit
  name: Cesium Labels API
  slug: cesium-labels-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: The Oauth API provides a mechanism to allow third-party applications to access a user's ion account data through the Oauth 2.0 authorization framework.
  name: Cesium OAuth API
  slug: cesium-oauth-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: The Tokens API provides a mechanism to create and manage access tokens. Access tokens are used to give applications access to your ion account, including access to stream your ion assets. Every accoun
  name: Cesium Tokens API
  slug: cesium-tokens-api
- baseURL: https://ion.cesium.com/
  baseurl_source: declared
  description: Routes related to the currently authenticated account.
  name: Cesium User API
  slug: cesium-user-api
artifact_total: 20
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/rules/cesium-rules.yml
  title: ''
  type: Spectral
  url: rules/cesium-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/json-ld/cesium-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cesium-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/vocabulary/cesium-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cesium-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/conformance/cesium-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cesium-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/plans/cesium-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cesium-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/data-model/cesium-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cesium-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/errors/cesium-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cesium-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/llms/cesium-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cesium-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/well-known/cesium-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesium-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/well-known/cesium-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cesium-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/hosts/cesium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cesium-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/vendors/cesium-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cesium-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/packages/cesium-packages.yml
  title: ''
  type: SDKs
  url: packages/cesium-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/packages/cesium-packages.yml
  title: ''
  type: Packages
  url: packages/cesium-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cesium.com/
- group: start
  title: ''
  type: SignUp
  url: https://cesium.com/ion/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://cesium.com/platform/cesium-ion/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://cesium.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://cesium.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CesiumGS
- group: company
  title: ''
  type: Blog
  url: https://cesium.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesium/refs/heads/main/security/cesium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cesium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cesium.com/
created: '2026-10-13'
description: Cesium provides an open platform for 3D geospatial applications, offering tools like CesiumJS, Cesium ion, and integrations for Unity, Unreal, and Omniverse. It serves developers, enterprises, and government agencies with streaming 3D Tiles, curated global content, and AI‑enabled workflows, enabling visualization, analysis, and design of complex spatial data.
image: https://images.prismic.io/cesium/d8282fb7-4939-4a71-a4e2-08005792e788_cesium-logo-globe.jpg?auto=compress,format&rect=0,9,1172,612&w=1200&h=627
json_schemas:
- name: Archive Metadata
  property_count: 7
  slug: cesium-archive-metadata2
- name: Asset Endpoint
  property_count: 4
  slug: cesium-asset-endpoint
- name: Asset Metadata
  property_count: 16
  slug: cesium-asset-metadata
- name: External Asset Endpoint
  property_count: 3
  slug: cesium-external-asset-endpoint
- name: Token Metadata
  property_count: 9
  slug: cesium-token-metadata-default-token
- name: Token Metadata
  property_count: 11
  slug: cesium-token-metadata
jsonld:
- class_count: 36
  name: Cesium Context
  property_count: 58
  slug: cesium-context
layout: provider
modified: '2026-10-13'
name: Cesium
nav: Providers
network: true
overview: 'Cesium publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Archives API, Asset Elements API, Assets API, and 7 more. Tagged areas include Company, Geospatial, 3D, Platform, and Open Source.


  The Cesium catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cesium''s developer surface includes signup flow, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Cesium Plans Pricing
  plan_count: 6
  slug: cesium-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Cesium API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: cesium-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 67.6
    developer_ergonomics: 9.5
    discoverability: 76.8
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Cesium Domain Security
  slug: cesium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cesium
tags:
- Company
- Geospatial
- 3D
- Platform
- Open Source
website: https://cesium.com/
---
