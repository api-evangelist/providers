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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The GraphQL API the Strangeworks Python SDK is built on. Exposes the workspace a user's API key belongs to, the compute backends available to it, and mutations for uploading workspace files, initiatin
  name: Strangeworks SDK GraphQL API
  slug: sdk
- description: The full Strangeworks platform GraphQL API covering user accounts, workspaces and members, invitations, billing accounts, credits and transactions, products and the product catalog, resources, jobs, f
  name: Strangeworks Platform GraphQL API
  slug: platform
- description: The product-side GraphQL API used by compute products published on the Strangeworks platform to register and update backends, create and update jobs, upload job files, store resource configuration, an
  name: Strangeworks Products GraphQL API
  slug: products
artifact_total: 9
asyncapis:
- description: ''
  name: Strangeworks Webhooks
  slug: strangeworks-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://strangeworks.com/press
- group: company
  title: ''
  type: Website
  url: https://strangeworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strangeworks.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strangeworks.com/welcome/get-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.strangeworks.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.strangeworks.com/
- group: operate
  title: ''
  type: Support
  url: https://strangeworks.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strangeworks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strangeworks.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strangeworks
- group: operate
  href: https://artifacts.apis.io/strangeworks/changelog/strangeworks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strangeworks-changelog.yml
- group: docs
  href: https://artifacts.apis.io/strangeworks/graphql/strangeworks-sdk.graphql
  title: ''
  type: GraphQL
  url: graphql/strangeworks-sdk.graphql
- group: build
  href: https://artifacts.apis.io/strangeworks/packages/strangeworks-packages.yml
  title: ''
  type: Packages
  url: packages/strangeworks-packages.yml
- group: build
  href: https://artifacts.apis.io/strangeworks/packages/strangeworks-packages.yml
  title: ''
  type: SDKs
  url: packages/strangeworks-packages.yml
- group: agent
  href: https://artifacts.apis.io/strangeworks/llms/strangeworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strangeworks-llms.txt
- group: auth
  href: https://artifacts.apis.io/strangeworks/authentication/strangeworks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strangeworks-authentication.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/conventions/strangeworks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/strangeworks-conventions.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/errors/strangeworks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/strangeworks-problem-types.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/lifecycle/strangeworks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/strangeworks-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/conformance/strangeworks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/strangeworks-conformance.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/data-model/strangeworks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/strangeworks-data-model.yml
- group: design
  href: https://artifacts.apis.io/strangeworks/asyncapi/strangeworks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/strangeworks-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/strangeworks/mcp/strangeworks-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/strangeworks-mcp.yml
- group: build
  href: https://artifacts.apis.io/strangeworks/mcp/strangeworks-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/strangeworks-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/strangeworks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/strangeworks/security/strangeworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strangeworks-domain-security.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://strangeworks.com/robots.txt
created: '2026-08-05'
description: Strangeworks is an Austin, Texas based optimization and quantum computing company founded in 2018 by whurley (William Hurley). It operates a "heterogeneous hybrid compute" platform that gives enterprises and governments managed access to quantum processors, quantum-inspired annealers and classical optimization solvers from a single API and Python SDK, alongside its Compute, Workflows, Decisions and HybridSolver products and an expert services practice. The platform is organized around workspaces, products, resources, jobs and backends, and is programmable through three public GraphQL endpoints (sdk, platform, products) at api.strangeworks.com plus a REST proxy that forwards calls to an activated resource. Compute partners reachable through the platform include IBM Quantum, Amazon Braket, Azure Quantum, IonQ, Rigetti, Quantinuum, QuEra, IQM, AQT, Pasqal, D-Wave, Toshiba, Hitachi, Fujitsu, NEC, Gurobi, JIJ, LightSolver and Quantagonia (acquired 2025).
image: https://strangeworks.com/og-image.png
layout: provider
modified: '2026-10-06'
name: Strangeworks
nav: Providers
network: true
overview: 'Strangeworks is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Optimization, High Performance Computing, and Artificial Intelligence.


  The Strangeworks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Strangeworks'' developer surface includes engineering blog, documentation, getting-started guide, signup flow, support, changelog, authentication, and 20 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 26.3
  previous_composite: 43.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/strangeworks/strangeworks-2026-08-17T082131.png
security:
- kind: authentication
  name: Strangeworks Authentication
  slug: strangeworks-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Strangeworks Domain Security
  slug: strangeworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Discover which Strangeworks compute backends are available and online
  slug: strangeworks-discover-backends
- name: Submit a compute job to a Strangeworks resource and poll it to completion
  slug: strangeworks-submit-and-poll-job
- name: Subscribe to Strangeworks job events instead of polling
  slug: strangeworks-webhook-job-events
slug: strangeworks
tags:
- Company
- Quantum Computing
- Optimization
- High Performance Computing
- Artificial Intelligence
- Developer Platform
- GraphQL
- Compute
- Scientific Computing
- Operations Research
website: https://strangeworks.com/
---
