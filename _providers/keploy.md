---
access_model:
  confidence: high
  label: Freemium (free Playground tier) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - pricing-page
  trial: true
  try_now: true
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
