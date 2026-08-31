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
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: NCKU's open data platform is built on CKAN and exposes the standard CKAN Action API. Endpoints such as /api/3/action/package_list and /api/3/action/package_show return JSON catalogs of the university'
  name: NCKU Open Data Platform (CKAN Action API)
  slug: opendata
- description: The NCKU Library catalog and discovery service runs on Ex Libris Primo backed by an Alma library services platform. Primo deployments expose a REST/JSON discovery layer (Primo VE) used by the public s
  name: NCKU Library Discovery (Ex Libris Primo)
  slug: primo
- description: The NCKU institutional repository (NCKUR) is a DSpace 7 platform hosting university scholarly output and theses. DSpace 7 ships a REST API and OAI-PMH harvesting interface; the repository homepage adv
  name: NCKU Institutional Repository (DSpace 7)
  slug: ir
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ncku-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://web.ncku.edu.tw/index.php?Lang=en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.ncku.edu.tw/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ncku-csie
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-cheng-kung-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/ncku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ncku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ncku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'National Cheng Kung University (NCKU) is a public research university based in Tainan, Taiwan, ranked #215 in the QS World University Rankings 2025. Its public, machine-readable footprint centers on a CKAN-powered open data platform that exposes the standard CKAN Action API, an Ex Libris Primo/Alma library discovery layer, and a DSpace 7 institutional repository. NCKU does not operate a single consolidated developer portal; the cataloged interfaces below are platform-standard APIs confirmed live rather than bespoke, documented university APIs.'
finops:
- name: Ncku Finops
  service_category: Education
  slug: ncku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ncku.png
jsonld:
- class_count: 24
  name: Ncku Context
  property_count: 0
  slug: ncku-context
layout: provider
modified: '2026-06-03'
name: National Cheng Kung University
nav: Providers
network: true
overview: 'National Cheng Kung University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Library.


  The National Cheng Kung University catalog on APIs.io includes 1 JSON-LD context.


  National Cheng Kung University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Ncku Plans Pricing
  plan_count: 2
  slug: ncku-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Ncku Rate Limits
  slug: ncku-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ncku/refs/heads/main/screenshots/ncku-2026-06-20T190150.png
security:
- kind: domain-security
  name: Ncku Domain Security
  slug: ncku-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ncku
tags:
- Education
- Higher Education
- University
- Open Data
- Library
- Taiwan
website: https://web.ncku.edu.tw/index.php?Lang=en
---
