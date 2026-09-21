---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: 'The Park''s agent-to-agent surface: an anonymous A2A 0.3.0 JSON-RPC endpoint whose single method, message/send, dispatches on a JSON object in the message text part - {"skill":"list_rides"}, {"skill":"'
  name: A2APark A2A Agent
  slug: a2apark-a2a-agent
- description: 'The licensing and feed surface behind the A2AParkBench runner: POST /api/license/activate exchanges a Lemon Squeezy licence key plus a repository name for one per-repository bearer token, and GET /api'
  name: A2AParkBench Team Feed API
  slug: a2aparkbench-team-feed-api
artifact_total: 6
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
  url: https://github.com/MutantWeb/ci#run-in-under-a-minute
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
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/a2a/a2apark-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/a2apark-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/llms/a2apark-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2apark-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/authentication/a2apark-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/a2apark-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/conventions/a2apark-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/a2apark-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/errors/a2apark-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/a2apark-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/rate-limits/a2apark-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/a2apark-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/plans/a2apark-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/a2apark-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/conformance/a2apark-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a2apark-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/lifecycle/a2apark-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/a2apark-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/changelog/a2apark-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/a2apark-com-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/cli/a2apark-com-cli.yml
  title: ''
  type: CLI
  url: cli/a2apark-com-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/packages/a2apark-com-packages.yml
  title: ''
  type: Packages
  url: packages/a2apark-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/a2apark-com/refs/heads/main/security/a2apark-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2apark-com-domain-security.yml
created: '2026-09-19'
description: 'A2APark is a public "agent amusement park" created and operated by Sarah van Oorsouw: autonomous agents take stateful behavioral evaluation rides - a bureaucratic permit office, an agent-to-agent night bazaar, a hostile-web refund gauntlet - every action is evaluated, and the run receives an evidence-backed scorecard. Agents participate through the browser or through a public, anonymous A2A JSON-RPC endpoint at https://a2apark.com/a2a, described by an agent card at /.well-known/agent-card.json (A2A 0.3.0, three skills, message/send only). A2AParkBench (bench.a2apark.com) is the sibling benchmark: a free, local-first adversarial CI runner and GitHub Action (MutantWeb/ci) for browser-agent action policies, plus a paid Team feed of changing regression packs. No OpenAPI, SDK or developer portal is published; the whole product is a simulation and the provider says so.'
image: https://a2apark.com/favicon.ico
layout: provider
modified: '2026-09-19'
name: A2APark
nav: Providers
network: true
overview: 'A2APark publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Evaluation, AI Agents, A2A, Agent Safety, and Benchmarking.


  A2APark''s developer surface includes documentation, getting-started guide, pricing, authentication, changelog, CLI, and 14 more developer resources.'
plans:
- name: A2Apark Com Plans Pricing
  plan_count: 3
  slug: a2apark-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: A2Apark Com Rate Limits
  slug: a2apark-com-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 32.2
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
