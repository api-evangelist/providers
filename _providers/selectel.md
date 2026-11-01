---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Selectel API as documented publicly: 38 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Selectel API
  slug: selectel-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/selectel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/selectel/rules/selectel-rules.yml
  title: ''
  type: Spectral
  url: rules/selectel-rules.yml
- group: design
  href: https://artifacts.apis.io/selectel/json-ld/selectel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/selectel-context.jsonld
- group: design
  href: https://artifacts.apis.io/selectel/vocabulary/selectel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/selectel-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/selectel/data-model/selectel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/selectel-data-model.yml
- group: design
  href: https://artifacts.apis.io/selectel/conventions/selectel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/selectel-conventions.yml
- group: auth
  href: https://artifacts.apis.io/selectel/authentication/selectel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/selectel-authentication.yml
- group: design
  href: https://artifacts.apis.io/selectel/conformance/selectel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/selectel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/selectel/llms/selectel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/selectel-llms.txt
- group: other
  href: https://artifacts.apis.io/selectel/hosts/selectel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/selectel-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://files.selectel.ru/docs/ru/terms-of-use-for-services.pdf
- group: operate
  title: ''
  type: Support
  url: https://selectel.ru/support
- group: auth
  title: ''
  type: Security
  url: https://selectel.ru/about/security/
- group: company
  title: ''
  type: Newsroom
  url: https://selectel.ru/solutions/media/
- group: company
  title: ''
  type: Blog
  url: https://selectel.ru/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.selectel.ru/
- group: auth
  href: https://artifacts.apis.io/selectel/security/selectel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/selectel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://selectel.ru/
created: '2026-10-28'
description: Selectel is a Russian cloud services provider offering a range of infrastructure solutions including virtual private servers, block storage, object storage, and managed Kubernetes. It serves developers and enterprises with a focus on performance, security, and flexible pricing, operating data centers across multiple regions. The company provides extensive documentation, APIs, and a developer portal to integrate cloud resources programmatically.
json_schemas:
- name: GetV1ProjectidBucketnameResponse
  property_count: 3
  slug: selectel-get-v1-projectid-bucketname-response
- name: GetV1ProjectidResponse
  property_count: 4
  slug: selectel-get-v1-projectid-response
- name: GetV1SslCertResponse
  property_count: 3
  slug: selectel-get-v1-ssl-cert-response
- name: GetV1SslCert1Response
  property_count: 3
  slug: selectel-get-v1-ssl-cert1-response
- name: PostIdentityV3AuthTokensRequest
  property_count: 1
  slug: selectel-post-identity-v3-auth-tokens-request
- name: PostV1ProjectidRequest
  property_count: 2
  slug: selectel-post-v1-projectid-request
jsonld:
- class_count: 8
  name: Selectel Context
  property_count: 11
  slug: selectel-context
layout: provider
modified: '2026-10-28'
name: Selectel
nav: Providers
network: true
overview: 'Selectel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, VPS, Storage, and Kubernetes.


  The Selectel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Selectel''s developer surface includes authentication, support, engineering blog, documentation, and 14 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Selectel API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: selectel-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 25.2
    developer_ergonomics: 35.0
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Selectel Authentication
  slug: selectel-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Selectel Domain Security
  slug: selectel-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: selectel
tags:
- Cloud
- Infrastructure
- VPS
- Storage
- Kubernetes
website: https://selectel.ru/
---
