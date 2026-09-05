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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 187
  human_in_the_loop: 1
  name: Kubeshop Agentic Access
  operation_count: 371
  slug: kubeshop-agentic-access
  summary_line: 371 operations · 187 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Testkube API operations
  name: Kubeshop api API
  slug: kubeshop-api-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Artifact operations
  name: Kubeshop artifacts API
  slug: kubeshop-artifacts-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The cluster-resources API from Kubeshop — 1 operation(s) for cluster-resources.
  name: Kubeshop cluster-resources API
  slug: kubeshop-cluster-resources-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The Executions API from Kubeshop — 19 operation(s) for executions.
  name: Kubeshop Executions API
  slug: kubeshop-executions-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Executor operations
  name: Kubeshop executor API
  slug: kubeshop-executor-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Keymap for fields in a form
  name: Kubeshop keymap API
  slug: kubeshop-keymap-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Listing all available labels
  name: Kubeshop labels API
  slug: kubeshop-labels-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Log operations
  name: Kubeshop logs API
  slug: kubeshop-logs-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The Organizations API from Kubeshop — 104 operation(s) for organizations.
  name: Kubeshop Organizations API
  slug: kubeshop-organizations-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The repository API from Kubeshop — 1 operation(s) for repository.
  name: Kubeshop repository API
  slug: kubeshop-repository-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The secrets API from Kubeshop — 2 operation(s) for secrets.
  name: Kubeshop secrets API
  slug: kubeshop-secrets-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The Status Pages API from Kubeshop — 2 operation(s) for status pages.
  name: Kubeshop Status Pages API
  slug: kubeshop-status-pages-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The tags API from Kubeshop — 1 operation(s) for tags.
  name: Kubeshop tags API
  slug: kubeshop-tags-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The template API from Kubeshop — 2 operation(s) for template.
  name: Kubeshop template API
  slug: kubeshop-template-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The templates API from Kubeshop — 1 operation(s) for templates.
  name: Kubeshop templates API
  slug: kubeshop-templates-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The test-sources API from Kubeshop — 2 operation(s) for test-sources.
  name: Kubeshop test-sources API
  slug: kubeshop-test-sources-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Test suites orchestration operations
  name: Kubeshop test-suites API
  slug: kubeshop-test-suites-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Test Triggers CRUD operations
  name: Kubeshop test-triggers API
  slug: kubeshop-test-triggers-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The Test Workflows API from Kubeshop — 22 operation(s) for test workflows.
  name: Kubeshop Test Workflows API
  slug: kubeshop-test-workflows-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Tests operations
  name: Kubeshop tests API
  slug: kubeshop-tests-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The Users API from Kubeshop — 2 operation(s) for users.
  name: Kubeshop Users API
  slug: kubeshop-users-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: Webhook operations
  name: Kubeshop webhook API
  slug: kubeshop-webhook-api
- baseURL: https://api.testkube.io
  baseurl_source: declared
  description: The webhook-template API from Kubeshop — 2 operation(s) for webhook-template.
  name: Kubeshop webhook-template API
  slug: kubeshop-webhook-template-api
artifact_total: 61
asyncapis:
- description: ''
  name: Kubeshop Testkube Webhooks
  slug: kubeshop-testkube-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Testkube Standalone Agent api API
  slug: open-kubeshop-api-api
- collection_type: open
  name: Testkube Standalone Agent api artifacts API
  slug: open-kubeshop-artifacts-api
- collection_type: open
  name: Testkube Standalone Agent api cluster-resources API
  slug: open-kubeshop-cluster-resources-api
- collection_type: open
  name: Testkube Standalone Agent api Executions API
  slug: open-kubeshop-executions-api
- collection_type: open
  name: Testkube Standalone Agent api executor API
  slug: open-kubeshop-executor-api
- collection_type: open
  name: Testkube Standalone Agent api keymap API
  slug: open-kubeshop-keymap-api
- collection_type: open
  name: Testkube Standalone Agent api labels API
  slug: open-kubeshop-labels-api
- collection_type: open
  name: Testkube Standalone Agent api logs API
  slug: open-kubeshop-logs-api
- collection_type: open
  name: Testkube Standalone Agent api Organizations API
  slug: open-kubeshop-organizations-api
- collection_type: open
  name: Testkube Standalone Agent api pro API
  slug: open-kubeshop-pro-api
- collection_type: open
  name: Testkube Standalone Agent api repository API
  slug: open-kubeshop-repository-api
- collection_type: open
  name: Testkube Standalone Agent api secrets API
  slug: open-kubeshop-secrets-api
- collection_type: open
  name: Testkube Standalone Agent api Status Pages API
  slug: open-kubeshop-status-pages-api
- collection_type: open
  name: Testkube Standalone Agent api tags API
  slug: open-kubeshop-tags-api
- collection_type: open
  name: Testkube Standalone Agent api template API
  slug: open-kubeshop-template-api
- collection_type: open
  name: Testkube Standalone Agent api templates API
  slug: open-kubeshop-templates-api
- collection_type: open
  name: Testkube Standalone Agent api test-sources API
  slug: open-kubeshop-test-sources-api
- collection_type: open
  name: Testkube Standalone Agent api test-suites API
  slug: open-kubeshop-test-suites-api
- collection_type: open
  name: Testkube Standalone Agent api test-triggers API
  slug: open-kubeshop-test-triggers-api
- collection_type: open
  name: Testkube Standalone Agent api Test Workflow Executions API
  slug: open-kubeshop-test-workflow-executions-api
- collection_type: open
  name: Testkube Standalone Agent api Test Workflow Templates API
  slug: open-kubeshop-test-workflow-templates-api
- collection_type: open
  name: Testkube Standalone Agent api Test Workflow With Executions API
  slug: open-kubeshop-test-workflow-with-executions-api
- collection_type: open
  name: Testkube Standalone Agent api Test Workflows API
  slug: open-kubeshop-test-workflows-api
- collection_type: open
  name: Testkube Standalone Agent api tests API
  slug: open-kubeshop-tests-api
- collection_type: open
  name: Testkube Standalone Agent api Triggers API
  slug: open-kubeshop-triggers-api
- collection_type: open
  name: Testkube Standalone Agent api Users API
  slug: open-kubeshop-users-api
- collection_type: open
  name: Testkube Standalone Agent api webhook API
  slug: open-kubeshop-webhook-api
- collection_type: open
  name: Testkube Standalone Agent api webhook-template API
  slug: open-kubeshop-webhook-template-api
- collection_type: open
  name: Testkube Standalone Agent api Webhook Templates API
  slug: open-kubeshop-webhook-templates-api
- collection_type: open
  name: Testkube Standalone Agent api Webhooks API
  slug: open-kubeshop-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kubeshop-testkube-agent-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kubeshop/testkube/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kubeshop/testkube/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kubeshop/testkube/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kubeshop/testkube/blob/main/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://testkube.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.testkube.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.testkube.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.testkube.io/openapi/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.testkube.io/articles/tutorial/quickstart
- group: operate
  title: ''
  type: Support
  url: https://testkube.io/contact
- group: company
  title: ''
  type: Blog
  url: https://testkube.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubeshop
- group: commercial
  title: ''
  type: Pricing
  url: https://testkube.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://testkube.io/get-started
- group: start
  title: ''
  type: Login
  url: https://app.testkube.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://testkube.io/terms-and-conditions/202602
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://testkube.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://testkube.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.testkube.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kubeshop-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kubeshop-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubeshop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kubeshop-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kubeshop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kubeshop-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kubeshop-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kubeshop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kubeshop-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/kubeshop-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kubeshop-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kubeshop-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kubeshop-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kubeshop-testkube-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubeshop-agentic-access.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/kubeshop-testkube-service.proto
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kubeshop-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kubeshop-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubeshop-domain-security.yml
created: '2026-07-17'
description: Kubeshop is the company behind Testkube, an open-core, Kubernetes-native test orchestration platform. Testkube runs agents inside Kubernetes clusters under a central control plane, orchestrating tests written for existing frameworks — Cypress, Playwright, k6, JMeter, pytest and others — then aggregating executions, logs, artifacts, JUnit reports, flakiness metrics and cross-environment insights for engineering teams. It is configured declaratively through Kubernetes Custom Resource Definitions (TestWorkflow, Webhook, TestTrigger), installed via Helm, and driven by a first-party CLI. Kubeshop publishes three OpenAPI 3.0.1 documents — an open-source API, a standalone agent API and a commercial control-plane API — plus a gRPC service definition and a hosted Model Context Protocol server exposing 30 tools to AI assistants over OAuth 2.1. The company is backed by Insight Partners.
image: https://cdn.prod.website-files.com/61e00b3936e571a4ea7a5a4c/623ca8e3c6062e36c7d5c173_Testkube-symbol.png
layout: provider
mcp_servers:
- description: Testkube's hosted MCP server lets AI assistants list and run test workflows, inspect executions, fetch logs and artifacts, and query results. The endpoint is scoped per organization and environment; o
  name: Kubeshop MCP Server
  slug: kubeshop-mcp-server
modified: '2026-07-19'
name: Kubeshop
nav: Providers
network: true
overview: 'Kubeshop publishes 23 APIs on the [APIs.io](https://apis.io/) network, including api API, artifacts API, cluster-resources API, and 20 more. Tagged areas include Company, Testing, Kubernetes, Continuous Integration, and Developer Tools.


  The Kubeshop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kubeshop''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Kubeshop Rate Limits
  slug: kubeshop-rate-limits
scopes:
- name: Kubeshop Scopes
  scope_count: 1
  slug: kubeshop-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 60.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 40.9
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubeshop/refs/heads/main/screenshots/kubeshop-2026-07-25T224316.png
security:
- kind: authentication
  name: Kubeshop Authentication
  slug: kubeshop-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Kubeshop Domain Security
  slug: kubeshop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kubeshop
tags:
- Company
- Testing
- Kubernetes
- Continuous Integration
- Developer Tools
- Test Automation
- Observability
- DevOps
- Cloud-Native
- Quality Assurance
- Open-Source
- MCP
website: https://testkube.io/
---
