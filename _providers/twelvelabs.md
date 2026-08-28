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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Twelvelabs Agentic Access
  operation_count: 22
  slug: twelvelabs-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 6
apis:
- description: Generate text from video with Pegasus (analyze, gist, summarize).
  name: TwelveLabs Analyze API
  slug: twelvelabs-analyze-api
- description: Create multimodal Marengo embeddings.
  name: TwelveLabs Embed API
  slug: twelvelabs-embed-api
- description: Create and manage video indexes.
  name: TwelveLabs Indexes API
  slug: twelvelabs-indexes-api
- description: Any-to-video semantic search powered by Marengo.
  name: TwelveLabs Search API
  slug: twelvelabs-search-api
- description: Upload and index video via asynchronous indexing tasks.
  name: TwelveLabs Tasks API
  slug: twelvelabs-tasks-api
- description: Manage videos within an index.
  name: TwelveLabs Videos API
  slug: twelvelabs-videos-api
artifact_total: 22
asyncapis:
- description: 'AsyncAPI 2.6 description of TwelveLabs'' **analyze (text generation) streaming** surface. TwelveLabs does not publish a WebSocket API. The only asynchronous / event-style transport documented for text '
  name: TwelveLabs Analyze Streaming (HTTP + NDJSON)
  slug: twelvelabs-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TwelveLabs Analyze API
  slug: open-twelvelabs-analyze-api
- collection_type: open
  name: TwelveLabs Analyze Embed API
  slug: open-twelvelabs-embed-api
- collection_type: open
  name: TwelveLabs Analyze Indexes API
  slug: open-twelvelabs-indexes-api
- collection_type: open
  name: TwelveLabs Analyze Search API
  slug: open-twelvelabs-search-api
- collection_type: open
  name: TwelveLabs Analyze Tasks API
  slug: open-twelvelabs-tasks-api
- collection_type: open
  name: TwelveLabs Analyze Videos API
  slug: open-twelvelabs-videos-api
- collection_type: open
  name: TwelveLabs API
  slug: open-twelvelabs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twelvelabs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twelvelabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twelvelabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twelvelabs-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/twelvelabs
- group: company
  title: ''
  type: Website
  url: https://www.twelvelabs.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.twelvelabs.io
- group: commercial
  title: ''
  type: Plans
  url: plans/twelvelabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/twelvelabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/twelvelabs-finops.yml
created: '2026-06-20'
description: TwelveLabs builds video-understanding foundation models (Marengo for search and embeddings, Pegasus for analyzing video and generating text). The TwelveLabs API lets developers upload and index video, run any-to-video semantic search, generate text from video (titles, topics, hashtags, summaries, chapters, highlights, and open-ended analysis), and create multimodal embeddings over a REST interface authenticated with an x-api-key header.
finops:
- name: Twelvelabs Finops
  service_category: AI and Machine Learning
  slug: twelvelabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/twelvelabs.png
layout: provider
modified: '2026-06-20'
name: TwelveLabs
nav: Providers
network: true
overview: 'TwelveLabs publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analyze API, Embed API, Indexes API, and 3 more. Tagged areas include Artificial Intelligence, Video Understanding, Multi-Modal, Search, and Embeddings.


  The TwelveLabs catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  TwelveLabs'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Twelvelabs Plans Pricing
  plan_count: 3
  slug: twelvelabs-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Twelvelabs Rate Limits
  slug: twelvelabs-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: TwelveLabs API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: twelvelabs-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.7
  delta: 2.3
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 59.8
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twelvelabs/refs/heads/main/screenshots/twelvelabs-2026-06-20T195846.png
security:
- kind: authentication
  name: Twelvelabs Authentication
  slug: twelvelabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Twelvelabs Domain Security
  slug: twelvelabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: twelvelabs
tags:
- Artificial Intelligence
- Video Understanding
- Multi-Modal
- Search
- Embeddings
website: https://www.twelvelabs.io
---
