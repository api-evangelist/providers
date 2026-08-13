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
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Rigetti Computing Agentic Access
  operation_count: 52
  slug: rigetti-computing-agentic-access
  summary_line: 52 operations · 17 acting · 3 human-in-the-loop
api_count: 9
apis:
- description: The account API from Rigetti Computing — 22 operation(s) for account.
  name: Rigetti Computing account API
  slug: rigetti-computing-account-api
- description: The authentication API from Rigetti Computing — 4 operation(s) for authentication.
  name: Rigetti Computing authentication API
  slug: rigetti-computing-authentication-api
- description: Check for the latest SDK versions.
  name: Rigetti Computing clientApplications API
  slug: rigetti-computing-clientapplications-api
- description: The Endpoint is the means of access to a Quantum Processor.
  name: Rigetti Computing endpoints API
  slug: rigetti-computing-endpoints-api
- description: The Engagement is the authorization mechanism for access to the Quantum Processor.
  name: Rigetti Computing engagements API
  slug: rigetti-computing-engagements-api
- description: The Healthcheck API from Rigetti Computing — 1 operation(s) for healthcheck.
  name: Rigetti Computing Healthcheck API
  slug: rigetti-computing-healthcheck-api
- description: The Quantum Processor is the heart of the Rigetti services.
  name: Rigetti Computing quantumProcessors API
  slug: rigetti-computing-quantumprocessors-api
- description: Find existing time on a Rigetti QPU and reserve it.
  name: Rigetti Computing reservations API
  slug: rigetti-computing-reservations-api
- description: The Rigetti QCS API API from Rigetti Computing — 2 operation(s) for rigetti qcs api.
  name: Rigetti Computing Rigetti QCS API API
  slug: rigetti-computing-rigetti-qcs-api-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rigetti-computing-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rigetti-computing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rigetti-computing-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/rigetti-computing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rigetti-computing-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rigetti-computing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rigetti-computing-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rigetti-computing-qcs-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rigetti-computing-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rigetti-computing-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rigetti-computing-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rigetti-computing-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rigetti-computing-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rigetti-computing-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.rigetti.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qcs.rigetti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rigetti.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rigetti.com/qcs
- group: start
  title: ''
  type: GettingStarted
  url: https://pyquil-docs.rigetti.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rigetti
- group: operate
  title: ''
  type: Support
  url: https://rigetti.zendesk.com
- group: company
  title: ''
  type: Blog
  url: https://www.rigetti.com/rigetti-computing-news
- group: start
  title: ''
  type: SignUp
  url: https://www.rigetti.com/get-quantum
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rigetti.com/uploads/Global/Rigetti-Terms-of-Service-2022.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rigetti.com/privacy-policy
created: '2026-07-17'
description: Rigetti Computing is a full-stack quantum computing company that builds superconducting quantum processors and delivers access to them through Quantum Cloud Services (QCS). Developers program Rigetti quantum processing units (QPUs) with the Quil quantum instruction language via the open-source pyQuil SDK, compile with quilc, and simulate locally with the Quantum Virtual Machine (QVM). The QCS HTTP API (api.qcs.rigetti.com) exposes REST-style operations for quantum processors, instruction set architectures, engagements, endpoints, reservations, groups, billing, and account management, secured with OAuth2 (Okta) JWT bearer tokens. This profile was seeded as a VC-portfolio lead and enriched by the API Evangelist pipeline from Rigetti's public QCS OpenAPI, SDKs, and developer documentation.
image: https://qcs.rigetti.com/static/img/rigetti-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: rigetti-computing-mcp.yml
  slug: rigetti-computing-mcpyml
modified: '2026-07-21'
name: Rigetti Computing
nav: Providers
network: true
overview: 'Rigetti Computing publishes 9 APIs on the [APIs.io](https://apis.io/) network, including account API, authentication API, clientApplications API, and 6 more. Tagged areas include Company, Quantum Computing, Quantum Cloud, Developer Tools, and SDKs.


  Rigetti Computing''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 107
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.6
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.5
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
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Rigetti Computing Authentication
  slug: rigetti-computing-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rigetti Computing Domain Security
  slug: rigetti-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rigetti-computing
tags:
- Company
- Quantum Computing
- Quantum Cloud
- Developer Tools
- SDKs
- Superconducting Qubits
- Scientific Computing
- Deep Tech
website: https://www.rigetti.com/
---
