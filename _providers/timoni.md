---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Timoni Agentic Access
  operation_count: 3
  slug: timoni-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: OCI artifact operations for Timoni packages
  name: Timoni Artifacts API
  slug: timoni-artifacts-api
- description: Timoni module management and distribution
  name: Timoni Modules API
  slug: timoni-modules-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Timoni Module Registry Artifacts API
  slug: open-timoni-artifacts-api
- collection_type: open
  name: Timoni Module Registry Artifacts Modules API
  slug: open-timoni-modules-api
- collection_type: open
  name: Timoni Module Registry API
  slug: open-timoni
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/stefanprodan/timoni/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/stefanprodan/timoni/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/stefanprodan/timoni/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/stefanprodan/timoni/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/stefanprodan/timoni/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/stefanprodan/timoni/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/timoni-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timoni-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timoni-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://timoni.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://timoni.sh/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stefanprodan/timoni
- group: start
  title: ''
  type: GettingStarted
  url: https://timoni.sh/quickstart/
- group: other
  title: ''
  type: Concepts
  url: https://timoni.sh/concepts/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/openapi/timoni-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-schema/timoni-module-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-ld/timoni-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/vocabulary/timoni-vocabulary.yml
created: '2026-03-26'
description: Timoni is a package manager for Kubernetes powered by CUE that provides a type-safe alternative to Helm charts. It enables software vendors to define complex application deployments packaged as Modules using CUE definitions, distributed as OCI artifacts in container registries with semantic versioning and cryptographic signing.
examples:
- key_count: 2
  name: Timoni List Module Tags Example
  slug: timoni-list-module-tags-example
finops:
- name: Timoni Finops
  service_category: API
  slug: timoni-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/timoni.png
json_schemas:
- name: Timoni Module
  property_count: 10
  slug: timoni-module
json_structures:
- name: Timoni Module Structure
  property_count: 0
  slug: timoni-module-structure
jsonld:
- class_count: 33
  name: Timoni Context
  property_count: 1
  slug: timoni-context
layout: provider
modified: '2026-05-19'
name: Timoni
nav: Providers
network: true
overview: 'Timoni publishes 2 APIs on the [APIs.io](https://apis.io/) network: Artifacts API and Modules API. Tagged areas include Containers, Kubernetes, Package Manager, and CUE.


  The Timoni catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Timoni''s developer surface includes authentication, documentation, getting-started guide, and 15 more developer resources.'
plans:
- name: Timoni Plans Pricing
  plan_count: 3
  slug: timoni-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Timoni Rate Limits
  slug: timoni-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Timoni API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: timoni-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 63.3
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/screenshots/timoni-2026-06-20T195403.png
security:
- kind: authentication
  name: Timoni Authentication
  slug: timoni-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Timoni Domain Security
  slug: timoni-domain-security
  summary_line: TLSv1.3
slug: timoni
tags:
- Containers
- Kubernetes
- Package Manager
- CUE
website: https://timoni.sh/
---
