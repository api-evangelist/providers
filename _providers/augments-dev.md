---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: MCP provides a server delivering TypeScript type signatures, documentation, and code examples for npm packages via a Model Context Protocol.
  name: Model Context Protocol (MCP)
  slug: model-context-protocol-mcp
- baseURL: https://registry.modelcontextprotocol.io
  baseurl_source: declared
  description: 'augments-dev 2026 07 28 API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: augments-dev 2026 07 28 API
  slug: 2026-07-28-api
- baseURL: https://registry.modelcontextprotocol.io
  baseurl_source: declared
  description: 'augments-dev core API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: augments-dev core API
  slug: core-api
- baseURL: https://registry.modelcontextprotocol.io
  baseurl_source: declared
  description: 'augments-dev draft API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: augments-dev draft API
  slug: draft-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/augments-dev/rules/augments-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/augments-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/augments-dev/json-ld/augments-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/augments-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/augments-dev/vocabulary/augments-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/augments-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/augments-dev/data-model/augments-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/augments-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/augments-dev/cli/augments-dev-cli.yml
  title: ''
  type: CLI
  url: cli/augments-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/augments-dev/conventions/augments-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/augments-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/augments-dev/authentication/augments-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/augments-dev-authentication.yml
- group: operate
  href: https://artifacts.apis.io/augments-dev/lifecycle/augments-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/augments-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/augments-dev/lifecycle/augments-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/augments-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/augments-dev/conformance/augments-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augments-dev-conformance.yml
- group: other
  href: https://artifacts.apis.io/augments-dev/a2a/augments-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/augments-dev-a2a.yml
- group: auth
  href: https://artifacts.apis.io/augments-dev/well-known/augments-dev-modelcontextprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augments-dev-modelcontextprotocol-security.txt
- group: agent
  href: https://artifacts.apis.io/augments-dev/well-known/augments-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/augments-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/augments-dev/hosts/augments-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augments-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/augments-dev/vendors/augments-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augments-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/augments-dev/packages/augments-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/augments-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/augments-dev/packages/augments-dev-packages.yml
  title: ''
  type: Packages
  url: packages/augments-dev-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- group: auth
  href: https://artifacts.apis.io/augments-dev/security/augments-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augments-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augments.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://modelcontextprotocol.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/augmnt
- group: company
  title: ''
  type: Blog
  url: https://blog.modelcontextprotocol.io
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://modelcontextprotocol.io/mcp
  - status: 200
    url: https://augments.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Augments.dev provides an MCP (Model Context Protocol) server that delivers TypeScript type signatures, documentation, and code examples for any npm package. By integrating with Claude, it enables AI models to fetch up-to-date API information, intent-aware formatting, and practical examples across the entire npm ecosystem. The service auto-discovers package metadata, resolves versions, and returns structured responses for queries about functions, hooks, and libraries, supporting developers and AI assistants in generating accurate, current code snippets and documentation.
image: https://augments.dev/opengraph-image?c5cca62aa75ffeb0
json_schemas:
- name: GetHealthzResponse
  property_count: 1
  slug: augments-dev-get-healthz-response
- name: GetV01ServersResponse
  property_count: 1
  slug: augments-dev-get-v01-servers-response
jsonld:
- class_count: 2
  name: Augments Dev Context
  property_count: 2
  slug: augments-dev-context
layout: provider
modified: '2026-10-30'
name: augments-dev
nav: Providers
network: true
overview: 'augments-dev is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including 2026 07 28 API, core API, draft API, and 1 more. Tagged areas include Company, AI, TypeScript, npm, and Documentation.


  The augments-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  augments-dev''s developer surface includes CLI, authentication, getting-started guide, documentation, engineering blog, and 19 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: augments-dev API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: augments-dev-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.4
    catalog_earned_first_party: 0.0
    catalog_gap: 51.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 70.9
    contract_quality: 47.0
    developer_ergonomics: 59.5
    discoverability: 62.5
    operational_transparency: 23.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Augments Dev Authentication
  slug: augments-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Augments Dev Domain Security
  slug: augments-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: augments-dev
tags:
- Company
- AI
- TypeScript
- npm
- Documentation
- CodeExamples
website: https://augments.dev/
---
