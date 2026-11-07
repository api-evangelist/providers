---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'EdgeDB API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: EdgeDB API
  slug: edgedb-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/edgedb-com/rules/edgedb-com-rules.yml
  title: ''
  type: Spectral
  url: rules/edgedb-com-rules.yml
- group: design
  href: https://artifacts.apis.io/edgedb-com/json-ld/edgedb-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/edgedb-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/edgedb-com/vocabulary/edgedb-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/edgedb-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/edgedb-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/edgedb-com/data-model/edgedb-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edgedb-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/edgedb-com/conformance/edgedb-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edgedb-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/edgedb-com/hosts/edgedb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edgedb-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/edgedb-com/vendors/edgedb-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edgedb-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geldata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geldata.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geldata.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1st1
- group: company
  title: ''
  type: Blog
  url: https://www.geldata.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.geldata.com/learn/quickstart/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edgedb.com/
- group: auth
  href: https://artifacts.apis.io/edgedb-com/security/edgedb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edgedb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.edgedb.com/
created: '2026-10-25'
description: EdgeDB, now operating as Gel, provides a modern, open‑source data platform built on PostgreSQL. It offers a graph‑style query language, strong type safety, and integrated tooling for developers. The platform aims to simplify data modeling, migrations, and access control while delivering high performance and scalability for cloud‑native applications.
image: https://www.geldata.com/logos/tw_card_intro.png
json_schemas:
- name: GetBranchMainGraphqlResponse
  property_count: 2
  slug: edgedb-com-get-branch-main-graphql-response
- name: GetUvInstallShResponse
  property_count: 1
  slug: edgedb-com-get-uv-install-sh-response
- name: PostApiBooksRequest
  property_count: 5
  slug: edgedb-com-post-api-books-request
- name: PostBranchMainGraphqlRequest
  property_count: 2
  slug: edgedb-com-post-branch-main-graphql-request
- name: PostBranchMainGraphqlResponse
  property_count: 2
  slug: edgedb-com-post-branch-main-graphql-response
- name: PostSearchRequest
  property_count: 1
  slug: edgedb-com-post-search-request
jsonld:
- class_count: 6
  name: Edgedb Com Context
  property_count: 10
  slug: edgedb-com-context
layout: provider
modified: '2026-10-25'
name: EdgeDB
nav: Providers
network: true
overview: 'EdgeDB is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Data Platform, Graph Queries, Authentication, and Artificial Intelligence.


  The EdgeDB catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EdgeDB''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: EdgeDB API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: edgedb-com-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 19.5
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/edgedb-com/edgedb-com-2026-11-03T131511.png
security:
- kind: domain-security
  name: Edgedb Com Domain Security
  slug: edgedb-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edgedb-com
tags:
- Database
- Data Platform
- Graph Queries
- Authentication
- Artificial Intelligence
- Cloud
- Open Source
website: https://www.edgedb.com/
---
