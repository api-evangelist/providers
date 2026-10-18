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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://gateway-hostname
  baseurl_source: declared
  description: The Almaws API from Ex Libris — 12 operation(s) for almaws.
  name: Ex Libris Almaws API
  slug: ex-libris-almaws-api
- baseURL: https://gateway-hostname
  baseurl_source: declared
  description: The Rapido API from Ex Libris — 9 operation(s) for rapido.
  name: Ex Libris Rapido API
  slug: ex-libris-rapido-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/rules/ex-libris-rules.yml
  title: ''
  type: Spectral
  url: rules/ex-libris-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/json-ld/ex-libris-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ex-libris-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/vocabulary/ex-libris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ex-libris-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/data-model/ex-libris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ex-libris-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/conformance/ex-libris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ex-libris-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/well-known/ex-libris-knowledge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ex-libris-knowledge-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/well-known/ex-libris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ex-libris-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/hosts/ex-libris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ex-libris-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/vendors/ex-libris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ex-libris-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/packages/ex-libris-packages.yml
  title: ''
  type: SDKs
  url: packages/ex-libris-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/packages/ex-libris-packages.yml
  title: ''
  type: Packages
  url: packages/ex-libris-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.exlibrisgroup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.exlibrisgroup.com/about/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exlibrisgroup.com/system_status
- group: auth
  title: ''
  type: Security
  url: https://knowledge.exlibrisgroup.com/Cross-Product/Security/GDPR
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ExLibrisGroup
- group: company
  title: ''
  type: Blog
  url: https://exlibrisgroup.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.exlibrisgroup.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ex-libris/refs/heads/main/security/ex-libris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ex-libris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.exlibrisgroup.com
coverage:
  checked: '2026-10-13'
  detail: The developer portal provides HTML documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://developers.exlibrisgroup.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Ex Libris provides library software and services for academic, research, and public libraries worldwide. Their portfolio includes Alma, Primo, Leganto, and other platforms that enable resource management, discovery, and digital services. The company focuses on integrated solutions for metadata, analytics, and collaborative networks, serving institutions of all sizes with cloud‑based and on‑premise options.
image: https://exlibrisgroup.com/wp-content/uploads/ExLibris-logo-endorsed-color.png
json_schemas:
- name: GetAlmawsVersionResourceNameParametersResponse
  property_count: 3
  slug: ex-libris-get-almaws-version-resource-name-parameters-response
jsonld:
- class_count: 1
  name: Ex Libris Context
  property_count: 3
  slug: ex-libris-context
layout: provider
modified: '2026-10-13'
name: Ex Libris
nav: Providers
network: true
overview: 'Ex Libris is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Almaws API and Rapido API. Tagged areas include Library, Software, Academic, Cloud, and Solutions.


  The Ex Libris catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ex Libris'' developer surface includes engineering blog, documentation, and 18 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Ex Libris API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ex-libris-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 22.0
    contract_quality: 20.4
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Ex Libris Domain Security
  slug: ex-libris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ex-libris
tags:
- Library
- Software
- Academic
- Cloud
- Solutions
website: https://www.exlibrisgroup.com
---
