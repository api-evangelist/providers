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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Scorecard Agentic Access
  operation_count: 35
  slug: scorecard-agentic-access
  summary_line: 35 operations · 20 acting
api_count: 1
apis:
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Metrics API from Scorecard — 1 operation(s) for metrics.
  name: Scorecard Metrics API
  slug: scorecard-metrics-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Projects API from Scorecard — 5 operation(s) for projects.
  name: Scorecard Projects API
  slug: scorecard-projects-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Records API from Scorecard — 5 operation(s) for records.
  name: Scorecard Records API
  slug: scorecard-records-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Runs API from Scorecard — 2 operation(s) for runs.
  name: Scorecard Runs API
  slug: scorecard-runs-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Systems API from Scorecard — 3 operation(s) for systems.
  name: Scorecard Systems API
  slug: scorecard-systems-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Test Cases API from Scorecard — 2 operation(s) for test cases.
  name: Scorecard Test Cases API
  slug: scorecard-test-cases-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Test Sets API from Scorecard — 2 operation(s) for test sets.
  name: Scorecard Test Sets API
  slug: scorecard-test-sets-api
artifact_total: 25
collections:
- collection_type: open
  name: Scorecard Metrics API
  slug: open-scorecard-metrics-api
- collection_type: open
  name: Scorecard Metrics Projects API
  slug: open-scorecard-projects-api
- collection_type: open
  name: Scorecard Metrics Records API
  slug: open-scorecard-records-api
- collection_type: open
  name: Scorecard Metrics Runs API
  slug: open-scorecard-runs-api
- collection_type: open
  name: Scorecard Metrics Systems API
  slug: open-scorecard-systems-api
- collection_type: open
  name: Scorecard Metrics Testcases API
  slug: open-scorecard-testcases-api
- collection_type: open
  name: Scorecard Metrics Testsets API
  slug: open-scorecard-testsets-api
common:
- group: commercial
  href: https://artifacts.apis.io/scorecard/plans/scorecard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scorecard-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/scorecard/capabilities/scorecard-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scorecard-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/scorecard/overlays/scorecard-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scorecard-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/scorecard/security/scorecard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scorecard-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scorecard/security/scorecard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scorecard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scorecard.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scorecard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scorecard.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scorecard.io/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scorecard.io/intro/sdk-quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.scorecard.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.scorecard.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getscorecard.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scorecard.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scorecard.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scorecard-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scorecard.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.scorecard.io/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://trust.scorecard.io/
- group: agent
  href: https://artifacts.apis.io/scorecard/mcp/scorecard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scorecard-mcp.yml
- group: build
  href: https://artifacts.apis.io/scorecard/packages/scorecard-packages.yml
  title: ''
  type: Packages
  url: packages/scorecard-packages.yml
- group: build
  href: https://artifacts.apis.io/scorecard/packages/scorecard-packages.yml
  title: ''
  type: SDKs
  url: packages/scorecard-packages.yml
- group: agent
  href: https://artifacts.apis.io/scorecard/llms/scorecard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scorecard-llms.txt
- group: auth
  href: https://artifacts.apis.io/scorecard/authentication/scorecard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scorecard-authentication.yml
- group: design
  href: https://artifacts.apis.io/scorecard/conventions/scorecard-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scorecard-conventions.yml
- group: design
  href: https://artifacts.apis.io/scorecard/errors/scorecard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scorecard-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scorecard/lifecycle/scorecard-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scorecard-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scorecard/conformance/scorecard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scorecard-conformance.yml
- group: design
  href: https://artifacts.apis.io/scorecard/data-model/scorecard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scorecard-data-model.yml
- group: agent
  href: https://artifacts.apis.io/scorecard/agentic-access/scorecard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scorecard-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/scorecard/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Scorecard is a simulation and evaluation platform for building, testing, and deploying frontier AI agents. Teams run their agents through thousands of realistic scenarios, judge outputs with configurable AI, human, and heuristic metrics, and ship new capabilities with confidence. The platform organizes work into Projects, Testsets, Testcases, Metrics, Runs, Records, Scores, and Systems, and exposes a REST API (bearer API keys prefixed ak_) plus official Python, TypeScript/Node, and Go SDKs, a hosted MCP server, tracing integrations for LangChain, the Vercel AI SDK, and the Claude Agent SDK, and a GitHub Actions integration for evals in CI. Scorecard was founded to solve AI agent evaluation at scale and is backed by Kindred Ventures.
finops:
- has_sources: true
  method: derived
  name: Scorecard Finops
  primary_unit: subscription
  service_category: ''
  slug: scorecard-finops
  template: false
image: https://cdn.prod.website-files.com/68012f5eeeda4ace0fca1c46/680be2472e0c42225eb5c6fb_bb737b32df1d17f3492808c99d78bb0b_scorecard-open-graph.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.scorecard.io over HTTP.
  name: Scorecard MCP Server
  slug: scorecard-ai
modified: '2026-07-21'
name: Scorecard
nav: Providers
network: true
overview: 'Scorecard publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Metrics API, Projects API, Records API, and 4 more. Tagged areas include Company, Artificial Intelligence, Agents, Evaluation, and Testing.


  The Scorecard catalog on APIs.io includes 1 Spectral governance ruleset.


  Scorecard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Scorecard Plans Pricing
  plan_count: 3
  slug: scorecard-plans-pricing
- name: Scorecard Price Estimates
  plan_count: 0
  slug: scorecard-price-estimates
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Scorecard API Rules
  rule_count: 61
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 10
  slug: scorecard-rules
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 61.3
    discoverability: 75.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/scorecard/scorecard-2026-08-17T081735.png
security:
- kind: authentication
  name: Scorecard Authentication
  slug: scorecard-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scorecard Domain Security
  slug: scorecard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scorecard Trust Center
  slug: scorecard-trust-center
  summary_line: SOC 2
skill_count: 2
skills:
- name: Build a Scorecard evaluation testset
  slug: scorecard-build-testset
- name: Run a Scorecard evaluation and record scores
  slug: scorecard-run-and-score
slug: scorecard
tags:
- Company
- Artificial Intelligence
- Agents
- Evaluation
- Testing
- LLM
- Observability
- Simulation
- Developer Tools
- MCP
website: https://www.scorecard.io/
---
