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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for IRIS, Sapienza's institutional research information system / repository (DSpace platform developed by CINECA). The endpoint (repositoryName "IRIS - UNIROM
  name: IRIS Research Catalogue OAI-PMH
  slug: iris-oai-pmh
- description: Open data and linked data publishing from the Sistema Bibliotecario Sapienza (Sapienza Library System), providing library and digital-resource datasets under CC BY 4.0 following the 5-star open data m
  name: Sapienza Library System Open Data & Linked Data
  slug: library-open-data
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapienza-university-of-rome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uniroma1.it/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Sapienza-University-Rome
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sapienza-universita-di-roma/
- group: commercial
  title: ''
  type: Plans
  url: plans/sapienza-university-of-rome-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sapienza-university-of-rome-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sapienza-university-of-rome-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Sapienza University of Rome (Sapienza Università di Roma) is Italy''s largest university and ranked #132 in the QS World University Rankings 2025. Its public machine-readable footprint is centered on research and library data rather than a unified developer portal: the IRIS institutional research catalogue exposes a DSpace OAI-PMH endpoint for harvesting research metadata, and the Sapienza Library System (Sistema Bibliotecario Sapienza) publishes open data and linked data following the 5-star open data model. There is no single official, documented public REST API gateway; identity is federated via the Italian IDEM Shibboleth/SAML federation. A GitHub organization carrying the Sapienza name exists but hosts research and coursework projects rather than official platform APIs.'
finops:
- name: Sapienza University Of Rome Finops
  service_category: Education
  slug: sapienza-university-of-rome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapienza-university-of-rome.png
jsonld:
- class_count: 17
  name: Sapienza University Of Rome Context
  property_count: 7
  slug: sapienza-university-of-rome-context
layout: provider
modified: '2026-06-03'
name: Sapienza University of Rome
nav: Providers
network: true
overview: 'Sapienza University of Rome publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Sapienza University of Rome catalog on APIs.io includes 1 JSON-LD context.


  Sapienza University of Rome''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Sapienza University Of Rome Plans Pricing
  plan_count: 2
  slug: sapienza-university-of-rome-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Sapienza University Of Rome Rate Limits
  slug: sapienza-university-of-rome-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sapienza-university-of-rome/refs/heads/main/screenshots/sapienza-university-of-rome-2026-06-20T193443.png
security:
- kind: domain-security
  name: Sapienza University Of Rome Domain Security
  slug: sapienza-university-of-rome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sapienza-university-of-rome
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- OAI-PMH
- Italy
website: https://www.uniroma1.it/en
---
