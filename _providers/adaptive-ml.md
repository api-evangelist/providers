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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Adaptive Ml Agentic Access
  operation_count: 13
  slug: adaptive-ml-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 9
apis:
- description: The artifacts::rest API from Adaptive ML — 1 operation(s) for artifacts::rest.
  name: Adaptive ML artifacts::rest API
  slug: adaptive-ml-artifacts-rest-api
- description: Upload large files in chunks
  name: Adaptive ML Chunked Upload API
  slug: adaptive-ml-chunked-upload-api
- description: The Completions API from Adaptive ML — 1 operation(s) for completions.
  name: Adaptive ML Completions API
  slug: adaptive-ml-completions-api
- description: The Datasets API from Adaptive ML — 1 operation(s) for datasets.
  name: Adaptive ML Datasets API
  slug: adaptive-ml-datasets-api
- description: The Embeddings API from Adaptive ML — 1 operation(s) for embeddings.
  name: Adaptive ML Embeddings API
  slug: adaptive-ml-embeddings-api
- description: The Feedback API from Adaptive ML — 2 operation(s) for feedback.
  name: Adaptive ML Feedback API
  slug: adaptive-ml-feedback-api
- description: The image::rest API from Adaptive ML — 1 operation(s) for image::rest.
  name: Adaptive ML image::rest API
  slug: adaptive-ml-image-rest-api
- description: Load interactions in the db
  name: Adaptive ML Interactions API
  slug: adaptive-ml-interactions-api
- description: Recipe operations
  name: Adaptive ML Recipes API
  slug: adaptive-ml-recipes-api
artifact_total: 14
asyncapis:
- description: ''
  name: Adaptive Ml Webhooks
  slug: adaptive-ml-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.adaptive-ml.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.adaptive-ml.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adaptive-ml.com/v0.14/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adaptive-ml.com/v0.14/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adaptive-ml.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.adaptive-ml.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.adaptive-ml.com/book-a-demo
- group: operate
  title: ''
  type: Support
  url: https://www.adaptive-ml.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adaptive-ml.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adaptive-ml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adaptive-ml-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/adaptive-ml-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adaptive-ml-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/adaptive-ml-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adaptive-ml-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adaptive-ml-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adaptive-ml-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adaptive-ml-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaptive-ml-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adaptive-ml-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adaptive-ml-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adaptive-ml-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaptive-ml-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/adaptive-ml-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adaptive-ml-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adaptive-ml-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptive-ml-domain-security.yml
created: '2026-07-17'
description: Adaptive ML builds Adaptive Engine, an enterprise platform for developing, evaluating, and serving specialized open-source large language models via reinforcement-learning post-training. The three-phase workflow (Adapt, Evaluate, Serve) lets teams fine-tune smaller models to outperform commercial APIs, measure them with custom AI judges and graders, and feed production signals back into training. Adaptive Engine is self-hosted (Kubernetes/Helm) and exposes an OpenAI-compatible REST API for chat completions and embeddings, plus interactions, comparisons, outcomes, dataset/recipe management, and chunked uploads. Tooling includes the Python adaptive-sdk and adaptive-harmony libraries and the adpt CLI. Adaptive ML was acquired by Datadog.
image: https://www.adaptive-ml.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: adaptive-ml-mcp.yml
  slug: adaptive-ml-mcpyml
modified: '2026-07-17'
name: Adaptive ML
nav: Providers
network: true
overview: 'Adaptive ML publishes 9 APIs on the [APIs.io](https://apis.io/) network, including artifacts::rest API, Chunked Upload API, Completions API, and 6 more. Tagged areas include Company, Ai Ml, LLM, Fine-Tuning, and Reinforcement Learning.


  The Adaptive ML catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adaptive ML''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 21 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.4
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adaptive-ml/refs/heads/main/screenshots/adaptive-ml-2026-07-25T181557.png
security:
- kind: authentication
  name: Adaptive Ml Authentication
  slug: adaptive-ml-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adaptive Ml Domain Security
  slug: adaptive-ml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaptive-ml
tags:
- Company
- Ai Ml
- LLM
- Fine-Tuning
- Reinforcement Learning
- Model Evaluation
- Inference
- OpenAI-Compatible
- MLOps
website: https://www.adaptive-ml.com
---
