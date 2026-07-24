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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: espace is Curtin University's open-access institutional repository of research publications and higher-degree-by-research theses, delivered on the Ex Libris Primo/Esploro discovery platform. Historica
  name: Curtin espace Institutional Repository
  slug: espace
- description: Curtin University publishes research data collection records through the national Research Data Australia (RDA) registry operated by the Australian Research Data Commons (ARDC). Curtin's records are d
  name: Curtin Research Data (via Research Data Australia)
  slug: researchdata
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curtin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curtin.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CurtinIDS
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Curtin-Open-Knowledge-Initiative
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/curtin-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/curtin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/curtin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/curtin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Curtin University is a public research university based in Perth, Western Australia, and is ranked #174 in the QS World University Rankings 2025. Curtin operates an institutional research repository (espace, built on Ex Libris Primo/Esploro), contributes datasets to the national Research Data Australia registry, and maintains several department-level open-source GitHub organizations. As of this review Curtin does not publish a centralized public developer portal or a documented general-purpose API program; the developer footprint is limited to library/repository discovery platforms and research-data harvesting interfaces operated through third-party platforms.'
finops:
- name: Curtin Finops
  service_category: Education
  slug: curtin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curtin.png
jsonld:
- class_count: 10
  name: Curtin Context
  property_count: 2
  slug: curtin-context
layout: provider
modified: '2026-06-03'
name: Curtin University
nav: Providers
network: true
overview: 'Curtin University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Curtin University catalog on APIs.io includes 1 JSON-LD context.


  Curtin University''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Curtin Plans Pricing
  plan_count: 2
  slug: curtin-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Curtin Rate Limits
  slug: curtin-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: 0.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curtin/refs/heads/main/screenshots/curtin-2026-06-20T175346.png
security:
- kind: domain-security
  name: Curtin Domain Security
  slug: curtin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curtin
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- Australia
website: https://www.curtin.edu.au/
---
