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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'Hosted, remote Model Context Protocol server (streamable HTTP, bearer kep_ PAT auth) at https://api.keploy.io/client/v1/mcp. Probed live 2026-09-03: anonymous tools/list returns 7 gateway tools (searc'
  name: Keploy MCP Server
  slug: keploy-mcp-server
- description: Self-hosted REST API of the Keploy Kubernetes Proxy, an in-cluster control plane (Helm chart k8s-proxy) that drives eBPF/sidecar recording, auto-replay, deduplication, schema generation, and reports f
  name: Keploy Kubernetes Proxy REST API
  slug: keploy-kubernetes-proxy-rest-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The API Keys API from Keploy — 2 operation(s) for api keys.
  name: Keploy API Keys API
  slug: keploy-api-keys-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Apps API from Keploy — 3 operation(s) for apps.
  name: Keploy Apps API
  slug: keploy-apps-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Branches API from Keploy — 2 operation(s) for branches.
  name: Keploy Branches API
  slug: keploy-branches-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Clusters API from Keploy — 2 operation(s) for clusters.
  name: Keploy Clusters API
  slug: keploy-clusters-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Company API from Keploy — 2 operation(s) for company.
  name: Keploy Company API
  slug: keploy-company-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Generation History API from Keploy — 2 operation(s) for generation history.
  name: Keploy Generation History API
  slug: keploy-generation-history-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Jobs API from Keploy — 5 operation(s) for jobs.
  name: Keploy Jobs API
  slug: keploy-jobs-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Load Tests API from Keploy — 4 operation(s) for load tests.
  name: Keploy Load Tests API
  slug: keploy-load-tests-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Recordings API from Keploy — 11 operation(s) for recordings.
  name: Keploy Recordings API
  slug: keploy-recordings-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The SmartSet API from Keploy — 4 operation(s) for smartset.
  name: Keploy Smart Set API
  slug: keploy-smartset-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Test Reports API from Keploy — 5 operation(s) for test reports.
  name: Keploy Test Reports API
  slug: keploy-test-reports-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Test Runs API from Keploy — 6 operation(s) for test runs.
  name: Keploy Test Runs API
  slug: keploy-test-runs-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Test Suites API from Keploy — 6 operation(s) for test suites.
  name: Keploy Test Suites API
  slug: keploy-test-suites-api
- baseURL: https://api.keploy.io/client/v1
  baseurl_source: declared
  description: The Users API from Keploy — 1 operation(s) for users.
  name: Keploy Users API
  slug: keploy-users-api
artifact_total: 22
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/overlays/keploy-cloud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keploy-cloud-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.keploy.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/security/keploy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keploy-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://keploy.io/blog/sitemap.xml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/packages/keploy-packages.yml
  title: ''
  type: Packages
  url: packages/keploy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/packages/keploy-packages.yml
  title: ''
  type: SDKs
  url: packages/keploy-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/llms/keploy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keploy-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/conformance/keploy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keploy-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/conformance/keploy-conformance.yml
  title: ''
  type: Compliance
  url: conformance/keploy-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/lifecycle/keploy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keploy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/changelog/keploy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/keploy-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/cli/keploy-cli.yml
  title: ''
  type: CLI
  url: cli/keploy-cli.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/plans/keploy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keploy-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/keploy/refs/heads/main/skills/_index.yml
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
overview: 'Keploy publishes 14 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Branches API, and 11 more. Tagged areas include Testing & QA, API Testing, Integration/Regression Testing, Unit Test Generation, and Contract Testing.


  Keploy''s developer surface includes engineering blog, changelog, CLI, pricing, signup flow, documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Keploy Plans Pricing
  plan_count: 3
  slug: keploy-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Keploy Rate Limits
  slug: keploy-rate-limits
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 39.5
  previous_composite: 57.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 22.2
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
website: https://www.keploy.io/
---
