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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-04'
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
  description: The Testcases API from Scorecard — 2 operation(s) for testcases.
  name: Scorecard Testcases API
  slug: scorecard-testcases-api
- baseURL: https://api2.scorecard.io/api/v2
  baseurl_source: declared
  description: The Testsets API from Scorecard — 2 operation(s) for testsets.
  name: Scorecard Testsets API
  slug: scorecard-testsets-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: Overlay
  url: overlays/scorecard-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/scorecard-trust-center.yml
- group: auth
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
  title: ''
  type: MCPServer
  url: mcp/scorecard-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/scorecard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scorecard-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scorecard-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/scorecard-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scorecard-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scorecard-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scorecard-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scorecard-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scorecard-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scorecard-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Scorecard is a simulation and evaluation platform for building, testing, and deploying frontier AI agents. Teams run their agents through thousands of realistic scenarios, judge outputs with configurable AI, human, and heuristic metrics, and ship new capabilities with confidence. The platform organizes work into Projects, Testsets, Testcases, Metrics, Runs, Records, Scores, and Systems, and exposes a REST API (bearer API keys prefixed ak_) plus official Python, TypeScript/Node, and Go SDKs, a hosted MCP server, tracing integrations for LangChain, the Vercel AI SDK, and the Claude Agent SDK, and a GitHub Actions integration for evals in CI. Scorecard was founded to solve AI agent evaluation at scale and is backed by Kindred Ventures.
image: https://cdn.prod.website-files.com/68012f5eeeda4ace0fca1c46/680be2472e0c42225eb5c6fb_bb737b32df1d17f3492808c99d78bb0b_scorecard-open-graph.jpg
layout: provider
mcp_servers:
- description: ''
  name: Scorecard MCP Server
  slug: scorecard-mcp-server
modified: '2026-07-21'
name: Scorecard
nav: Providers
network: true
overview: 'Scorecard publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Metrics API, Projects API, Records API, and 4 more. Tagged areas include Company, Artificial Intelligence, Agents, Evaluation, and Testing.


  Scorecard''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 49.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scorecard/refs/heads/main/screenshots/scorecard-2026-08-17T081735.png
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
