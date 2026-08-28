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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Public DSpace 8 REST API for Texas ScholarWorks, the UT Austin institutional repository of theses, dissertations, faculty research, and open-access scholarship. The API root reports "DSpace at UT Aust
  name: Texas ScholarWorks DSpace REST API
  slug: scholarworks-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for Texas ScholarWorks. An Identify request returns repositoryName "DSpace at UT Austin" with a baseURL of https://repositories.lib.utexas.edu/server/oai/reque
  name: Texas ScholarWorks OAI-PMH Endpoint
  slug: scholarworks-oai
- description: UT Austin publishes and archives research datasets in the Texas Data Repository, a Dataverse instance hosted by the Texas Digital Library (shared across Texas institutions). The Dataverse REST API was
  name: Texas Data Repository (Dataverse) API
  slug: texas-data-repository
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-texas-at-austin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.utexas.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/utexas
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-texas-at-austin/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://it.utexas.edu/services/web-publishing-software-development
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-texas-at-austin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-texas-at-austin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-texas-at-austin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Texas at Austin is a flagship public research university in Austin, Texas, United States, ranked #65 in the QS World University Rankings 2025. Its public, machine-readable API footprint is concentrated in its library and research-data infrastructure rather than a single centralized developer portal. The UT Libraries operate Texas ScholarWorks, a DSpace 8 institutional repository exposing a public DSpace REST API and an OAI-PMH metadata-harvesting endpoint, and the university participates in the Texas Data Repository, a Dataverse instance hosted by the Texas Digital Library that offers a documented REST API. Enterprise integration APIs (the UT Austin API Registry / Identity and Access Management services) exist but are gated behind UT EID authentication and internal ServiceNow access.'
finops:
- name: University Of Texas At Austin Finops
  service_category: Education
  slug: university-of-texas-at-austin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-texas-at-austin.png
jsonld:
- class_count: 11
  name: University Of Texas At Austin Context
  property_count: 3
  slug: university-of-texas-at-austin-context
layout: provider
modified: '2026-06-03'
name: University of Texas at Austin
nav: Providers
network: true
overview: 'University of Texas at Austin publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The University of Texas at Austin catalog on APIs.io includes 1 JSON-LD context.


  University of Texas at Austin''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Texas At Austin Plans Pricing
  plan_count: 2
  slug: university-of-texas-at-austin-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of Texas At Austin Rate Limits
  slug: university-of-texas-at-austin-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: 4.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: University Of Texas At Austin Domain Security
  slug: university-of-texas-at-austin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-texas-at-austin
tags:
- Education
- Higher Education
- University
- Research
- Library
- Open Data
- Institutional Repository
- United States
- Texas
website: https://www.utexas.edu/
---
