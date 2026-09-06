---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: REST API for Keploy Cloud (base https://api.keploy.io/client/v1) providing AI test-suite generation and execution, app/test-suite management, recordings/mocks, test and load-test reports, schema cover
  name: Keploy Cloud API
  slug: keploy-cloud-api
- description: 'Hosted, remote Model Context Protocol server (streamable HTTP, bearer kep_ PAT auth) at https://api.keploy.io/client/v1/mcp. Probed live 2026-09-03: anonymous tools/list returns 7 gateway tools (searc'
  name: Keploy MCP Server
  slug: keploy-mcp-server
- description: Self-hosted REST API of the Keploy Kubernetes Proxy, an in-cluster control plane (Helm chart k8s-proxy) that drives eBPF/sidecar recording, auto-replay, deduplication, schema generation, and reports f
  name: Keploy Kubernetes Proxy REST API
  slug: keploy-kubernetes-proxy-rest-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keploy-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://keploy.io/blog/sitemap.xml
- group: build
  title: ''
  type: Packages
  url: packages/keploy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keploy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keploy-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/keploy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/keploy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keploy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/keploy-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/keploy-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/keploy-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://keploy.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keploy
- group: start
  title: ''
  type: SignUp
  url: https://app.keploy.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keploy.io/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://keploy.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://keploy.io/docs/server/installation/
created: '2026-07-03'
description: Open-source, AI-native testing platform that captures real production API traffic with eBPF and replays it in CI as deterministic tests, auto-generated mocks, and production-like sandboxes with zero code changes. Publishes a first-party OpenAPI 3.0.3 for its Cloud REST API, a hosted MCP server with a 112-tool catalog, llms.txt, and a Kubernetes Proxy REST API for in-cluster recording and replay.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keploy.png
layout: provider
mcp_servers:
- description: ''
  name: Keploy MCP Server
  slug: keploy-mcp-server
- description: ''
  name: Keploy MCP Server
  slug: keploy-mcp-server-2
modified: '2026-09-03'
name: Keploy
nav: Providers
network: true
overview: 'Keploy publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud API. Tagged areas include Testing & QA, API Testing, Integration/Regression Testing, Unit Test Generation, and Contract Testing.


  Keploy''s developer surface includes engineering blog, changelog, CLI, pricing, signup flow, documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Keploy Plans Pricing
  plan_count: 3
  slug: keploy-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Keploy Rate Limits
  slug: keploy-rate-limits
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 61.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 58.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/screenshots/keploy-2026-07-25T223630.png
security:
- kind: authentication
  name: Keploy Authentication
  slug: keploy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keploy Domain Security
  slug: keploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keploy
tags:
- Testing & QA
- API Testing
- Integration/Regression Testing
- Unit Test Generation
- Contract Testing
- CI/CD
- Developer Tools
- AI / Agent Tooling
- eBPF / Observability
- Test Data & Mocking
---
