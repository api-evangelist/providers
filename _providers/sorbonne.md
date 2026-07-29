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
api_count: 3
apis:
- description: HAL Sorbonne Université is the institution's open archive of scholarly publications. Its metadata is harvestable through the standards-based OAI-PMH protocol served by the central HAL infrastructure (
  name: HAL Sorbonne Université Open Archive (OAI-PMH)
  slug: hal-oai
- description: The HAL Solr-based search API exposes structured queries over the HAL corpus, including publications affiliated with Sorbonne Université. It returns JSON/XML and supports faceting and filtering on col
  name: HAL Search API
  slug: hal-search
- description: Sorbonne Université maintains a research-data collection on the French national Recherche Data Gouv repository, built on Dataverse 6.0. The Dataverse Native REST API is live (the version endpoint retu
  name: Recherche Data Gouv Dataverse - Sorbonne Université Collection
  slug: dataverse
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sorbonne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sorbonne-universite.fr/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sorbonne-universite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/sorbonne-universite/
- group: commercial
  title: ''
  type: Plans
  url: plans/sorbonne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sorbonne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sorbonne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Sorbonne University (Sorbonne Université) is a public research university in Paris, France, formed in 2018 from the merger of Paris-Sorbonne and Pierre et Marie Curie universities. It serves roughly 53,000 students across faculties of Arts & Humanities, Health Sciences, and Science & Engineering, and is ranked #81 in the QS World University Rankings 2025. Sorbonne University does not operate a centralized public developer portal; its programmatic surface is delivered through open-science infrastructure: the HAL Sorbonne Université open archive (harvestable via the standards-based OAI-PMH and HAL search APIs) and a Sorbonne University collection on the national Recherche Data Gouv Dataverse, which exposes a live Dataverse Native REST API. An official GitHub organization exists but currently hosts no public repositories.'
finops:
- name: Sorbonne Finops
  service_category: Education
  slug: sorbonne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sorbonne.png
jsonld:
- class_count: 11
  name: Sorbonne Context
  property_count: 12
  slug: sorbonne-context
layout: provider
modified: '2026-06-03'
name: Sorbonne University
nav: Providers
network: true
overview: 'Sorbonne University publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Science, and Research Data.


  The Sorbonne University catalog on APIs.io includes 1 JSON-LD context.


  Sorbonne University''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Sorbonne Plans Pricing
  plan_count: 2
  slug: sorbonne-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 1
  name: Sorbonne Rate Limits
  slug: sorbonne-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -3.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sorbonne/refs/heads/main/screenshots/sorbonne-2026-06-20T194214.png
security:
- kind: domain-security
  name: Sorbonne Domain Security
  slug: sorbonne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sorbonne
tags:
- Education
- Higher Education
- University
- Open Science
- Research Data
- Open Access
- OAI-PMH
- Dataverse
- France
website: https://www.sorbonne-universite.fr/en
---
