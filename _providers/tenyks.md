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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tenyks Agentic Access
  operation_count: 8
  slug: tenyks-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 3
apis:
- description: Obtain a Bearer access token from an API key and secret.
  name: Tenyks Auth API
  slug: tenyks-auth-api
- description: Upload and ingest annotations, models and predictions from cloud storage.
  name: Tenyks Data Upload API
  slug: tenyks-data-upload-api
- description: Create and retrieve datasets.
  name: Tenyks Datasets API
  slug: tenyks-datasets-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tenyks Auth API
  slug: open-tenyks-auth-api
- collection_type: open
  name: Tenyks Auth Data Upload API
  slug: open-tenyks-data-upload-api
- collection_type: open
  name: Tenyks Auth Datasets API
  slug: open-tenyks-datasets-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenyks-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tenyks-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tenyks.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tenyks.ai/docs/the-foundations
- group: company
  title: ''
  type: Blog
  url: https://www.tenyks.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenyks.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.tenyks.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/tenyks
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenyks-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tenyks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tenyks-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tenyks-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tenyks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tenyks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tenyks-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tenyks-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tenyks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tenyks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tenyks-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tenyks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tenyks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tenyks.ai
- group: auth
  title: ''
  type: TrustCenter
  url: security/tenyks-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tenyks-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tenyks is a University of Cambridge spin-out (Y Combinator; backed by Speedinvest) building a visual-intelligence platform for computer vision. Its original product is an MLOps monitoring and validation platform that helps ML engineers working with computer-vision data find and fix what is wrong with their models — data-quality analysis, model performance comparison, text-to-image / image-to-image / object-level similarity search, embeddings, tagging and custom metadata across image and video datasets. Tenyks has since extended into a Vision AI / Video AI Agents platform that turns everyday camera feeds into privacy-first operational analytics for brick-and-mortar businesses. The Tenyks API (currently alpha, for Premium/Dashboard users, with a freemium Sandbox) lets teams authenticate with an API key + secret to obtain a Bearer token, then create datasets and models, and upload and ingest annotations and predictions directly from AWS S3, GCS or Azure. A Python SDK and CLI wrap
  the same surface.
image: https://cdn.prod.website-files.com/63a0220866f41638081f4fce/63d07b4812f0f901e939d964_tenyks_logo-color.png
layout: provider
mcp_servers:
- description: ''
  name: tenyks-mcp.yml
  slug: tenyks-mcpyml
modified: '2026-07-21'
name: Tenyks
nav: Providers
network: true
overview: 'Tenyks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Data Upload API, and Datasets API. Tagged areas include Company, Computer Vision, Machine Learning, MLOps, and Data Quality.


  Tenyks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 71.2
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Tenyks Authentication
  slug: tenyks-authentication
  summary_line: http/apiKey-exchange · 1 scheme
- kind: domain-security
  name: Tenyks Domain Security
  slug: tenyks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tenyks Trust Center
  slug: tenyks-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: tenyks
tags:
- Company
- Computer Vision
- Machine Learning
- MLOps
- Data Quality
- Model Validation
- Visual Intelligence
- Video Analytics
- Artificial Intelligence
- Developer Tools
website: https://docs.tenyks.ai/
---
