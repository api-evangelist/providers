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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Arrays API from Slope Software — 2 operation(s) for arrays.
  name: Slope Software Arrays API
  slug: slope-software-arrays-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Authorize API from Slope Software — 2 operation(s) for authorize.
  name: Slope Software Authorize API
  slug: slope-software-authorize-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The DataTables API from Slope Software — 7 operation(s) for datatables.
  name: Slope Software DataTables API
  slug: slope-software-datatables-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The DecrementTables API from Slope Software — 2 operation(s) for decrementtables.
  name: Slope Software DecrementTables API
  slug: slope-software-decrementtables-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Files API from Slope Software — 4 operation(s) for files.
  name: Slope Software Files API
  slug: slope-software-files-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The ImprovementScales API from Slope Software — 2 operation(s) for improvementscales.
  name: Slope Software ImprovementScales API
  slug: slope-software-improvementscales-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The ModelPointFields API from Slope Software — 2 operation(s) for modelpointfields.
  name: Slope Software ModelPointFields API
  slug: slope-software-modelpointfields-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Models API from Slope Software — 13 operation(s) for models.
  name: Slope Software Models API
  slug: slope-software-models-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Products API from Slope Software — 1 operation(s) for products.
  name: Slope Software Products API
  slug: slope-software-products-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Projections API from Slope Software — 6 operation(s) for projections.
  name: Slope Software Projections API
  slug: slope-software-projections-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Reports API from Slope Software — 2 operation(s) for reports.
  name: Slope Software Reports API
  slug: slope-software-reports-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The ScenarioTables API from Slope Software — 4 operation(s) for scenariotables.
  name: Slope Software ScenarioTables API
  slug: slope-software-scenariotables-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The TableStructures API from Slope Software — 3 operation(s) for tablestructures.
  name: Slope Software TableStructures API
  slug: slope-software-tablestructures-api
- baseURL: https://api.slopesoftware.com
  baseurl_source: declared
  description: The Users API from Slope Software — 1 operation(s) for users.
  name: Slope Software Users API
  slug: slope-software-users-api
arazzos:
- description: Kick off a workbook report, poll for completion, and fetch a download URL.
  name: Generate and download a SLOPE workbook report
  slug: slope-software-generate-report
- description: Find a model, create a projection from a template, run it, and poll for completion.
  name: Run a SLOPE projection from a template
  slug: slope-software-run-projection
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Slope Arrays API
  slug: open-slope-software-arrays-api
- collection_type: open
  name: Slope Arrays Authorize API
  slug: open-slope-software-authorize-api
- collection_type: open
  name: Slope Arrays DataTables API
  slug: open-slope-software-datatables-api
- collection_type: open
  name: Slope Arrays DecrementTables API
  slug: open-slope-software-decrementtables-api
- collection_type: open
  name: Slope Arrays Files API
  slug: open-slope-software-files-api
- collection_type: open
  name: Slope Arrays ImprovementScales API
  slug: open-slope-software-improvementscales-api
- collection_type: open
  name: Slope Arrays ModelPointFields API
  slug: open-slope-software-modelpointfields-api
- collection_type: open
  name: Slope Arrays Models API
  slug: open-slope-software-models-api
- collection_type: open
  name: Slope Arrays Products API
  slug: open-slope-software-products-api
- collection_type: open
  name: Slope Arrays Projections API
  slug: open-slope-software-projections-api
- collection_type: open
  name: Slope Arrays Reports API
  slug: open-slope-software-reports-api
- collection_type: open
  name: Slope Arrays ScenarioTables API
  slug: open-slope-software-scenariotables-api
- collection_type: open
  name: Slope Arrays TableStructures API
  slug: open-slope-software-tablestructures-api
- collection_type: open
  name: Slope Arrays Users API
  slug: open-slope-software-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/slope-software-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Slope Software
nav: Providers
network: true
overview: 'Slope Software publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Arrays API, Authorize API, DataTables API, and 11 more. Tagged areas include Company, Actuarial, Insurance, Actuarial Modeling, and Valuation.


  Slope Software''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 51.2
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 40.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slope-software/refs/heads/main/screenshots/slope-software-2026-09-02T155856.png
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
- Financial-Services
- Life Insurance
- Annuities
- Pension
- Risk Management
- Cloud
- Reporting
website: https://slopesoftware.com/
---
