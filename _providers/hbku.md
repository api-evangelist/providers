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
  name: Hbku Agentic Access
  operation_count: 157
  slug: hbku-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: Figshare exposes an OAI-PMH v2.0 metadata harvesting endpoint that provides access to public article metadata across the platform, including HBKU works hosted in Manara - Qatar Research Repository. Ha
  name: Figshare OAI-PMH (Manara - HBKU Research)
  slug: figshare-oai
- description: The altmetric API from Hamad Bin Khalifa University — 1 operation(s) for altmetric.
  name: Hamad Bin Khalifa University altmetric API
  slug: hbku-altmetric-api
- description: The articles API from Hamad Bin Khalifa University — 34 operation(s) for articles.
  name: Hamad Bin Khalifa University articles API
  slug: hbku-articles-api
- description: The authors API from Hamad Bin Khalifa University — 2 operation(s) for authors.
  name: Hamad Bin Khalifa University authors API
  slug: hbku-authors-api
- description: The collections API from Hamad Bin Khalifa University — 21 operation(s) for collections.
  name: Hamad Bin Khalifa University collections API
  slug: hbku-collections-api
- description: The institutions API from Hamad Bin Khalifa University — 20 operation(s) for institutions.
  name: Hamad Bin Khalifa University institutions API
  slug: hbku-institutions-api
- description: The oauth API from Hamad Bin Khalifa University — 1 operation(s) for oauth.
  name: Hamad Bin Khalifa University oauth API
  slug: hbku-oauth-api
- description: The other API from Hamad Bin Khalifa University — 7 operation(s) for other.
  name: Hamad Bin Khalifa University other API
  slug: hbku-other-api
- description: The profiles API from Hamad Bin Khalifa University — 2 operation(s) for profiles.
  name: Hamad Bin Khalifa University profiles API
  slug: hbku-profiles-api
- description: The projects API from Hamad Bin Khalifa University — 17 operation(s) for projects.
  name: Hamad Bin Khalifa University projects API
  slug: hbku-projects-api
- description: The symplectic API from Hamad Bin Khalifa University — 5 operation(s) for symplectic.
  name: Hamad Bin Khalifa University symplectic API
  slug: hbku-symplectic-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hbku-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hbku-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hbku-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hbku-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.hbku.edu.qa/en/home
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cri-lab-hbku
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hamad-bin-khalifa-university/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/hbku
- group: build
  title: ''
  type: Library
  url: https://www.hbku.edu.qa/en/hbku-library
- group: other
  title: ''
  type: Repository
  url: https://manara.qnl.qa/hbku
- group: commercial
  title: ''
  type: Plans
  url: plans/hbku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hbku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hbku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hbku.edu.qa/en/news
created: '2026-06-03'
description: 'Hamad Bin Khalifa University (HBKU) is a research-intensive graduate university founded in 2010 as part of Qatar Foundation, located in Education City, Doha, Qatar, and ranked #183 in the QS World University Rankings 2025. HBKU does not operate a centralized public developer portal or documented institutional API; its student information, academic catalog, and library discovery systems are gated behind authentication. The most significant public, machine-readable footprint is its scholarly research output, which is deposited in Manara - Qatar Research Repository, a Figshare-powered repository hosted by Qatar National Library that exposes HBKU works through Figshare''s public REST API v2 and OAI-PMH metadata harvesting endpoint.'
examples:
- key_count: 4
  name: Hbku Get Article Example
  slug: hbku-get-article-example
- key_count: 4
  name: Hbku List Articles Example
  slug: hbku-list-articles-example
- key_count: 4
  name: Hbku Search Articles Example
  slug: hbku-search-articles-example
finops:
- name: Hbku Finops
  service_category: Education
  slug: hbku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hbku.png
json_schemas:
- name: Figshare Article
  property_count: 17
  slug: hbku-article
- name: Figshare Author
  property_count: 7
  slug: hbku-author
- name: Figshare Collection
  property_count: 6
  slug: hbku-collection
json_structures:
- name: Hbku Article Structure
  property_count: 15
  slug: hbku-article-structure
- name: Hbku Author Structure
  property_count: 7
  slug: hbku-author-structure
jsonld:
- class_count: 22
  name: Hbku Context
  property_count: 12
  slug: hbku-context
layout: provider
modified: '2026-06-03'
name: Hamad Bin Khalifa University
nav: Providers
network: true
overview: 'Hamad Bin Khalifa University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Hamad Bin Khalifa University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Hamad Bin Khalifa University''s developer surface includes authentication, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Hbku Plans Pricing
  plan_count: 2
  slug: hbku-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 1
  name: Hbku Rate Limits
  slug: hbku-rate-limits
rules:
- name: Hamad Bin Khalifa University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hbku-jsonschema-spectral-rules
- name: Hamad Bin Khalifa University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: hbku-rules
scopes:
- name: Hbku Scopes
  scope_count: 1
  slug: hbku-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.9
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.7
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/screenshots/hbku-2026-06-20T182545.png
security:
- kind: authentication
  name: Hbku Authentication
  slug: hbku-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hbku Domain Security
  slug: hbku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hbku
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- Qatar
- Middle East
website: https://www.hbku.edu.qa/en/home
---
