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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 3
  name: Rigetti And Co Agentic Access
  operation_count: 52
  slug: rigetti-and-co-agentic-access
  summary_line: 52 operations · 16 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The account API from Rigetti & Co — 22 operation(s) for account.
  name: Rigetti & Co Account API
  slug: rigetti-and-co-account-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The authentication API from Rigetti & Co — 4 operation(s) for authentication.
  name: Rigetti & Co Authentication API
  slug: rigetti-and-co-authentication-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: Check for the latest SDK versions.
  name: Rigetti & Co Client Applications API
  slug: rigetti-and-co-clientapplications-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Endpoint is the means of access to a Quantum Processor.
  name: Rigetti & Co Endpoints API
  slug: rigetti-and-co-endpoints-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Engagement is the authorization mechanism for access to the Quantum Processor.
  name: Rigetti & Co Engagements API
  slug: rigetti-and-co-engagements-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Quantum Processor is the heart of the Rigetti services.
  name: Rigetti & Co Quantum Processors API
  slug: rigetti-and-co-quantumprocessors-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: Find existing time on a Rigetti QPU and reserve it.
  name: Rigetti & Co Reservations API
  slug: rigetti-and-co-reservations-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Rigetti QCS API API from Rigetti & Co — 2 operation(s) for rigetti qcs api.
  name: Rigetti & Co Rigetti QCS API
  slug: rigetti-and-co-rigetti-qcs-api-api
- baseURL: https://api.qcs.rigetti.com
  baseurl_source: declared
  description: The Health Check API from Rigetti & Co — 1 operation(s) for health check.
  name: Rigetti & Co Health Check API
  slug: rigetti-and-co-health-check-api
artifact_total: 26
collections:
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
  href: https://artifacts.apis.io/rigetti-and-co/agentic-access/rigetti-and-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rigetti-and-co-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rigetti-and-co/security/rigetti-and-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rigetti-and-co-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rigetti-and-co/authentication/rigetti-and-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rigetti-and-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/rigetti-and-co/conventions/rigetti-and-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rigetti-and-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/rigetti-and-co/errors/rigetti-and-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rigetti-and-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rigetti-and-co/lifecycle/rigetti-and-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rigetti-and-co-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rigetti-and-co/lifecycle/rigetti-and-co-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/rigetti-and-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rigetti-and-co/conformance/rigetti-and-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rigetti-and-co-conformance.yml
- group: design
  href: https://artifacts.apis.io/rigetti-and-co/data-model/rigetti-and-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rigetti-and-co-data-model.yml
- group: build
  href: https://artifacts.apis.io/rigetti-and-co/packages/rigetti-and-co-packages.yml
  title: ''
  type: Packages
  url: packages/rigetti-and-co-packages.yml
- group: build
  href: https://artifacts.apis.io/rigetti-and-co/packages/rigetti-and-co-packages.yml
  title: ''
  type: SDKs
  url: packages/rigetti-and-co-packages.yml
- group: agent
  href: https://artifacts.apis.io/rigetti-and-co/mcp/rigetti-and-co-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rigetti-and-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rigetti-and-co/llms/rigetti-and-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rigetti-and-co-llms.txt
- group: other
  href: https://artifacts.apis.io/rigetti-and-co/overlays/rigetti-and-co-qcs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rigetti-and-co-qcs-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rigetti-and-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rigetti-and-co/well-known/rigetti-and-co-well-known.yml
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
modified: '2026-09-16'
name: Rigetti & Co
nav: Providers
network: true
overview: 'Rigetti & Co publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Client Applications API, and 6 more. Tagged areas include Company, Quantum Computing, Quantum, Infrastructure, and Developers.


  The Rigetti & Co catalog on APIs.io includes 1 Spectral governance ruleset.


  Rigetti & Co''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Rigetti & Co API Rules
  rule_count: 65
  severity_counts:
    error: 46
    hint: 0
    info: 6
    warn: 13
  slug: rigetti-and-co-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 38.5
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
screenshot: https://apis.io/screenshots/rigetti-and-co/rigetti-and-co-2026-08-17T081558.png
security:
- kind: authentication
  name: Rigetti And Co Authentication
  slug: rigetti-and-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rigetti And Co Domain Security
  slug: rigetti-and-co-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Check Rigetti QCS account balance and billing
  slug: rigetti-and-co-account-billing
- name: Open an execution engagement against a Rigetti endpoint
  slug: rigetti-and-co-create-engagement
- name: Discover Rigetti quantum processors and their capabilities
  slug: rigetti-and-co-discover-quantum-processors
- name: Reserve execution time on a Rigetti QPU
  slug: rigetti-and-co-reserve-qpu-time
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
