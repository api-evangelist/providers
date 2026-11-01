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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Komodo provides a web application for managing servers, builds, deployments, and automated procedures as described in its documentation.
  name: Komodo API
  slug: komodo-api
- description: 'Komodo API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Komodo API
  slug: komo-do-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/komo-do/rules/komo-do-rules.yml
  title: ''
  type: Spectral
  url: rules/komo-do-rules.yml
- group: design
  href: https://artifacts.apis.io/komo-do/json-ld/komo-do-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/komo-do-context.jsonld
- group: design
  href: https://artifacts.apis.io/komo-do/vocabulary/komo-do-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/komo-do-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/komo-do/data-model/komo-do-data-model.yml
  title: ''
  type: DataModel
  url: data-model/komo-do-data-model.yml
- group: build
  href: https://artifacts.apis.io/komo-do/cli/komo-do-cli.yml
  title: ''
  type: CLI
  url: cli/komo-do-cli.yml
- group: auth
  href: https://artifacts.apis.io/komo-do/authentication/komo-do-authentication.yml
  title: ''
  type: Authentication
  url: authentication/komo-do-authentication.yml
- group: design
  href: https://artifacts.apis.io/komo-do/conformance/komo-do-conformance.yml
  title: ''
  type: Conformance
  url: conformance/komo-do-conformance.yml
- group: other
  href: https://artifacts.apis.io/komo-do/hosts/komo-do-hosts.yml
  title: ''
  type: Hosts
  url: hosts/komo-do-hosts.yml
- group: other
  href: https://artifacts.apis.io/komo-do/vendors/komo-do-vendors.yml
  title: ''
  type: Vendors
  url: vendors/komo-do-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://komo.do/docs/releases/v2.0.0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rs/komodo_client/latest/komodo_client
- group: auth
  href: https://artifacts.apis.io/komo-do/security/komo-do-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/komo-do-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://komo.do/
- group: docs
  title: ''
  type: Documentation
  url: https://komo.do/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://komo.do/docs/ecosystem/api
- group: start
  title: ''
  type: GettingStarted
  url: https://komo.do/docs/setup
coverage:
  checked: '2026-10-28'
  detail: Documentation is HTML only and provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://komo.do/docs/intro
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Komodo provides an open-source build and deployment system for managing servers, containers, and clusters. It offers a web-based interface to monitor CPU, memory, and disk usage, set alerts, and open shell sessions directly from the browser. Features include Docker Swarm management, automated image building from Git repositories, resource synchronization via declarative TOML files, and extensive automation through procedures and actions. Komodo aims to simplify infrastructure orchestration and DevOps workflows with a unified platform.
image: https://komo.do/img/monitor-lizard.png
json_schemas:
- name: PostWriteUpdatebuildRequest
  property_count: 2
  slug: komo-do-post-write-updatebuild-request
- name: PostWriteUpdatebuildResponse
  property_count: 2
  slug: komo-do-post-write-updatebuild-response
jsonld:
- class_count: 2
  name: Komo Do Context
  property_count: 4
  slug: komo-do-context
layout: provider
modified: '2026-10-28'
name: Komodo
nav: Providers
network: true
overview: 'Komodo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Infrastructure, Automation, and OpenSource.


  The Komodo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Komodo''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Komodo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: komo-do-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Komo Do Authentication
  slug: komo-do-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Komo Do Domain Security
  slug: komo-do-domain-security
  summary_line: TLSv1.3 · HSTS
slug: komo-do
tags:
- Company
- DevOps
- Infrastructure
- Automation
- OpenSource
website: https://komo.do/
---
