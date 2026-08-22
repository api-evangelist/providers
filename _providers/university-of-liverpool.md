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
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for the University of Liverpool Repository, an EPrints-based open-access archive of research outputs (journal articles, conference papers, theses, reports, an
  name: University of Liverpool Repository OAI-PMH
  slug: repository-oai
- description: OAI-PMH 2.0 metadata-harvesting interface for DataCat, the University of Liverpool research data catalogue (EPrints-based), exposing metadata records for finalised research datasets. Verified live and
  name: DataCat Research Data Catalogue OAI-PMH
  slug: datacat-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-liverpool-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liverpool.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/livuni
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-liverpool/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-liverpool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-liverpool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-liverpool-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Liverpool is a public research university in Liverpool, United Kingdom, a founding member of the Russell Group, ranked #165 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on scholarly and research-data infrastructure rather than a unified developer portal: the EPrints-based University of Liverpool Repository and the DataCat research data catalogue both expose live OAI-PMH metadata-harvesting interfaces. No general-purpose public API developer portal, course/timetable API, or self-service API key program was found to be publicly documented at the time of review; most institutional systems (SSO/IdP, student administration, mobile backends) sit behind authentication and are not publicly cataloged.'
finops:
- name: University Of Liverpool Finops
  service_category: Education
  slug: university-of-liverpool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-liverpool.png
jsonld:
- class_count: 21
  name: University Of Liverpool Context
  property_count: 6
  slug: university-of-liverpool-context
layout: provider
modified: '2026-06-03'
name: University of Liverpool
nav: Providers
network: true
overview: 'University of Liverpool publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Liverpool catalog on APIs.io includes 1 JSON-LD context.


  University of Liverpool''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: University Of Liverpool Plans Pricing
  plan_count: 2
  slug: university-of-liverpool-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: University Of Liverpool Rate Limits
  slug: university-of-liverpool-rate-limits
score:
  band: emerging
  composite: 17.8
  delta: -1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-liverpool/refs/heads/main/screenshots/university-of-liverpool-2026-06-20T200201.png
security:
- kind: domain-security
  name: University Of Liverpool Domain Security
  slug: university-of-liverpool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-liverpool
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- OAI-PMH
- United Kingdom
website: https://www.liverpool.ac.uk/
---
