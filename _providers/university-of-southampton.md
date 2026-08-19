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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Public SPARQL query endpoint for the University of Southampton Open Data Service, backed by a triple store (Sesame) with an arc2 front end. Allows querying of campus, building, organizational, catalog
  name: Open Data Service SPARQL Endpoint
  slug: open-data-sparql
- description: Linked open data published at data.southampton.ac.uk. Resource pages offer machine-readable representations via content negotiation and "get the data" links in RDF/XML (.rdf), Turtle (.ttl), N-Triples
  name: Open Data Linked Data (RDF) Service
  slug: open-data-linked-data
- description: OAI-PMH metadata harvesting interface for ePrints Soton, the University's institutional research repository, built on the EPrints platform (originally developed at Southampton). The repository is read
  name: ePrints Soton OAI-PMH Interface
  slug: eprints-oai-pmh
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-southampton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.southampton.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/southampton
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-southampton/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.southampton.ac.uk/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/southampton
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-southampton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-southampton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-southampton-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.soton.ac.uk/data/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.soton.ac.uk/data/feed/
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-southampton-context.jsonld
created: '2026-06-03'
description: 'The University of Southampton is a public research university in Southampton, United Kingdom, ranked #70 in the QS World University Rankings 2025. It is a founding member of the Russell Group and a recognized pioneer of open and linked data in higher education. Its developer/API footprint is centered on the University of Southampton Open Data Service (data.southampton.ac.uk), which publishes campus, building, organizational, catalogue, and facilities data as linked data with a public SPARQL endpoint and multiple machine-readable formats (RDF/XML, Turtle, N-Triples, CSV, KML, ICS). The University is also the home of the EPrints open-source repository platform; its institutional research repository (ePrints Soton) exposes an OAI-PMH metadata harvesting interface. There is no single unified commercial API developer portal; access is open and standards-based rather than key-gated.'
finops:
- name: University Of Southampton Finops
  service_category: Education
  slug: university-of-southampton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-southampton.png
jsonld:
- class_count: 6
  name: University Of Southampton Context
  property_count: 8
  slug: university-of-southampton-context
layout: provider
modified: '2026-06-03'
name: University of Southampton
nav: Providers
network: true
overview: 'University of Southampton publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Linked Data.


  The University of Southampton catalog on APIs.io includes 1 JSON-LD context.


  University of Southampton''s developer surface includes GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: University Of Southampton Plans Pricing
  plan_count: 2
  slug: university-of-southampton-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 1
  name: University Of Southampton Rate Limits
  slug: university-of-southampton-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: -1.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-southampton/refs/heads/main/screenshots/university-of-southampton-2026-06-20T200226.png
security:
- kind: domain-security
  name: University Of Southampton Domain Security
  slug: university-of-southampton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-southampton
tags:
- Education
- Higher Education
- University
- Open Data
- Linked Data
- SPARQL
- OAI-PMH
- Research
- United Kingdom
website: https://www.southampton.ac.uk/
---
