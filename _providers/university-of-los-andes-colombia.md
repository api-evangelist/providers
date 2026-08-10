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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: OAI-PMH metadata harvesting interface for the DSpace-based institutional repository "Seneca", which collects and preserves the University's open-access scholarly output (articles, theses, books, datas
  name: Repositorio Institucional Seneca - OAI-PMH
  slug: repositorio-oai
- description: DSpace REST API surface for the "Seneca" institutional repository, typically exposed under the /server/api path of a modern DSpace deployment, providing programmatic access to communities, collections
  name: Repositorio Institucional Seneca - DSpace REST API
  slug: repositorio-rest
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-los-andes-colombia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uniandes.edu.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://co.linkedin.com/school/universidad-de-los-andes/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-los-andes-colombia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-los-andes-colombia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-los-andes-colombia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universidad de los Andes (Uniandes) is a private research university in Bogota, Colombia, founded in 1948, and ranked #179 in the QS World University Rankings 2025. Its publicly observable developer/API footprint is limited: the strongest public machine-readable surface is the DSpace-based institutional repository "Seneca" (repositorio.uniandes.edu.co), which exposes an OAI-PMH metadata interface and a DSpace REST API for open-access scholarly content. Student-facing systems such as the Ellucian Banner SIS (MiBanner) are authentication-gated and do not publish public API documentation. No dedicated public developer portal or documented open API program was found at time of review.'
finops:
- name: University Of Los Andes Colombia Finops
  service_category: Education
  slug: university-of-los-andes-colombia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-los-andes-colombia.png
jsonld:
- class_count: 12
  name: University Of Los Andes Colombia Context
  property_count: 7
  slug: university-of-los-andes-colombia-context
layout: provider
modified: '2026-06-03'
name: University of Los Andes Colombia
nav: Providers
network: true
overview: 'University of Los Andes Colombia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Colombia, and Latin America.


  The University of Los Andes Colombia catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: University Of Los Andes Colombia Plans Pricing
  plan_count: 2
  slug: university-of-los-andes-colombia-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 1
  name: University Of Los Andes Colombia Rate Limits
  slug: university-of-los-andes-colombia-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-los-andes-colombia/refs/heads/main/screenshots/university-of-los-andes-colombia-2026-06-20T200202.png
security:
- kind: domain-security
  name: University Of Los Andes Colombia Domain Security
  slug: university-of-los-andes-colombia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-los-andes-colombia
tags:
- Education
- Higher Education
- University
- Colombia
- Latin America
- Open Access
- Institutional Repository
- Research
website: https://www.uniandes.edu.co/
---
