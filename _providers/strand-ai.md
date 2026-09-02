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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Strand Ai Agentic Access
  operation_count: 11
  slug: strand-ai-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- description: The Jobs API from Strand AI — 4 operation(s) for jobs.
  name: Strand AI Jobs API
  slug: strand-ai-jobs-api
- description: The Predict API from Strand AI — 2 operation(s) for predict.
  name: Strand AI Predict API
  slug: strand-ai-predict-api
- description: The Samples API from Strand AI — 3 operation(s) for samples.
  name: Strand AI Samples API
  slug: strand-ai-samples-api
- description: The Uploads API from Strand AI — 2 operation(s) for uploads.
  name: Strand AI Uploads API
  slug: strand-ai-uploads-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Strand AI Platform Jobs API
  slug: open-strand-ai-jobs-api
- collection_type: open
  name: Strand AI Platform Jobs Predict API
  slug: open-strand-ai-predict-api
- collection_type: open
  name: Strand AI Platform Jobs Samples API
  slug: open-strand-ai-samples-api
- collection_type: open
  name: Strand AI Platform Jobs Uploads API
  slug: open-strand-ai-uploads-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.strandai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strandai.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.strandai.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strandai.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.strandai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.strandai.com/sign-in?requestAccess
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Strand-AI
- group: company
  title: ''
  type: Website
  url: https://strandai.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strand-ai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/strand-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strand-ai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/strand-ai-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/strand-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strand-ai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/strand-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/strand-ai-platform-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/strand-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/strand-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strand-ai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/strand-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strand-ai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strand-ai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strand-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Strand AI (YC W26) builds multimodal foundation models for spatial biology that predict missing patient bio-data from the data a patient already has. Its Lattice model turns a single H&E-stained whole-slide image into per-pixel predictions for a panel of protein markers, recovering spatial protein signal without running multiplex immunofluorescence. The Strand Platform API is a production REST surface (https://app.strandai.com/api/v1) for uploading whole-slide images, estimating and submitting Lattice inference jobs, streaming job status over Server-Sent Events, and downloading OME-Zarr results as AnnData (Python) or SpatialExperiment (R). Access is invite-only, authenticated with organization-scoped bearer API keys, and metered in credits (1 credit per 224x224-px patch per marker). Official Python (strand-sdk) and R (strandai) clients are published. Outputs are for research and hypothesis generation, not clinical use.
image: https://avatars.githubusercontent.com/u/252118542?v=4
layout: provider
mcp_servers:
- description: ''
  name: Strand AI MCP Server
  slug: strand-ai-mcp-server
modified: '2026-07-21'
name: Strand AI
nav: Providers
network: true
overview: 'Strand AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, Predict API, Samples API, and 1 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Life Sciences, and Spatial Biology.


  Strand AI''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, changelog, and 17 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 51.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Strand Ai Authentication
  slug: strand-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Strand Ai Domain Security
  slug: strand-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: strand-ai
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Life Sciences
- Spatial Biology
- Bioinformatics
- Drug Discovery
- Foundation Models
- Digital Pathology
- Healthcare
website: https://strandai.com
---
