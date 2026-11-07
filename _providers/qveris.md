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
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Qveris Agentic Access
  operation_count: 2
  slug: qveris-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://qveris.ai/api/v1
  baseurl_source: declared
  description: The Agent Lifecycle API from QVeris — 2 operation(s) for agent lifecycle.
  name: QVeris Agent Lifecycle API
  slug: qveris-agent-lifecycle-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/qveris/data-model/qveris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qveris-data-model.yml
- group: agent
  href: https://artifacts.apis.io/qveris/agentic-access/qveris-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qveris-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/qveris/rules/qveris-rules.yml
  title: ''
  type: Spectral
  url: rules/qveris-rules.yml
- group: design
  href: https://artifacts.apis.io/qveris/vocabulary/qveris-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qveris-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/qveris/cli/qveris-cli.yml
  title: ''
  type: CLI
  url: cli/qveris-cli.yml
- group: design
  href: https://artifacts.apis.io/qveris/conventions/qveris-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/qveris-conventions.yml
- group: design
  href: https://artifacts.apis.io/qveris/conventions/qveris-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qveris-conventions.yml
- group: auth
  href: https://artifacts.apis.io/qveris/authentication/qveris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qveris-authentication.yml
- group: design
  href: https://artifacts.apis.io/qveris/lifecycle/qveris-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qveris-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qveris/errors/qveris-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qveris-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qveris/conformance/qveris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qveris-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qveris/llms/qveris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qveris-llms.txt
- group: other
  href: https://artifacts.apis.io/qveris/a2a/qveris-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/qveris-a2a.yml
- group: agent
  href: https://artifacts.apis.io/qveris/mcp/qveris-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qveris-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qveris/well-known/qveris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qveris-well-known.yml
- group: other
  href: https://artifacts.apis.io/qveris/hosts/qveris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qveris-hosts.yml
- group: build
  href: https://artifacts.apis.io/qveris/packages/qveris-packages.yml
  title: ''
  type: Packages
  url: packages/qveris-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://qveris.ai/security
- group: start
  title: ''
  type: Sandbox
  url: https://qveris.ai/playground
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@qverisai/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://qveris.ai/whats-new
- group: docs
  title: ''
  type: APIReference
  url: https://qveris.ai/docs/api-reference/call
- group: auth
  href: https://artifacts.apis.io/qveris/security/qveris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qveris-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qveris/security/qveris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qveris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qveris.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://qveris.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://qveris.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://qveris.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://qveris.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QVerisAI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qveris.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qveris.ai/privacy
- group: operate
  title: ''
  type: HelpCenter
  url: https://qveris.ai/help
created: '2026-10-30'
description: QVeris AI, LLC provides a unified platform that aggregates professional data services and tools, enabling AI applications to discover, inspect, and invoke data sources directly within their existing workflows. The platform offers a Model Connectivity Protocol (MCP) server, CLI, SDKs, and a sandboxed execution environment, delivering structured JSON results, usage tracking, and credit‑based billing. By connecting to finance, research, product, and other data providers, QVeris empowers developers to enrich AI models with reliable, up‑to‑date information.
image: https://qveris.ai/logo-color.png
json_schemas:
- name: AgentAnonymousRegisterRequest
  property_count: 0
  slug: qveris-agent-anonymous-register-request
- name: AgentClaimStartRequest
  property_count: 0
  slug: qveris-agent-claim-start-request
- name: APIResponse_AgentAnonymousRegisterResponse_
  property_count: 0
  slug: qveris-apiresponse-agent-anonymous-register-response
- name: APIResponse_Union_AgentClaimStartResponse__AgentClaimRiskBlockResponse__
  property_count: 0
  slug: qveris-apiresponse-union-agent-claim-start-response-agent-claim-risk-block-response
layout: provider
mcp_servers:
- description: Remote MCP server at qveris.ai.
  name: QVeris MCP Server
  slug: qveris-mcp-yml
modified: '2026-10-30'
name: QVeris
nav: Providers
network: true
overview: 'QVeris publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent Lifecycle API. Tagged areas include Artificial Intelligence, Data, Platform, Developer Tools, and MCP.


  The QVeris catalog on APIs.io includes 1 Spectral governance ruleset.


  QVeris'' developer surface includes CLI, authentication, sandbox, changelog, API reference, documentation, getting-started guide, and 26 more developer resources.'
plans:
- name: Qveris Plans Pricing
  plan_count: 0
  slug: qveris-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Qveris Rate Limits
  slug: qveris-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: QVeris API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: qveris-rules
scopes:
- name: Qveris Scopes
  scope_count: 0
  slug: qveris-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 55.1
    developer_ergonomics: 47.6
    discoverability: 75.0
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qveris/qveris-2026-11-03T141845.png
security:
- kind: authentication
  name: Qveris Authentication
  slug: qveris-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qveris Domain Security
  slug: qveris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qveris Vulnerability Disclosure
  slug: qveris-vulnerability-disclosure
  summary_line: no policy recorded
slug: qveris
tags:
- Artificial Intelligence
- Data
- Platform
- Developer Tools
- MCP
website: https://qveris.ai/
---
