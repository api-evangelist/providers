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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Open data portal for the University of Bologna built on CKAN, exposing the standard CKAN Action API over institutional datasets (course catalog, curricula, financial and social reports, organizational
  name: University of Bologna Open Data (CKAN API)
  slug: opendata-ckan
- description: AMS Acta is the AlmaDL institutional repository of the University of Bologna, running on EPrints 3.4.x. It exposes an OAI-PMH 2.0 metadata-harvesting interface (Dublin Core), confirmed live via an Ide
  name: AMS Acta Institutional Repository (OAI-PMH)
  slug: amsacta-oai-pmh
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bologna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unibo.it/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unibo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/unibo/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dati.unibo.it/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bologna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bologna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bologna-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bologna (Alma Mater Studiorum - Università di Bologna) is the oldest university in the Western world and a leading Italian research institution, ranked #133 in the QS World University Rankings 2025. Its public developer and API footprint centers on open data and open scholarship rather than a unified developer portal: a CKAN-based open data portal at dati.unibo.it exposes a standard CKAN Action API over institutional datasets, and the AlmaDL AMS Acta institutional repository (EPrints) exposes an OAI-PMH metadata-harvesting interface. The university also maintains an official open-source GitHub organization. Most administrative, course, and identity systems require institutional credentials and are not openly documented.'
finops:
- name: University Of Bologna Finops
  service_category: Education
  slug: university-of-bologna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bologna.png
jsonld:
- class_count: 18
  name: University Of Bologna Context
  property_count: 7
  slug: university-of-bologna-context
layout: provider
modified: '2026-06-03'
name: University of Bologna
nav: Providers
network: true
overview: 'University of Bologna publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Research.


  The University of Bologna catalog on APIs.io includes 1 JSON-LD context.


  University of Bologna''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: University Of Bologna Plans Pricing
  plan_count: 2
  slug: university-of-bologna-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: University Of Bologna Rate Limits
  slug: university-of-bologna-rate-limits
score:
  band: emerging
  composite: 20.9
  delta: -3.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bologna/refs/heads/main/screenshots/university-of-bologna-2026-06-20T200136.png
security:
- kind: domain-security
  name: University Of Bologna Domain Security
  slug: university-of-bologna-domain-security
  summary_line: TLSv1.2 · DMARC
slug: university-of-bologna
tags:
- Education
- Higher Education
- University
- Open Data
- Research
- Italy
- Europe
website: https://www.unibo.it/en
---
