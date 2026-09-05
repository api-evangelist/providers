---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Simscale Agentic Access
  operation_count: 21
  slug: simscale-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: CAD geometry upload and import
  name: SimScale Geometry API
  slug: simscale-geometry-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: Mesh generation and configuration
  name: SimScale Mesh Operations API
  slug: simscale-mesh-operations-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: Simulation project management
  name: SimScale Projects API
  slug: simscale-projects-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: Post-processing and results reporting
  name: SimScale Reports API
  slug: simscale-reports-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: Simulation execution and status
  name: SimScale Simulation Runs API
  slug: simscale-simulation-runs-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: Simulation setup and configuration
  name: SimScale Simulations API
  slug: simscale-simulations-api
- baseURL: https://api.simscale.com
  baseurl_source: declared
  description: File storage management
  name: SimScale Storage API
  slug: simscale-storage-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SimScale REST Geometry API
  slug: open-simscale-geometry-api
- collection_type: open
  name: SimScale REST Geometry Mesh Operations API
  slug: open-simscale-mesh-operations-api
- collection_type: open
  name: SimScale REST Geometry Projects API
  slug: open-simscale-projects-api
- collection_type: open
  name: SimScale REST Geometry Reports API
  slug: open-simscale-reports-api
- collection_type: open
  name: SimScale REST Geometry Simulation Runs API
  slug: open-simscale-simulation-runs-api
- collection_type: open
  name: SimScale REST Geometry Simulations API
  slug: open-simscale-simulations-api
- collection_type: open
  name: SimScale REST Geometry Storage API
  slug: open-simscale-storage-api
- collection_type: open
  name: SimScale REST API
  slug: open-simscale
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simscale-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simscale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simscale-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.simscale.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simscale
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SimScaleGmbH
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.simscale.com/product/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.simscale.com/docs/
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/SimScaleGmbH/simscale-python-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simscale.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simscale.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simscale.com/privacy-policy/
created: '2026-05-02'
description: SimScale is a cloud-based computer-aided engineering (CAE) platform offering computational fluid dynamics (CFD), finite element analysis (FEA), and thermal simulation capabilities. The SimScale REST API enables programmatic project management, geometry upload, mesh generation, simulation setup and execution, and results extraction for engineering automation workflows.
examples:
- key_count: 4
  name: Simscale Create Project Example
  slug: simscale-create-project-example
- key_count: 4
  name: Simscale Create Simulation Run Example
  slug: simscale-create-simulation-run-example
finops:
- name: Simscale Finops
  service_category: API
  slug: simscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simscale.png
json_schemas:
- name: SimScale Project
  property_count: 8
  slug: simscale-project
- name: SimScale Simulation
  property_count: 7
  slug: simscale-simulation
json_structures:
- name: Simscale Project Structure
  property_count: 0
  slug: simscale-project-structure
jsonld:
- class_count: 25
  name: Simscale Context
  property_count: 4
  slug: simscale-context
layout: provider
modified: '2026-05-02'
name: SimScale
nav: Providers
network: true
overview: 'SimScale publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Geometry API, Mesh Operations API, Projects API, and 4 more. Tagged areas include CAE, CFD, FEA, Simulation, and Engineering.


  The SimScale catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SimScale''s developer surface includes authentication, engineering blog, documentation, pricing, and 9 more developer resources.'
plans:
- name: Simscale Plans Pricing
  plan_count: 3
  slug: simscale-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Simscale Rate Limits
  slug: simscale-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SimScale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simscale-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: SimScale API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: simscale-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 62.7
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simscale/refs/heads/main/screenshots/simscale-2026-06-20T193939.png
security:
- kind: authentication
  name: Simscale Authentication
  slug: simscale-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Simscale Domain Security
  slug: simscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simscale Vulnerability Disclosure
  slug: simscale-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: simscale
tags:
- CAE
- CFD
- FEA
- Simulation
- Engineering
website: https://www.simscale.com/product/api/
---
