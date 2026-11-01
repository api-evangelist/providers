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
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: APIs to configure multiple envoy proxies
  name: Enroute API
  slug: enroute-api
- description: 'Saaras core API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Saaras core API
  slug: core-api
- description: 'Saaras prologue API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Saaras prologue API
  slug: prologue-api
- description: 'Saaras Techincal Reference API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Saaras Techincal Reference API
  slug: technical-reference-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/getenroute/rules/getenroute-rules.yml
  title: ''
  type: Spectral
  url: rules/getenroute-rules.yml
- group: design
  href: https://artifacts.apis.io/getenroute/json-ld/getenroute-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getenroute-context.jsonld
- group: design
  href: https://artifacts.apis.io/getenroute/vocabulary/getenroute-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getenroute-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getenroute/data-model/getenroute-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getenroute-data-model.yml
- group: design
  href: https://artifacts.apis.io/getenroute/conformance/getenroute-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getenroute-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getenroute/llms/getenroute-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getenroute-llms.txt
- group: other
  href: https://artifacts.apis.io/getenroute/hosts/getenroute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getenroute-hosts.yml
- group: other
  href: https://artifacts.apis.io/getenroute/vendors/getenroute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getenroute-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getenroute/security/getenroute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getenroute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saaras.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getenroute.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getenroute.io/
- group: company
  title: ''
  type: Blog
  url: https://www.saaras.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saarasio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saaras.io/privacy-policy
created: '2026-10-20'
description: Saaras provides cloud‑native API gateway and service‑mesh solutions built on Kubernetes. Their EnRoute Gateway offers high‑performance traffic management, security, observability, and dynamic routing for modern cloud applications. Saaras also delivers Istio‑based subscriptions, FIPS‑validated distributions, and consulting services to help enterprises adopt API management at scale.
image: https://cdn.prod.website-files.com/64b201b4cb1acb69f6045d61/68b13ed02bbaac65da5244fa_c9ba6b1c2e383134de237d1cfa16205d_opengraph.jpg
json_schemas:
- name: GetGetResponse
  property_count: 1
  slug: getenroute-get-get-response
- name: PostTokenResponse
  property_count: 5
  slug: getenroute-post-token-response
- name: PostV1SecretDataEnroutedemoComRequest
  property_count: 1
  slug: getenroute-post-v1-secret-data-enroutedemo-com-request
jsonld:
- class_count: 3
  name: Getenroute Context
  property_count: 7
  slug: getenroute-context
layout: provider
modified: '2026-10-20'
name: Saaras
nav: Providers
network: true
overview: 'Saaras is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including core API, prologue API, Techincal Reference API, and 1 more. Tagged areas include Company, API Gateway, Kubernetes, Service Mesh, and Cloud-Native.


  The Saaras catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Saaras'' developer surface includes documentation, API reference, engineering blog, and 12 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Saaras API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: getenroute-rules
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.0
    catalog_earned_first_party: 0.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 19.0
    developer_ergonomics: 19.0
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getenroute Domain Security
  slug: getenroute-domain-security
  summary_line: TLSv1.3 · HSTS
slug: getenroute
tags:
- Company
- API Gateway
- Kubernetes
- Service Mesh
- Cloud-Native
website: https://www.saaras.io/
---
