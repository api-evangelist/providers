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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-08-19'
api_count: 22
apis:
- description: The Admin API from Transload — 36 operation(s) for admin.
  name: Transload Admin API
  slug: transload-admin-api
- description: The Ai Results API from Transload — 3 operation(s) for ai results.
  name: Transload Ai Results API
  slug: transload-ai-results-api
- description: The Artifacts API from Transload — 1 operation(s) for artifacts.
  name: Transload Artifacts API
  slug: transload-artifacts-api
- description: The Cameras API from Transload — 2 operation(s) for cameras.
  name: Transload Cameras API
  slug: transload-cameras-api
- description: The Customer API from Transload — 9 operation(s) for customer.
  name: Transload Customer API
  slug: transload-customer-api
- description: The Customers API from Transload — 2 operation(s) for customers.
  name: Transload Customers API
  slug: transload-customers-api
- description: The Exports API from Transload — 1 operation(s) for exports.
  name: Transload Exports API
  slug: transload-exports-api
- description: The Handling Units API from Transload — 1 operation(s) for handling units.
  name: Transload Handling Units API
  slug: transload-handling-units-api
- description: The Healthz API from Transload — 1 operation(s) for healthz.
  name: Transload Healthz API
  slug: transload-healthz-api
- description: The Ingestor API from Transload — 4 operation(s) for ingestor.
  name: Transload Ingestor API
  slug: transload-ingestor-api
- description: The Internal API from Transload — 16 operation(s) for internal.
  name: Transload Internal API
  slug: transload-internal-api
- description: The Measurement API from Transload — 1 operation(s) for measurement.
  name: Transload Measurement API
  slug: transload-measurement-api
- description: The Media Assets API from Transload — 2 operation(s) for media assets.
  name: Transload Media Assets API
  slug: transload-media-assets-api
- description: The Processing Jobs API from Transload — 2 operation(s) for processing jobs.
  name: Transload Processing Jobs API
  slug: transload-processing-jobs-api
- description: The Qa API from Transload — 18 operation(s) for qa.
  name: Transload Qa API
  slug: transload-qa-api
- description: The Qa Classification API from Transload — 6 operation(s) for qa classification.
  name: Transload Qa Classification API
  slug: transload-qa-classification-api
- description: The Qa Measurement API from Transload — 9 operation(s) for qa measurement.
  name: Transload Qa Measurement API
  slug: transload-qa-measurement-api
- description: The Readyz API from Transload — 1 operation(s) for readyz.
  name: Transload Readyz API
  slug: transload-readyz-api
- description: The Reference Measurements API from Transload — 2 operation(s) for reference measurements.
  name: Transload Reference Measurements API
  slug: transload-reference-measurements-api
- description: The Refresh Token API from Transload — 1 operation(s) for refresh token.
  name: Transload Refresh Token API
  slug: transload-refresh-token-api
- description: The Scans API from Transload — 5 operation(s) for scans.
  name: Transload Scans API
  slug: transload-scans-api
- description: The Sites API from Transload — 2 operation(s) for sites.
  name: Transload Sites API
  slug: transload-sites-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pipeline Backend Admin API
  slug: open-transload-admin-api
- collection_type: open
  name: Pipeline Backend Admin Ai Results API
  slug: open-transload-ai-results-api
- collection_type: open
  name: Pipeline Backend Admin Artifacts API
  slug: open-transload-artifacts-api
- collection_type: open
  name: Pipeline Backend Admin Cameras API
  slug: open-transload-cameras-api
- collection_type: open
  name: Pipeline Backend Admin Customer API
  slug: open-transload-customer-api
- collection_type: open
  name: Pipeline Backend Admin Customers API
  slug: open-transload-customers-api
- collection_type: open
  name: Pipeline Backend Admin Exports API
  slug: open-transload-exports-api
- collection_type: open
  name: Pipeline Backend Admin Handling Units API
  slug: open-transload-handling-units-api
- collection_type: open
  name: Pipeline Backend Admin Healthz API
  slug: open-transload-healthz-api
- collection_type: open
  name: Pipeline Backend Admin Ingestor API
  slug: open-transload-ingestor-api
- collection_type: open
  name: Pipeline Backend Admin Internal API
  slug: open-transload-internal-api
- collection_type: open
  name: Pipeline Backend Admin Measurement API
  slug: open-transload-measurement-api
- collection_type: open
  name: Pipeline Backend Admin Media Assets API
  slug: open-transload-media-assets-api
- collection_type: open
  name: Pipeline Backend Admin Processing Jobs API
  slug: open-transload-processing-jobs-api
- collection_type: open
  name: Pipeline Backend Admin Qa API
  slug: open-transload-qa-api
- collection_type: open
  name: Pipeline Backend Admin Qa Classification API
  slug: open-transload-qa-classification-api
- collection_type: open
  name: Pipeline Backend Admin Qa Measurement API
  slug: open-transload-qa-measurement-api
- collection_type: open
  name: Pipeline Backend Admin Readyz API
  slug: open-transload-readyz-api
- collection_type: open
  name: Pipeline Backend Admin Reference Measurements API
  slug: open-transload-reference-measurements-api
- collection_type: open
  name: Pipeline Backend Admin Refresh Token API
  slug: open-transload-refresh-token-api
- collection_type: open
  name: Pipeline Backend Admin Scans API
  slug: open-transload-scans-api
- collection_type: open
  name: Pipeline Backend Admin Sites API
  slug: open-transload-sites-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/transload-pipeline-backend-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transload-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transload-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://transload.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transload.io/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://transload.io/gdpr/
- group: operate
  title: ''
  type: Support
  url: mailto:contact@transload.io
- group: docs
  title: ''
  type: Documentation
  url: https://api.transload.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.transload.io/docs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/transload-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transload-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/transload-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transload-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transload-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/transload-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Transload (YC Spring 2026) measures freight with security cameras, turning the CCTV already installed in logistics warehouses into a 3D dimensioner for the loading dock. Its computer vision captures the true size of every pallet, couch, or tire as it moves through the warehouse — no new hardware or process changes — recovering rebilling revenue and trailer utilization for trucking companies (the company reports ~15% of shipments measure larger than declared). Founded 2026 in San Francisco by Nils Börner, Julius Scheel, and Jago Wahl-Schwentker (TU Munich). Its bearer-authenticated Pipeline Backend API is publicly described by an OpenAPI 3.0.3 served at api.transload.io/docs, covering customers, sites, cameras, scans, processing stages, AI measurement results, and customer handling-unit data.
image: https://bookface-images.s3.amazonaws.com/small_logos/1bddf9622d95fa25a8b10500158d81f74f5df2f7.png
layout: provider
mcp_servers:
- description: ''
  name: transload-mcp.yml
  slug: transload-mcpyml
modified: '2026-07-21'
name: Transload
nav: Providers
network: true
overview: 'Transload publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Ai Results API, Artifacts API, and 19 more. Tagged areas include Company, Logistics, Freight, Computer Vision, and Warehouses.


  Transload''s developer surface includes authentication, support, documentation, API reference, and 12 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.8
  delta: 0.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 16.7
    contract_quality: 35.7
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 29.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Transload Authentication
  slug: transload-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Transload Domain Security
  slug: transload-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transload
tags:
- Company
- Logistics
- Freight
- Computer Vision
- Warehouses
- Supply Chain
- Measurement
- Cameras
- Trucking
website: https://transload.io
---
