---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Empiriolabs Ai Agentic Access
  operation_count: 7
  slug: empiriolabs-ai-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The chatCompletions API from EmpirioLabs AI — 1 operation(s) for chatcompletions.
  name: EmpirioLabs AI Chat Completions API
  slug: empiriolabs-ai-chatcompletions-api
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The completions API from EmpirioLabs AI — 1 operation(s) for completions.
  name: EmpirioLabs AI Completions API
  slug: empiriolabs-ai-completions-api
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The gemini API from EmpirioLabs AI — 1 operation(s) for gemini.
  name: EmpirioLabs AI Gemini API
  slug: empiriolabs-ai-gemini-api
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The messages API from EmpirioLabs AI — 1 operation(s) for messages.
  name: EmpirioLabs AI Messages API
  slug: empiriolabs-ai-messages-api
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The models API from EmpirioLabs AI — 2 operation(s) for models.
  name: EmpirioLabs AI Models API
  slug: empiriolabs-ai-models-api
- baseURL: https://api.empiriolabs.ai
  baseurl_source: declared
  description: The responses API from EmpirioLabs AI — 1 operation(s) for responses.
  name: EmpirioLabs AI Responses API
  slug: empiriolabs-ai-responses-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/empiriolabs-ai/capabilities/empiriolabs-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/empiriolabs-ai-capability-edges.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.empiriolabs.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/empiriolabs-ai/agentic-access/empiriolabs-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/empiriolabs-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/empiriolabs-ai/rate-limits/empiriolabs-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/empiriolabs-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/empiriolabs-ai/plans/empiriolabs-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/empiriolabs-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/rules/empiriolabs-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/empiriolabs-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/json-ld/empiriolabs-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/empiriolabs-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/vocabulary/empiriolabs-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/empiriolabs-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/empiriolabs-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/data-model/empiriolabs-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/empiriolabs-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/empiriolabs-ai/cli/empiriolabs-ai-cli.yml
  title: ''
  type: CLI
  url: cli/empiriolabs-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/empiriolabs-ai/changelog/empiriolabs-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/empiriolabs-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/conventions/empiriolabs-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/empiriolabs-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/empiriolabs-ai/authentication/empiriolabs-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/empiriolabs-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/lifecycle/empiriolabs-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/empiriolabs-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/errors/empiriolabs-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/empiriolabs-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/empiriolabs-ai/conformance/empiriolabs-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/empiriolabs-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/empiriolabs-ai/overlays/empiriolabs-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/empiriolabs-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/empiriolabs-ai/llms/empiriolabs-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/empiriolabs-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/empiriolabs-ai/mcp/empiriolabs-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/empiriolabs-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/empiriolabs-ai/mcp/empiriolabs-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/empiriolabs-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/empiriolabs-ai/well-known/empiriolabs-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/empiriolabs-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/empiriolabs-ai/hosts/empiriolabs-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/empiriolabs-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/empiriolabs-ai/vendors/empiriolabs-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/empiriolabs-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/empiriolabs-ai/packages/empiriolabs-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/empiriolabs-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/empiriolabs-ai/packages/empiriolabs-ai-packages.yml
  title: ''
  type: Packages
  url: packages/empiriolabs-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.empiriolabs.ai/
- group: start
  title: ''
  type: Sandbox
  url: https://platform.empiriolabs.ai/dashboard/playground
- group: other
  title: ''
  type: Leadership
  url: https://empiriolabs.ai/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.empiriolabs.ai/documentation/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.empiriolabs.ai`
- group: auth
  href: https://artifacts.apis.io/empiriolabs-ai/security/empiriolabs-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/empiriolabs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://empiriolabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.empiriolabs.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.empiriolabs.ai/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.empiriolabs.ai/support
- group: company
  title: ''
  type: Blog
  url: https://empiriolabs.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EmpirioLabs-AI
- group: commercial
  title: ''
  type: Pricing
  url: https://empiriolabs.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://empiriolabs.ai/policy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://empiriolabs.ai/policy/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://platform.empiriolabs.ai/auth/sign-up
created: '2026-10-28'
description: EmpirioLabs AI is a specialized AI inference and integration provider. It hosts open-source models on GPU infrastructure it manages, runs optimized endpoints for proprietary models, helps teams ship their own models to large audiences, and offers on-demand GPU Cloud instances and hosted AI agents.
image: https://media.empiriolabs.ai/assets/empirio-og-logo.png
json_schemas:
- name: ChatRequest
  property_count: 2
  slug: empiriolabs-ai-chat-request
- name: ChatResponse
  property_count: 5
  slug: empiriolabs-ai-chat-response
- name: CompletionRequest
  property_count: 2
  slug: empiriolabs-ai-completion-request
- name: CompletionResponse
  property_count: 5
  slug: empiriolabs-ai-completion-response
- name: ModelDetail
  property_count: 5
  slug: empiriolabs-ai-model-detail
- name: Models_listModels_Response_200
  property_count: 1
  slug: empiriolabs-ai-models-list-models-response-200
jsonld:
- class_count: 7
  name: Empiriolabs Ai Context
  property_count: 14
  slug: empiriolabs-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.empiriolabs.ai.
  name: EmpirioLabs AI MCP Server
  slug: empiriolabs-ai-mcp-yml
modified: '2026-10-28'
name: EmpirioLabs AI
nav: Providers
network: true
overview: 'EmpirioLabs AI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat Completions API, Completions API, Gemini API, and 3 more. Tagged areas include Company, AI, Inference, Cloud, and Platform.


  The EmpirioLabs AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EmpirioLabs AI''s developer surface includes API reference, CLI, changelog, authentication, sandbox, documentation, getting-started guide, and 35 more developer resources.'
plans:
- name: Empiriolabs Ai Plans Pricing
  plan_count: 3
  slug: empiriolabs-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 8
  name: Empiriolabs Ai Rate Limits
  slug: empiriolabs-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: EmpirioLabs AI API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: empiriolabs-ai-rules
scopes:
- name: Empiriolabs Ai Scopes
  scope_count: 0
  slug: empiriolabs-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 56.5
    developer_ergonomics: 85.0
    discoverability: 66.7
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Empiriolabs Ai Authentication
  slug: empiriolabs-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Empiriolabs Ai Domain Security
  slug: empiriolabs-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: chat-completion
  slug: empiriolabs-ai-chat-completion
- name: list-models
  slug: empiriolabs-ai-models-list
slug: empiriolabs-ai
tags:
- Company
- AI
- Inference
- Cloud
- Platform
website: https://empiriolabs.ai
---
