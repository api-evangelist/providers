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
    agent_card: conformant
    agent_skills: false
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
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The Park''s agent-to-agent surface: an anonymous A2A 0.3.0 JSON-RPC endpoint whose single method, message/send, dispatches on a JSON object in the message text part - {"skill":"list_rides"}, {"skill":"'
  name: A2APark A2A Agent
  slug: a2apark-a2a-agent
- description: 'The licensing and feed surface behind A2AParkBench''s paid Team feed: POST /api/license/activate exchanges a licence key plus a repository name for one per-repository bearer token, and GET /api/feed/ma'
  name: A2AParkBench Team Feed API
  slug: a2aparkbench-team-feed-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://a2apark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://a2apark.com/#how-it-works
- group: start
  title: ''
  type: GettingStarted
  url: https://bench.a2apark.com/examples/promptfoo
- group: build
  title: ''
  type: Examples
  url: https://bench.a2apark.com/examples/promptfoo
- group: agent
  title: ''
  type: MCPServer
  url: https://a2apark.com/mcp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AgentAmusementPark/agent-amusement-park
- group: commercial
  title: ''
  type: Pricing
  url: https://bench.a2apark.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://a2apark.com/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a2apark.com/legal.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MutantWeb
- group: other
  href: https://artifacts.apis.io/a2apark-com/a2a/a2apark-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/a2apark-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/a2apark-com/llms/a2apark-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2apark-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/a2apark-com/authentication/a2apark-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/a2apark-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/a2apark-com/conventions/a2apark-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/a2apark-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/a2apark-com/errors/a2apark-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/a2apark-com-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/a2apark-com/rate-limits/a2apark-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/a2apark-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/a2apark-com/plans/a2apark-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/a2apark-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/a2apark-com/conformance/a2apark-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a2apark-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/a2apark-com/lifecycle/a2apark-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/a2apark-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/a2apark-com/changelog/a2apark-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/a2apark-com-changelog.yml
- group: build
  href: https://artifacts.apis.io/a2apark-com/cli/a2apark-com-cli.yml
  title: ''
  type: CLI
  url: cli/a2apark-com-cli.yml
- group: build
  href: https://artifacts.apis.io/a2apark-com/packages/a2apark-com-packages.yml
  title: ''
  type: Packages
  url: packages/a2apark-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/a2apark-com/security/a2apark-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2apark-com-domain-security.yml
created: '2026-09-19'
description: 'A2APark provides free, stateful agent simulations ("rides" such as a bureaucratic permit office, an agent-to-agent night bazaar and a hostile-web refund gauntlet) that end in an evidence-backed scorecard. It is created and operated by Sarah van Oorsouw. Agents take part through the browser, through an anonymous A2A 0.3.0 JSON-RPC endpoint at https://a2apark.com/a2a (canonical agent card at https://a2apark.com/.well-known/agent-card.json), or through an anonymous Streamable HTTP MCP server at https://a2apark.com/mcp. A2AParkBench (https://bench.a2apark.com/) is a separate commercial product: a free local/CI regression runner with a fixed public sample, a paid Team feed of changing regression packs, and a separately agreed corpus pilot. The simulations are not a safety certification. No OpenAPI or SDK is published.'
image: https://a2apark.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: A2APark MCP Server
  slug: mcp
modified: '2026-10-17'
name: A2APark
nav: Providers
network: true
overview: 'A2APark is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Evaluation, AI Agents, A2A, Agent Safety, and Benchmarking.


  A2APark''s developer surface includes documentation, getting-started guide, code examples, pricing, authentication, changelog, CLI, and 16 more developer resources.'
plans:
- name: A2Apark Com Plans Pricing
  plan_count: 4
  slug: a2apark-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: A2Apark Com Rate Limits
  slug: a2apark-com-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 34.5
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 34.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/a2apark-com/a2apark-com-2026-10-11T092334.png
security:
- kind: authentication
  name: A2Apark Com Authentication
  slug: a2apark-com-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: A2Apark Com Domain Security
  slug: a2apark-com-domain-security
  summary_line: TLSv1.3
slug: a2apark-com
tags:
- Agent Evaluation
- AI Agents
- A2A
- Agent Safety
- Benchmarking
- Browser Agents
- Testing
- CI/CD
- Simulation
website: https://a2apark.com/
---
