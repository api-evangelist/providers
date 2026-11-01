---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Meatspace Run Agentic Access
  operation_count: 10
  slug: meatspace-run-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- description: Flesh-in-the-loop service API allowing AI agents to submit content and receive human decisions.
  name: MeatSpace API
  slug: meatspace-api
- baseURL: https://meatspace.run
  baseurl_source: declared
  description: The Keys API from meatspace-run — 1 operation(s) for keys.
  name: meatspace-run Keys API
  slug: meatspace-run-keys-api
- baseURL: https://meatspace.run
  baseurl_source: declared
  description: The Mcp API from meatspace-run — 1 operation(s) for mcp.
  name: meatspace-run MCP API
  slug: meatspace-run-mcp-api
- baseURL: https://meatspace.run
  baseurl_source: declared
  description: The Requests API from meatspace-run — 3 operation(s) for requests.
  name: meatspace-run Requests API
  slug: meatspace-run-requests-api
- baseURL: https://meatspace.run
  baseurl_source: declared
  description: The Review API from meatspace-run — 1 operation(s) for review.
  name: meatspace-run Review API
  slug: meatspace-run-review-api
- baseURL: https://meatspace.run
  baseurl_source: declared
  description: The Status API from meatspace-run — 1 operation(s) for status.
  name: meatspace-run Status API
  slug: meatspace-run-status-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/meatspace-run/agentic-access/meatspace-run-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meatspace-run-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/meatspace-run/rules/meatspace-run-rules.yml
  title: ''
  type: Spectral
  url: rules/meatspace-run-rules.yml
- group: design
  href: https://artifacts.apis.io/meatspace-run/json-ld/meatspace-run-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meatspace-run-context.jsonld
- group: design
  href: https://artifacts.apis.io/meatspace-run/vocabulary/meatspace-run-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meatspace-run-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/meatspace-run/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/meatspace-run/data-model/meatspace-run-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meatspace-run-data-model.yml
- group: design
  href: https://artifacts.apis.io/meatspace-run/errors/meatspace-run-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meatspace-run-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meatspace-run/conformance/meatspace-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meatspace-run-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meatspace-run/llms/meatspace-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meatspace-run-llms.txt
- group: other
  href: https://artifacts.apis.io/meatspace-run/a2a/meatspace-run-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/meatspace-run-a2a.yml
- group: agent
  href: https://artifacts.apis.io/meatspace-run/mcp/meatspace-run-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/meatspace-run-mcp.yml
- group: other
  href: https://artifacts.apis.io/meatspace-run/hosts/meatspace-run-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meatspace-run-hosts.yml
- group: other
  href: https://artifacts.apis.io/meatspace-run/vendors/meatspace-run-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meatspace-run-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://meatspace.run/sdk/meatspace.js
- group: auth
  href: https://artifacts.apis.io/meatspace-run/authentication/meatspace-run-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meatspace-run-authentication.yml
- group: auth
  href: https://artifacts.apis.io/meatspace-run/security/meatspace-run-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meatspace-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meatspace.run/
- group: docs
  title: ''
  type: Documentation
  url: https://meatspace.run/docs
- group: docs
  title: ''
  type: APIReference
  url: https://meatspace.run/api/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://meatspace.run/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meatspace.run/terms
created: '2026-10-30'
description: MeatSpace provides a human-in-the-loop API for AI agents, enabling subjective or ambiguous decisions to be routed to human reviewers. It offers REST, MCP, and a browser SDK, with instant API keys via POST /api/keys. Use cases include judgment, taste, approval, and tie‑breaks, while avoiding deterministic low‑stakes checks.
jsonld:
- class_count: 6
  name: Meatspace Run Context
  property_count: 27
  slug: meatspace-run-context
layout: provider
mcp_servers:
- description: Remote MCP server at meatspace.run.
  name: meatspace-run MCP Server
  slug: meatspace-run-mcp-yml
modified: '2026-10-30'
name: meatspace-run
nav: Providers
network: true
overview: 'meatspace-run publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Keys API, MCP API, Requests API, and 3 more. Tagged areas include Company, AI, Human-in-the-loop, API, and Automation.


  The meatspace-run catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  meatspace-run''s developer surface includes authentication, documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: meatspace-run API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: meatspace-run-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 49.4
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Meatspace Run Authentication
  slug: meatspace-run-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Meatspace Run Domain Security
  slug: meatspace-run-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: meatspace-run-create-human-decision
  slug: meatspace-run-create-human-decision
slug: meatspace-run
tags:
- Company
- AI
- Human-in-the-loop
- API
- Automation
website: https://meatspace.run/
---
