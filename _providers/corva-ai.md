---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.corva.ai
  baseurl_source: declared
  description: The Corva Platform API serves platform entities and their relationships — wells, rigs, drillout units, programs, pads and frac fleets, together with users, dashboards, alerts, apps, tasks, files and A
  name: Corva Platform API
  slug: corva-platform-api
- baseURL: https://data.corva.ai
  baseurl_source: declared
  description: The Corva Data API serves the records stored in Corva datasets — one-second operational data, engineering calculations and metrics, time- and depth-based datasets, reference datasets and aggregation q
  name: Corva Data API
  slug: corva-data-api
- description: Corva Dev Center is an SDK and app hosting environment for building custom applications on top of Corva data assets. It provides Python and JavaScript SDKs, UI component libraries, app templates (fron
  name: Corva Dev Center
  slug: corva-dev-center-api
artifact_total: 9
asyncapis:
- description: ''
  name: Corva Ai Event Surface
  slug: corva-ai-event-surface
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/corva-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corva-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corva.ai/
- group: other
  title: ''
  type: Platform
  url: https://www.corva.ai/platform
- group: other
  title: ''
  type: DevCenter
  url: https://www.corva.ai/platform/dev-center
- group: docs
  title: ''
  type: DevCenterDocs
  url: https://dc-docs.corva.ai/docs/intro
- group: operate
  title: ''
  type: Community
  url: https://community.corva.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corva-ai
- group: other
  title: ''
  type: Drilling
  url: https://www.corva.ai/energy/drilling
- group: other
  title: ''
  type: Completions
  url: https://www.corva.ai/energy/completions
- group: other
  title: ''
  type: Geoscience
  url: https://www.corva.ai/energy/geoscience
- group: other
  title: ''
  type: Sustainability
  url: https://www.corva.ai/energy/sustainability
- group: company
  title: ''
  type: Careers
  url: https://www.corva.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.corva.ai/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/corvaai
- group: company
  title: ''
  type: Blog
  url: https://www.corva.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/corva/
- group: company
  title: ''
  type: Newsroom
  url: https://www.corva.ai/company/insights
- group: docs
  title: ''
  type: Documentation
  url: https://dc-docs.corva.ai/docs/intro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dc-docs.corva.ai/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://dc-docs.corva.ai/docs/API/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://dc-docs.corva.ai/docs/API/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.corva.ai/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.corva.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.corva.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corva.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corva.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.corva.ai/acceptable-use-policy
- group: company
  title: ''
  type: About
  url: https://www.corva.ai/company/about-corva-real-time-energy-data-solutions
- group: build
  title: ''
  type: Packages
  url: packages/corva-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/corva-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/corva-ai-cli.yml
- group: design
  title: ''
  type: Components
  url: components/corva-ai-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corva-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corva-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/corva-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/corva-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corva-ai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/corva-ai-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/corva-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/corva-ai-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corva-ai-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/corva-ai-mcp.yml
- group: other
  title: ''
  type: X-EventSurface
  url: asyncapi/corva-ai-event-surface.yml
- group: agent
  title: ''
  type: X-WellKnownProbe
  url: well-known/corva-ai-well-known.yml
created: '2024-07-02'
description: 'Corva is a Houston-based AI software company providing a real-time drilling, completions, geoscience and sustainability analytics platform for upstream oil and gas. Corva ingests rig sensor and operational data and exposes it through TWO REST APIs on two hosts: the Platform API at api.corva.ai (wells, rigs, pads, programs, frac fleets, users, dashboards, alerts and apps; 513 paths and 771 operations described by a published Swagger 2.0 contract) and the Data API at data.corva.ai (time, depth, reference and timeseries dataset records, aggregations and permitted customer writes; described by a published OpenAPI 3.1 contract). Corva Dev Center is an SDK and app-hosting environment where customers build frontend, backend, scheduled, stream and task applications on Corva data, with a Python SDK, npm component libraries and a public app marketplace. Access is enterprise-only: there is no public pricing, no free tier and no self-serve signup, and API key creation is not enabled by
  default for most customer users.'
finops:
- name: Corva Ai Finops
  service_category: API
  slug: corva-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corva-ai.png
layout: provider
modified: '2026-09-05'
name: Corva AI
nav: Providers
network: true
overview: 'Corva AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Corva Platform API and Corva Data API. Tagged areas include Analytics, Artificial Intelligence, Completions, Custom Apps, and Data API.


  The Corva AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Corva AI''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, CLI, and 39 more developer resources.'
plans:
- name: Corva Ai Plans Pricing
  plan_count: 0
  slug: corva-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Corva Ai Rate Limits
  slug: corva-ai-rate-limits
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 32.4
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 70.8
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/corva-ai/refs/heads/main/screenshots/corva-ai-2026-06-20T175049.png
security:
- kind: authentication
  name: Corva Ai Authentication
  slug: corva-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Corva Ai Domain Security
  slug: corva-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corva-ai
tags:
- Analytics
- Artificial Intelligence
- Completions
- Custom Apps
- Data API
- Dev Center
- Dev Center Apps
- Drilling
- Energy
- Geoscience
- Oil and Gas
- Platform API
- Predictive Drilling
- Python SDK
- Real-Time
- Real-Time Analytics
- Sensor Data
- Sustainability
- Time Series
- WITS
- Well Data
website: https://www.corva.ai/
---
