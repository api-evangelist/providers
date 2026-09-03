---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.ginkgobioworks.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.ginkgo.bio/ — a different registrable domain (ginkgobioworks.com -> ginkgo.bio), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Async, job-polling REST API for running inference on public and Ginkgo-proprietary biological foundation models — protein/DNA masked language modeling and mean-embedding generation. Authenticated with
  name: Ginkgo AI Model API
  slug: ginkgo-ai-model-api
artifact_total: 3
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Ginkgo Bioworks
nav: Providers
network: true
overview: 'Ginkgo Bioworks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Artificial Intelligence, and Machine-Learning.


  Ginkgo Bioworks'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.2
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Machine-Learning
- Protein Models
- Bioinformatics
- Inference API
website: https://www.ginkgobioworks.com
---
