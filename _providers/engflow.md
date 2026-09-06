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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The EngFlow cluster gRPC / Protocol Buffers API surface — cluster info, IAM (roles/policies/users/groups), authentication, event store and result store build-event streaming, secret management, and no
  name: EngFlow Cluster API (gRPC)
  slug: engflow-cluster-api-grpc
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/EngFlow/engflowapis/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/EngFlow/engflowapis/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/EngFlow/engflowapis/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.engflow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.engflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.engflow.com
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/EngFlow/engflowapis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.engflow.com/re/index.html
- group: company
  title: ''
  type: Blog
  url: https://blog.engflow.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EngFlow
- group: commercial
  title: ''
  type: Pricing
  url: https://www.engflow.com/product/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.engflow.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.engflow.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engflow.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engflow.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/EngFlow/engflowapis
- group: build
  title: ''
  type: Packages
  url: packages/engflow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/engflow-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/engflow-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/engflow-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/engflow-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.engflow.com
- group: design
  title: ''
  type: Conventions
  url: conventions/engflow-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/engflow-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/engflow-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/engflow-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/engflow-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/engflow-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: EngFlow provides remote build execution, remote caching, CI runners, and a Build & Test UI that accelerate large-scale software builds for Bazel, BuildStream, Goma, Pants, Soong, CMake, and Buck2. EngFlow clusters expose a gRPC / Protocol Buffers API surface — the open Remote Execution API (REAPI v2) and Remote Asset API, plus EngFlow's own cluster, IAM, authentication, event store, result store, secret, notification, and resource-usage services, all published as Protocol Buffer interface definitions in the EngFlow/engflowapis repository. Clusters authenticate via mTLS, cluster-issued JWT bearer tokens, OIDC federation, SAML, GitHub tokens, and basic auth, and provision users over SCIM 2.0. EngFlow was founded by former Google/Bazel engineers and is backed by a16z.
image: https://avatars.githubusercontent.com/u/61729484?v=4
layout: provider
modified: '2026-07-19'
name: EngFlow
nav: Providers
network: true
overview: 'EngFlow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remote Execution, Remote Caching, Build Systems, and Bazel.


  EngFlow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 42.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/engflow/refs/heads/main/screenshots/engflow-2026-07-25T213344.png
security:
- kind: authentication
  name: Engflow Authentication
  slug: engflow-authentication
  summary_line: mutualTLS/http-bearer/oauth2/openIdConnect/saml/http-basic/scim · 7 schemes
- kind: domain-security
  name: Engflow Domain Security
  slug: engflow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: engflow
tags:
- Company
- Remote Execution
- Remote Caching
- Build Systems
- Bazel
- CI/CD
- Developer Tools
- gRPC
- Protocol Buffers
- DevOps
- Continuous Integration
website: https://www.engflow.com
---
