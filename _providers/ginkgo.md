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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Async, job-polling REST API for running inference on public and Ginkgo-proprietary biological foundation models — protein/DNA masked language modeling and mean-embedding generation. Authenticated with
  name: Ginkgo AI Model API
  slug: ginkgo-ai-model-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ginkgobioworks.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ginkgobioworks.github.io/ginkgo-ai-client/
- group: docs
  title: ''
  type: Documentation
  url: https://ginkgobioworks.github.io/ginkgo-ai-client/
- group: docs
  title: ''
  type: APIReference
  url: https://ginkgobioworks.github.io/ginkgo-ai-client/api_reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://ginkgobioworks.github.io/ginkgo-ai-client/
- group: start
  title: ''
  type: SignUp
  url: https://models.ginkgobioworks.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ginkgobioworks
- group: build
  title: ''
  type: Packages
  url: packages/ginkgo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ginkgo-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ginkgo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ginkgo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ginkgo-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ginkgo-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ginkgo-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ginkgo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ginkgo-llms.txt
created: '2026-07-17'
description: 'Ginkgo Bioworks is a synthetic biology company operating autonomous labs and a horizontal platform for engineering biology. Its public developer surface is the Ginkgo AI Model API (api.ginkgobioworks.ai), which runs inference on public and Ginkgo-proprietary biological foundation models — protein and DNA masked language models and embedding models such as ESM2 (650M/3B), ginkgo-aa0-650M, and ginkgo-maskedlm-3utr-v1. The API is an async, job-polling REST service: callers POST a transform request, receive a job result URL, and poll until the job completes. Authentication is via an x-api-key header, credits and keys are issued from the models portal, and an official Python client (ginkgo-ai-client) is published to PyPI. Ginkgo was surfaced as a Felicis portfolio company and enriched into the API Evangelist network.'
image: https://www.ginkgobioworks.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ginkgo-mcp.yml
  slug: ginkgo-mcpyml
modified: '2026-07-19'
name: Ginkgo Bioworks
nav: Providers
network: true
overview: 'Ginkgo Bioworks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Artificial Intelligence, and Machine Learning.


  Ginkgo Bioworks'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 11 more developer resources.'
random_paper: 72
score:
  band: emerging
  composite: 22.9
  delta: -1.9
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.8
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ginkgo/refs/heads/main/screenshots/ginkgo-2026-07-25T215827.png
security:
- kind: authentication
  name: Ginkgo Authentication
  slug: ginkgo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ginkgo Domain Security
  slug: ginkgo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ginkgo
tags:
- Company
- Synthetic Biology
- Biotechnology
- Artificial Intelligence
- Machine Learning
- Protein Models
- Bioinformatics
- Inference API
website: https://www.ginkgobioworks.com
---
