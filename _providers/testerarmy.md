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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://tester.army/api/v1
  baseurl_source: declared
  description: The Groups API from Testerarmy — 5 operation(s) for groups.
  name: Testerarmy Groups API
  slug: testerarmy-groups-api
- baseURL: https://tester.army/api/v1
  baseurl_source: declared
  description: The Projects API from Testerarmy — 13 operation(s) for projects.
  name: Testerarmy Projects API
  slug: testerarmy-projects-api
- baseURL: https://tester.army/api/v1
  baseurl_source: declared
  description: The Test Runs API from Testerarmy — 5 operation(s) for test runs.
  name: Testerarmy Test Runs API
  slug: testerarmy-test-runs-api
- baseURL: https://tester.army/api/v1
  baseurl_source: declared
  description: The Tests API from Testerarmy — 3 operation(s) for tests.
  name: Testerarmy Tests API
  slug: testerarmy-tests-api
- baseURL: https://tester.army/api/v1
  baseurl_source: declared
  description: The Webhooks API from Testerarmy — 2 operation(s) for webhooks.
  name: Testerarmy Webhooks API
  slug: testerarmy-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Testerarmy Webhooks
  slug: testerarmy-webhooks
collections:
- collection_type: open
  name: TestArmy Groups API
  slug: open-testerarmy-groups-api
- collection_type: open
  name: TestArmy Groups Projects API
  slug: open-testerarmy-projects-api
- collection_type: open
  name: TestArmy Groups Test Runs API
  slug: open-testerarmy-test-runs-api
- collection_type: open
  name: TestArmy Groups Tests API
  slug: open-testerarmy-tests-api
- collection_type: open
  name: TestArmy Groups Webhooks API
  slug: open-testerarmy-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/testerarmy/plans/testerarmy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/testerarmy-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://tester.army/blog/feed.xml
- group: other
  href: https://artifacts.apis.io/testerarmy/capabilities/testerarmy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/testerarmy-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.tester.army/
- group: other
  href: https://artifacts.apis.io/testerarmy/overlays/testerarmy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/testerarmy-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/testerarmy/security/testerarmy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/testerarmy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/testerarmy/authentication/testerarmy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/testerarmy-authentication.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/errors/testerarmy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/testerarmy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/lifecycle/testerarmy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/testerarmy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/conventions/testerarmy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/testerarmy-conventions.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/conformance/testerarmy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/testerarmy-conformance.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/data-model/testerarmy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/testerarmy-data-model.yml
- group: agent
  href: https://artifacts.apis.io/testerarmy/mcp/testerarmy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/testerarmy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/testerarmy/well-known/testerarmy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/testerarmy-well-known.yml
- group: build
  href: https://artifacts.apis.io/testerarmy/packages/testerarmy-packages.yml
  title: ''
  type: Packages
  url: packages/testerarmy-packages.yml
- group: build
  href: https://artifacts.apis.io/testerarmy/packages/testerarmy-packages.yml
  title: ''
  type: SDKs
  url: packages/testerarmy-packages.yml
- group: build
  href: https://artifacts.apis.io/testerarmy/cli/testerarmy-cli.yml
  title: ''
  type: CLI
  url: cli/testerarmy-cli.yml
- group: start
  href: https://artifacts.apis.io/testerarmy/sandbox/testerarmy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/testerarmy-sandbox.yml
- group: design
  href: https://artifacts.apis.io/testerarmy/asyncapi/testerarmy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/testerarmy-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/testerarmy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/testerarmy/llms/testerarmy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/testerarmy-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tester.army/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tester.army/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tester.army/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tester.army/get-started/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://tester.army/pricing
- group: company
  title: ''
  type: Blog
  url: https://tester.army/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tester-army
- group: operate
  title: ''
  type: Support
  url: https://tester.army/discord
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tester.army/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tester.army/privacy
created: '2026-07-17'
description: TesterArmy is an AI-powered QA testing platform (Y Combinator, batch P26) whose browser and mobile agents test web and mobile apps like a real user - navigating pages, filling forms, handling login, OAuth and OTP flows, and catching broken flows, rendering bugs and confusing UX. You describe tests in plain English and the agent runs them in the TesterArmy cloud (or locally), on every GitHub pull request or on a schedule, returning screenshots, recordings and actionable bug reports. It exposes a public REST API (bearer API-key auth), a first-party CLI (testerarmy / ta), inbound trigger webhooks, and mobile app upload and testing.
finops:
- has_sources: true
  method: derived
  name: Testerarmy Finops
  primary_unit: subscription
  service_category: ''
  slug: testerarmy-finops
  template: false
image: https://tester.army/logo.png
layout: provider
mcp_servers:
- description: Official hosted MCP server for TesterArmy documentation (Claude Code, Cursor, etc.). It serves docs/search; it is not a wrapper of the REST API.
  name: Testerarmy MCP Server
  slug: testerarmy-docs
modified: '2026-10-06'
name: Testerarmy
nav: Providers
network: true
overview: 'Testerarmy publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Groups API, Projects API, Test Runs API, and 2 more. Tagged areas include Company, QA, Software Testing, Browser Automation, and AI Agents.


  The Testerarmy catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Testerarmy''s developer surface includes authentication, CLI, sandbox, documentation, API reference, getting-started guide, pricing, and 24 more developer resources.'
plans:
- name: Testerarmy Plans Pricing
  plan_count: 4
  slug: testerarmy-plans-pricing
- name: Testerarmy Price Estimates
  plan_count: 0
  slug: testerarmy-price-estimates
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Testerarmy API Rules
  rule_count: 64
  severity_counts:
    error: 53
    hint: 0
    info: 5
    warn: 6
  slug: testerarmy-rules
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 85.0
    discoverability: 71.7
    operational_transparency: 10.5
  previous_composite: 57.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/testerarmy/testerarmy-2026-08-17T082329.png
security:
- kind: authentication
  name: Testerarmy Authentication
  slug: testerarmy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Testerarmy Domain Security
  slug: testerarmy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: testerarmy-cli
  slug: testerarmy-cli
- name: testerarmy-create-and-run-test
  slug: testerarmy-create-and-run-test
- name: testerarmy-pull-request-run
  slug: testerarmy-pull-request-run
slug: testerarmy
tags:
- Company
- QA
- Software Testing
- Browser Automation
- AI Agents
- Developer Tools
- CI/CD
- End-to-End Testing
- Mobile Testing
website: https://www.tester.army/
---
