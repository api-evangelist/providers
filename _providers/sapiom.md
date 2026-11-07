---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for transaction management, payment authorization, agents, spending rules, analytics, and phone verification. Bearer-token authenticated; JSON envelope with cursor pagination.
  name: Sapiom REST API
  slug: sapiom-rest-api
artifact_total: 9
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sapiom.ai/
- group: commercial
  href: https://artifacts.apis.io/sapiom/plans/sapiom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sapiom-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.sapiom.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sapiom.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sapiom.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sapiom.ai/agents/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.sapiom.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sapiom
- group: start
  title: ''
  type: SignUp
  url: https://app.sapiom.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.sapiom.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.sapiom.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.sapiom.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.sapiom.ai/privacy-policy
- group: agent
  href: https://artifacts.apis.io/sapiom/llms/sapiom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sapiom-llms.txt
- group: agent
  href: https://artifacts.apis.io/sapiom/mcp/sapiom-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sapiom-mcp.yml
- group: build
  href: https://artifacts.apis.io/sapiom/packages/sapiom-packages.yml
  title: ''
  type: Packages
  url: packages/sapiom-packages.yml
- group: build
  href: https://artifacts.apis.io/sapiom/packages/sapiom-packages.yml
  title: ''
  type: SDKs
  url: packages/sapiom-packages.yml
- group: build
  href: https://artifacts.apis.io/sapiom/cli/sapiom-cli.yml
  title: ''
  type: CLI
  url: cli/sapiom-cli.yml
- group: agent
  href: https://artifacts.apis.io/sapiom/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sapiom/well-known/sapiom-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sapiom-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sapiom/authentication/sapiom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sapiom-authentication.yml
- group: design
  href: https://artifacts.apis.io/sapiom/conventions/sapiom-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sapiom-conventions.yml
- group: design
  href: https://artifacts.apis.io/sapiom/errors/sapiom-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sapiom-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/sapiom/rate-limits/sapiom-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sapiom-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sapiom/lifecycle/sapiom-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sapiom-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sapiom/conformance/sapiom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sapiom-conformance.yml
- group: auth
  href: https://artifacts.apis.io/sapiom/security/sapiom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sapiom-domain-security.yml
- group: start
  href: https://artifacts.apis.io/sapiom/sandbox/sapiom-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sapiom-sandbox.yml
- group: design
  href: https://artifacts.apis.io/sapiom/data-model/sapiom-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sapiom-data-model.yml
created: '2026-07-17'
description: 'Sapiom is an execution engine for AI agents that gives agents and code instant, pay-per-use access to a catalog of paid capabilities through a single API key and wallet — no per-vendor accounts. Capabilities include web search and scraping, access to 400+ AI models, image/video generation, audio/text-to-speech, browser automation, compute sandboxes, databases (Postgres/Redis/vector/search), messaging and queues, file storage, private git repositories, GitHub export, email enrichment, domains/DNS, and phone verification. It is reachable three ways: a typed SDK client (@sapiom/tools / ctx.sapiom.*), a hosted remote MCP server (~130 tools), and a REST API (https://api.sapiom.ai/v1) for transaction, agent, spending-rule, and analytics management. Metered access is authorized via an x402 (HTTP 402) payment flow with per-agent spend rules. Sapiom is backed by Accel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapiom.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.sapiom.ai.
  name: Sapiom MCP Server
  slug: sapiom-mcp-yml
modified: '2026-07-21'
name: Sapiom
nav: Providers
network: true
overview: 'Sapiom is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Infrastructure, and MCP.


  Sapiom''s developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 23 more developer resources.'
plans:
- name: Sapiom Plans Pricing
  plan_count: 0
  slug: sapiom-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Sapiom Rate Limits
  slug: sapiom-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 82.1
    discoverability: 75.0
    operational_transparency: 23.7
  previous_composite: 38.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sapiom/sapiom-2026-09-02T154410.png
security:
- kind: authentication
  name: Sapiom Authentication
  slug: sapiom-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sapiom Domain Security
  slug: sapiom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: sapiom-agent-builder
  slug: sapiom-agent-builder
- name: sapiom-deploy
  slug: sapiom-deploy
- name: use-sapiom
  slug: sapiom-use-sapiom
slug: sapiom
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Infrastructure
- MCP
- API Gateway
- Payments
- Agentic Commerce
- Developer Tools
- SDK
website: https://www.sapiom.ai/
---
