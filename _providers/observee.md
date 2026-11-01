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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Observee provides a Model Context Protocol (MCP) API for connecting AI agents to 1000+ apps.
  name: Observee MCP API
  slug: observee-mcp-api
artifact_total: 5
asyncapis:
- description: ''
  name: Observee Webhooks
  slug: observee-webhooks
common:
- group: design
  href: https://artifacts.apis.io/observee/rules/observee-rules.yml
  title: ''
  type: Spectral
  url: rules/observee-rules.yml
- group: design
  href: https://artifacts.apis.io/observee/json-ld/observee-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/observee-context.jsonld
- group: design
  href: https://artifacts.apis.io/observee/vocabulary/observee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/observee-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/observee/asyncapi/observee-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/observee-webhooks.yml
- group: design
  href: https://artifacts.apis.io/observee/data-model/observee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/observee-data-model.yml
- group: design
  href: https://artifacts.apis.io/observee/errors/observee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/observee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/observee/conformance/observee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/observee-conformance.yml
- group: agent
  href: https://artifacts.apis.io/observee/llms/observee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/observee-llms.txt
- group: other
  href: https://artifacts.apis.io/observee/a2a/observee-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/observee-a2a.yml
- group: agent
  href: https://artifacts.apis.io/observee/well-known/observee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/observee-well-known.yml
- group: other
  href: https://artifacts.apis.io/observee/hosts/observee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/observee-hosts.yml
- group: other
  href: https://artifacts.apis.io/observee/vendors/observee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/observee-vendors.yml
- group: build
  href: https://artifacts.apis.io/observee/packages/observee-packages.yml
  title: ''
  type: SDKs
  url: packages/observee-packages.yml
- group: build
  href: https://artifacts.apis.io/observee/packages/observee-packages.yml
  title: ''
  type: Packages
  url: packages/observee-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/observee-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.observee.ai/mcpaiagents
- group: docs
  title: ''
  type: Documentation
  url: https://docs.observee.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.observee.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/observee/security/observee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/observee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://observee.ai/
coverage:
  checked: '2026-10-18'
  detail: OpenAPI spec at https://docs.observee.ai/api-reference/openapi.json describes a sandbox Mintlify server unrelated to Observee, so no valid contract was found.
  evidence:
  - status: 200
    url: https://docs.observee.ai/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Observee provides a fast‑to‑deploy Model Context Protocol (MCP) platform that lets AI agents instantly connect to over a thousand third‑party applications such as Gmail, Slack, Notion, and Jira. The service offers built‑in authentication, analytics, observability, and a unified endpoint, reducing the complexity of building and scaling AI‑agent integrations. Observee’s platform is designed for developers and enterprises seeking to accelerate AI‑driven workflows with secure, observable, and scalable MCP servers.
image: https://observee.ai/hero.png
jsonld:
- class_count: 2
  name: Observee Context
  property_count: 4
  slug: observee-context
layout: provider
modified: '2026-10-18'
name: Observee
nav: Providers
network: true
overview: 'Observee publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Artificial Intelligence, MCP, Integration, Observability, and Platform.


  The Observee catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Observee''s developer surface includes getting-started guide, documentation, API reference, and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Observee API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: observee-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.9
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
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
- kind: domain-security
  name: Observee Domain Security
  slug: observee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: observee
tags:
- Artificial Intelligence
- MCP
- Integration
- Observability
- Platform
website: https://observee.ai/
---
