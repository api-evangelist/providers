---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 75
  human_in_the_loop: 6
  name: Tembo Agentic Access
  operation_count: 152
  slug: tembo-agentic-access
  summary_line: 152 operations · 75 acting · 6 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Agents API from Tembo — 13 operation(s) for agents.
  name: Tembo Agents API
  slug: tembo-agents-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The API Keys API from Tembo — 2 operation(s) for api keys.
  name: Tembo API Keys API
  slug: tembo-api-keys-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Artifacts API from Tembo — 2 operation(s) for artifacts.
  name: Tembo Artifacts API
  slug: tembo-artifacts-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Authentication API from Tembo — 1 operation(s) for authentication.
  name: Tembo Authentication API
  slug: tembo-authentication-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Billing API from Tembo — 2 operation(s) for billing.
  name: Tembo Billing API
  slug: tembo-billing-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Insights API from Tembo — 3 operation(s) for insights.
  name: Tembo Insights API
  slug: tembo-insights-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Integrations API from Tembo — 13 operation(s) for integrations.
  name: Tembo Integrations API
  slug: tembo-integrations-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The MCP Connections API from Tembo — 4 operation(s) for mcp connections.
  name: Tembo MCP Connections API
  slug: tembo-mcp-connections-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Messages API from Tembo — 3 operation(s) for messages.
  name: Tembo Messages API
  slug: tembo-messages-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Models API from Tembo — 2 operation(s) for models.
  name: Tembo Models API
  slug: tembo-models-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The OAuth API from Tembo — 1 operation(s) for oauth.
  name: Tembo OAuth API
  slug: tembo-oauth-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Organizations API from Tembo — 10 operation(s) for organizations.
  name: Tembo Organizations API
  slug: tembo-organizations-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Projects API from Tembo — 12 operation(s) for projects.
  name: Tembo Projects API
  slug: tembo-projects-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Pull requests API from Tembo — 2 operation(s) for pull requests.
  name: Tembo Pull requests API
  slug: tembo-pull-requests-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Repositories API from Tembo — 2 operation(s) for repositories.
  name: Tembo Repositories API
  slug: tembo-repositories-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Runtimes API from Tembo — 1 operation(s) for runtimes.
  name: Tembo Runtimes API
  slug: tembo-runtimes-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Sessions API from Tembo — 10 operation(s) for sessions.
  name: Tembo Sessions API
  slug: tembo-sessions-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Skills API from Tembo — 4 operation(s) for skills.
  name: Tembo Skills API
  slug: tembo-skills-api
- baseURL: https://api.tembo.io
  baseurl_source: declared
  description: The Users API from Tembo — 8 operation(s) for users.
  name: Tembo Users API
  slug: tembo-users-api
artifact_total: 33
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/agentic-access/tembo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tembo-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/plans/tembo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tembo-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/rules/tembo-rules.yml
  title: ''
  type: Spectral
  url: rules/tembo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/json-ld/tembo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tembo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/vocabulary/tembo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tembo-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/data-model/tembo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tembo-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/changelog/tembo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tembo-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/conventions/tembo-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tembo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/conventions/tembo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tembo-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tembo.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/errors/tembo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tembo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/conformance/tembo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tembo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/llms/tembo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tembo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/mcp/tembo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tembo-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/well-known/tembo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tembo-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/well-known/tembo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tembo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/hosts/tembo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tembo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/vendors/tembo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tembo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/packages/tembo-packages.yml
  title: ''
  type: Packages
  url: packages/tembo-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tembo.io/security
- group: start
  title: ''
  type: Sandbox
  url: https://www.tembo.io/sandbox
- group: build
  title: ''
  type: SDKs
  url: https://www.tembo.io/sdk
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/authentication/tembo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tembo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tembo.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/security/tembo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tembo-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tembo/refs/heads/main/security/tembo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tembo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tembo.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tembo.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tembo.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tembo.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tembo.io/support
- group: company
  title: ''
  type: Blog
  url: https://www.tembo.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tembo.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tembo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tembo.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.tembo.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tembo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tembo.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tembo.io
created: '2026-10-13'
description: 'Tembo (tembo.io) is a cloud platform for running AI coding agents (Claude Code, Codex, Cursor, Amp, OpenCode and others) in isolated, shareable sandbox environments connected to repositories, issue trackers, observability tools and databases, with a self-hosted Enterprise option. It publishes a public REST API (OpenAPI 3.1, 152 operations at api.tembo.io), TypeScript and Python SDKs, and an official remote MCP server at mcp.tembo.io. Surfaced by the databases-postgres market-gap harvest: Tembo was previously known for its managed Postgres platform, but its current site, docs and API describe the agent platform only, and the former tembo-io GitHub organization lists 0 public repositories (checked 2026-10-13).'
image: https://www.tembo.io/images/og-image.png
json_schemas:
- name: AgentOptionsInput
  property_count: 0
  slug: tembo-agent-options-input
- name: AgentOptions
  property_count: 4
  slug: tembo-agent-options
- name: AgentState
  property_count: 0
  slug: tembo-agent-state
- name: SessionEventData
  property_count: 16
  slug: tembo-session-event-data
- name: TipTapDocument
  property_count: 0
  slug: tembo-tip-tap-document
- name: TriggerFilters
  property_count: 0
  slug: tembo-trigger-filters
jsonld:
- class_count: 53
  name: Tembo Context
  property_count: 73
  slug: tembo-context
layout: provider
mcp_servers:
- description: Official Tembo MCP server. Per the docs, its tools are generated from the same OpenAPI schema as the Tembo API reference and TypeScript SDK, and it can perform the same API operations available to the
  name: Tembo MCP Server
  slug: tembo-mcp-server
modified: '2026-10-13'
name: Tembo
nav: Providers
network: true
overview: 'Tembo publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, API Keys API, Artifacts API, and 16 more. Tagged areas include Company, AI Agents, Coding Agents, Developer Tools, and Sandbox.


  The Tembo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tembo''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 32 more developer resources.'
plans:
- name: Tembo Plans Pricing
  plan_count: 4
  slug: tembo-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Tembo API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: tembo-rules
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 65.6
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Tembo Authentication
  slug: tembo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tembo Domain Security
  slug: tembo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tembo Trust Center
  slug: tembo-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: tembo
tags:
- Company
- AI Agents
- Coding Agents
- Developer Tools
- Sandbox
- MCP
- Automation
website: https://www.tembo.io
---
