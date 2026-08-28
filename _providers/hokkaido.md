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
api_count: 1
apis:
- description: Publicly crawlable XML sitemap index for the HUSCAP repository, providing a machine-readable list of repository item URLs. This is an open, robots.txt- permitted endpoint usable for programmatic disco
  name: HUSCAP XML Sitemaps
  slug: huscap-sitemap
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hokkaido-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.global.hokudai.ac.jp/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hokkaidouni/
- group: commercial
  title: ''
  type: Plans
  url: plans/hokkaido-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hokkaido-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hokkaido-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://eprints.lib.hokudai.ac.jp/
created: '2026-06-03'
description: 'Hokkaido University (北海道大学) is a national research university in Sapporo, Japan, founded in 1876 as Sapporo Agricultural College and ranked #173 in the QS World University Rankings 2025. It operates 12 undergraduate schools, 21 graduate schools, and numerous research institutes. Its public, machine-readable developer footprint is limited and centered on scholarly infrastructure: the HUSCAP institutional repository (Hokkaido University Collection of Scholarly and Academic Papers) and public XML sitemaps. The university does not publish a dedicated developer portal or documented public REST API; most institutional systems (ELMS LMS, syllabus search, researcher directory) are web UIs without documented programmatic access.'
finops:
- name: Hokkaido Finops
  service_category: Education
  slug: hokkaido-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hokkaido.png
jsonld:
- class_count: 10
  name: Hokkaido Context
  property_count: 5
  slug: hokkaido-context
layout: provider
modified: '2026-07-25'
name: Hokkaido University
nav: Providers
network: true
overview: 'Hokkaido University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Hokkaido University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Hokkaido Plans Pricing
  plan_count: 2
  slug: hokkaido-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Hokkaido Rate Limits
  slug: hokkaido-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hokkaido/refs/heads/main/screenshots/hokkaido-2026-06-20T182813.png
security:
- kind: domain-security
  name: Hokkaido Domain Security
  slug: hokkaido-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hokkaido
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- Japan
website: https://www.global.hokudai.ac.jp/
---
