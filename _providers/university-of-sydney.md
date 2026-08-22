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
- description: The University of Sydney's institutional repository, Sydney eScholarship, exposes an OAI-PMH metadata harvesting interface for open-access theses, research outputs, and digital collections. The interf
  name: Sydney eScholarship Repository (OAI-PMH)
  slug: escholarship-oai
- description: The University of Sydney Library runs on the Ex Libris Alma library services platform with the Primo discovery layer. Ex Libris provides documented Alma REST APIs and Primo Search/PNX APIs, but access
  name: Library Discovery (Ex Libris Primo / Alma)
  slug: primo-alma
- description: 'The myUni student portal is backed by internal JSON APIs (for example student degrees and credits) used by the authenticated student web application. These endpoints require an active student session '
  name: myUni Student Portal API (gated)
  slug: myuni
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sydney-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sydney.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Sydney-Informatics-Hub
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-sydney/
- group: build
  title: ''
  type: Library
  url: https://www.library.sydney.edu.au/
- group: start
  title: ''
  type: ServicePortal
  url: https://sydneyuni.service-now.com/sm
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sydney-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sydney-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sydney-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Sydney is Australia''s first university, founded in 1850, and is ranked #32 in the QS World University Rankings 2025. Its public digital footprint centers on student, library, and research-data services rather than a formal, openly documented developer API program. The library runs on Ex Libris Alma and Primo (which expose vendor APIs and OAI-PMH), the Sydney eScholarship Repository offers an OAI-PMH metadata interface, and the myUni student portal is backed by internal authenticated APIs. Most institutional APIs are gated behind authentication or vendor key issuance, and no central public developer portal was found at time of review.'
finops:
- name: University Of Sydney Finops
  service_category: Education
  slug: university-of-sydney-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sydney.png
jsonld:
- class_count: 9
  name: University Of Sydney Context
  property_count: 9
  slug: university-of-sydney-context
layout: provider
modified: '2026-06-03'
name: University of Sydney
nav: Providers
network: true
overview: 'University of Sydney publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Library, and Research.


  The University of Sydney catalog on APIs.io includes 1 JSON-LD context.


  University of Sydney''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Sydney Plans Pricing
  plan_count: 2
  slug: university-of-sydney-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Sydney Rate Limits
  slug: university-of-sydney-rate-limits
score:
  band: emerging
  composite: 17.4
  delta: -1.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sydney/refs/heads/main/screenshots/university-of-sydney-2026-06-20T200254.png
security:
- kind: domain-security
  name: University Of Sydney Domain Security
  slug: university-of-sydney-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-sydney
tags:
- Education
- Higher Education
- University
- Library
- Research
- Open Data
- Australia
website: https://www.sydney.edu.au/
---
