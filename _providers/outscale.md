---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Outscale Agentic Access
  operation_count: 28
  slug: outscale-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.{region}.outscale.com/api/v1
  baseurl_source: declared
  description: The Clusters API from 3DS OUTSCALE — 8 operation(s) for clusters.
  name: 3DS OUTSCALE Clusters API
  slug: outscale-clusters-api
- baseURL: https://api.{region}.outscale.com/api/v1
  baseurl_source: declared
  description: The MyIp API from 3DS OUTSCALE — 1 operation(s) for myip.
  name: 3DS OUTSCALE My Ip API
  slug: outscale-myip-api
- baseURL: https://api.{region}.outscale.com/api/v1
  baseurl_source: declared
  description: The Projects API from 3DS OUTSCALE — 6 operation(s) for projects.
  name: 3DS OUTSCALE Projects API
  slug: outscale-projects-api
- baseURL: https://api.{region}.outscale.com/api/v1
  baseurl_source: declared
  description: The Quotas API from 3DS OUTSCALE — 1 operation(s) for quotas.
  name: 3DS OUTSCALE Quotas API
  slug: outscale-quotas-api
- baseURL: https://api.{region}.outscale.com/api/v1
  baseurl_source: declared
  description: The Templates API from 3DS OUTSCALE — 5 operation(s) for templates.
  name: 3DS OUTSCALE Templates API
  slug: outscale-templates-api
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/outscale/capabilities/outscale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/outscale-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/outscale/agentic-access/outscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/outscale-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/outscale/rules/outscale-rules.yml
  title: ''
  type: Spectral
  url: rules/outscale-rules.yml
- group: design
  href: https://artifacts.apis.io/outscale/json-ld/outscale-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/outscale-context.jsonld
- group: design
  href: https://artifacts.apis.io/outscale/vocabulary/outscale-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outscale-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/outscale/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/outscale/data-model/outscale-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outscale-data-model.yml
- group: design
  href: https://artifacts.apis.io/outscale/errors/outscale-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/outscale-problem-types.yml
- group: design
  href: https://artifacts.apis.io/outscale/conformance/outscale-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outscale-conformance.yml
- group: other
  href: https://artifacts.apis.io/outscale/overlays/outscale-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/outscale-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/outscale/hosts/outscale-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outscale-hosts.yml
- group: build
  href: https://artifacts.apis.io/outscale/packages/outscale-packages.yml
  title: ''
  type: SDKs
  url: packages/outscale-packages.yml
- group: build
  href: https://artifacts.apis.io/outscale/packages/outscale-packages.yml
  title: ''
  type: Packages
  url: packages/outscale-packages.yml
- group: auth
  href: https://artifacts.apis.io/outscale/authentication/outscale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outscale-authentication.yml
- group: auth
  href: https://artifacts.apis.io/outscale/security/outscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outscale.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.outscale.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.outscale.com/api.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outscale
created: '2026-10-28'
description: 3DS OUTSCALE, a subsidiary of Dassault Systèmes, provides a public cloud computing platform offering IaaS services such as virtual servers, storage, networking, and compatible APIs with AWS. The company focuses on European data sovereignty and enterprise-grade security, delivering scalable infrastructure for businesses worldwide.
image: https://docs.outscale.com/_/img/logo.svg
json_schemas:
- name: ClusterInput
  property_count: 19
  slug: outscale-cluster-input
- name: Cluster Response List
  property_count: 3
  slug: outscale-cluster-response-list
- name: ClusterUpdate
  property_count: 11
  slug: outscale-cluster-update
- name: ProjectInput
  property_count: 7
  slug: outscale-project-input
- name: ProjectResponseList
  property_count: 3
  slug: outscale-project-response-list
- name: PublicIpsResponse
  property_count: 2
  slug: outscale-public-ips-response
jsonld:
- class_count: 70
  name: Outscale Context
  property_count: 132
  slug: outscale-context
layout: provider
modified: '2026-10-28'
name: 3DS OUTSCALE
nav: Providers
network: true
overview: '3DS OUTSCALE publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clusters API, My Ip API, Projects API, and 2 more. Tagged areas include Cloud, IaaS, Compute, Storage, and Networking.


  The 3DS OUTSCALE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  3DS OUTSCALE''s developer surface includes authentication, documentation, API reference, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 3DS OUTSCALE API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: outscale-rules
scopes:
- name: Outscale Scopes
  scope_count: 0
  slug: outscale-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Outscale Authentication
  slug: outscale-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Outscale Domain Security
  slug: outscale-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 2
skills:
- name: create-cluster
  slug: outscale-create-cluster
- name: create-project
  slug: outscale-create-project
slug: outscale
tags:
- Cloud
- IaaS
- Compute
- Storage
- Networking
website: https://outscale.com/
---
