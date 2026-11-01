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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.sailresearch.com/v1
  baseurl_source: declared
  description: Submit and manage batches of requests.
  name: Sail Research Batches API
  slug: sail-research-batches-api-api
- baseURL: https://api.sailresearch.com/v1
  baseurl_source: declared
  description: OpenAI-compatible Chat Completions API endpoints.
  name: Sail Research Chat Completions API
  slug: sail-research-chat-completions-api-api
- baseURL: https://api.sailresearch.com/v1
  baseurl_source: declared
  description: Anthropic-compatible Messages API endpoints.
  name: Sail Research Messages API
  slug: sail-research-messages-api-api
- baseURL: https://api.sailresearch.com/v1
  baseurl_source: declared
  description: Model discovery endpoints.
  name: Sail Research Models API
  slug: sail-research-models-api-api
- baseURL: https://api.sailresearch.com/v1
  baseurl_source: declared
  description: OpenAI-compatible Responses API endpoints.
  name: Sail Research Responses API
  slug: sail-research-responses-api-api
artifact_total: 20
asyncapis:
- description: ''
  name: Sail Research Webhooks
  slug: sail-research-webhooks
collections:
- collection_type: open
  name: Sail Batches API API
  slug: open-sail-research-batches-api-api
- collection_type: open
  name: Sail Batches API Chat Completions API API
  slug: open-sail-research-chat-completions-api-api
- collection_type: open
  name: Sail Batches API Messages API API
  slug: open-sail-research-messages-api-api
- collection_type: open
  name: Sail Batches API Models API API
  slug: open-sail-research-models-api-api
- collection_type: open
  name: Sail Batches API Responses API API
  slug: open-sail-research-responses-api-api
common:
- group: commercial
  href: https://artifacts.apis.io/sail-research/plans/sail-research-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sail-research-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sail-research/capabilities/sail-research-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sail-research-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.sailresearch.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sailresearch.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sailresearch.com/api-reference/chat-completions-api/create-a-chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sailresearch.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.sailresearch.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sailresearch.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sailresearch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sailresearch.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.sailresearch.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailresearch
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sailresearch.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sailresearch.com
- group: docs
  href: https://artifacts.apis.io/sail-research/openapi/_original/sail-research-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/sail-research-openapi-original.json
- group: auth
  href: https://artifacts.apis.io/sail-research/authentication/sail-research-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sail-research-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sail-research/security/sail-research-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sail-research-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sail-research/llms/sail-research-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sail-research-llms.txt
- group: agent
  href: https://artifacts.apis.io/sail-research/mcp/sail-research-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sail-research-mcp.yml
- group: build
  href: https://artifacts.apis.io/sail-research/packages/sail-research-packages.yml
  title: ''
  type: Packages
  url: packages/sail-research-packages.yml
- group: build
  href: https://artifacts.apis.io/sail-research/packages/sail-research-packages.yml
  title: ''
  type: SDKs
  url: packages/sail-research-packages.yml
- group: build
  href: https://artifacts.apis.io/sail-research/cli/sail-research-cli.yml
  title: ''
  type: CLI
  url: cli/sail-research-cli.yml
- group: design
  href: https://artifacts.apis.io/sail-research/conventions/sail-research-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sail-research-conventions.yml
- group: design
  href: https://artifacts.apis.io/sail-research/conventions/sail-research-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sail-research-conventions.yml
- group: design
  href: https://artifacts.apis.io/sail-research/errors/sail-research-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sail-research-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sail-research/lifecycle/sail-research-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sail-research-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sail-research/conformance/sail-research-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sail-research-conformance.yml
- group: design
  href: https://artifacts.apis.io/sail-research/asyncapi/sail-research-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sail-research-webhooks.yml
- group: design
  href: https://artifacts.apis.io/sail-research/data-model/sail-research-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sail-research-data-model.yml
- group: other
  href: https://artifacts.apis.io/sail-research/overlays/sail-research-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sail-research-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sail-research/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailresearchco
created: '2026-07-17'
description: 'Sail Research provides infrastructure for long-horizon agents: cost-efficient inference for leading open-source models (GLM, DeepSeek, Kimi, Nemotron and others) run on demand. Its API is OpenAI- and Anthropic-compatible (Chat Completions, Responses, Messages, Batches), so existing clients migrate by changing the base URL and key. Completion windows (asap/priority/standard/flex) trade latency for lower per-token price for background and agentic workloads, and Sailboxes provide full persistent VMs for long-running agents. Sail raised $80M and is backed by Kleiner Perkins. This profile was enriched by the API Evangelist pipeline from Sail''s public OpenAPI, docs, SDKs, CLI, and MCP surface.'
finops:
- has_sources: true
  method: derived
  name: Sail Research Finops
  primary_unit: 1m input tokens
  service_category: ''
  slug: sail-research-finops
  template: false
image: https://www.sailresearch.com/og-image.png
layout: provider
mcp_servers:
- description: Sail's hosted documentation MCP server. Connects agents/IDEs to Sail's docs so they can answer questions about models, pricing, completion windows, Sailbox setup and execution, and the platform in gen
  name: Sail Research MCP Server
  slug: sail-docs
modified: '2026-09-16'
name: Sail Research
nav: Providers
network: true
overview: 'Sail Research publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batches API, Chat Completions API, Messages API, and 2 more. Tagged areas include Company, Artificial Intelligence, LLM, Inference, and Agents.


  The Sail Research catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sail Research''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Sail Research Plans Pricing
  plan_count: 7
  slug: sail-research-plans-pricing
- name: Sail Research Price Estimates
  plan_count: 0
  slug: sail-research-price-estimates
random_paper: 19
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 57.7
    developer_ergonomics: 68.5
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 57.6
  provenance:
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
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sail-research/sail-research-2026-08-17T081712.png
security:
- kind: authentication
  name: Sail Research Authentication
  slug: sail-research-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sail Research Domain Security
  slug: sail-research-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 3
skills:
- name: Call Sail with the Anthropic Messages API
  slug: sail-research-anthropic-messages
- name: Run batch inference at scale on Sail
  slug: sail-research-batch-inference
- name: Run a background agent response on Sail
  slug: sail-research-run-background-response
slug: sail-research
tags:
- Company
- Artificial Intelligence
- LLM
- Inference
- Agents
- Machine Learning
- Developer Tools
- Open Source Models
- Infrastructure
website: https://www.sailresearch.com/
---
