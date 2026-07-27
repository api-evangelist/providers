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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Rmit Agentic Access
  operation_count: 157
  slug: rmit-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: The RMIT Research Repository is RMIT University's open access research portal, powered by Clarivate's Esploro research information management platform. It provides public web-based discovery of RMIT p
  name: RMIT Research Repository (Esploro)
  slug: research-repository
- description: The altmetric API from RMIT University — 1 operation(s) for altmetric.
  name: RMIT University altmetric API
  slug: rmit-altmetric-api
- description: The articles API from RMIT University — 34 operation(s) for articles.
  name: RMIT University articles API
  slug: rmit-articles-api
- description: The authors API from RMIT University — 2 operation(s) for authors.
  name: RMIT University authors API
  slug: rmit-authors-api
- description: The collections API from RMIT University — 21 operation(s) for collections.
  name: RMIT University collections API
  slug: rmit-collections-api
- description: The institutions API from RMIT University — 20 operation(s) for institutions.
  name: RMIT University institutions API
  slug: rmit-institutions-api
- description: The oauth API from RMIT University — 1 operation(s) for oauth.
  name: RMIT University oauth API
  slug: rmit-oauth-api
- description: The other API from RMIT University — 7 operation(s) for other.
  name: RMIT University other API
  slug: rmit-other-api
- description: The profiles API from RMIT University — 2 operation(s) for profiles.
  name: RMIT University profiles API
  slug: rmit-profiles-api
- description: The projects API from RMIT University — 17 operation(s) for projects.
  name: RMIT University projects API
  slug: rmit-projects-api
- description: The symplectic API from RMIT University — 5 operation(s) for symplectic.
  name: RMIT University symplectic API
  slug: rmit-symplectic-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rmit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rmit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rmit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rmit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rmit-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.rmit.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RMIT-University
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/rmit-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RMIT
- group: commercial
  title: ''
  type: Plans
  url: plans/rmit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rmit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rmit-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rmit.edu.au/news/all-news
created: '2026-06-03'
description: 'RMIT University is a public research university in Melbourne, Australia, specializing in technology, design and enterprise, and ranked #123 in the QS World University Rankings 2025. RMIT does not operate a centralized, publicly documented developer portal. Its most accessible programmatic surface is its research output: the RMIT Research Repository runs on Clarivate''s Esploro platform, and RMIT''s research data is published via a Figshare-hosted repository whose records are exposed through the public Figshare REST API (api.figshare.com) and syndicated to Research Data Australia. Student-facing systems such as timetables, the curriculum catalogue, and identity/SSO sit behind authentication and are not offered as public APIs.'
examples:
- key_count: 3
  name: Rmit Article Detail Example
  slug: rmit-article-detail-example
- key_count: 3
  name: Rmit Articles Search Example
  slug: rmit-articles-search-example
finops:
- name: Rmit Finops
  service_category: Education
  slug: rmit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rmit.png
json_schemas:
- name: Figshare Article
  property_count: 15
  slug: rmit-article
- name: Figshare Author
  property_count: 7
  slug: rmit-author
json_structures:
- name: Rmit Article Structure
  property_count: 11
  slug: rmit-article-structure
- name: Rmit Author Structure
  property_count: 7
  slug: rmit-author-structure
jsonld:
- class_count: 25
  name: Rmit Context
  property_count: 7
  slug: rmit-context
layout: provider
modified: '2026-06-03'
name: RMIT University
nav: Providers
network: true
overview: 'RMIT University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The RMIT University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RMIT University''s developer surface includes authentication, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Rmit Plans Pricing
  plan_count: 2
  slug: rmit-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Rmit Rate Limits
  slug: rmit-rate-limits
rules:
- name: RMIT University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rmit-jsonschema-spectral-rules
- name: RMIT University API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: rmit-rules
scopes:
- name: Rmit Scopes
  scope_count: 1
  slug: rmit-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 75.9
    developer_ergonomics: 13.0
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 48.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rmit/refs/heads/main/screenshots/rmit-2026-06-20T193137.png
security:
- kind: authentication
  name: Rmit Authentication
  slug: rmit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rmit Domain Security
  slug: rmit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rmit Vulnerability Disclosure
  slug: rmit-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: rmit
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Australia
website: https://www.rmit.edu.au/
---
