---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Rigetti And Co Agentic Access
  operation_count: 52
  slug: rigetti-and-co-agentic-access
  summary_line: 52 operations · 17 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: The account API from Rigetti & Co — 22 operation(s) for account.
  name: Rigetti & Co account API
  slug: rigetti-and-co-account-api
- description: The authentication API from Rigetti & Co — 4 operation(s) for authentication.
  name: Rigetti & Co authentication API
  slug: rigetti-and-co-authentication-api
- description: Check for the latest SDK versions.
  name: Rigetti & Co clientApplications API
  slug: rigetti-and-co-clientapplications-api
- description: The Endpoint is the means of access to a Quantum Processor.
  name: Rigetti & Co endpoints API
  slug: rigetti-and-co-endpoints-api
- description: The Engagement is the authorization mechanism for access to the Quantum Processor.
  name: Rigetti & Co engagements API
  slug: rigetti-and-co-engagements-api
- description: The Healthcheck API from Rigetti & Co — 1 operation(s) for healthcheck.
  name: Rigetti & Co Healthcheck API
  slug: rigetti-and-co-healthcheck-api
- description: The Quantum Processor is the heart of the Rigetti services.
  name: Rigetti & Co quantumProcessors API
  slug: rigetti-and-co-quantumprocessors-api
- description: Find existing time on a Rigetti QPU and reserve it.
  name: Rigetti & Co reservations API
  slug: rigetti-and-co-reservations-api
- description: The Rigetti QCS API API from Rigetti & Co — 2 operation(s) for rigetti qcs api.
  name: Rigetti & Co Rigetti QCS API API
  slug: rigetti-and-co-rigetti-qcs-api-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rigetti-and-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rigetti-and-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rigetti-and-co-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rigetti-and-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rigetti-and-co-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rigetti-and-co-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rigetti-and-co-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rigetti-and-co-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rigetti-and-co-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/rigetti-and-co-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rigetti-and-co-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rigetti-and-co-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rigetti-and-co-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rigetti-and-co-qcs-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rigetti-and-co-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qcs.rigetti.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rigetti.com/qcs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rigetti.com/qcs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rigetti.com/qcs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://rigetti.zendesk.com
- group: company
  title: ''
  type: Blog
  url: https://www.rigetti.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rigetti
- group: start
  title: ''
  type: SignUp
  url: https://www.rigetti.com/get-quantum
- group: start
  title: ''
  type: Login
  url: https://qcs.rigetti.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rigetti.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rigetti.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rigetti.com/qcs/changelog
- group: company
  title: ''
  type: Website
  url: https://www.rigetti.com
created: '2026-07-17'
description: Rigetti Computing (Rigetti & Co) is a full-stack quantum computing company that builds superconducting quantum processors and delivers access to them through Quantum Cloud Services (QCS). The QCS HTTP API is an OpenAPI 3.0.2 REST/RPC interface (aligned with Google API Improvement Proposals) for discovering quantum processors and their instruction set architectures, reserving execution time, opening execution engagements against endpoints, and managing accounts and billing. Quantum programs are built and run with the pyQuil and qcs-sdk Python/Rust SDKs, while low-latency job execution, readout, and translation run over a companion gRPC surface. Authentication is OAuth2 (Okta) bearer JWT. Surfaced as an a16z portfolio company and enriched by the API Evangelist pipeline from Rigetti's published OpenAPI, gRPC protos, client packages, and QCS documentation.
image: https://docs.rigetti.com/img/rigetti.png
layout: provider
mcp_servers:
- description: ''
  name: rigetti-and-co-mcp.yml
  slug: rigetti-and-co-mcpyml
modified: '2026-07-21'
name: Rigetti & Co
nav: Providers
network: true
overview: 'Rigetti & Co publishes 9 APIs on the [APIs.io](https://apis.io/) network, including account API, authentication API, clientApplications API, and 6 more. Tagged areas include Company, Quantum Computing, Quantum, Infrastructure, and Developers.


  Rigetti & Co''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 91
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Rigetti And Co Authentication
  slug: rigetti-and-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rigetti And Co Domain Security
  slug: rigetti-and-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rigetti-and-co
tags:
- Company
- Quantum Computing
- Quantum
- Infrastructure
- Developers
- Cloud Computing
- QPU
- API
website: https://www.rigetti.com
---
