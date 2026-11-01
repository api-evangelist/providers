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
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Trilo provides an AI‑powered workspace with collaborative features; public documentation exists but no machine‑readable API contract was found.
  name: Trilo API
  slug: trilo-api
artifact_total: 10
asyncapis:
- description: ''
  name: Trilo Chat Webhooks
  slug: trilo-chat-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/trilo-chat/plans/trilo-chat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trilo-chat-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/rules/trilo-chat-rules.yml
  title: ''
  type: Spectral
  url: rules/trilo-chat-rules.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/json-ld/trilo-chat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trilo-chat-context.jsonld
- group: design
  href: https://artifacts.apis.io/trilo-chat/vocabulary/trilo-chat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trilo-chat-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/asyncapi/trilo-chat-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trilo-chat-webhooks.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/data-model/trilo-chat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trilo-chat-data-model.yml
- group: build
  href: https://artifacts.apis.io/trilo-chat/cli/trilo-chat-cli.yml
  title: ''
  type: CLI
  url: cli/trilo-chat-cli.yml
- group: operate
  href: https://artifacts.apis.io/trilo-chat/changelog/trilo-chat-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/trilo-chat-changelog.yml
- group: auth
  href: https://artifacts.apis.io/trilo-chat/authentication/trilo-chat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trilo-chat-authentication.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/errors/trilo-chat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trilo-chat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trilo-chat/conformance/trilo-chat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trilo-chat-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trilo-chat/llms/trilo-chat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trilo-chat-llms.txt
- group: other
  href: https://artifacts.apis.io/trilo-chat/a2a/trilo-chat-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trilo-chat-a2a.yml
- group: agent
  href: https://artifacts.apis.io/trilo-chat/mcp/trilo-chat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trilo-chat-mcp.yml
- group: agent
  href: https://artifacts.apis.io/trilo-chat/well-known/trilo-chat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trilo-chat-well-known.yml
- group: other
  href: https://artifacts.apis.io/trilo-chat/hosts/trilo-chat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trilo-chat-hosts.yml
- group: other
  href: https://artifacts.apis.io/trilo-chat/vendors/trilo-chat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trilo-chat-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trilohq
- group: operate
  title: ''
  type: ChangeLog
  url: https://trilo.chat/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trilo.chat/developers/cli/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trilo.chat/llms.txt
- group: auth
  href: https://artifacts.apis.io/trilo-chat/security/trilo-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trilo-chat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trilo.chat/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trilo.chat/
- group: operate
  title: ''
  type: Support
  url: https://trilo.chat/support
- group: company
  title: ''
  type: Blog
  url: https://trilo.chat/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://trilo.chat/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trilo.chat/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trilo.chat/privacy
coverage:
  checked: '2026-10-31'
  detail: The public documentation is readable but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://docs.trilo.chat/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Trilo is an AI‑powered workspace that unifies chat, tasks, documents, calendar, and social media scheduling into a single collaborative platform. Its autonomous AI coworkers operate 24/7, handling meetings, knowledge management, and workflow automation, eliminating tool sprawl and boosting team productivity. The service is delivered via web and native apps for macOS, iOS, Android, and integrates with popular tools through MCP.
image: https://trilo.chat/logo_black0.png
jsonld:
- class_count: 2
  name: Trilo Chat Context
  property_count: 4
  slug: trilo-chat-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.trilo.chat.
  name: trilo-chat MCP Server
  slug: trilo-chat-mcp-yml
modified: '2026-10-31'
name: trilo-chat
nav: Providers
network: true
overview: 'trilo-chat publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Collaboration, Productivity, Workspace, and Chatbot.


  The trilo-chat catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  trilo-chat''s developer surface includes CLI, changelog, authentication, getting-started guide, API reference, documentation, support, and 22 more developer resources.'
plans:
- name: Trilo Chat Plans Pricing
  plan_count: 3
  slug: trilo-chat-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Trilo Chat Rate Limits
  slug: trilo-chat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: trilo-chat API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: trilo-chat-rules
scopes:
- name: Trilo Chat Scopes
  scope_count: 0
  slug: trilo-chat-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 45.5
    developer_ergonomics: 54.8
    discoverability: 56.7
    operational_transparency: 28.9
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Trilo Chat Authentication
  slug: trilo-chat-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Trilo Chat Domain Security
  slug: trilo-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trilo-chat
tags:
- AI
- Collaboration
- Productivity
- Workspace
- Chatbot
website: https://trilo.chat/
---
