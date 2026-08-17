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
  name: Yale Agentic Access
  operation_count: 6
  slug: yale-agentic-access
  summary_line: 6 operations
api_count: 8
apis:
- description: Returns public information for course offerings (course sections) for a given termCode and subjectCode, including titles, descriptions, instructors, meeting times, prerequisites and distributional des
  name: Courses Web Service v3
  slug: courses
- description: The Yale API Portal is the discovery hub for Yale's enterprise (SOA), portal and vendor/third-party APIs. Portal APIs include Buildings (name and location of Yale campus buildings), Courses, Course Su
  name: Yale API Portal (Enterprise & Portal APIs)
  slug: portal
- description: Yale University Library publishes International Image Interoperability Framework (IIIF) manifests for objects in its digital collections, enabling interoperable viewing and reuse of digitized images a
  name: Yale Digital Collections IIIF
  slug: iiif
- description: Search configuration metadata
  name: Yale University Configuration API
  slug: yale-configuration-api
- description: Linked Art JSON-LD document retrieval
  name: Yale University Documents API
  slug: yale-documents-api
- description: Faceted aggregation over search results
  name: Yale University Facets API
  slug: yale-facets-api
- description: Related entity discovery
  name: Yale University Related API
  slug: yale-related-api
- description: Search and discovery across LUX scopes
  name: Yale University Search API
  slug: yale-search-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LUX Yale Collections Discovery Configuration API
  slug: open-yale-configuration-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Documents API
  slug: open-yale-documents-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Facets API
  slug: open-yale-facets-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Related API
  slug: open-yale-related-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Search API
  slug: open-yale-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yale.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yale.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/yalelibrary
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/project-lux
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/yale-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/yale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yale-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://news.yale.edu/news-rss
created: '2026-06-03'
description: 'Yale University is a private Ivy League research university in New Haven, Connecticut, United States, ranked #17 in the QS World University Rankings 2025. Its public developer footprint centers on the Yale API Portal (developers.yale.edu), which exposes enterprise (SOA) and portal APIs such as the Courses Web Service and Buildings service behind an API key gated to holders of a valid Yale netid. Yale also operates LUX, a large public cross-collection discovery platform built on Linked Art / IIIF that serves JSON-LD data and a search API across more than 41 million cultural-heritage records, and publishes IIIF manifests for its digital library collections. Source code for LUX and many library systems is openly available on GitHub.'
examples:
- key_count: 2
  name: Yale Getdocument Example
  slug: yale-getDocument-example
- key_count: 2
  name: Yale Search Example
  slug: yale-search-example
- key_count: 2
  name: Yale Searchestimate Example
  slug: yale-searchEstimate-example
finops:
- name: Yale Finops
  service_category: Education
  slug: yale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yale.png
json_schemas:
- name: LUX Linked Art Entity
  property_count: 14
  slug: yale-linkedartentity
- name: LUX OrderedCollection
  property_count: 8
  slug: yale-orderedcollection
- name: LUX OrderedCollectionPage
  property_count: 7
  slug: yale-orderedcollectionpage
json_structures:
- name: Yale Linkedartentity Structure
  property_count: 13
  slug: yale-linkedartentity-structure
- name: Yale Orderedcollectionpage Structure
  property_count: 7
  slug: yale-orderedcollectionpage-structure
jsonld:
- class_count: 10
  name: Yale Context
  property_count: 17
  slug: yale-context
layout: provider
modified: '2026-06-03'
name: Yale University
nav: Providers
network: true
overview: 'Yale University publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Documents API, Facets API, and 2 more. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Yale University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yale University''s developer surface includes GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Yale Plans Pricing
  plan_count: 2
  slug: yale-plans-pricing
random_paper: 129
rate_limits:
- limit_count: 1
  name: Yale Rate Limits
  slug: yale-rate-limits
rules:
- name: Yale University API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yale-jsonschema-spectral-rules
- name: Yale University API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: yale-rules
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.4
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/yale/refs/heads/main/screenshots/yale-2026-06-20T201720.png
security:
- kind: domain-security
  name: Yale Domain Security
  slug: yale-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: yale
tags:
- Education
- Higher Education
- University
- Research
- Library
- Cultural Heritage
- Linked Data
- United States
website: https://www.yale.edu/
---
