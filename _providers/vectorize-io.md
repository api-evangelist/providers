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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Vectorize Io Agentic Access
  operation_count: 37
  slug: vectorize-io-agentic-access
  summary_line: 37 operations · 22 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Manage AI platform (embedding / model) connectors.
  name: Vectorize AI Platform Connectors API
  slug: vectorize-io-ai-platform-connectors-api
- description: Manage destination (vector database) connectors.
  name: Vectorize Destination Connectors API
  slug: vectorize-io-destination-connectors-api
- description: Vectorize Iris document extraction.
  name: Vectorize Extraction API
  slug: vectorize-io-extraction-api
- description: Upload generic files to the platform.
  name: Vectorize Files API
  slug: vectorize-io-files-api
- description: Create and operate RAG pipelines, retrieval, and deep research.
  name: Vectorize Pipelines API
  slug: vectorize-io-pipelines-api
- description: Manage data source connectors.
  name: Vectorize Source Connectors API
  slug: vectorize-io-source-connectors-api
- description: Push and manage files against File Upload connectors.
  name: Vectorize Uploads API
  slug: vectorize-io-uploads-api
- description: List and retrieve workspaces.
  name: Vectorize Workspaces API
  slug: vectorize-io-workspaces-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vectorize AI Platform Connectors API
  slug: open-vectorize-io-ai-platform-connectors-api
- collection_type: open
  name: Vectorize AI Platform Connectors Destination Connectors API
  slug: open-vectorize-io-destination-connectors-api
- collection_type: open
  name: Vectorize AI Platform Connectors Extraction API
  slug: open-vectorize-io-extraction-api
- collection_type: open
  name: Vectorize AI Platform Connectors Files API
  slug: open-vectorize-io-files-api
- collection_type: open
  name: Vectorize AI Platform Connectors Pipelines API
  slug: open-vectorize-io-pipelines-api
- collection_type: open
  name: Vectorize AI Platform Connectors Source Connectors API
  slug: open-vectorize-io-source-connectors-api
- collection_type: open
  name: Vectorize AI Platform Connectors Uploads API
  slug: open-vectorize-io-uploads-api
- collection_type: open
  name: Vectorize AI Platform Connectors Workspaces API
  slug: open-vectorize-io-workspaces-api
- collection_type: open
  name: Vectorize API
  slug: open-vectorize-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vectorize-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectorize-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vectorize-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vectorize-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vectorize-io
- group: company
  title: ''
  type: Website
  url: https://vectorize.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vectorize.io
- group: commercial
  title: ''
  type: Plans
  url: plans/vectorize-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vectorize-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vectorize-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.vectorize.io/feed/
created: '2026-06-20'
description: Vectorize is a RAG (retrieval-augmented generation) pipeline platform that ingests unstructured data, chunks and embeds it, and serves low-latency retrieval against a managed vector database. The Vectorize API lets developers create, start, and stop RAG pipelines, run retrieval, manage source / destination / AI-platform connectors, upload files, extract documents with Iris, and run deep research.
finops:
- name: Vectorize Io Finops
  service_category: AI and Machine Learning
  slug: vectorize-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vectorize-io.png
layout: provider
modified: '2026-06-20'
name: Vectorize
nav: Providers
network: true
overview: 'Vectorize publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AI Platform Connectors API, Destination Connectors API, Extraction API, and 5 more. Tagged areas include Artificial Intelligence, RAG, Vectorization, Embeddings, and Retrieval.


  Vectorize''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Vectorize Io Plans Pricing
  plan_count: 4
  slug: vectorize-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Vectorize Io Rate Limits
  slug: vectorize-io-rate-limits
score:
  band: developing
  composite: 39.7
  delta: 2.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectorize-io/refs/heads/main/screenshots/vectorize-io-2026-06-20T200845.png
security:
- kind: authentication
  name: Vectorize Io Authentication
  slug: vectorize-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vectorize Io Domain Security
  slug: vectorize-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vectorize-io
tags:
- Artificial Intelligence
- RAG
- Vectorization
- Embeddings
- Retrieval
- Vector Database
website: https://vectorize.io/
---
