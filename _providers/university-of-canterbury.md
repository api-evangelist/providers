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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: University Of Canterbury Agentic Access
  operation_count: 157
  slug: university-of-canterbury-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 13
apis:
- description: 'OAI-PMH 2.0 metadata harvesting interface for the UC Research Repository, a DSpace 7 institutional repository of theses, dissertations and research outputs. Verified live (HTTP 200) returning a valid '
  name: UC Research Repository OAI-PMH
  slug: research-repository-oai
- description: DSpace 7 REST API backing the UC Research Repository, providing programmatic access to communities, collections and items. The API root (https://ir.canterbury.ac.nz/server/api) is part of the standard
  name: UC Research Repository DSpace REST API
  slug: research-repository-rest
- description: Self-hosted GitLab instance operated by the University of Canterbury College of Engineering. The web application is reachable (HTTP 200) and the GitLab REST API v4 is present (HTTP 401 to unauthentica
  name: UC Engineering GitLab API
  slug: eng-git-gitlab
- description: The altmetric API from University of Canterbury — 1 operation(s) for altmetric.
  name: University of Canterbury altmetric API
  slug: university-of-canterbury-altmetric-api
- description: The articles API from University of Canterbury — 34 operation(s) for articles.
  name: University of Canterbury articles API
  slug: university-of-canterbury-articles-api
- description: The authors API from University of Canterbury — 2 operation(s) for authors.
  name: University of Canterbury authors API
  slug: university-of-canterbury-authors-api
- description: The collections API from University of Canterbury — 21 operation(s) for collections.
  name: University of Canterbury collections API
  slug: university-of-canterbury-collections-api
- description: The institutions API from University of Canterbury — 20 operation(s) for institutions.
  name: University of Canterbury institutions API
  slug: university-of-canterbury-institutions-api
- description: The oauth API from University of Canterbury — 1 operation(s) for oauth.
  name: University of Canterbury oauth API
  slug: university-of-canterbury-oauth-api
- description: The other API from University of Canterbury — 7 operation(s) for other.
  name: University of Canterbury other API
  slug: university-of-canterbury-other-api
- description: The profiles API from University of Canterbury — 2 operation(s) for profiles.
  name: University of Canterbury profiles API
  slug: university-of-canterbury-profiles-api
- description: The projects API from University of Canterbury — 17 operation(s) for projects.
  name: University of Canterbury projects API
  slug: university-of-canterbury-projects-api
- description: The symplectic API from University of Canterbury — 5 operation(s) for symplectic.
  name: University of Canterbury symplectic API
  slug: university-of-canterbury-symplectic-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-canterbury-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-canterbury-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-canterbury-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-canterbury-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.canterbury.ac.nz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uccser
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-canterbury/
- group: build
  title: ''
  type: SourceCode
  url: https://eng-git.canterbury.ac.nz/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-canterbury-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-canterbury-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-canterbury-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University of Canterbury (Te Whare Wananga o Waitaha) is a public research university in Christchurch, New Zealand, ranked #261 in the QS World University Rankings 2025. Its public, machine-accessible developer footprint is centered on scholarly and research infrastructure rather than a unified developer portal: the UC Research Repository (a DSpace 7 platform) exposes a live OAI-PMH 2.0 metadata harvesting interface and a DSpace REST API, the institutional Canterbury Figshare instance is reachable through figshare''s public REST and OAI-PMH endpoints, and the College of Engineering runs a self-hosted GitLab. No consolidated, publicly documented university-wide API program was confirmed; entries below reflect only endpoints verified live.'
examples:
- key_count: 4
  name: University Of Canterbury List Articles Example
  slug: university-of-canterbury-list-articles-example
- key_count: 4
  name: University Of Canterbury Search Articles Example
  slug: university-of-canterbury-search-articles-example
finops:
- name: University Of Canterbury Finops
  service_category: Education
  slug: university-of-canterbury-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-canterbury.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-canterbury-article
- name: Figshare Collection
  property_count: 6
  slug: university-of-canterbury-collection
json_structures:
- name: University Of Canterbury Article Structure
  property_count: 16
  slug: university-of-canterbury-article-structure
- name: University Of Canterbury Collection Structure
  property_count: 6
  slug: university-of-canterbury-collection-structure
jsonld:
- class_count: 7
  name: University Of Canterbury Context
  property_count: 15
  slug: university-of-canterbury-context
layout: provider
modified: '2026-06-03'
name: University of Canterbury
nav: Providers
network: true
overview: 'University of Canterbury publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Canterbury catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Canterbury''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: University Of Canterbury Plans Pricing
  plan_count: 2
  slug: university-of-canterbury-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 1
  name: University Of Canterbury Rate Limits
  slug: university-of-canterbury-rate-limits
rules:
- name: University of Canterbury API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-canterbury-jsonschema-spectral-rules
- name: University of Canterbury API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: university-of-canterbury-rules
scopes:
- name: University Of Canterbury Scopes
  scope_count: 1
  slug: university-of-canterbury-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.4
  delta: -5.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 75.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 50.7
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
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-canterbury/refs/heads/main/screenshots/university-of-canterbury-2026-06-20T200141.png
security:
- kind: authentication
  name: University Of Canterbury Authentication
  slug: university-of-canterbury-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Canterbury Domain Security
  slug: university-of-canterbury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-canterbury
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Repository
- OAI-PMH
- New Zealand
website: https://www.canterbury.ac.nz/
---
