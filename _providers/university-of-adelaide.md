---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: University Of Adelaide Agentic Access
  operation_count: 157
  slug: university-of-adelaide-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: DSpace 7.6.1 REST (HAL/JSON) API for the University of Adelaide institutional repository "Adelaide Research & Scholarship", exposing communities, collections, items, and bitstreams for theses, article
  name: Adelaide Research & Scholarship REST API
  slug: dspace-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the "Adelaide Research & Scholarship" DSpace repository. Confirmed live; the Identify response reports repository name "Adelaide Research & Scholarship" wi
  name: Adelaide Research & Scholarship OAI-PMH
  slug: dspace-oai-pmh
- description: The altmetric API from University of Adelaide — 1 operation(s) for altmetric.
  name: University of Adelaide altmetric API
  slug: university-of-adelaide-altmetric-api
- description: The articles API from University of Adelaide — 34 operation(s) for articles.
  name: University of Adelaide articles API
  slug: university-of-adelaide-articles-api
- description: The authors API from University of Adelaide — 2 operation(s) for authors.
  name: University of Adelaide authors API
  slug: university-of-adelaide-authors-api
- description: The collections API from University of Adelaide — 21 operation(s) for collections.
  name: University of Adelaide collections API
  slug: university-of-adelaide-collections-api
- description: The institutions API from University of Adelaide — 20 operation(s) for institutions.
  name: University of Adelaide institutions API
  slug: university-of-adelaide-institutions-api
- description: The oauth API from University of Adelaide — 1 operation(s) for oauth.
  name: University of Adelaide oauth API
  slug: university-of-adelaide-oauth-api
- description: The other API from University of Adelaide — 7 operation(s) for other.
  name: University of Adelaide other API
  slug: university-of-adelaide-other-api
- description: The profiles API from University of Adelaide — 2 operation(s) for profiles.
  name: University of Adelaide profiles API
  slug: university-of-adelaide-profiles-api
- description: The projects API from University of Adelaide — 17 operation(s) for projects.
  name: University of Adelaide projects API
  slug: university-of-adelaide-projects-api
- description: The symplectic API from University of Adelaide — 5 operation(s) for symplectic.
  name: University of Adelaide symplectic API
  slug: university-of-adelaide-symplectic-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-university-of-adelaide-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-university-of-adelaide-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-university-of-adelaide-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-university-of-adelaide-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-university-of-adelaide-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-university-of-adelaide-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-university-of-adelaide-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-university-of-adelaide-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-university-of-adelaide-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-university-of-adelaide-symplectic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-adelaide-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-adelaide-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-adelaide-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-adelaide-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.adelaide.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/universityofadelaide
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/uniofadelaide/
- group: auth
  title: ''
  type: Authentication
  url: https://login.adelaide.edu.au/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-adelaide-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-adelaide-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-adelaide-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Adelaide is a public research university in Adelaide, South Australia, founded in 1874, and ranked #72 in the QS World University Rankings 2025. Its public, developer-facing footprint is centered on open scholarly infrastructure rather than a unified developer portal: the "Adelaide Research & Scholarship" institutional repository runs on DSpace 7.6.1 and exposes both a REST API and an OAI-PMH metadata endpoint, and the university operates an Adelaide Figshare research-data instance backed by the shared Figshare public API and OAI-PMH. Authentication is handled by a CAS-based single sign-on, and the institution maintains a public GitHub organization built largely around its Drupal "Shepherd" site-management platform. No consolidated, self-service public API developer portal was found.'
finops:
- name: University Of Adelaide Finops
  service_category: Education
  slug: university-of-adelaide-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-adelaide.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-adelaide-article
- name: Figshare Collection
  property_count: 6
  slug: university-of-adelaide-collection
json_structures:
- name: University Of Adelaide Article Structure
  property_count: 15
  slug: university-of-adelaide-article-structure
- name: University Of Adelaide Collection Structure
  property_count: 5
  slug: university-of-adelaide-collection-structure
jsonld:
- class_count: 7
  name: University Of Adelaide Context
  property_count: 2
  slug: university-of-adelaide-context
layout: provider
modified: '2026-06-03'
name: University of Adelaide
nav: Providers
network: true
overview: 'University of Adelaide publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Institutional Repository.


  The University of Adelaide catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Adelaide''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: University Of Adelaide Plans Pricing
  plan_count: 2
  slug: university-of-adelaide-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Adelaide Rate Limits
  slug: university-of-adelaide-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Adelaide API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-adelaide-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of Adelaide API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: university-of-adelaide-rules
scopes:
- name: University Of Adelaide Scopes
  scope_count: 1
  slug: university-of-adelaide-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 41.8
  delta: -3.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 73.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-adelaide/refs/heads/main/screenshots/university-of-adelaide-2026-06-20T200125.png
security:
- kind: authentication
  name: University Of Adelaide Authentication
  slug: university-of-adelaide-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Adelaide Domain Security
  slug: university-of-adelaide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-adelaide
tags:
- Education
- Higher Education
- University
- Research
- Institutional Repository
- Open Data
- Australia
website: https://www.adelaide.edu.au/
---
