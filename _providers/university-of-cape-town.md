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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: University Of Cape Town Agentic Access
  operation_count: 9
  slug: university-of-cape-town-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 7
apis:
- description: DataFirst is a UCT research unit and data service providing online access to survey and administrative microdata from South Africa and other African countries. Its open data portal is built on the NAD
  name: DataFirst Microdata Catalog API (NADA)
  slug: datafirst-nada
- description: OpenUCT is the University of Cape Town's open access institutional repository, launched in 2014 and built on DSpace. It preserves and openly shares UCT scholarly outputs including theses, dissertation
  name: OpenUCT Institutional Repository OAI-PMH
  slug: openuct-oai-pmh
- description: ZivaHub is UCT's institutional open data repository for research data and scholarly outputs, powered by Figshare for Institutions and certified with the CoreTrustSeal in 2025. Public ZivaHub content i
  name: ZivaHub Open Data (Figshare API)
  slug: zivahub-figshare
- description: Public articles (research outputs / datasets)
  name: University of Cape Town articles API
  slug: university-of-cape-town-articles-api
- description: Browse and search the microdata catalog.
  name: University of Cape Town catalog API
  slug: university-of-cape-town-catalog-api
- description: Public collections
  name: University of Cape Town collections API
  slug: university-of-cape-town-collections-api
- description: Public projects
  name: University of Cape Town projects API
  slug: university-of-cape-town-projects-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-cape-town-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-cape-town-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uct.ac.za/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uct-cbio
- group: company
  title: ''
  type: LinkedIn
  url: https://za.linkedin.com/school/university-of-cape-town/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-cape-town-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-cape-town-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-cape-town-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-cape-town-zivahub-figshare.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-cape-town-datafirst-nada.yaml
- group: docs
  title: ''
  type: x-json-schema
  url: json-schema/university-of-cape-town-article-schema.json
- group: docs
  title: ''
  type: x-json-schema
  url: json-schema/university-of-cape-town-study-schema.json
- group: other
  title: ''
  type: x-json-structure
  url: json-structure/university-of-cape-town-article-structure.json
- group: other
  title: ''
  type: x-json-structure
  url: json-structure/university-of-cape-town-study-structure.json
- group: design
  title: ''
  type: x-spectral-rules
  url: rules/university-of-cape-town-rules.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-cape-town-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-cape-town-context.jsonld
created: '2026-06-03'
description: 'The University of Cape Town (UCT) is South Africa''s leading public research university, ranked #96 in the QS World University Rankings 2025 and the highest-ranked university on the African continent. UCT does not operate a single consolidated developer portal, but several of its research and library units expose public, machine-readable interfaces. DataFirst runs a NADA-based microdata catalog with a public REST API, the OpenUCT institutional repository exposes a DSpace OAI-PMH metadata harvesting endpoint, and the ZivaHub open data repository is built on Figshare for Institutions and is reachable through the public Figshare API. Most operational, student-information, and identity systems remain gated behind institutional authentication.'
examples:
- key_count: 24
  name: University Of Cape Town Getarticle Example
  slug: university-of-cape-town-getArticle-example
- key_count: 2
  name: University Of Cape Town Listcatalog Example
  slug: university-of-cape-town-listCatalog-example
- key_count: 2
  name: University Of Cape Town Searcharticles Example
  slug: university-of-cape-town-searchArticles-example
finops:
- name: University Of Cape Town Finops
  service_category: Education
  slug: university-of-cape-town-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-cape-town.png
json_schemas:
- name: ZivaHub Article
  property_count: 19
  slug: university-of-cape-town-article
- name: DataFirst Catalog Study
  property_count: 13
  slug: university-of-cape-town-study
json_structures:
- name: University Of Cape Town Article Structure
  property_count: 15
  slug: university-of-cape-town-article-structure
- name: University Of Cape Town Study Structure
  property_count: 13
  slug: university-of-cape-town-study-structure
jsonld:
- class_count: 21
  name: University Of Cape Town Context
  property_count: 7
  slug: university-of-cape-town-context
layout: provider
modified: '2026-06-03'
name: University of Cape Town
nav: Providers
network: true
overview: 'University of Cape Town publishes 4 APIs on the [APIs.io](https://apis.io/) network, including articles API, catalog API, collections API, and 1 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Cape Town catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Cape Town''s developer surface includes GitHub presence and 17 more developer resources.'
plans:
- name: University Of Cape Town Plans Pricing
  plan_count: 2
  slug: university-of-cape-town-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: University Of Cape Town Rate Limits
  slug: university-of-cape-town-rate-limits
rules:
- name: University of Cape Town API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-cape-town-jsonschema-spectral-rules
- name: University of Cape Town API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: university-of-cape-town-rules
score:
  band: thin
  composite: 35.4
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.6
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-cape-town/refs/heads/main/screenshots/university-of-cape-town-2026-06-20T200148.png
security:
- kind: domain-security
  name: University Of Cape Town Domain Security
  slug: university-of-cape-town-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-cape-town
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Institutional Repository
- OAI-PMH
- South Africa
- Africa
website: https://www.uct.ac.za/
---
