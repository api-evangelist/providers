---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 71
  human_in_the_loop: 3
  name: Hud Ai Agentic Access
  operation_count: 154
  slug: hud-ai-agentic-access
  summary_line: 154 operations · 71 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The builds API from HUD — 16 operation(s) for builds.
  name: HUD Builds API
  slug: hud-ai-builds-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The byok-credentials API from HUD — 2 operation(s) for byok-credentials.
  name: HUD Byok Credentials API
  slug: hud-ai-byok-credentials-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The checks API from HUD — 4 operation(s) for checks.
  name: HUD Checks API
  slug: hud-ai-checks-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The completions API from HUD — 1 operation(s) for completions.
  name: HUD Completions API
  slug: hud-ai-completions-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The data API from HUD — 7 operation(s) for data.
  name: HUD Data API
  slug: hud-ai-data-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The env-vars API from HUD — 4 operation(s) for env-vars.
  name: HUD Env Vars API
  slug: hud-ai-env-vars-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The imports API from HUD — 7 operation(s) for imports.
  name: HUD Imports API
  slug: hud-ai-imports-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The inference API from HUD — 1 operation(s) for inference.
  name: HUD Inference API
  slug: hud-ai-inference-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The instances API from HUD — 2 operation(s) for instances.
  name: HUD Instances API
  slug: hud-ai-instances-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The jobs API from HUD — 19 operation(s) for jobs.
  name: HUD Jobs API
  slug: hud-ai-jobs-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The limits API from HUD — 3 operation(s) for limits.
  name: HUD Limits API
  slug: hud-ai-limits-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The member-secrets API from HUD — 2 operation(s) for member-secrets.
  name: HUD Member Secrets API
  slug: hud-ai-member-secrets-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The models API from HUD — 10 operation(s) for models.
  name: HUD Models API
  slug: hud-ai-models-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The oauth API from HUD — 1 operation(s) for oauth.
  name: HUD OAuth API
  slug: hud-ai-oauth-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The qa-agents API from HUD — 5 operation(s) for qa-agents.
  name: HUD Qa Agents API
  slug: hud-ai-qa-agents-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The qa API from HUD — 3 operation(s) for qa.
  name: HUD Qa API
  slug: hud-ai-qa-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The registry API from HUD — 4 operation(s) for registry.
  name: HUD Registry API
  slug: hud-ai-registry-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The rollouts API from HUD — 6 operation(s) for rollouts.
  name: HUD Rollouts API
  slug: hud-ai-rollouts-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The storage API from HUD — 3 operation(s) for storage.
  name: HUD Storage API
  slug: hud-ai-storage-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The tasks API from HUD — 9 operation(s) for tasks.
  name: HUD Tasks API
  slug: hud-ai-tasks-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The tasksets API from HUD — 5 operation(s) for tasksets.
  name: HUD Tasksets API
  slug: hud-ai-tasksets-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The teams API from HUD — 5 operation(s) for teams.
  name: HUD Teams API
  slug: hud-ai-teams-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The traces API from HUD — 11 operation(s) for traces.
  name: HUD Traces API
  slug: hud-ai-traces-api
- baseURL: https://api.beta.hud.ai
  baseurl_source: declared
  description: The usage API from HUD — 2 operation(s) for usage.
  name: HUD Usage API
  slug: hud-ai-usage-api
artifact_total: 43
common:
- group: other
  href: https://artifacts.apis.io/hud-ai/capabilities/hud-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hud-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/hud-ai/agentic-access/hud-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hud-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/hud-ai/rate-limits/hud-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hud-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/hud-ai/plans/hud-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hud-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/rules/hud-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/hud-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/json-ld/hud-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hud-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/hud-ai/vocabulary/hud-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hud-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hud-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/data-model/hud-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hud-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/hud-ai/cli/hud-ai-cli.yml
  title: ''
  type: CLI
  url: cli/hud-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/hud-ai/changelog/hud-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hud-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/conventions/hud-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hud-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/conventions/hud-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hud-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/hud-ai/authentication/hud-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hud-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hud-ai/scopes/hud-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hud-ai-scopes.yml
- group: operate
  href: https://artifacts.apis.io/hud-ai/lifecycle/hud-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hud-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/lifecycle/hud-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hud-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/errors/hud-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/hud-ai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/errors/hud-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hud-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hud-ai/conformance/hud-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hud-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/hud-ai/overlays/hud-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hud-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/hud-ai/llms/hud-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hud-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/hud-ai/a2a/hud-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hud-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/hud-ai/mcp/hud-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hud-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hud-ai/mcp/hud-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hud-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hud-ai/well-known/hud-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hud-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/hud-ai/hosts/hud-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hud-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/hud-ai/vendors/hud-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hud-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/hud-ai/packages/hud-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/hud-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/hud-ai/packages/hud-ai-packages.yml
  title: ''
  type: Packages
  url: packages/hud-ai-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.beta.hud.ai`
- group: auth
  href: https://artifacts.apis.io/hud-ai/security/hud-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hud-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hud.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hud.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hud.ai/platform/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hud.ai/platform/quickstart
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.hud.ai/llms.txt
- group: build
  title: ''
  type: CLI
  url: https://docs.hud.ai/v6/reference/cli
- group: company
  title: ''
  type: Blog
  url: https://www.hud.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hud-evals
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/wkjtmHYYjm
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hud.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hud.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hud.ai/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hud-evals/
- group: other
  title: ''
  type: X
  url: https://x.com/hud_evals
created: '2026-10-27'
description: HUD (Human Union Data, Inc.) is a platform for building reinforcement-learning environments, tasks and benchmarks used to train and evaluate AI agents and models. Teams create environments with the open-source hud Python SDK and CLI or import Harbor tasks, run evaluations across frontier models, inspect traces, run automated QA agents that detect grader mistakes and reward hacking, train models on their own environments, and can list task data on DataVendor. The platform is exposed through a REST API at api.beta.hud.ai (routes under /v2, team API-key authentication).
image: https://github.com/hud-evals.png
json_schemas:
- name: BuildRegisterResponse
  property_count: 25
  slug: hud-ai-build-register-response
- name: BuildResponse
  property_count: 24
  slug: hud-ai-build-response
- name: ModelResponse
  property_count: 26
  slug: hud-ai-model-response
- name: RegistryDetailResponse
  property_count: 31
  slug: hud-ai-registry-detail-response
- name: TraceAnalysisContextResponse
  property_count: 23
  slug: hud-ai-trace-analysis-context-response
- name: TraceInfoResponse
  property_count: 37
  slug: hud-ai-trace-info-response
jsonld:
- class_count: 120
  name: Hud Ai Context
  property_count: 315
  slug: hud-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.beta.hud.ai over streamable HTTP requiring an API key; 8 tools listed.
  name: HUD Platform MCP
  slug: hud-platform
modified: '2026-10-27'
name: HUD
nav: Providers
network: true
overview: 'HUD publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Builds API, Byok Credentials API, Checks API, and 21 more. Tagged areas include Company, Artificial Intelligence, Reinforcement Learning, AI Evaluation, and AI Agents.


  The HUD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HUD''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 39 more developer resources.'
plans:
- name: Hud Ai Plans Pricing
  plan_count: 3
  slug: hud-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Hud Ai Rate Limits
  slug: hud-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: HUD API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: hud-ai-rules
scopes:
- name: Hud Ai Scopes
  scope_count: 5
  slug: hud-ai-scopes
  summary_line: 5 scopes
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hud Ai Authentication
  slug: hud-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Hud Ai Domain Security
  slug: hud-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: hud-ai-diagnose-eval-run
  slug: hud-ai-diagnose-eval-run
- name: hud-ai-explore-catalog
  slug: hud-ai-explore-catalog
- name: hud-environment-builder
  slug: hud-ai-hud-environment-builder
- name: hud-ai-run-qa-checks
  slug: hud-ai-run-qa-checks
slug: hud-ai
tags:
- Company
- Artificial Intelligence
- Reinforcement Learning
- AI Evaluation
- AI Agents
- Benchmarks
- Machine Learning
- Training Data
website: https://www.hud.ai/
---
