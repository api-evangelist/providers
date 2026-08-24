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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Victoria University Of Wellington Agentic Access
  operation_count: 7
  slug: victoria-university-of-wellington-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 4
apis:
- description: OAI-PMH metadata harvesting feed for the Open Access Te Herenga Waka—Victoria University of Wellington research repository, hosted on Figshare. The university's records are exposed via the Figshare OA
  name: Open Access Repository OAI-PMH
  slug: open-access-oai-pmh
- description: The university library's discovery service, branded Te Waharoa, runs on Ex Libris Primo backed by Alma resource management. The public discovery view uses VID 64VUW_INST:VUWNUI. Primo provides program
  name: Te Waharoa Library Discovery (Primo / Alma)
  slug: primo-discovery
- description: An undocumented JSON configuration endpoint served by the university's main website that returns global site object data such as base URLs, logo, and navigation roots. Not a published developer API, b
  name: Website Global Object Endpoint
  slug: web-globalobject
- description: The Articles API from Victoria University of Wellington — 7 operation(s) for articles.
  name: Victoria University of Wellington Articles API
  slug: victoria-university-of-wellington-articles-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare API (Open Access Repository) Articles API
  slug: open-victoria-university-of-wellington-articles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/victoria-university-of-wellington-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/victoria-university-of-wellington-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wgtn.ac.nz/news/rss
- group: company
  title: ''
  type: Website
  url: https://www.wgtn.ac.nz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/victoriauniversity
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/VUW-Library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/victoria-university-of-wellington/
- group: commercial
  title: ''
  type: Plans
  url: plans/victoria-university-of-wellington-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/victoria-university-of-wellington-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/victoria-university-of-wellington-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Te Herenga Waka—Victoria University of Wellington is a public research university in Wellington, New Zealand, ranked #244 in the QS World University Rankings 2025. It does not operate a centralized, publicly documented developer portal; instead its public, machine-readable footprint is found in standards-based scholarly and library infrastructure. Confirmed public interfaces include a Figshare-powered Open Access research repository exposing an OAI-PMH metadata feed and the Figshare v2 REST API, and an Ex Libris Primo (Te Waharoa) discovery service backed by Alma. The university also maintains public GitHub organizations for its web UI toolkit and library engineering work.'
examples:
- key_count: 25
  name: Victoria University Of Wellington Article Details Example
  slug: victoria-university-of-wellington-article-details-example
finops:
- name: Victoria University Of Wellington Finops
  service_category: Education
  slug: victoria-university-of-wellington-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/victoria-university-of-wellington.png
json_schemas:
- name: FigshareArticle
  property_count: 25
  slug: victoria-university-of-wellington-article
json_structures:
- name: Victoria University Of Wellington Article Structure
  property_count: 22
  slug: victoria-university-of-wellington-article-structure
jsonld:
- class_count: 3
  name: Victoria University Of Wellington Context
  property_count: 6
  slug: victoria-university-of-wellington-context
layout: provider
modified: '2026-06-03'
name: Victoria University of Wellington
nav: Providers
network: true
overview: 'Victoria University of Wellington publishes 1 API on the [APIs.io](https://apis.io/) network: Articles API. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Victoria University of Wellington catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Victoria University of Wellington''s developer surface includes engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Victoria University Of Wellington Plans Pricing
  plan_count: 2
  slug: victoria-university-of-wellington-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Victoria University Of Wellington Rate Limits
  slug: victoria-university-of-wellington-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Victoria University of Wellington API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: victoria-university-of-wellington-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Victoria University of Wellington API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: victoria-university-of-wellington-rules
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 55.2
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/victoria-university-of-wellington/refs/heads/main/screenshots/victoria-university-of-wellington-2026-06-20T201017.png
security:
- kind: domain-security
  name: Victoria University Of Wellington Domain Security
  slug: victoria-university-of-wellington-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: victoria-university-of-wellington
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Library
- New Zealand
website: https://www.wgtn.ac.nz/
---
