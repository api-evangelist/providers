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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Freeplay Agentic Access
  operation_count: 29
  slug: freeplay-agentic-access
  summary_line: 29 operations · 12 acting
api_count: 1
apis:
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: List agents within a project.
  name: Freeplay Agents API
  slug: freeplay-agents-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Create, version, retrieve, and deploy prompt templates.
  name: Freeplay Prompt Templates API
  slug: freeplay-prompt-templates-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Create, list, and retrieve batch test runs.
  name: Freeplay Test Runs API
  slug: freeplay-test-runs-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Agent Datasets API from Freeplay — 5 operation(s) for agent datasets.
  name: Freeplay Agent Datasets API
  slug: freeplay-agent-datasets-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Configuration API from Freeplay — 9 operation(s) for configuration.
  name: Freeplay Configuration API
  slug: freeplay-configuration-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Evaluation Criteria API from Freeplay — 17 operation(s) for evaluation criteria.
  name: Freeplay Evaluation Criteria API
  slug: freeplay-evaluation-criteria-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Insights API from Freeplay — 1 operation(s) for insights.
  name: Freeplay Insights API
  slug: freeplay-insights-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Models API from Freeplay — 2 operation(s) for models.
  name: Freeplay Models API
  slug: freeplay-models-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Observability API from Freeplay — 9 operation(s) for observability.
  name: Freeplay Observability API
  slug: freeplay-observability-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Prompt Datasets API from Freeplay — 9 operation(s) for prompt datasets.
  name: Freeplay Prompt Datasets API
  slug: freeplay-prompt-datasets-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Prompt Optimization API from Freeplay — 3 operation(s) for prompt optimization.
  name: Freeplay Prompt Optimization API
  slug: freeplay-prompt-optimization-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Review Queues API from Freeplay — 1 operation(s) for review queues.
  name: Freeplay Review Queues API
  slug: freeplay-review-queues-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Saved Searches API from Freeplay — 2 operation(s) for saved searches.
  name: Freeplay Saved Searches API
  slug: freeplay-saved-searches-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Search & Analytics API from Freeplay — 6 operation(s) for search & analytics.
  name: Freeplay Search & Analytics API
  slug: freeplay-search-analytics-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: The Tags API from Freeplay — 1 operation(s) for tags.
  name: Freeplay Tags API
  slug: freeplay-tags-api
artifact_total: 35
collections:
- collection_type: open
  name: Freeplay HTTP Agents API
  slug: open-freeplay-agents-api
- collection_type: open
  name: Freeplay HTTP Agents Completions API
  slug: open-freeplay-completions-api
- collection_type: open
  name: Freeplay HTTP Agents Datasets API
  slug: open-freeplay-datasets-api
- collection_type: open
  name: Freeplay HTTP Agents Feedback API
  slug: open-freeplay-feedback-api
- collection_type: open
  name: Freeplay HTTP Agents Projects API
  slug: open-freeplay-projects-api
- collection_type: open
  name: Freeplay HTTP Agents Prompt Templates API
  slug: open-freeplay-prompt-templates-api
- collection_type: open
  name: Freeplay HTTP Agents Search API
  slug: open-freeplay-search-api
- collection_type: open
  name: Freeplay HTTP Agents Sessions API
  slug: open-freeplay-sessions-api
- collection_type: open
  name: Freeplay HTTP Agents Test Runs API
  slug: open-freeplay-test-runs-api
- collection_type: open
  name: Freeplay HTTP Agents Traces API
  slug: open-freeplay-traces-api
- collection_type: open
  name: Freeplay HTTP API
  slug: open-freeplay
common:
- group: other
  href: https://artifacts.apis.io/freeplay/capabilities/freeplay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/freeplay-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/freeplay/agentic-access/freeplay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freeplay-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/freeplay/security/freeplay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/freeplay-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/freeplay/security/freeplay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freeplay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/freeplay/authentication/freeplay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/freeplay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freeplayai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freeplay-ai
- group: company
  title: ''
  type: Website
  url: https://freeplay.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freeplay.ai/
- group: commercial
  href: https://artifacts.apis.io/freeplay/plans/freeplay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/freeplay-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/freeplay/rate-limits/freeplay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/freeplay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/freeplay/finops/freeplay-finops.yml
  title: ''
  type: FinOps
  url: finops/freeplay-finops.yml
created: '2026-06-20'
description: Freeplay is an LLM product experimentation, evaluation, and observability platform for cross-functional teams. Its HTTP API and SDKs make Freeplay the source of truth for prompt templates, record completions and sessions/traces from production, curate test datasets, run batch test runs and LLM-judge evaluations, and capture human and customer feedback.
finops:
- has_sources: true
  method: generated
  name: Freeplay Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: freeplay-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freeplay.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.freeplay.ai over HTTP; 3 tools listed.
  name: Freeplay MCP Server
  slug: freeplay
modified: '2026-06-20'
name: Freeplay
nav: Providers
network: true
overview: 'Freeplay publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Prompt Templates API, Test Runs API, and 12 more. Tagged areas include Artificial Intelligence, LLM, Evaluation, Observability, and Prompt Management.


  The Freeplay catalog on APIs.io includes 1 Spectral governance ruleset.


  Freeplay''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Freeplay Plans Pricing
  plan_count: 3
  slug: freeplay-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Freeplay Rate Limits
  slug: freeplay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Freeplay API Rules
  rule_count: 47
  severity_counts:
    error: 35
    hint: 0
    info: 2
    warn: 10
  slug: freeplay-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 49.6
    developer_ergonomics: 29.8
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 42.3
      derived: 0
      marker_coverage: 57.7
      total: 26
    mcp: first-party
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
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/freeplay/freeplay-2026-06-20T181534.png
security:
- kind: authentication
  name: Freeplay Authentication
  slug: freeplay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freeplay Domain Security
  slug: freeplay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Freeplay Trust Center
  slug: freeplay-trust-center
  summary_line: SOC 2, ISO 27001
slug: freeplay
tags:
- Artificial Intelligence
- LLM
- Evaluation
- Observability
- Prompt Management
- Experimentation
website: https://freeplay.ai/
---
