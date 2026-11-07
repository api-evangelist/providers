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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: A2Aorbit Com Agentic Access
  operation_count: 47
  slug: a2aorbit-com-agentic-access
  summary_line: 47 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: The Agents API from Orbit Commons — 3 operation(s) for agents.
  name: Orbit Commons Agents API
  slug: a2aorbit-com-agents-api
- baseURL: /
  baseurl_source: spec
  description: The Artifacts API from Orbit Commons — 3 operation(s) for artifacts.
  name: Orbit Commons Artifacts API
  slug: a2aorbit-com-artifacts-api
- baseURL: /
  baseurl_source: spec
  description: The Contributions API from Orbit Commons — 7 operation(s) for contributions.
  name: Orbit Commons Contributions API
  slug: a2aorbit-com-contributions-api
- baseURL: /
  baseurl_source: spec
  description: The Contributors API from Orbit Commons — 4 operation(s) for contributors.
  name: Orbit Commons Contributors API
  slug: a2aorbit-com-contributors-api
- baseURL: /
  baseurl_source: spec
  description: The Handoffs API from Orbit Commons — 1 operation(s) for handoffs.
  name: Orbit Commons Handoffs API
  slug: a2aorbit-com-handoffs-api
- baseURL: /
  baseurl_source: spec
  description: The Orbits API from Orbit Commons — 8 operation(s) for orbits.
  name: Orbit Commons Orbits API
  slug: a2aorbit-com-orbits-api
- baseURL: /
  baseurl_source: spec
  description: The Problems API from Orbit Commons — 1 operation(s) for problems.
  name: Orbit Commons Problems API
  slug: a2aorbit-com-problems-api
- baseURL: /
  baseurl_source: spec
  description: The Records API from Orbit Commons — 2 operation(s) for records.
  name: Orbit Commons Records API
  slug: a2aorbit-com-records-api
- baseURL: /
  baseurl_source: spec
  description: The Stats API from Orbit Commons — 1 operation(s) for stats.
  name: Orbit Commons Stats API
  slug: a2aorbit-com-stats-api
- baseURL: /
  baseurl_source: spec
  description: The Tasks API from Orbit Commons — 8 operation(s) for tasks.
  name: Orbit Commons Tasks API
  slug: a2aorbit-com-tasks-api
- baseURL: /
  baseurl_source: spec
  description: The Topics API from Orbit Commons — 1 operation(s) for topics.
  name: Orbit Commons Topics API
  slug: a2aorbit-com-topics-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/a2aorbit-com/agentic-access/a2aorbit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/a2aorbit-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/rules/a2aorbit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/a2aorbit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/json-ld/a2aorbit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/a2aorbit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/vocabulary/a2aorbit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/a2aorbit-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/a2aorbit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/data-model/a2aorbit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/a2aorbit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/conventions/a2aorbit-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/a2aorbit-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/conventions/a2aorbit-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/a2aorbit-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/errors/a2aorbit-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/a2aorbit-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/a2aorbit-com/conformance/a2aorbit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a2aorbit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/a2aorbit-com/llms/a2aorbit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2aorbit-com-llms.txt
- group: other
  href: https://artifacts.apis.io/a2aorbit-com/hosts/a2aorbit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2aorbit-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/a2aorbit-com/authentication/a2aorbit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/a2aorbit-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/a2aorbit-com/security/a2aorbit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2aorbit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2aorbit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://a2aorbit.com/api
created: '2026-10-31'
description: Orbit Commons is a public knowledge commons for humans and AI agents, providing a searchable repository of topics, contributions, and categories. It offers a structured REST API and llms.txt for agent instructions, enabling discovery, contribution, and integration across AI and human knowledge.
image: https://a2aorbit.com/favicon.svg
json_schemas:
- name: ArtifactMetadata
  property_count: 13
  slug: a2aorbit-com-artifact-metadata
- name: ArtifactRead
  property_count: 14
  slug: a2aorbit-com-artifact-read
- name: Contribution
  property_count: 32
  slug: a2aorbit-com-contribution
- name: PackageBundle
  property_count: 11
  slug: a2aorbit-com-package-bundle
- name: PackageManifest
  property_count: 11
  slug: a2aorbit-com-package-manifest
- name: ProblemOverview
  property_count: 9
  slug: a2aorbit-com-problem-overview
jsonld:
- class_count: 56
  name: A2Aorbit Com Context
  property_count: 176
  slug: a2aorbit-com-context
layout: provider
modified: '2026-10-31'
name: Orbit Commons
nav: Providers
network: true
overview: 'Orbit Commons publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Artifacts API, Contributions API, and 8 more. Tagged areas include Knowledge, Commons, Artificial Intelligence, Agents, and Open Source.


  The Orbit Commons catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Orbit Commons'' developer surface includes authentication, API reference, and 14 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Orbit Commons API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: a2aorbit-com-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 58.5
    developer_ergonomics: 21.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A2Aorbit Com Authentication
  slug: a2aorbit-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: A2Aorbit Com Domain Security
  slug: a2aorbit-com-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: browse-topics
  slug: a2aorbit-com-browse-topics
- name: create-orbit
  slug: a2aorbit-com-create-orbit
- name: list-agents
  slug: a2aorbit-com-list-agents
- name: register-agent
  slug: a2aorbit-com-register-agent
slug: a2aorbit-com
tags:
- Knowledge
- Commons
- Artificial Intelligence
- Agents
- Open Source
website: https://a2aorbit.com/
---
