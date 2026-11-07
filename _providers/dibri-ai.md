---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://dibri.ai/api/v1
  baseurl_source: declared
  description: 'Dibri REST API: POST /api/v1/agent/query sends one question with an agent bearer token and returns an answer built only from the vault''s approved documents, with sources, a 0-100 confidence score, or '
  name: Dibri API
  slug: dibri-ai-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/dibri-ai/rate-limits/dibri-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dibri-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dibri-ai/plans/dibri-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dibri-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/rules/dibri-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dibri-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/json-ld/dibri-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dibri-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/dibri-ai/vocabulary/dibri-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dibri-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dibri-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/data-model/dibri-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dibri-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/components/dibri-ai-components.yml
  title: ''
  type: Components
  url: components/dibri-ai-components.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/conventions/dibri-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dibri-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dibri-ai/authentication/dibri-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dibri-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/lifecycle/dibri-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dibri-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/errors/dibri-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dibri-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dibri-ai/conformance/dibri-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dibri-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/dibri-ai/overlays/dibri-ai-dibri-ai-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dibri-ai-dibri-ai-openapi-generated-overlay.yaml
- group: build
  href: https://artifacts.apis.io/dibri-ai/mcp/dibri-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dibri-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dibri-ai/mcp/dibri-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dibri-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/dibri-ai/hosts/dibri-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dibri-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/dibri-ai/integrations/dibri-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dibri-ai-integration-edges.yml
- group: auth
  href: https://artifacts.apis.io/dibri-ai/security/dibri-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dibri-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dibri.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dibri.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://dibri.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://dibri.ai/developers#rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://dibri.ai/developers#quickstart
- group: docs
  title: ''
  type: Guide
  url: https://dibri.ai/guide
- group: commercial
  title: ''
  type: Pricing
  url: https://dibri.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://dibri.ai/contact-sales
- group: start
  title: ''
  type: SignUp
  url: https://dibri.ai/register
- group: start
  title: ''
  type: Login
  url: https://dibri.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dibri.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dibri.ai/privacy
created: '2026-11-05'
description: 'Dibri (styled DIBRI), operated by Exhort Technologies LLC, a Wisconsin limited liability company, offers verified knowledge for AI agents: a source of truth an AI support agent checks before it answers. Answers are built only from documents the organization approved, returned with sources and a 0-100 confidence score, or as a clear refusal the agent can hand to a human. It is delivered through a REST API (POST /api/v1/agent/query with an agent bearer token) and an MCP server, plus a website widget, hosted agent pages and a team app, with 100 free answers a month.'
json_schemas:
- name: PostApiV1AgentQueryRequest
  property_count: 1
  slug: dibri-ai-post-api-v1-agent-query-request
jsonld:
- class_count: 1
  name: Dibri Ai Context
  property_count: 1
  slug: dibri-ai-context
layout: provider
mcp_servers:
- description: Dibri's official remote MCP server (Streamable HTTP) at https://dibri.ai/mcp. With an agent token it offers one tool, `ask`, which returns an answer built only from the vault's approved documents, wit
  name: Dibri MCP server
  slug: dibri-mcp-server
modified: '2026-11-05'
name: Dibri
nav: Providers
network: true
overview: 'Dibri is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Knowledge Base, and RAG.


  The Dibri catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dibri''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, signup flow, and 24 more developer resources.'
plans:
- name: Dibri Ai Plans Pricing
  plan_count: 5
  slug: dibri-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Dibri Ai Rate Limits
  slug: dibri-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Dibri API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: dibri-ai-rules
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 75.2
    catalog_earned_first_party: 24.0
    catalog_gap: 39.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 56.5
    discoverability: 61.7
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dibri Ai Authentication
  slug: dibri-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dibri Ai Domain Security
  slug: dibri-ai-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: dibri-ai-ask-a-verified-question
  slug: dibri-ai-ask-a-verified-question
- name: dibri-ai-review-knowledge-gaps
  slug: dibri-ai-review-knowledge-gaps
slug: dibri-ai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Knowledge Base
- RAG
- Customer Service
- MCP
- REST API
website: https://dibri.ai/
---
