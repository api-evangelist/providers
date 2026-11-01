---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for Teddy agent functions and artifacts.
  name: Teddy API
  slug: teddy-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/teddyagent-app/rules/teddyagent-app-rules.yml
  title: ''
  type: Spectral
  url: rules/teddyagent-app-rules.yml
- group: design
  href: https://artifacts.apis.io/teddyagent-app/json-ld/teddyagent-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/teddyagent-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/teddyagent-app/vocabulary/teddyagent-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teddyagent-app-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/teddyagent-app/plans/teddyagent-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/teddyagent-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/teddyagent-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/teddyagent-app/data-model/teddyagent-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/teddyagent-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/teddyagent-app/authentication/teddyagent-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teddyagent-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/teddyagent-app/errors/teddyagent-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/teddyagent-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/teddyagent-app/conformance/teddyagent-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teddyagent-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/teddyagent-app/llms/teddyagent-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teddyagent-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/teddyagent-app/mcp/teddyagent-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/teddyagent-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/teddyagent-app/well-known/teddyagent-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teddyagent-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/teddyagent-app/hosts/teddyagent-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teddyagent-app-hosts.yml
- group: auth
  href: https://artifacts.apis.io/teddyagent-app/security/teddyagent-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teddyagent-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teddyagent.app/
- group: docs
  title: ''
  type: Documentation
  url: https://teddyagent.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://teddyagent.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://teddyagent.app/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://teddyagent.app/openapi.json
  - status: 401
    url: https://teddyagent.app/mcp
  - status: 200
    url: https://teddyagent.app/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: 'Teddy is an AI‑powered agent that helps you create, organize, and share knowledge. Class notes, practice quizzes, documentation or reports: whatever your AI prepares, with its own link and organized in folders. Nothing to install, no servers to maintain. Works where you already work. If you can ask your AI for it, Teddy saves it, files it into folders and gives you a URL to review or share. Record the lecture, hand the transcript to your AI and study from a clean summary. Let your agent publish what it understands about a project, for you and for whoever comes next.'
image: https://teddyagent.app/brand/mark.svg
jsonld:
- class_count: 23
  name: Teddyagent App Context
  property_count: 79
  slug: teddyagent-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at teddyagent.app.
  name: teddyagent-app MCP Server
  slug: teddyagent-app-mcp-yml
modified: '2026-10-30'
name: teddyagent-app
nav: Providers
network: true
overview: 'teddyagent-app publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Education, Productivity, and Collaboration.


  The teddyagent-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  teddyagent-app''s developer surface includes authentication, documentation, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Teddyagent App Plans Pricing
  plan_count: 2
  slug: teddyagent-app-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Teddyagent App Rate Limits
  slug: teddyagent-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: teddyagent-app API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: teddyagent-app-rules
scopes:
- name: Teddyagent App Scopes
  scope_count: 0
  slug: teddyagent-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.8
    catalog_earned_first_party: 8.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 20.7
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Teddyagent App Authentication
  slug: teddyagent-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Teddyagent App Domain Security
  slug: teddyagent-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: publish-artifact
  slug: teddyagent-app-publish-artifact
slug: teddyagent-app
tags:
- Company
- AI
- Education
- Productivity
- Collaboration
- Knowledge-Management
website: https://teddyagent.app/
---
