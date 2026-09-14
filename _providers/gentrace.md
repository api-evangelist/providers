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
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Gentrace Agentic Access
  operation_count: 16
  slug: gentrace-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://gentrace.ai/api
  baseurl_source: declared
  description: The Datasets API from Gentrace — 2 operation(s) for datasets.
  name: Gentrace Datasets API
  slug: gentrace-datasets-api
- baseURL: https://gentrace.ai/api
  baseurl_source: declared
  description: The Experiments API from Gentrace — 2 operation(s) for experiments.
  name: Gentrace Experiments API
  slug: gentrace-experiments-api
- baseURL: https://gentrace.ai/api
  baseurl_source: declared
  description: The Pipelines API from Gentrace — 2 operation(s) for pipelines.
  name: Gentrace Pipelines API
  slug: gentrace-pipelines-api
- baseURL: https://gentrace.ai/api
  baseurl_source: declared
  description: The TestCases API from Gentrace — 2 operation(s) for testcases.
  name: Gentrace TestCases API
  slug: gentrace-testcases-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gentrace Datasets API
  slug: open-gentrace-datasets-api
- collection_type: open
  name: Gentrace Datasets Experiments API
  slug: open-gentrace-experiments-api
- collection_type: open
  name: Gentrace Datasets Pipelines API
  slug: open-gentrace-pipelines-api
- collection_type: open
  name: Gentrace Datasets TestCases API
  slug: open-gentrace-testcases-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gentrace-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gentrace-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gentrace-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gentrace.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gentrace.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gentrace.ai/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gentrace
- group: build
  title: ''
  type: Packages
  url: packages/gentrace-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gentrace-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gentrace-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gentrace-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gentrace-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gentrace-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/gentrace-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gentrace-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gentrace-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gentrace-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gentrace was a developer platform for evaluating and testing LLM and AI applications ("evals as infrastructure"). It provided pipelines, datasets, experiments, and test cases so teams could run offline and online evaluations, grade model outputs, track regressions, and observe AI features in production via OpenTelemetry-based instrumentation. The platform shipped a REST API (v4) secured with bearer API keys, first-party Python and TypeScript/Node SDKs, and a documented object model of pipelines, datasets, experiments, and test cases. Gentrace was based in San Francisco and backed by Matrix Partners. The company has since shut down its hosted product, but its OpenAPI specification, SDK packages, and documentation mirror remain publicly available.
image: https://mintcdn.com/gentrace/9dIPysEl4JbHm2X9/logo/dark.svg
layout: provider
modified: '2026-07-19'
name: Gentrace
nav: Providers
network: true
overview: 'Gentrace publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Experiments API, Pipelines API, and 1 more. Tagged areas include Company, Artificial Intelligence, LLM, Evaluation, and Testing.


  Gentrace''s developer surface includes authentication, documentation, API reference, and 15 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/gentrace/refs/heads/main/screenshots/gentrace-2026-07-25T215644.png
security:
- kind: authentication
  name: Gentrace Authentication
  slug: gentrace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gentrace Domain Security
  slug: gentrace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gentrace
tags:
- Company
- Artificial Intelligence
- LLM
- Evaluation
- Testing
- Observability
- Machine-Learning
- Developer Tools
website: https://gentrace.ai
---
