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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'e18e API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: e18e API
  slug: e18e-dev-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/e18e-dev/rules/e18e-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/e18e-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/e18e-dev/json-ld/e18e-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/e18e-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/e18e-dev/vocabulary/e18e-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/e18e-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/e18e-dev/data-model/e18e-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/e18e-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/e18e-dev/cli/e18e-dev-cli.yml
  title: ''
  type: CLI
  url: cli/e18e-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/e18e-dev/conformance/e18e-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/e18e-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/e18e-dev/llms/e18e-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e18e-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/e18e-dev/hosts/e18e-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e18e-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/e18e-dev/vendors/e18e-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e18e-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/e18e
- group: auth
  href: https://artifacts.apis.io/e18e-dev/security/e18e-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e18e-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e18e.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://e18e.dev/docs/
- group: company
  title: ''
  type: Blog
  url: https://e18e.dev/blog
- group: learn
  title: ''
  type: Learning
  url: https://e18e.dev/learn/
- group: operate
  title: ''
  type: Community
  url: https://chat.e18e.dev
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are static HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract files.
  evidence:
  - status: 200
    url: https://e18e.dev/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: e18e (Ecosystem Performance) is an initiative focused on improving JavaScript package performance by cleaning up redundant dependencies, speeding up builds, and leveling up code quality. The platform offers documentation, learning resources, and community engagement through Discord and sponsorships, aiming to provide visibility and support for open‑source developers working on ecosystem optimization.
image: https://e18e.dev/e18e-og-image.png
json_schemas:
- name: GetDataResponse
  property_count: 1
  slug: e18e-dev-get-data-response
- name: PostDataResponse
  property_count: 1
  slug: e18e-dev-post-data-response
jsonld:
- class_count: 2
  name: E18E Dev Context
  property_count: 1
  slug: e18e-dev-context
layout: provider
modified: '2026-11-06'
name: e18e
nav: Providers
network: true
overview: 'e18e is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ecosystem, Performance, JavaScript, Open Source, and Community.


  The e18e catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  e18e''s developer surface includes CLI, documentation, engineering blog, and 13 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: e18e API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: e18e-dev-rules
score:
  band: emerging
  composite: 18.0
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
    contract_quality: 19.3
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: E18E Dev Domain Security
  slug: e18e-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: e18e-dev
tags:
- Ecosystem
- Performance
- JavaScript
- Open Source
- Community
website: https://e18e.dev/
---
