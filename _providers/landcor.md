---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: verified
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
  score: 26.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Landcor Agentic Access
  operation_count: 12
  slug: landcor-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.landcor.com
  baseurl_source: declared
  description: The AVM Summary API from Landcor Data — 1 operation(s) for avm summary.
  name: Landcor Data AVM Summary API
  slug: landcor-avm-summary-api
- baseURL: https://api.landcor.com
  baseurl_source: declared
  description: The Comparables API from Landcor Data — 1 operation(s) for comparables.
  name: Landcor Data Comparables API
  slug: landcor-comparables-api
- baseURL: https://api.landcor.com
  baseurl_source: declared
  description: The Health API from Landcor Data — 1 operation(s) for health.
  name: Landcor Data Health API
  slug: landcor-health-api
- baseURL: https://api.landcor.com
  baseurl_source: declared
  description: The Property API from Landcor Data — 4 operation(s) for property.
  name: Landcor Data Property API
  slug: landcor-property-api
- baseURL: https://api.landcor.com
  baseurl_source: declared
  description: The Valuation API from Landcor Data — 5 operation(s) for valuation.
  name: Landcor Data Valuation API
  slug: landcor-valuation-api
arazzos:
- description: Resolve a BC street address to a Landcor PID, then pull property detail, the AVM valuation range and the valuation history.
  name: Landcor — address to valuation
  slug: landcor-address-to-valuation
- description: Run a proposed mortgage amount against Landcor's AVM value for a BC property and retrieve the password-protected PDF valuation report for the file.
  name: Landcor — loan-to-value check and valuation report
  slug: landcor-ltv-check-and-report
artifact_total: 11
collections:
- collection_type: open
  name: Landcor Property API
  slug: open-landcor-property-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/landcor-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/landcor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landcor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/landcor-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.landcor.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.landcor.com/redoc
- group: design
  title: ''
  type: Conventions
  url: conventions/landcor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landcor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landcor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/landcor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landcor-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/landcor-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/landcor-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/landcor-address-to-valuation.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/landcor-ltv-check-and-report.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landcor-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/landcor-property-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/landcor-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.landcor.com/
- group: other
  title: ''
  type: Products
  url: https://www.landcor.com/online-property-tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landcor.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://store.landcor.com/user/user_add.aspx
- group: start
  title: ''
  type: Login
  url: https://store.landcor.com/user/login.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.landcor.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.landcor.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.landcor.com/about-us/landcor-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.landcor.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landcor.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landcor.com/acceptable-use/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.landcor.com/security-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Landcor
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/landcor-data-corporation
created: '2026-07-26'
description: 'Landcor Data Corporation is a New Westminster, British Columbia property data and automated valuation company, founded in 2000, that sells residential valuations, assessment detail and land title documents across the roughly 1.9 million residential properties in BC. It sits in the valuation and public-record layer of the Canadian value chain rather than the listings layer: its inputs are BC Assessment detail, Land Title and Survey Authority (LTSA) title and document search, BC Registry Services, municipal tax certificates and materials licensed from the Integrated Cadastral Information Society (ICIS), and its outputs are the Valuator AVM report, the Adjusted Value Profiler, the Property Profiler, Title Search Plus and historic valuation reports sold to lenders, appraisers, notaries, insurers and brokerages. Its API posture is the unusual case in this study: a real, live, anonymously readable machine-readable contract exists with no developer programme around it. The host api.landcor.com
  runs a FastAPI service on Azure App Service in Canada Central that serves a valid OpenAPI 3.1.0 document titled "Landcor Property API" version 0.1.0 at /openapi.json, with Swagger UI at /docs and ReDoc at /redoc, all returning HTTP 200 without credentials. Twelve operations cover property search, property detail, PDF report retrieval, valuation range, valuation history, loan-to-value checks, neighbourhood sales series, comparables, address autocomplete and an AVM narrative summary. Every operation except /health requires an HTTP Bearer token and returns 401 "Missing token" without one, and no route to obtain that token is published anywhere: landcor.com carries no developer, API, partner or data-licensing page, does not link api.landcor.com at all, and the store.landcor.com self-serve account is for buying individual reports through the web store, not for API credentials. RESO is absent, which is the expected Canadian answer. Landcor is not among the nineteen Canadian organizations RESO
  lists as members, holds no Web API or Data Dictionary certification, exposes no OData $metadata document, and uses its own PID identifier rather than the RESO Universal Property Identifier. No open, unlicensed dataset is published: the underlying assessment, title and cadastral data is licensed to Landcor from provincial bodies and resold, so the public record itself is a commercial product here.'
image: https://www.landcor.com/wp-content/uploads/2026/01/favicon-152.png
layout: provider
modified: '2026-07-26'
name: Landcor Data
nav: Providers
network: true
overview: 'Landcor Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AVM Summary API, Comparables API, Health API, and 2 more. Tagged areas include Real-Estate, Canada, Valuation, AVM, and Property Records.


  Landcor Data''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 26 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/landcor/refs/heads/main/screenshots/landcor-2026-08-07T171419.png
security:
- kind: authentication
  name: Landcor Authentication
  slug: landcor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Landcor Domain Security
  slug: landcor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: landcor
tags:
- Real-Estate
- Canada
- Valuation
- AVM
- Property Records
- Title
- Land Registry
- Mortgage
- PropTech
- Property Data
website: https://www.landcor.com/
---
