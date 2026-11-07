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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for ThousandBirds' Chidori AI agent platform, providing debugging, tracing, and tool integration capabilities.
  name: Chidori API
  slug: chidori-api
- description: 'ThousandBirds API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: ThousandBirds API
  slug: thousandbirds-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/thousandbirds/rules/thousandbirds-rules.yml
  title: ''
  type: Spectral
  url: rules/thousandbirds-rules.yml
- group: design
  href: https://artifacts.apis.io/thousandbirds/vocabulary/thousandbirds-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thousandbirds-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/thousandbirds/conventions/thousandbirds-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thousandbirds-conventions.yml
- group: auth
  href: https://artifacts.apis.io/thousandbirds/authentication/thousandbirds-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thousandbirds-authentication.yml
- group: design
  href: https://artifacts.apis.io/thousandbirds/conformance/thousandbirds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thousandbirds-conformance.yml
- group: other
  href: https://artifacts.apis.io/thousandbirds/hosts/thousandbirds-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thousandbirds-hosts.yml
- group: other
  href: https://artifacts.apis.io/thousandbirds/vendors/thousandbirds-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thousandbirds-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/ThousandBirdsInc/chidori/releases
- group: auth
  href: https://artifacts.apis.io/thousandbirds/security/thousandbirds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thousandbirds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thousandbirds.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://thousandbirds.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://thousandbirds.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThousandBirdsInc
- group: start
  title: ''
  type: GettingStarted
  url: https://thousandbirds.ai/docs/quickstart
- group: company
  title: ''
  type: About
  url: https://thousandbirds.ai/about
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.thousandbirds.ai/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Thousand Birds builds AI agents that are fully debuggable, offering a TypeScript runtime called Chidori. The platform records every LLM call, tool invocation, and side effect, enabling step‑by‑step replay of agent runs. Users can debug production failures, trace execution, and integrate with tools like Tael for observability. The open‑source project emphasizes deterministic agents, reproducible debugging, and seamless integration with modern AI workflows.
layout: provider
modified: '2026-10-19'
name: ThousandBirds
nav: Providers
network: true
overview: 'ThousandBirds is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Debugging, TypeScript, and Open Source.


  The ThousandBirds catalog on APIs.io includes 1 Spectral governance ruleset.


  ThousandBirds'' developer surface includes authentication, changelog, documentation, engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ThousandBirds API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: thousandbirds-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 10.5
  previous_composite: 20.6
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
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/thousandbirds/thousandbirds-2026-11-03T144701.png
security:
- kind: authentication
  name: Thousandbirds Authentication
  slug: thousandbirds-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thousandbirds Domain Security
  slug: thousandbirds-domain-security
  summary_line: TLSv1.3 · HSTS
slug: thousandbirds
tags:
- Artificial Intelligence
- Agents
- Debugging
- TypeScript
- Open Source
website: https://thousandbirds.ai/
---
