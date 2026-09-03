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
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tenyks Agentic Access
  operation_count: 8
  slug: tenyks-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Obtain a Bearer access token from an API key and secret.
  name: Tenyks Auth API
  slug: tenyks-auth-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Upload and ingest annotations, models and predictions from cloud storage.
  name: Tenyks Data Upload API
  slug: tenyks-data-upload-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Create and retrieve datasets.
  name: Tenyks Datasets API
  slug: tenyks-datasets-api
artifact_total: 11
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Tenyks
nav: Providers
network: true
overview: 'Tenyks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Data Upload API, and Datasets API. Tagged areas include Company, Computer-Vision, Machine-Learning, MLOps, and Data Quality.


  Tenyks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 41.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenyks/refs/heads/main/screenshots/tenyks-2026-08-17T082314.png
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
- Computer-Vision
- Machine-Learning
- MLOps
- Data Quality
- Model Validation
- Visual Intelligence
- Video Analytics
- Artificial Intelligence
- Developer Tools
website: https://docs.tenyks.ai/
---
