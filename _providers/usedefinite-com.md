---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Definite provides APIs for its ontology platform, covering vault, ledger, decision streams, and other services.
  name: Definite API
  slug: definite-api
- description: 'Definite API as documented publicly: 59 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Definite API
  slug: usedefinite-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/usedefinite-com/rules/usedefinite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/usedefinite-com-rules.yml
- group: design
  href: https://artifacts.apis.io/usedefinite-com/json-ld/usedefinite-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usedefinite-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/usedefinite-com/vocabulary/usedefinite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usedefinite-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usedefinite-com/data-model/usedefinite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usedefinite-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/usedefinite-com/conventions/usedefinite-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/usedefinite-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/usedefinite-com/conventions/usedefinite-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usedefinite-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/usedefinite-com/authentication/usedefinite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usedefinite-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/usedefinite-com/conformance/usedefinite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usedefinite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usedefinite-com/llms/usedefinite-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usedefinite-com-llms.txt
- group: other
  href: https://artifacts.apis.io/usedefinite-com/hosts/usedefinite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usedefinite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/usedefinite-com/vendors/usedefinite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usedefinite-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usedefinite.com/security
- group: start
  title: ''
  type: Login
  url: https://app.usedefinite.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usedefinite.com/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UseDefinite
- group: auth
  href: https://artifacts.apis.io/usedefinite-com/security/usedefinite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usedefinite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usedefinite.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.usedefinite.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usedefinite.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usedefinite.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.usedefinite.com/contact
coverage:
  checked: '2026-10-29'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.usedefinite.com/api/vault
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Definite provides an ontology layer for finance, connecting disparate financial systems, mapping data and relationships to give finance teams a unified context for dashboards, reconciliation, planning, billing, tax, and analytics. Backed by Y Combinator, it enables teams to turn operational finance into strategic insight through integrated workflows and APIs.
image: https://www.usedefinite.com/opengraph-image
json_schemas:
- name: PostV1ProgramsProgramidRunsRequest
  property_count: 7
  slug: usedefinite-com-post-v1-programs-programid-runs-request
- name: PostV1ProgramsProgramidRunsResponse
  property_count: 1
  slug: usedefinite-com-post-v1-programs-programid-runs-response
jsonld:
- class_count: 2
  name: Usedefinite Com Context
  property_count: 8
  slug: usedefinite-com-context
layout: provider
modified: '2026-10-29'
name: Definite
nav: Providers
network: true
overview: 'Definite is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Ontology, Integration, and Software-as-a-Service.


  The Definite catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Definite''s developer surface includes authentication, getting-started guide, documentation, support, and 17 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Definite API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: usedefinite-com-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 25.0
    discoverability: 64.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/usedefinite-com/usedefinite-com-2026-11-03T145526.png
security:
- kind: authentication
  name: Usedefinite Com Authentication
  slug: usedefinite-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Usedefinite Com Domain Security
  slug: usedefinite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usedefinite-com
tags:
- Company
- Finance
- Ontology
- Integration
- Software-as-a-Service
website: https://www.usedefinite.com
---
