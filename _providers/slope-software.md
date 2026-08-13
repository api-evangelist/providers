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
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-12'
api_count: 14
apis:
- description: The Arrays API from Slope Software — 2 operation(s) for arrays.
  name: Slope Software Arrays API
  slug: slope-software-arrays-api
- description: The Authorize API from Slope Software — 2 operation(s) for authorize.
  name: Slope Software Authorize API
  slug: slope-software-authorize-api
- description: The DataTables API from Slope Software — 7 operation(s) for datatables.
  name: Slope Software DataTables API
  slug: slope-software-datatables-api
- description: The DecrementTables API from Slope Software — 2 operation(s) for decrementtables.
  name: Slope Software DecrementTables API
  slug: slope-software-decrementtables-api
- description: The Files API from Slope Software — 4 operation(s) for files.
  name: Slope Software Files API
  slug: slope-software-files-api
- description: The ImprovementScales API from Slope Software — 2 operation(s) for improvementscales.
  name: Slope Software ImprovementScales API
  slug: slope-software-improvementscales-api
- description: The ModelPointFields API from Slope Software — 2 operation(s) for modelpointfields.
  name: Slope Software ModelPointFields API
  slug: slope-software-modelpointfields-api
- description: The Models API from Slope Software — 13 operation(s) for models.
  name: Slope Software Models API
  slug: slope-software-models-api
- description: The Products API from Slope Software — 1 operation(s) for products.
  name: Slope Software Products API
  slug: slope-software-products-api
- description: The Projections API from Slope Software — 6 operation(s) for projections.
  name: Slope Software Projections API
  slug: slope-software-projections-api
- description: The Reports API from Slope Software — 2 operation(s) for reports.
  name: Slope Software Reports API
  slug: slope-software-reports-api
- description: The ScenarioTables API from Slope Software — 4 operation(s) for scenariotables.
  name: Slope Software ScenarioTables API
  slug: slope-software-scenariotables-api
- description: The TableStructures API from Slope Software — 3 operation(s) for tablestructures.
  name: Slope Software TableStructures API
  slug: slope-software-tablestructures-api
- description: The Users API from Slope Software — 1 operation(s) for users.
  name: Slope Software Users API
  slug: slope-software-users-api
arazzos:
- description: Kick off a workbook report, poll for completion, and fetch a download URL.
  name: Generate and download a SLOPE workbook report
  slug: slope-software-generate-report
- description: Find a model, create a projection from a template, run it, and poll for completion.
  name: Run a SLOPE projection from a template
  slug: slope-software-run-projection
artifact_total: 20
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/slope-software-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slope-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slopesoftware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.slopesoftware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://slopesoftware.com/wp-content/uploads/2022/02/SLOPE-API.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://api.slopesoftware.com/
- group: company
  title: ''
  type: Blog
  url: https://slopesoftware.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.slopesoftware.com/
- group: start
  title: ''
  type: SignUp
  url: https://slopesoftware.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.slopesoftware.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slopesoftware.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://security.slopesoftware.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/slope-software-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slope-software-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slope-software-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/slope-software-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slope-software-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/slope-software-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/slope-software-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/slope-software-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/slope-software-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slope-software-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-software-run-projection.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slope-software-generate-report.yml
created: '2026-07-17'
description: 'Slope Software builds SLOPE, a cloud-native actuarial modeling platform for life, annuity, pension, and supplemental health/disability/LTC insurers. SLOPE lets actuaries develop transparent, flexible projection models, aggregate and manage assumptions and data tables, run high-performance valuation, pricing, ALM, and experience-study calculations, and analyze results with dynamic reporting. The SLOPE REST API automates the full valuation workflow end to end: ingesting scenario and data tables, uploading model point files, creating projections from templates, kicking off runs, checking status, and pulling results back down to integrate with downstream systems.'
image: https://slopesoftware.com/wp-content/uploads/2021/09/cropped-slope-fullcolor-logomark-square.png
layout: provider
mcp_servers:
- description: ''
  name: slope-software-mcp.yml
  slug: slope-software-mcpyml
modified: '2026-07-21'
name: Slope Software
nav: Providers
network: true
overview: 'Slope Software publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Arrays API, Authorize API, DataTables API, and 11 more. Tagged areas include Company, Actuarial, Insurance, Actuarial Modeling, and Valuation.


  Slope Software''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 41.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.5
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 41.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Slope Software Authentication
  slug: slope-software-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Slope Software Domain Security
  slug: slope-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Slope Software Trust Center
  slug: slope-software-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: slope-software
tags:
- Company
- Actuarial
- Insurance
- Actuarial Modeling
- Valuation
- Financial Services
- Life Insurance
- Annuities
- Pension
- Risk Management
- Cloud
- Reporting
website: https://slopesoftware.com/
---
