---
access_model:
  confidence: high
  label: Free and open · no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: 'The University of Leeds institutional research data repository, running EPrints 3 on the university''s own infrastructure, with a live unauthenticated OAI-PMH 2.0 interface. Verified 2026-08-30: Identi'
  name: Research Data Leeds Repository (OAI-PMH)
  slug: research-data-oai
- description: A second, separate institution-run EPrints deployment holding digitised Special Collections — Bronte, incunabula, the Liddle Collection, cookery, history of science, the Leeds Permanent Library. It ex
  name: Leeds Digital Library (OAI-PMH and OpenSearch)
  slug: digital-library
- description: 'The data layer behind the University of Leeds Libraries wayfinding application, published as two unauthenticated static JSON documents. spaces.json returned 68 campus and library spaces on 2026-08-30 '
  name: Spacefinder Campus Space Data
  slug: spacefinder
- description: A static IIIF Image API level 0 service on the institution's own host, serving high-resolution floor plans for the Brotherton, Edward Boyle, Health Sciences and Laidlaw libraries in "original" and "cr
  name: Library Floor Plans IIIF Image API
  slug: library-floorplans-iiif
- description: 'RELATIONSHIP, NOT A CONTRACT. University of Leeds Libraries discovery and resource management run on the Ex Libris Alma library services platform with the Primo discovery layer. The tenancy is a real '
  name: Library Search (Ex Libris Alma / Primo) — tenancy
  slug: library-discovery-primo
- description: RELATIONSHIP, NOT A CONTRACT. Leeds' scholarly publications repository is White Rose Research Online, a shared EPrints platform operated by the White Rose University Consortium on behalf of Leeds, She
  name: White Rose Research Online (OAI-PMH) — consortium tenancy
  slug: white-rose-research-online
artifact_total: 16
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/uol-library/spacefinder/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.leeds.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uol-library
- group: build
  title: ''
  type: GitHub
  url: https://github.com/arc-leeds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-leeds/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leeds.ac.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leeds.ac.uk/privacy
- group: operate
  title: ''
  type: Support
  url: https://it.leeds.ac.uk/it
- group: company
  title: ''
  type: Blog
  url: https://library.leeds.ac.uk/news
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalogue.leeds.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://archive.researchdata.leeds.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://leeds.primo.exlibrisgroup.com/discovery/search?vid=44LEE_INST:VU1
- group: other
  title: ''
  type: OpenData
  url: https://spacefinder.leeds.ac.uk/spaces.json
- group: other
  title: ''
  type: ResearchComputing
  url: https://arcdocs.leeds.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://generative-ai.leeds.ac.uk/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-leeds-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-leeds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-leeds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-leeds-finops.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-leeds-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-leeds-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-leeds-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-leeds-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-leeds-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-leeds-rules.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Leeds is a public research university in Leeds, United Kingdom, a member of the Russell Group, with more than 34,000 students and over 7,000 staff. Its programmable footprint is small, real, and almost entirely the work of one department: University of Leeds Libraries. Four surfaces were verified live on 2026-08-30 and every one of them runs on a leeds.ac.uk host under the institution''s own operation — two self-hosted EPrints repositories exposing OAI-PMH 2.0 (Research Data Leeds, and the Digital Library of digitised Special Collections), a IIIF Image API level 0 service behind the library floor plans, and Spacefinder, an unauthenticated JSON dataset of 68 campus study spaces with geolocation, opening hours, facilities and accessibility. All four are anonymous, keyless and read-only. There is no central developer portal, no API gateway, no registration, no status page, no changelog and no published OpenAPI — the four OpenAPI documents in this repository were
  derived by API Evangelist from probed responses, not published by Leeds. Library discovery is an Ex Libris Alma/Primo tenancy and the university''s publications repository is White Rose Research Online, a three-university consortium platform; both are recorded here as tenant relationships, not as Leeds contracts. Advanced Research Computing (ARC) operates the Aire HPC service for researchers, but its allocation and service surfaces are behind institutional login.'
examples:
- key_count: 9
  name: University Of Leeds Floorplans Iiif Info Example
  slug: university-of-leeds-floorplans-iiif-info-example
finops:
- name: University Of Leeds Finops
  service_category: Education
  slug: university-of-leeds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-leeds.png
json_schemas:
- name: University of Leeds Spacefinder Space
  property_count: 28
  slug: university-of-leeds-spacefinder-space
jsonld:
- class_count: 23
  name: University Of Leeds Context
  property_count: 2
  slug: university-of-leeds-context
layout: provider
modified: '2026-08-30'
name: University of Leeds
nav: Providers
network: true
overview: 'University of Leeds publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Research Data Leeds Repository (OAI-PMH), Leeds Digital Library (OAI-PMH and OpenSearch), Spacefinder Campus Space Data, and 1 more. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The University of Leeds catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Leeds'' developer surface includes GitHub presence, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: University Of Leeds Plans Pricing
  plan_count: 2
  slug: university-of-leeds-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Leeds Rate Limits
  slug: university-of-leeds-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of Leeds API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-leeds-rules
scopes:
- name: University Of Leeds Scopes
  scope_count: 0
  slug: university-of-leeds-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -14.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 3.8
    contract_quality: 25.8
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 3.8
    operational_transparency: 7.9
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
security:
- kind: authentication
  name: University Of Leeds Authentication
  slug: university-of-leeds-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Leeds Domain Security
  slug: university-of-leeds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-leeds
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Research Data
- Research Repository
- Libraries
- Open Data
- OAI-PMH
- IIIF
- Research Computing
- Digital Collections
website: https://www.leeds.ac.uk/
---
