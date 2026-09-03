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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Rigetti And Co Agentic Access
  operation_count: 52
  slug: rigetti-and-co-agentic-access
  summary_line: 52 operations · 17 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The account API from Rigetti & Co — 22 operation(s) for account.
  name: Rigetti & Co account API
  slug: rigetti-and-co-account-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The authentication API from Rigetti & Co — 4 operation(s) for authentication.
  name: Rigetti & Co authentication API
  slug: rigetti-and-co-authentication-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: Check for the latest SDK versions.
  name: Rigetti & Co clientApplications API
  slug: rigetti-and-co-clientapplications-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Endpoint is the means of access to a Quantum Processor.
  name: Rigetti & Co endpoints API
  slug: rigetti-and-co-endpoints-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Engagement is the authorization mechanism for access to the Quantum Processor.
  name: Rigetti & Co engagements API
  slug: rigetti-and-co-engagements-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Healthcheck API from Rigetti & Co — 1 operation(s) for healthcheck.
  name: Rigetti & Co Healthcheck API
  slug: rigetti-and-co-healthcheck-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Quantum Processor is the heart of the Rigetti services.
  name: Rigetti & Co quantumProcessors API
  slug: rigetti-and-co-quantumprocessors-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: Find existing time on a Rigetti QPU and reserve it.
  name: Rigetti & Co reservations API
  slug: rigetti-and-co-reservations-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Rigetti QCS API API from Rigetti & Co — 2 operation(s) for rigetti qcs api.
  name: Rigetti & Co Rigetti QCS API API
  slug: rigetti-and-co-rigetti-qcs-api-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rigetti QCS account API
  slug: open-rigetti-and-co-account-api
- collection_type: open
  name: Rigetti QCS account authentication API
  slug: open-rigetti-and-co-authentication-api
- collection_type: open
  name: Rigetti QCS account clientApplications API
  slug: open-rigetti-and-co-clientapplications-api
- collection_type: open
  name: Rigetti QCS account endpoints API
  slug: open-rigetti-and-co-endpoints-api
- collection_type: open
  name: Rigetti QCS account engagements API
  slug: open-rigetti-and-co-engagements-api
- collection_type: open
  name: Rigetti QCS account Healthcheck API
  slug: open-rigetti-and-co-healthcheck-api
- collection_type: open
  name: Rigetti QCS account quantumProcessors API
  slug: open-rigetti-and-co-quantumprocessors-api
- collection_type: open
  name: Rigetti QCS account reservations API
  slug: open-rigetti-and-co-reservations-api
- collection_type: open
  name: Rigetti QCS account Rigetti QCS API API
  slug: open-rigetti-and-co-rigetti-qcs-api-api
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
  name: Rigetti & Co MCP Server
  slug: rigetti-co-mcp-server
modified: '2026-07-21'
name: Rigetti & Co
nav: Providers
network: true
overview: 'Rigetti & Co publishes 9 APIs on the [APIs.io](https://apis.io/) network, including account API, authentication API, clientApplications API, and 6 more. Tagged areas include Company, Quantum Computing, Quantum, Infrastructure, and Developers.


  Rigetti & Co''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.0
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.6
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rigetti-and-co/refs/heads/main/screenshots/rigetti-and-co-2026-08-17T081558.png
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
website: https://www.rigetti.com
---
