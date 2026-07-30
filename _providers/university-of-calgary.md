---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: University Of Calgary Agentic Access
  operation_count: 67
  slug: university-of-calgary-agentic-access
  summary_line: 67 operations · 38 acting
api_count: 16
apis:
- description: PRISM is the University of Calgary's institutional repository, running on DSpace 8.3 (now served from ucalgary.scholaris.ca). It exposes the standard DSpace REST API for programmatic access to communi
  name: PRISM Institutional Repository (DSpace)
  slug: prism-dspace
- description: The University of Calgary's PRISM research-data repository is a Dataverse collection hosted on the Borealis (Canadian Dataverse) platform, exposing the public Dataverse REST API (Borealis runs Dataver
  name: PRISM Research Data Repository (Borealis Dataverse)
  slug: prism-dataverse
- description: The Application.wadl API from University of Calgary — 2 operation(s) for application.wadl.
  name: University of Calgary Application.wadl API
  slug: university-of-calgary-application-wadl-api
- description: Endpoints to utilize the Auroral Transport Model
  name: University of Calgary Auroral Transport Model (ATM) API
  slug: university-of-calgary-auroral-transport-model-atm-api
- description: Authenticate via email and password to get an Access Token. Use your API Key if you are building software without user interaction to run against the API.
  name: University of Calgary Authenticate API
  slug: university-of-calgary-authenticate-api
- description: Retrieve information about data in the database
  name: University of Calgary Availability API
  slug: university-of-calgary-availability-api
- description: Search for conjunctions between multiple sets of data sources
  name: University of Calgary Conjunction Search API
  slug: university-of-calgary-conjunction-search-api
- description: Endpoints supporting data distribution
  name: University of Calgary Data Distribution API
  slug: university-of-calgary-data-distribution-api
- description: Search for data products
  name: University of Calgary Data Products Search API
  slug: university-of-calgary-data-products-search-api
- description: Interact with data sources
  name: University of Calgary Data Sources API
  slug: university-of-calgary-data-sources-api
- description: Search ephemeris records
  name: University of Calgary Ephemeris Search API
  slug: university-of-calgary-ephemeris-search-api
- description: Operations relating to managing ephemeris and data products data
  name: University of Calgary Manage Data API
  slug: university-of-calgary-manage-data-api
- description: Endpoints for Scientist In The Loop (SITL) operations
  name: University of Calgary Operations - SITL API
  slug: university-of-calgary-operations-sitl-api
- description: Endpoints providing real-time data streams
  name: University of Calgary Real-Time Data API
  slug: university-of-calgary-real-time-data-api
- description: Various helper endpoints
  name: University of Calgary Utilities API
  slug: university-of-calgary-utilities-api
- description: Various utilities
  name: University of Calgary Utils API
  slug: university-of-calgary-utils-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-calgary-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-calgary-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-calgary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-calgary-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucalgary.ca/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucalgary
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/ucalgary/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://libguides.ucalgary.ca/apis
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-calgary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-calgary-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-calgary-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-calgary-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-calgary-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-calgary-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.ucalgary.ca/news/rss.xml
created: '2026-06-03'
description: 'The University of Calgary is a public research university in Calgary, Alberta, Canada, ranked #198 in the QS World University Rankings 2025. Its public, documented developer footprint centers on research and scholarly infrastructure rather than a single central developer portal: the Space Remote Sensing (SRS) group operates a documented RESTful API at api.phys.ucalgary.ca and the related AuroraX auroral-science API at api.aurorax.space, with Python and IDL client libraries. The institutional repository PRISM runs on DSpace 8.3 (REST API plus OAI-PMH) and the PRISM research-data repository is hosted on the Borealis Dataverse platform, which exposes a public Dataverse REST API. The university also maintains a GitHub organization and a library guide cataloging third-party scholarly APIs.'
examples:
- key_count: 11
  name: University Of Calgary Datasets Example
  slug: university-of-calgary-datasets-example
finops:
- name: University Of Calgary Finops
  service_category: Education
  slug: university-of-calgary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-calgary.png
json_schemas:
- name: DataSource
  property_count: 6
  slug: university-of-calgary-data-source
- name: Dataset
  property_count: 11
  slug: university-of-calgary-dataset
- name: Observatory
  property_count: 4
  slug: university-of-calgary-observatory
json_structures:
- name: University Of Calgary Data Source Structure
  property_count: 6
  slug: university-of-calgary-data-source-structure
- name: University Of Calgary Dataset Structure
  property_count: 10
  slug: university-of-calgary-dataset-structure
jsonld:
- class_count: 23
  name: University Of Calgary Context
  property_count: 2
  slug: university-of-calgary-context
layout: provider
modified: '2026-06-03'
name: University of Calgary
nav: Providers
network: true
overview: 'University of Calgary publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Application.wadl API, Auroral Transport Model (ATM) API, Authenticate API, and 11 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Calgary catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Calgary''s developer surface includes authentication, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: University Of Calgary Plans Pricing
  plan_count: 2
  slug: university-of-calgary-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 1
  name: University Of Calgary Rate Limits
  slug: university-of-calgary-rate-limits
rules:
- name: University of Calgary API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-calgary-jsonschema-spectral-rules
- name: University of Calgary API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: university-of-calgary-rules
score:
  band: developing
  composite: 43.0
  delta: -4.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-calgary/refs/heads/main/screenshots/university-of-calgary-2026-06-20T200144.png
security:
- kind: authentication
  name: University Of Calgary Authentication
  slug: university-of-calgary-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: University Of Calgary Domain Security
  slug: university-of-calgary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Calgary Vulnerability Disclosure
  slug: university-of-calgary-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-calgary
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Repository
- Space Physics
- Canada
website: https://www.ucalgary.ca/
---
