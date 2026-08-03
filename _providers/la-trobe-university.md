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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: La Trobe University Agentic Access
  operation_count: 11
  slug: la-trobe-university-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 4
apis:
- description: OAI-PMH metadata harvesting interface for the La Trobe OPAL repository, served via the Figshare platform OAI provider, scoped to the La Trobe portal set (portal_234) and supporting the oai_dc metadata
  name: OPAL (Open @ La Trobe) OAI-PMH Endpoint
  slug: opal-figshare-oai-pmh
- description: An institutional API gateway is reachable at api.latrobe.edu.au, but it is not a public, self-service developer product. Unauthenticated requests return HTTP 302 redirecting to a /signin page, indicat
  name: La Trobe API Gateway (Gated)
  slug: api-gateway
- description: The articles API from La Trobe University — 7 operation(s) for articles.
  name: La Trobe University articles API
  slug: la-trobe-university-articles-api
- description: The collections API from La Trobe University — 4 operation(s) for collections.
  name: La Trobe University collections API
  slug: la-trobe-university-collections-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/la-trobe-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-trobe-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.latrobe.edu.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/la-trobe-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/latrobe
- group: commercial
  title: ''
  type: Plans
  url: plans/la-trobe-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/la-trobe-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/la-trobe-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'La Trobe University is a public research university based in Melbourne, Victoria, Australia, ranked #217 in the QS World University Rankings 2025. Like most universities, La Trobe does not operate a single consolidated public developer portal; the bulk of its API surface (an internal API gateway at api.latrobe.edu.au) sits behind sign-in and institutional federation. Its most clearly public, documented machine-readable interface is its open research repository, OPAL (Open @ La Trobe), which is hosted on the Figshare platform and therefore exposes the standard Figshare REST API and an OAI-PMH metadata endpoint for harvesting open-access publications, theses, and research data. Library discovery runs on Ex Libris Alma and Primo.'
examples:
- key_count: 50
  name: La Trobe University Get Article Example
  slug: la-trobe-university-get-article-example
- key_count: 7
  name: La Trobe University Search Articles Request Example
  slug: la-trobe-university-search-articles-request-example
finops:
- name: La Trobe University Finops
  service_category: Education
  slug: la-trobe-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/la-trobe-university.png
json_schemas:
- name: La Trobe OPAL Article
  property_count: 50
  slug: la-trobe-university-article
json_structures:
- name: La Trobe University Article Structure
  property_count: 32
  slug: la-trobe-university-article-structure
jsonld:
- class_count: 28
  name: La Trobe University Context
  property_count: 13
  slug: la-trobe-university-context
layout: provider
modified: '2026-06-03'
name: La Trobe University
nav: Providers
network: true
overview: 'La Trobe University publishes 2 APIs on the [APIs.io](https://apis.io/) network: articles API and collections API. Tagged areas include Education, Higher Education, University, Australia, and Research.


  The La Trobe University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: La Trobe University Plans Pricing
  plan_count: 2
  slug: la-trobe-university-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 1
  name: La Trobe University Rate Limits
  slug: la-trobe-university-rate-limits
rules:
- name: La Trobe University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: la-trobe-university-jsonschema-spectral-rules
- name: La Trobe University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: la-trobe-university-rules
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/la-trobe-university/refs/heads/main/screenshots/la-trobe-university-2026-06-20T184236.png
security:
- kind: domain-security
  name: La Trobe University Domain Security
  slug: la-trobe-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: la-trobe-university
tags:
- Education
- Higher Education
- University
- Australia
- Research
- Open Data
- Repository
- Library
website: https://www.latrobe.edu.au/
---
