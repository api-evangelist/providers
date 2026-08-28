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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ucd Agentic Access
  operation_count: 14
  slug: ucd-agentic-access
  summary_line: 14 operations
api_count: 9
apis:
- description: The UCD Digital Library Data Services expose IIIF Image API 2.0 and Presentation API 2.0 endpoints serving images and manifests for digitized cultural-heritage objects and collections, consumable by I
  name: UCD Digital Library Image & Presentation API (IIIF)
  slug: digital-library-iiif
- description: Geospatial Data API for the UCD Digital Library, providing boundary and search data for map visualisations (used with LeafletJS) via geoFilter and geoBounds query parameters, alongside an unAPI metada
  name: UCD Digital Library Geospatial Data API
  slug: digital-library-geospatial
- description: Research Repository UCD is the institution's green open-access scholarly repository, built on DSpace-CRIS. It provides an OAI-PMH harvesting interface and the DSpace REST API for programmatic access t
  name: Research Repository UCD (DSpace OAI-PMH / REST)
  slug: research-repository
- description: The CBÉ API from University College Dublin — 2 operation(s) for cbé.
  name: University College Dublin CBÉ API
  slug: ucd-cb-api
- description: The CBÉD API from University College Dublin — 3 operation(s) for cbéd.
  name: University College Dublin CBÉD API
  slug: ucd-cb-d-api
- description: The CBÉG API from University College Dublin — 3 operation(s) for cbég.
  name: University College Dublin CBÉG API
  slug: ucd-cb-g-api
- description: The CBÉS API from University College Dublin — 3 operation(s) for cbés.
  name: University College Dublin CBÉS API
  slug: ucd-cb-s-api
- description: The Metadata API from University College Dublin — 1 operation(s) for metadata.
  name: University College Dublin Metadata API
  slug: ucd-metadata-api
- description: The Reference API from University College Dublin — 2 operation(s) for reference.
  name: University College Dublin Reference API
  slug: ucd-reference-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ API
  slug: open-ucd-cb-api
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ CBÉD API
  slug: open-ucd-cb-d-api
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ CBÉG API
  slug: open-ucd-cb-g-api
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ CBÉS API
  slug: open-ucd-cb-s-api
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ Metadata API
  slug: open-ucd-metadata-api
- collection_type: open
  name: Dúchas API (National Folklore Collection, UCD) CBÉ Reference API
  slug: open-ucd-reference-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucd.ie/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/University-College-Dublin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-college-dublin/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.ucd.ie/help/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucd-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University College Dublin (UCD) is Ireland''s largest university and ranks #126 in the QS World University Rankings 2025. Its public, machine-readable footprint is concentrated in library and cultural-heritage systems rather than a central developer portal: the UCD Digital Library exposes IIIF Image and Presentation APIs plus a Geospatial Data API and unAPI endpoint, the DSpace-based Research Repository UCD offers OAI-PMH harvesting and a REST API, and the National Folklore Collection held at UCD is served via the Dúchas API. There is no unified, self-service institutional API program; most administrative and identity systems are gated behind institutional affiliation.'
examples:
- key_count: 2
  name: Ucd Getmanuscriptvolumes Example
  slug: ucd-getManuscriptVolumes-example
- key_count: 2
  name: Ucd Getpersonbyid Example
  slug: ucd-getPersonById-example
- key_count: 2
  name: Ucd Getphotographbyid Example
  slug: ucd-getPhotographById-example
finops:
- name: Ucd Finops
  service_category: Education
  slug: ucd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucd.png
json_schemas:
- name: Duchas Person
  property_count: 14
  slug: ucd-person
- name: Duchas Photograph
  property_count: 24
  slug: ucd-photograph
- name: Duchas Volume
  property_count: 8
  slug: ucd-volume
json_structures:
- name: Ucd Person Structure
  property_count: 8
  slug: ucd-person-structure
- name: Ucd Photograph Structure
  property_count: 12
  slug: ucd-photograph-structure
- name: Ucd Volume Structure
  property_count: 6
  slug: ucd-volume-structure
jsonld:
- class_count: 23
  name: Ucd Context
  property_count: 6
  slug: ucd-context
layout: provider
modified: '2026-06-03'
name: University College Dublin
nav: Providers
network: true
overview: 'University College Dublin publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CBÉ API, CBÉD API, CBÉG API, and 3 more. Tagged areas include Education, Higher Education, University, Ireland, and Library.


  The University College Dublin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University College Dublin''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Ucd Plans Pricing
  plan_count: 2
  slug: ucd-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ucd Rate Limits
  slug: ucd-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: University College Dublin API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ucd-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: University College Dublin API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: ucd-rules
score:
  band: thin
  composite: 37.6
  delta: 3.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 60.1
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucd/refs/heads/main/screenshots/ucd-2026-08-17T130228.png
security:
- kind: authentication
  name: Ucd Authentication
  slug: ucd-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Ucd Domain Security
  slug: ucd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ucd
tags:
- Education
- Higher Education
- University
- Ireland
- Library
- Digital Library
- IIIF
- Open Access
- Cultural Heritage
website: https://www.ucd.ie/
---
