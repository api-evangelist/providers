---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pennsylvania State University Agentic Access
  operation_count: 6
  slug: pennsylvania-state-university-agentic-access
  summary_line: 6 operations
api_count: 7
apis:
- description: Penn State University Libraries' faculty and research metadata service, maintained with OSVPR and West Arete. Publishes cleaned researcher metadata (publications, presentations, performances, advising
  name: Researcher Metadata Database (RMD) API
  slug: rmd
- description: Penn State Information Technology operates a web developer portal that catalogs internal REST services and events and lets developers find, subscribe to, and request elevated access for APIs. Document
  name: Penn State IT Web Developer Services
  slug: developer-portal
- description: University buildings and their facility attributes.
  name: Pennsylvania State University Buildings API
  slug: pennsylvania-state-university-buildings-api
- description: Penn State campus reference data.
  name: Pennsylvania State University Campuses API
  slug: pennsylvania-state-university-campuses-api
- description: Change events for buildings and rooms.
  name: Pennsylvania State University Events API
  slug: pennsylvania-state-university-events-api
- description: Service health and status.
  name: Pennsylvania State University Health API
  slug: pennsylvania-state-university-health-api
- description: Rooms within buildings.
  name: Pennsylvania State University Rooms API
  slug: pennsylvania-state-university-rooms-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LionSpaceFIS REST Buildings API
  slug: open-pennsylvania-state-university-buildings-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Campuses API
  slug: open-pennsylvania-state-university-campuses-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Events API
  slug: open-pennsylvania-state-university-events-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Health API
  slug: open-pennsylvania-state-university-health-api
- collection_type: open
  name: LionSpaceFIS REST Buildings Rooms API
  slug: open-pennsylvania-state-university-rooms-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pennsylvania-state-university-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pennsylvania-state-university-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pennsylvania-state-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pennsylvania-state-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.psu.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developer.psu.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PennState
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/psu-libraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/penn-state-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/pennsylvania-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pennsylvania-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pennsylvania-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Pennsylvania State University (Penn State) is a public, land-grant research university with its primary campus at University Park, PA, and is ranked #69 in the QS World University Rankings 2025. Its public developer footprint is centered on a Penn State IT web developer portal (docs.developer.psu.edu) that catalogs internal REST services such as PSU ID, Academic Course, Cornerstone, Sponsored Accounts, and ASR Lookup, though those API reference pages sit behind Shibboleth/WebAccess single sign-on. Publicly reachable APIs include the Office of Physical Plant LionSpaceFIS facilities REST API and the University Libraries Researcher Metadata Database (RMD), which exposes researcher/publication metadata via an OpenAPI-described REST API gated by a license key. Penn State also maintains public open-source GitHub organizations.'
examples:
- key_count: 2
  name: Pennsylvania State University Gethealth Example
  slug: pennsylvania-state-university-getHealth-example
- key_count: 2
  name: Pennsylvania State University Listbuildings Example
  slug: pennsylvania-state-university-listBuildings-example
- key_count: 2
  name: Pennsylvania State University Listrooms Example
  slug: pennsylvania-state-university-listRooms-example
finops:
- name: Pennsylvania State University Finops
  service_category: Education
  slug: pennsylvania-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pennsylvania-state-university.png
json_schemas:
- name: Building
  property_count: 21
  slug: pennsylvania-state-university-building
- name: Room
  property_count: 22
  slug: pennsylvania-state-university-room
json_structures:
- name: Pennsylvania State University Building Structure
  property_count: 21
  slug: pennsylvania-state-university-building-structure
- name: Pennsylvania State University Room Structure
  property_count: 22
  slug: pennsylvania-state-university-room-structure
jsonld:
- class_count: 24
  name: Pennsylvania State University Context
  property_count: 0
  slug: pennsylvania-state-university-context
layout: provider
modified: '2026-06-03'
name: Pennsylvania State University
nav: Providers
network: true
overview: 'Pennsylvania State University publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Buildings API, Campuses API, Events API, and 2 more. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Pennsylvania State University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Pennsylvania State University''s developer surface includes GitHub presence and 12 more developer resources.'
plans:
- name: Pennsylvania State University Plans Pricing
  plan_count: 2
  slug: pennsylvania-state-university-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Pennsylvania State University Rate Limits
  slug: pennsylvania-state-university-rate-limits
rules:
- name: Pennsylvania State University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pennsylvania-state-university-jsonschema-spectral-rules
- name: Pennsylvania State University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: pennsylvania-state-university-rules
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 66.4
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pennsylvania-state-university/refs/heads/main/screenshots/pennsylvania-state-university-2026-06-20T191542.png
security:
- kind: domain-security
  name: Pennsylvania State University Domain Security
  slug: pennsylvania-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pennsylvania State University Vulnerability Disclosure
  slug: pennsylvania-state-university-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pennsylvania State University Trust Center
  slug: pennsylvania-state-university-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: pennsylvania-state-university
tags:
- Education
- Higher Education
- University
- Research
- Library
- Facilities
- United States
website: https://www.psu.edu/
---
