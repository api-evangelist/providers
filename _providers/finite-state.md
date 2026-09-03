---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    agent_card: conformant
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: Token-authenticated REST API for the Finite State platform, served under /api/public/v0 on the platform host. Interactive Swagger documentation is published per organization at https://[org].finitesta
  name: Finite State Platform API
  slug: platform-api
- description: 'Public, anonymous, read-only JSON-RPC 2.0 API exposing Finite State''s published content: blog posts, resources, videos, events, podcasts and press articles. Four allowlisted methods (content.list, con'
  name: Finite State A2A Content API
  slug: a2a-content-api
- description: 'GraphQL API historically documented at https://platform.finitestate.io/api/v1/graphql and still the transport used by the official Python SDK, which authenticates via a client-credentials exchange at '
  name: Finite State GraphQL API
  slug: graphql-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/finite-state-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/FiniteStateInc/finite-state-sdk-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/FiniteStateInc/finite-state-sdk-python/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/FiniteStateInc/finite-state-sdk-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/FiniteStateInc/finite-state-sdk-python/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://finitestate.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.finitestate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finitestate.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finitestate.io/docs/dev-tools/finite-state-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.finitestate.io/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://finitestate.io/support
- group: company
  title: ''
  type: Blog
  url: https://finitestate.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://finitestate.io/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FiniteStateInc
- group: commercial
  title: ''
  type: Pricing
  url: https://finitestate.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://finitestate.io/request-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finitestate.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finitestate.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.finitestate.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.finitestate.io/changelog
- group: other
  title: ''
  type: AgentCard
  url: a2a/finite-state-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finite-state-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finite-state-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/finite-state-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/finite-state-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/finite-state-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finite-state-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finite-state-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finite-state-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finite-state-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finite-state-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/finite-state-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finite-state-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finite-state-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: Finite State is a product security platform for connected-device and embedded software manufacturers. It performs binary and firmware composition analysis, source-code scanning and third-party scan ingestion, SBOM generation and lifecycle management (CycloneDX and SPDX), VEX, EPSS- and reachability-based vulnerability prioritization, license-policy enforcement, and evidence-backed compliance reporting for regimes such as the EU Cyber Resilience Act, FDA 524B, ISO 21434 and IEC 62443. Programmatic access is offered through a token-authenticated REST API on the platform host, a legacy GraphQL API with an official Python SDK, the fs-cli command-line tool, and CI/CD integrations for GitHub Actions, Jenkins and Azure DevOps. Finite State also publishes an anonymous, read-only A2A JSON-RPC content API described by an agent card at its canonical well-known path.
image: https://finitestate.io/images/backgrounds/hero-space.jpg
layout: provider
modified: '2026-08-04'
name: Finite State
nav: Providers
network: true
overview: 'Finite State publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Product Security, Software Supply Chain Security, SBOM, Firmware Analysis, and Vulnerability Management.


  Finite State''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 50.0
  previous_composite: 36.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finite-state/refs/heads/main/screenshots/finite-state-2026-08-07T165305.png
security:
- kind: authentication
  name: Finite State Authentication
  slug: finite-state-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Finite State Domain Security
  slug: finite-state-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finite-state
tags:
- Product Security
- Software Supply Chain Security
- SBOM
- Firmware Analysis
- Vulnerability Management
- Binary Analysis
- Connected Devices
- Compliance
- Cybersecurity
- IoT
website: https://finitestate.io
---
