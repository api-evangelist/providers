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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Manage account info.
  name: Figure Eight Account Info API
  slug: figure-eight-account-info-api
- description: Create and update jobs.
  name: Figure Eight Job Create/Update API
  slug: figure-eight-job-create-update-api
- description: Read and Update the Ontology for a job
  name: Figure Eight Job Ontology API
  slug: figure-eight-job-ontology-api
- description: Request rows, judgments, and reports.
  name: Figure Eight Job Results API
  slug: figure-eight-job-results-api
- description: Control job status.
  name: Figure Eight Job Status API
  slug: figure-eight-job-status-api
- description: Load data to jobs and work with that data.
  name: Figure Eight Manage Job Data API
  slug: figure-eight-manage-job-data-api
- description: Manage various job settings.
  name: Figure Eight Manage Job Settings API
  slug: figure-eight-manage-job-settings-api
- description: Monitor contributor status and settings.
  name: Figure Eight Monitor Contributors API
  slug: figure-eight-monitor-contributors-api
- description: Upload data to run through a Workflow. Download reports.
  name: Figure Eight Workflow Data Upload/Download API
  slug: figure-eight-workflow-data-upload-download-api
- description: Rules for routing data
  name: Figure Eight Workflow Filter Rules API
  slug: figure-eight-workflow-filter-rules-api
- description: Manage Workflow Step Routes
  name: Figure Eight Workflow Step Routes API
  slug: figure-eight-workflow-step-routes-api
- description: Manage Workflow Steps
  name: Figure Eight Workflow Steps API
  slug: figure-eight-workflow-steps-api
- description: Copy, launch, pause and resume workflows, check status and configuration values
  name: Figure Eight Workflows API
  slug: figure-eight-workflows-api
artifact_total: 31
asyncapis:
- description: ''
  name: Figure Eight Webhooks
  slug: figure-eight-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appen Platform Account Info API
  slug: open-figure-eight-account-info-api
- collection_type: open
  name: Appen Platform Account Info Job Create/Update API
  slug: open-figure-eight-job-create-update-api
- collection_type: open
  name: Appen Platform Account Info Job Ontology API
  slug: open-figure-eight-job-ontology-api
- collection_type: open
  name: Appen Platform Account Info Job Results API
  slug: open-figure-eight-job-results-api
- collection_type: open
  name: Appen Platform Account Info Job Status API
  slug: open-figure-eight-job-status-api
- collection_type: open
  name: Appen Platform Account Info Manage Job Data API
  slug: open-figure-eight-manage-job-data-api
- collection_type: open
  name: Appen Platform Account Info Manage Job Settings API
  slug: open-figure-eight-manage-job-settings-api
- collection_type: open
  name: Appen Platform Account Info Monitor Contributors API
  slug: open-figure-eight-monitor-contributors-api
- collection_type: open
  name: Appen Platform Account Info Workflow Data Upload/Download API
  slug: open-figure-eight-workflow-data-upload-download-api
- collection_type: open
  name: Appen Platform Account Info Workflow Filter Rules API
  slug: open-figure-eight-workflow-filter-rules-api
- collection_type: open
  name: Appen Platform Account Info Workflow Step Routes API
  slug: open-figure-eight-workflow-step-routes-api
- collection_type: open
  name: Appen Platform Account Info Workflow Steps API
  slug: open-figure-eight-workflow-steps-api
- collection_type: open
  name: Appen Platform Account Info Workflows API
  slug: open-figure-eight-workflows-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-eight-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figure-eight-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/apis-docs/CrowdFlower/FigureEightAPI/1.0.0
- group: docs
  title: ''
  type: Documentation
  url: http://crowdflower.github.io/CML/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrowdFlower
- group: build
  title: ''
  type: Packages
  url: packages/figure-eight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/figure-eight-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figure-eight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figure-eight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figure-eight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figure-eight-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/figure-eight-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figure-eight-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/figure-eight-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figure-eight-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/figure-eight-well-known.yml
created: '2026-07-17'
description: Figure Eight (formerly CrowdFlower, and originally Dolores Labs) was a human-in-the-loop machine learning and artificial intelligence company founded in San Francisco in 2007 by Lukas Biewald and Chris Van Pelt. Its platform turned unlabeled text, image, audio, and video into high-quality AI training data by combining automation with a distributed contributor workforce. The company exposed a RESTful, key-authenticated JSON API for programmatically creating, configuring, launching, and monitoring annotation jobs and multi-step workflows, and for downloading aggregated judgments and reports. Figure Eight was acquired by Appen in March 2019 for up to $300M; by 2020 its assets were fully integrated into Appen and the API is now served as the Appen Platform API at api.appen.com. This profile captures that surviving API surface. figure-eight.com now redirects to appen.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/figure-eight.png
layout: provider
mcp_servers:
- description: ''
  name: Figure Eight MCP Server
  slug: figure-eight-mcp-server
modified: '2026-07-19'
name: Figure Eight
nav: Providers
network: true
overview: 'Figure Eight publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account Info API, Job Create/Update API, Job Ontology API, and 10 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Data Labeling, and Data Annotation.


  The Figure Eight catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Figure Eight''s developer surface includes API reference, documentation, authentication, and 13 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 57.9
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 30.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figure-eight/refs/heads/main/screenshots/figure-eight-2026-07-25T214447.png
security:
- kind: authentication
  name: Figure Eight Authentication
  slug: figure-eight-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Figure Eight Domain Security
  slug: figure-eight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: figure-eight
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Data Labeling
- Data Annotation
- Training Data
- Human-in-the-Loop
- Crowdsourcing
- Acquired
---
