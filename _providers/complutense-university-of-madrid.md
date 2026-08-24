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
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: DataStore query API of the UniversiDATA open-data platform (DKAN), of which Complutense University of Madrid is a founding participant. Returns the records of published data resources (including UCM d
  name: UniversiDATA DataStore API
  slug: universidata-datastore
- description: CKAN-compatible metadata API of the UniversiDATA platform. Lists datasets and resources and returns dataset/resource metadata, including UCM open datasets. Supports actions such as current_package_lis
  name: UniversiDATA CKAN Dataset API
  slug: universidata-ckan
- description: DCAT catalog API of UniversiDATA, exposing the dataset catalog per participating university. The UCM catalog is reachable via the university acronym path segment on the DCAT endpoint.
  name: UniversiDATA DCAT Catalog API
  slug: universidata-dcat
- description: Docta Complutense is UCM's open-access institutional repository, migrated in 2023 to DSpace 7. As a DSpace platform it underpins open-access discovery of theses, articles, and research outputs; progra
  name: Docta Complutense Institutional Repository
  slug: docta-complutense
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/complutense-university-of-madrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucm.es/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UniversidadComplutense
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-complutense-de-madrid/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.universidata.es/el-api
- group: commercial
  title: ''
  type: Plans
  url: plans/complutense-university-of-madrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/complutense-university-of-madrid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/complutense-university-of-madrid-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Complutense University of Madrid (Universidad Complutense de Madrid, UCM) is a major public research university in Spain, ranked #164 in the QS World University Rankings 2025. Its public, machine-readable footprint is centered on open data: UCM is a founding member of UniversiDATA, a collaborative open-data portal for Spanish higher education built on DKAN, which exposes a documented DataStore API, CKAN Dataset API, and DCAT catalog API covering UCM datasets (degree programs, enrollments, staff, budgets, mobility, and procurement). UCM also operates Docta Complutense, its institutional repository on DSpace 7, and maintains an official GitHub organization. No general-purpose UCM developer portal for SIS, course, or library APIs was found publicly documented.'
finops:
- name: Complutense University Of Madrid Finops
  service_category: Education
  slug: complutense-university-of-madrid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/complutense-university-of-madrid.png
jsonld:
- class_count: 20
  name: Complutense University Of Madrid Context
  property_count: 0
  slug: complutense-university-of-madrid-context
layout: provider
modified: '2026-06-03'
name: Complutense University of Madrid
nav: Providers
network: true
overview: 'Complutense University of Madrid publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Research.


  The Complutense University of Madrid catalog on APIs.io includes 1 JSON-LD context.


  Complutense University of Madrid''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Complutense University Of Madrid Plans Pricing
  plan_count: 2
  slug: complutense-university-of-madrid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Complutense University Of Madrid Rate Limits
  slug: complutense-university-of-madrid-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/complutense-university-of-madrid/refs/heads/main/screenshots/complutense-university-of-madrid-2026-06-20T174834.png
security:
- kind: domain-security
  name: Complutense University Of Madrid Domain Security
  slug: complutense-university-of-madrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: complutense-university-of-madrid
tags:
- Education
- Higher Education
- University
- Open Data
- Research
- Spain
website: https://www.ucm.es/
---
