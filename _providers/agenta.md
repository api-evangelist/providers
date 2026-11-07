---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Agenta Agentic Access
  operation_count: 25
  slug: agenta-agentic-access
  summary_line: 25 operations · 9 acting
api_count: 2
apis:
- baseURL: https://cloud.agenta.ai/api
  baseurl_source: declared
  description: Create and manage LLM applications and their variants.
  name: Agenta Applications API
  slug: agenta-applications-api
- baseURL: https://cloud.agenta.ai/api
  baseurl_source: declared
  description: Run evaluations of variants against testsets.
  name: Agenta Evaluations API
  slug: agenta-evaluations-api
- baseURL: https://cloud.agenta.ai/api
  baseurl_source: declared
  description: Configure evaluators used to score variants.
  name: Agenta Evaluators API
  slug: agenta-evaluators-api
- baseURL: https://cloud.agenta.ai/api
  baseurl_source: declared
  description: Query observability traces and spans.
  name: Agenta Traces API
  slug: agenta-traces-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Authentication discovery, organization access checks, and SSO callback endpoints.
  name: Agenta Access API
  slug: agenta-access-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Internal administration endpoints — restricted to platform operators.
  name: Agenta Admin API
  slug: agenta-admin-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Attach evaluator-style feedback to existing traces and spans.
  name: Agenta Annotations API
  slug: agenta-annotations-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Subscription, plan, and usage endpoints for workspace billing.
  name: Agenta Billing API
  slug: agenta-billing-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Chat platform channels — connections, agents, spaces, grants, and the inbound event log.
  name: Agenta Channels API
  slug: agenta-channels-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Deprecated endpoints kept for backwards compatibility — avoid in new integrations.
  name: Agenta Deprecated API
  slug: agenta-deprecated-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Deployment environments (e.g. production, staging) and their active variants.
  name: Agenta Environments API
  slug: agenta-environments-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: The Events API from Agenta — 1 operation(s) for events.
  name: Agenta Events API
  slug: agenta-events-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Organize applications and other resources into folder hierarchies.
  name: Agenta Folders API
  slug: agenta-folders-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: The Gateway API from Agenta — 1 operation(s) for gateway.
  name: Agenta Gateway API
  slug: agenta-gateway-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: 'The Gateway: LLM API from Agenta — 4 operation(s) for gateway: llm.'
  name: 'Agenta Gateway: LLM API'
  slug: agenta-gateway-llm-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: 'The Gateway: MCP API from Agenta — 8 operation(s) for gateway: mcp.'
  name: 'Agenta Gateway: MCP API'
  slug: agenta-gateway-mcp-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Run an application against a payload and capture the resulting trace.
  name: Agenta Invocations API
  slug: agenta-invocations-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Create and revoke API keys used to authenticate programmatic requests.
  name: Agenta Keys API
  slug: agenta-keys-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Stable legacy endpoints retained for existing integrations — not deprecated, but new integrations should prefer the canonical surface.
  name: Agenta Legacy API
  slug: agenta-legacy-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Durable object-store mounts for agent working directories.
  name: Agenta Mounts API
  slug: agenta-mounts-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Manage organizations, workspaces, SSO domains, and identity providers.
  name: Agenta Organizations API
  slug: agenta-organizations-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Manage projects within a workspace.
  name: Agenta Projects API
  slug: agenta-projects-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Saved query definitions used to filter and retrieve trace data.
  name: Agenta Queries API
  slug: agenta-queries-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Manage provider credentials and secret values stored in the vault.
  name: Agenta Secrets API
  slug: agenta-secrets-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Agent sessions — runner coordination (invoke/cancel/steer/attach/detach/heartbeat/liveness), state persistence (durable SDK state and sandbox resume pointer), records, and streams.
  name: Agenta Sessions API
  slug: agenta-sessions-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: The Skills API from Agenta — 11 operation(s) for skills.
  name: Agenta Skills API
  slug: agenta-skills-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: API server liveness and readiness status.
  name: Agenta Status API
  slug: agenta-status-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: External tool connections and OAuth integrations available to applications.
  name: Agenta Tools API
  slug: agenta-tools-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Inbound provider event triggers and their watchable event catalog.
  name: Agenta Triggers API
  slug: agenta-triggers-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: User profile and account management — view profile, update username, reset password.
  name: Agenta Users API
  slug: agenta-users-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: The Wallets API from Agenta — 2 operation(s) for wallets.
  name: Agenta Wallets API
  slug: agenta-wallets-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Register and manage webhooks that fire on platform events.
  name: Agenta Webhooks API
  slug: agenta-webhooks-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Workflow definitions — the runnable pipelines that back an application.
  name: Agenta Workflows API
  slug: agenta-workflows-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Manage workspaces within an organization and their members.
  name: Agenta Workspaces API
  slug: agenta-workspaces-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: OTLP-compatible endpoints for ingesting traces directly from OpenTelemetry-instrumented services.
  name: Agenta Open Telemetry API
  slug: agenta-open-telemetry-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Individual test cases within a testset.
  name: Agenta Test Cases API
  slug: agenta-test-cases-api
- baseURL: https://eu.cloud.agenta.ai/api
  baseurl_source: declared
  description: Test datasets — collections of input/output pairs used in evaluations.
  name: Agenta Test Sets API
  slug: agenta-test-sets-api
artifact_total: 52
collections:
- collection_type: open
  name: Agenta Applications API
  slug: open-agenta-applications-api
- collection_type: open
  name: Agenta Applications Configs API
  slug: open-agenta-configs-api
- collection_type: open
  name: Agenta Applications Evaluations API
  slug: open-agenta-evaluations-api
- collection_type: open
  name: Agenta Applications Evaluators API
  slug: open-agenta-evaluators-api
- collection_type: open
  name: Agenta Applications OpenTelemetry API
  slug: open-agenta-opentelemetry-api
- collection_type: open
  name: Agenta Applications Testsets API
  slug: open-agenta-testsets-api
- collection_type: open
  name: Agenta Applications Traces API
  slug: open-agenta-traces-api
- collection_type: open
  name: Agenta API
  slug: open-agenta
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://agenta.ai/pricing
- group: other
  href: https://artifacts.apis.io/agenta/capabilities/agenta-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agenta-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/agenta/agentic-access/agenta-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenta-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/agenta/security/agenta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenta-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/agenta/authentication/agenta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenta-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agenta-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agenta-ai
- group: company
  title: ''
  type: Website
  url: https://agenta.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agenta.ai/
- group: commercial
  href: https://artifacts.apis.io/agenta/plans/agenta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenta-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/agenta/rate-limits/agenta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenta-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agenta/finops/agenta-finops.yml
  title: ''
  type: FinOps
  url: finops/agenta-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://agenta.ai/blog
created: '2026-06-20'
description: Agenta is an open-source LLMOps platform that brings prompt management, LLM evaluation, and LLM observability together in one place. Its cloud REST API at https://cloud.agenta.ai/api exposes apps and variants, versioned prompt configurations, evaluations and evaluators, testsets, and OpenTelemetry-based tracing, all authenticated with a Bearer API key. The platform is MIT licensed and can be self-hosted or used via Agenta Cloud.
finops:
- has_sources: true
  method: generated
  name: Agenta Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: agenta-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agenta.png
layout: provider
modified: '2026-06-20'
name: Agenta
nav: Providers
network: true
overview: 'Agenta publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Evaluations API, Evaluators API, and 34 more. Tagged areas include Artificial Intelligence, LLMOps, Prompt Management, LLM Evaluation, and Observability.


  The Agenta catalog on APIs.io includes 1 Spectral governance ruleset.


  Agenta''s developer surface includes pricing, authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Agenta Plans Pricing
  plan_count: 6
  slug: agenta-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Agenta Rate Limits
  slug: agenta-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Agenta API Rules
  rule_count: 58
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 17
  slug: agenta-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 50.7
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/agenta/agenta-2026-06-20T170004.png
security:
- kind: authentication
  name: Agenta Authentication
  slug: agenta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agenta Domain Security
  slug: agenta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenta
tags:
- Artificial Intelligence
- LLMOps
- Prompt Management
- LLM Evaluation
- Observability
website: https://agenta.ai/
---
