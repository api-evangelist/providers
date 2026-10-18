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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Serverless functions API documented at OpenFaaS docs.
  name: OpenFaaS API
  slug: openfaas-api-2
- baseURL: https://github.com
  baseurl_source: declared
  description: The Alexellis API from OpenFaaS — 1 operation(s) for alexellis.
  name: OpenFaaS Alexellis API
  slug: openfaas-alexellis-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Async Function API from OpenFaaS — 2 operation(s) for async function.
  name: OpenFaaS Async Function API
  slug: openfaas-async-function-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Auth API from OpenFaaS — 1 operation(s) for auth.
  name: OpenFaaS Auth API
  slug: openfaas-auth-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Function API from OpenFaaS — 1 operation(s) for function.
  name: OpenFaaS Function API
  slug: openfaas-function-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The OpenFaaS API API from OpenFaaS — 1 operation(s) for openfaas api.
  name: OpenFaaS OpenFaaS API
  slug: openfaas-openfaas-api-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The System API from OpenFaaS — 2 operation(s) for system.
  name: OpenFaaS System API
  slug: openfaas-system-api
artifact_total: 18
common:
- group: operate
  title: ''
  type: Support
  url: https://www.openfaas.com/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openfaas.com/contributing/get-started/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/plans/openfaas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openfaas-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/rules/openfaas-rules.yml
  title: ''
  type: Spectral
  url: rules/openfaas-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/json-ld/openfaas-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openfaas-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/vocabulary/openfaas-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openfaas-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/data-model/openfaas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openfaas-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/authentication/openfaas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openfaas-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/conformance/openfaas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openfaas-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/hosts/openfaas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openfaas-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/vendors/openfaas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openfaas-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.openfaas.com/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openfaas
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openfaas.com/reference/yaml/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openfaas/refs/heads/main/security/openfaas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openfaas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openfaas.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openfaas.com
- group: company
  title: ''
  type: Blog
  url: https://www.openfaas.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openfaas.com/pricing
coverage:
  checked: '2026-10-14'
  detail: OpenFaaS API docs are HTML only; attempts to fetch OpenAPI at https://api.openfaas.com/openapi.json returned 401 unauthorized.
  evidence:
  - status: 401
    url: https://api.openfaas.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: OpenFaaS provides an open-source serverless functions framework that enables developers to deploy functions on any cloud, Kubernetes, or on‑premises environment. It emphasizes portability, simplicity, and production‑grade features, offering a rich ecosystem of templates, a web UI, and extensive language support. The platform is used by enterprises and hobbyists alike to build scalable, event‑driven applications with minimal operational overhead.
image: https://www.openfaas.com/images/preview_image.png
json_schemas:
- name: GetFunctionFunctionidResponse
  property_count: 10
  slug: openfaas-get-function-functionid-response
- name: GetSystemFunctionEnvResponse
  property_count: 10
  slug: openfaas-get-system-function-env-response
- name: PostRequest
  property_count: 2
  slug: openfaas-post-request
- name: PutRequest
  property_count: 2
  slug: openfaas-put-request
- name: PutSystemFunctionsRequest
  property_count: 5
  slug: openfaas-put-system-functions-request
- name: PutSystemFunctionsResponse
  property_count: 10
  slug: openfaas-put-system-functions-response
jsonld:
- class_count: 6
  name: Openfaas Context
  property_count: 11
  slug: openfaas-context
layout: provider
modified: '2026-10-14'
name: OpenFaaS
nav: Providers
network: true
overview: 'OpenFaaS is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Alexellis API, Async Function API, Auth API, and 4 more. Tagged areas include Company, Serverless, Open Source, Functions, and Kubernetes.


  The OpenFaaS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenFaaS''s developer surface includes support, getting-started guide, authentication, API reference, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Openfaas Plans Pricing
  plan_count: 3
  slug: openfaas-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: OpenFaaS API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: openfaas-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
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
- kind: authentication
  name: Openfaas Authentication
  slug: openfaas-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Openfaas Domain Security
  slug: openfaas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openfaas
tags:
- Company
- Serverless
- Open Source
- Functions
- Kubernetes
website: https://www.openfaas.com
---
